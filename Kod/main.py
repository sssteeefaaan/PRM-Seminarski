from visual import visualize
from traceback import print_exc
import json

def main():
    try:
        with open('config.json') as f:
            config = json.load(f)
        visualize(attributes=config['attributes'], data_source=config['data_source'],
                  display=config['display'], optional=config['optional'])
    except BaseException as e:
        print("Error occurred")
        print_exc()

if __name__ == '__main__':
    main()
