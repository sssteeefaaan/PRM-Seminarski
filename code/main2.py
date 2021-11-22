from visual import visualizeDataFileArray
from compareFuncs import *
import json

def main():
    with open('config.json') as f:
        config = json.load(f)
    
    attr, display, data_source, optional = config.values()
        
    cmpMeta = [(config['attributes'][x]['xml_parser'], config['attributes'][x]['c'], funcs[config['attributes'][x]['h']]) for x in config['attributes'] if config['attributes'][x]['use']]
    
    (a, c, h) = zip(*cmpMeta)
    visualizeDataFileArray(data_source['urls'], a, c, h, display['t'])
        
if __name__ == '__main__':
        main()