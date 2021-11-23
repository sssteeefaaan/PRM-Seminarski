from visual import visualizeDataFileArray
from compareFuncs import *
import json


def main():
    with open('config.json') as f:
        config = json.load(f)

    attr, display, data_source, optional = config.values()

    cmpMeta = [(attr[x]['xml_parser'], attr[x]['c'], funcs[attr[x]['h']])
               for x in attr if attr[x]['use']]

    (a, c, h) = zip(*cmpMeta)
    visualizeDataFileArray(data_source['urls'], a, c, h, display=display)


if __name__ == '__main__':
    main()
