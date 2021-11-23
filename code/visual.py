import threading
import matplotlib
import networkx as nx
import matplotlib.pyplot as plt
from alert import *
from compareFuncs import *
from xmlparser import *
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, thread
from threading import Thread
from multiprocessing import Process
import datetime as dt


def visualize(attributes, c, h, data_source={}, display={}, optional={}):
    files = data_source['files'] + downloadXMLFiles(
        data_source['urls'], downloadLoc=data_source['download_location'])

#
    t = display['t'] if display['t'] else 0.5
    refresh_rate = display['refresh_rate'] if display['refresh_rate'] else 0.0001
    fifo_count = display['fifo_count'] if display['fifo_count'] else 100
    node_colors = display['node_colors'] if display['node_colors'] else []
    # layout_ind = display['layout_ind'] if display['layout_ind'] else 0
#
    G = nx.Graph()
    A = []
    color_map = []

    mng = plt.get_current_fig_manager()
    mng.set_window_title('Vizualizacija klasterizacije IDS alerta')
    fig = plt.figure(1)

    def on_key(event):
        if event.key == ' ':
            fig.canvas.start_event_loop(0)
        if event.key == 'escape':
            fig.canvas.stop_event_loop()

    fig.canvas.mpl_connect('key_release_event', on_key)

    i = 1
    mypos = None
    for file in files:
        name = file.replace(".xml", "").replace("downloads/", "")
        parsedData = parseXML(file)
        partial = []

        for row in parsedData:
            row['alertid'] = len(A) + 1
            a = Alert(attributes, row)

            G.add_nodes_from([
                (a.dict['alertid'], {
                    # attributes
                    # 'key': 'value'
                })
            ])
            color_map.append(node_colors[i - 1])

            for node in A:
                weight = F(a.vector, node.vector, c, h)
                if weight >= t:
                    G.add_weighted_edges_from(
                        [(a.dict['alertid'], node.dict['alertid'], weight)])
                    # attributes
                    # 'key': 'value'
                    # weight = str(weight),
                    # label = str(weight)

            partial.append(a)
            A.append(a)

            # mypos = nx.drawing.nx_agraph.graphviz_layout(G)
            # mypos = nx.drawing.nx_pydot.graphviz_layout(G, prog="twopi")
            # mypos = nx.spring_layout(G, k=1, seed=100, pos=mypos)
            # mypos = nx.kamada_kawai_layout(G)

            nx.draw_networkx(G, pos=mypos, node_color=color_map)
            plt.title(name)
            plt.pause(refresh_rate)
            plt.clf()

        savetoCSV(list(map(lambda x: x.dict, partial)),
                  dt.datetime.now().strftime("%d/%m/%Y@%h-%m-%s"), dataLoc=optional['csv']['location'])
        i = (i + 1) % len(node_colors)

    th1 = Thread(target=savetoCSV, args=[
                 list(map(lambda x: x.dict, A)), 'Data'], kwargs={"dataLoc": optional['csv']['location']})
    th1.start()

    clusters = list(nx.find_cliques(G))

    i = 0
    for cluster in clusters:
        for node in cluster:
            # if color_map[node - 1] == -1:
            color_map[node - 1] = node_colors[i]
        i = (i + 1) % len(node_colors)

    if layout_ind == 0:
        mypos = nx.kamada_kawai_layout(G)
    elif layout_ind == 1:
        # , scale=0.75, center=(0,0), fixed=None)
        mypos = nx.spring_layout(G, k=1, seed=100, pos=mypos)

    nx.draw_networkx(G, pos=mypos, node_color=color_map)
    plt.show()

    th1.join()

# ne koristi
# def visualizeDataURL(url, attributes, c, h, t, time = 15):
#     parsedData = parseXMLFromUrl(url)

#     G = nx.Graph()
#     A = []

#     interval = time / ((len(parsedData)) << 2)

#     for row in parsedData:
#         a = Alert(attributes, row)

#         G.add_nodes_from([
#             (a.dict['alertid'], {
#                 # attributes
#                 #'key': 'value'
#                 })
#             ])

#         for node in A:
#             weight = F(a.vector, node.vector, c, h)
#             if weight >= t:
#                 G.add_weighted_edges_from([(a.dict['alertid'], node.dict['alertid'], weight)])
#                     # attributes
#                     #'key': 'value'
#                     # weight = str(weight),
#                     # label = str(weight)

