from visual import visualize
from compareFuncs import *
import json


def main():
    with open('config.json') as f:
        config = json.load(f)

    cmpMeta = [(config['attributes'][x]['xml_parser'], config['attributes'][x]['c'], funcs[config['attributes'][x]['h']['options'][config['attributes'][x]['h']['chosen']]])
               for x in config['attributes'] if config['attributes'][x]['use']]

    (a, c, h) = zip(*cmpMeta)
    visualize(
        a, c, h, data_source=config['data_source'], display=config['display'], optional=config['optional'])

if __name__ == '__main__':
    main()
