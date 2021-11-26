import csv
import requests
import xml.etree.ElementTree as ET
from sys import setrecursionlimit
from urllib.request import urlopen
import os

setrecursionlimit(1000000)

def checkDir(dir):
    if not os.path.exists(dir):
        print(f"Path '{dir}' doesn't exist!")
        os.mkdir(dir)
        print(str.format("Path '{dir}' created!"))


def downloadXMLFiles(urls, downloadLoc='downloads/'):
    checkDir(downloadLoc)
    files = []
    for url in urls:
        name = (downloadLoc + " ".join(url.split("/")[-4:])).replace("_", "-")
        if not os.path.exists(name):
            print(f'Downloading \'{url}\'')
            try:
                data = requests.get(url).content
                with open(name, 'wb') as f:
                    f.write(data)
                print('Done')
            except BaseException as err:
                er = err.__str__()
                print(
                    f"Error '{er}' occurred while downloading '{url}'! Skipping")
        else:
            print(f"File '{name}' exists! Skipping...")
        files.append(name)
    return files


def getFileNameFromUrl(url, downloadLoc='downloads/'):
    checkDir(downloadLoc)
    return downloadLoc + "-".join(url.split('/')[-4:])


def downloadXMLRawData(url, fileName=""):
    resp = requests.get(url)
    if not fileName:
        fileName = getFileNameFromUrl(url)
    return (resp.content, fileName)


def downloadXML(url, fileName=""):
    name = ""
    try:
        (data, name) = downloadXMLRawData(url, fileName)
        with open(name, 'wb') as f:
            f.write(data)
    except BaseException as err:
        er = err.__str__()
        print(
            f"Error '{er}' occurred while downloading '{url}'! Skipping")
    return name.removesuffix(".xml")


def parsRec(parsed, x, depth=0, parents=[]):
    parents.append(x.tag)

    if "\n" not in x.text:
        key = x.tag
        i = 2
        while key in parsed.keys():
            key = parents[-i] + " " + key
            i += 1
        parsed[key] = x.text

    for key, value in x.attrib.items():
        key1 = key
        i = 1
        while key1 in parsed.keys():
            key1 = parents[-i] + " " + key1
            i += 1
        parsed[key1] = value

    for y in x:
        parsed |= parsRec(parsed, y, depth + 1, parents)

    return parsed


def parseXML(xmlfile):
    parsedRows = []
    try:
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        for x in root:
            parsedRows.append({})
            parsRec(parsedRows[-1], x)

    except BaseException as err:
        er = err.__str__()
        print(f"Error '{er}' occurred! Skipping '{xmlfile}' ...")

    return parsedRows


def parseXMLFromUrl(url):
    parsedRows = []
    try:
        with urlopen(url) as xmlFile:
            tree = ET.parse(xmlFile)
            root = tree.getroot()
            for x in root:
                parsedRows.append({})
                parsRec(parsedRows[-1], x)

    except BaseException as err:
        er = err.__str__()
        print(f"Error '{er}' occurred! Skipping '{url}' ...")

    return parsedRows


def savetoCSV(parsedData, fileName, dataLoc='data/'):
    checkDir(dataLoc)

    try:
        with open(dataLoc + fileName + ".csv", 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=parsedData[0].keys())
            writer.writeheader()
            writer.writerows(parsedData)
    except BaseException as err:
        er = err.__str__()
        print(
            f"Error '{er}' occurred! Skipping csv saving of '{fileName}' ...")
