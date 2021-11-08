import networkx as nx
import matplotlib.pyplot as plt
from alert import *
from compareFuncs import *
from xmlparser import *

def visualizeData(url, attributes, c, h, t, speed = 0):
    parsedData = parseXMLFromUrl(url)

    G = nx.Graph()
    A = []
    
    interval = speed
    if speed <= 0:
        interval = 30.0 / ((len(parsedData) + 10) << 1)

    for row in parsedData:
        a = Alert(attributes, row)
    
        G.add_nodes_from([
            (a.dict['alertid'], {
                # attributes
                #'key': 'value'
                })
            ])
        
        for node in A:
            weight = F(a.vector, node.vector, c, h)
            if weight >= t:
                G.add_weighted_edges_from([(a.dict['alertid'], node.dict['alertid'], weight)])
                    # attributes
                    #'key': 'value'
                    # weight = str(weight),
                    # label = str(weight)
                    
        mypos = nx.spring_layout(G, seed=100)
        nx.draw_networkx(G, pos=mypos)
        plt.pause(interval)
        plt.clf()
        
        A.append(a)

    savetoCSV(list(map(lambda x: x.dict, A)), getFileNameFromUrl(url) + '.csv')
    nx.draw_networkx(G)
    plt.show()