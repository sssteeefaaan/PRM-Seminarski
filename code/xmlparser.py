import csv
import requests
import xml.etree.ElementTree as ET
from sys import setrecursionlimit
from urllib.request import urlopen

downloadLoc = 'downloads/'
setrecursionlimit(1000000)

def getFileNameFromUrl(url):
    return downloadLoc + "-".join(url.split('/')[-4:])

def downloadXMLRawData(url, fileName = ""):
    resp = requests.get(url)
    if not fileName:
        fileName = getFileNameFromUrl(url)
    return (resp.content, fileName)

def downloadXML(url, fileName = ""):
    (data, name) = downloadXMLRawData(url, fileName)
    with open(name, 'wb') as f:
        f.write(data)
        
    return name.removesuffix(".xml")
    
def parsRec(parsed, x, depth = 0, parents = []):
    parents.append(x.tag)
    
    if "\n" not in x.text:
        key = x.tag
        i = 2
        while key in parsed.keys():
            key = parents[-i] + " " + key
            i += 1
        parsed[key] = x.text
        # fields.add(key)
    #     print(("\t" * depth) + key + ": " + x.text)
    # else:
    #     print(("\t" * depth) + x.tag + ":")
        
    for key, value in x.attrib.items():
        key1 = key
        i = 1
        while key1 in parsed.keys():
            key1 = parents[-i] + " " + key1
            i += 1
        parsed[key1] = value
        # fields.add(key1)
        # print(("\t" * (depth + 1)) + key1 + ": " + value)
        
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
    
def savetoCSV(parsedData, fileName):
	with open(fileName, 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = parsedData[0].keys())
		writer.writeheader()
		writer.writerows(parsedData)
        
def main():
    for url in [
        'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_dmz/mid-level-phase-1.xml',
        'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_dmz/mid-level-phase-2.xml',
        'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_dmz/mid-level-phase-3.xml',
        'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_dmz/mid-level-phase-4.xml',
        'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_dmz/mid-level-phase-5.xml',
        'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_inside/mid-level-phase-1.xml',
        'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_inside/mid-level-phase-2.xml',
        'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_inside/mid-level-phase-3.xml',
        'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_inside/mid-level-phase-4.xml',
        'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_inside/mid-level-phase-5.xml',
        'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_inside/mid-level-phase-1.xml',
        'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_inside/mid-level-phase-2.xml',
        'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_inside/mid-level-phase-3.xml',
        'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_inside/mid-level-phase-4.xml',
        'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_inside/mid-level-phase-5.xml',
        'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_dmz/mid-level-phase-1.xml',
        'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_dmz/mid-level-phase-2.xml',
        'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_dmz/mid-level-phase-3.xml',
        'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_dmz/mid-level-phase-4.xml',
        'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_dmz/mid-level-phase-5.xml',
        ]:
	    name = downloadXML(url)
	    parsed = parseXML(name + ".xml")
	    savetoCSV(parsed, name + ".csv")