#         mypos = nx.spring_layout(G, seed=100)
#         nx.draw_networkx(G, pos=mypos)
#         plt.pause(interval)
#         plt.clf()

#         A.append(a)

#     savetoCSV(list(map(lambda x: x.dict, A)), getFileNameFromUrl(url) + '.csv')
#     nx.draw_networkx(G)
#     plt.show()

# def visualizeDataURLArray(urls, attributes, c, h, t, time = 10):
#     G = nx.Graph()
#     A = []
#     i = 1
#     color_map = []

#     for url in urls:
#         print(f'Downloading: \'{url}\'')
#         name = '-'.join(url.split('/')[-4:])
#         parsedData = parseXMLFromUrl(url)
#         interval = time / ((len(parsedData)) << 2)
#         partial = []

#         for row in parsedData:
#             row['alertid'] = len(A) + 1
#             a = Alert(attributes, row)

#             G.add_nodes_from([
#                 (a.dict['alertid'], {
#                     # attributes
#                     #'key': 'value'
#                     })
#                 ])
#             color_map.append(colors[i - 1])

#             for node in A:
#                 weight = F(a.vector, node.vector, c, h)
#                 if weight >= t:
#                     G.add_weighted_edges_from([(a.dict['alertid'], node.dict['alertid'], weight)])
#                         # attributes
#                         #'key': 'value'
#                         # weight = str(weight),
#                         # label = str(weight)

#             mypos = nx.spring_layout(G, seed=100)
#             nx.draw_networkx(G, pos=mypos, node_color=color_map)
#             plt.title(name)
#             plt.pause(0.00001)
#             plt.clf()

#             partial.append(a)
#             A.append(a)

#         savetoCSV(list(map(lambda x: x.dict, partial)), 'data/' + str(i) + '. ' + name + '.csv')
#         i = (i + 1)%len(colors)

#     clusters = list(nx.find_cliques(G))
#     i = 0
#     color_map = [-1] * len(color_map)
#     for cluster in clusters:
#         for node in cluster:
#             if color_map[node - 1] == -1:
#                 color_map[node - 1] = colors[i]
#         i = (i + 1)%len(colors)
#     savetoCSV(list(map(lambda x: x.dict, A)), 'data/Data.csv')
#     nx.draw_networkx(G, node_color=color_map)
#     plt.show()

# def parseURL(url):
#     print(f'Downloading \'{url}\'')
#     return ('-'.join(url.split('/')[-4:]), parseXMLFromUrl(url))

# def visualizeDataURLArrayMP(urls, attributes, c, h, t, time = 10, size=5):
    G = nx.Graph()
    A = []
    i = 1
    color_map = []

    def checkEdge(rank):
        length = len(A)
        for i in range(0, num):
            index = i * size + rank
            if length > index:
                weight = F(a.vector, A[index].vector, c, h)
                if weight >= t:
                    G.add_weighted_edges_from(
                        [(a.dict['alertid'], A[index].dict['alertid'], weight)])
                    # attributes
                    # 'key': 'value'
                    # weight = str(weight),
                    # label = str(weight)

    with ThreadPoolExecutor() as executor:
        results = executor.map(parseURL, urls)

    for res in results:
        name, parsedData = res
        partial = []

        for row in parsedData:
            row['alertid'] = len(A) + 1
            a = Alert(attributes, row)

            G.add_nodes_from([
                (a.dict['alertid'], {
                    # attributes
                    # 'key': 'value'
                })
            ])
            color_map.append(colors[i-1])

            num = len(A) // size
            threads = []
            for rank in range(0, size):
                threads.append(Thread(target=checkEdge, args=[rank]))
                threads[rank].start()

            for thread in threads:
                thread.join()

            mypos = nx.spring_layout(G, seed=100)
            nx.draw_networkx(G, pos=mypos, node_color=color_map)
            plt.title(name)
            plt.pause(0.00001)
            plt.clf()

            partial.append(a)
            A.append(a)

        savetoCSV(list(map(lambda x: x.dict, partial)),
                  'data/' + str(i) + '. ' + name + '.csv')
        i += 1

    clusters = list(nx.find_cliques(G))
    i = 0
    color_map = [-1]*len(color_map)
    for cluster in clusters:
        for node in cluster:
            if color_map[node - 1] == -1:
                color_map[node-1] = colors[i]
        i = (i + 1) % len(colors)
    savetoCSV(list(map(lambda x: x.dict, A)), 'data/Data.csv')
    nx.draw_networkx(G, node_color=color_map)
    plt.show()
