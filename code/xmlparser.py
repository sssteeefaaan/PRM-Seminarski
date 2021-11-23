import csv
import requests
import xml.etree.ElementTree as ET
from sys import setrecursionlimit
from urllib.request import urlopen
import os

setrecursionlimit(1000000)


def downloadXMLFiles(urls, downloadLoc='downloads/'):

    if not os.path.exists(downloadLoc):
        os.mkdir(downloadLoc)

    files = []
    for url in urls:
        name = (downloadLoc + " ".join(url.split("/")[-4:])).replace("_", "-")
        if not os.path.exists(name):
            print(f'Downloading \'{url}\'')
            data = requests.get(url).content
            with open(name, 'wb') as f:
                f.write(data)
            print('Done')
        files.append(name)
    return files


def getFileNameFromUrl(url, downloadLoc='downloads/'):
    if not os.path.exists(downloadLoc):
        os.mkdir(downloadLoc)

    return downloadLoc + "-".join(url.split('/')[-4:])


def downloadXMLRawData(url, fileName=""):
    resp = requests.get(url)
    if not fileName:
        fileName = getFileNameFromUrl(url)
    return (resp.content, fileName)


def downloadXML(url, fileName=""):
    (data, name) = downloadXMLRawData(url, fileName)
    with open(name, 'wb') as f:
        f.write(data)

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
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    parsedRows = []

    for x in root:
        parsedRows.append({})
        parsRec(parsedRows[-1], x)

    return parsedRows


def parseXMLFromUrl(url):
    with urlopen(url) as xmlFile:
        tree = ET.parse(xmlFile)
        root = tree.getroot()
        parsedRows = []

        for x in root:
            parsedRows.append({})
            parsRec(parsedRows[-1], x)

    return parsedRows


def savetoCSV(parsedData, fileName, dataLoc='data/'):

    if not os.path.exists(dataLoc):
        os.mkdir(dataLoc)

    with open(dataLoc + fileName + ".csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=parsedData[0].keys())
        writer.writeheader()
        writer.writerows(parsedData)
