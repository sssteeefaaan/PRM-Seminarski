import networkx as nx
import matplotlib.pyplot as plt
from alert import Alert
from compareFuncs import *
from xmlparser import os, downloadXMLFiles, parseXML, savetoCSV
import datetime as dt
from layout import layout_types


def visualize(attributes, c, h, data_source={}, display={}, optional={}):
    files = data_source['files'][1:] + downloadXMLFiles(
        data_source['urls'], downloadLoc=data_source['download_location'])

    t = display['t'] if display['t'] else 0.5
    refresh_rate = display['refresh_rate'] if display['refresh_rate'] else 0.0001
    fifo_count = display['fifo_count'] if display['fifo_count'] else 100
    node_colors = display['node_colors'] if display['node_colors'] else []
    chosen_layout = display['chosen_layout'] if display['chosen_layout'] in layout_types.keys(
    ) else "graphviz"
    snapshot = optional['snapshot']
    csv = optional['csv']

    if snapshot['generate'] and not os.path.exists(snapshot['location']):
        os.mkdir(snapshot['location'])

    G = nx.Graph()
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

    i = 0
    id = 0
    mypos = None
    partial = []
    for file in files:

        #name = file.replace(".xml", "").split("/")[-1]
        parsedData = parseXML(file)

        for row in parsedData:
<<<<<<< HEAD
            
            print(id)
            
=======
            print(id, row)

>>>>>>> 4800695c4d2e184dc10034238691a67119fa4778
            label = dt.datetime.now().strftime("%d. %B %Y @ %H-%M-%S-%f ms")
            row['alertid'] = id = id + 1
            a = Alert(attributes, row)

            G.add_nodes_from([(a.dict['alertid'])])

            max = [0, a]

            for node in partial:
                weight = F(a.vector, node.vector, c, h)
                if weight >= t:
                    G.add_weighted_edges_from(
                        [(a.dict['alertid'], node.dict['alertid'], weight)])

                    if weight > max[0]:
                        max = [weight, node]

            if max[1].dict['alertid'] == a.dict['alertid']:
                color_map.append(node_colors[i])
                i = (i + 1) % len(node_colors)
            else:
                color_map.append(max[1].color)

            a.color = color_map[-1]

            mypos = layout_types[chosen_layout](
                G, dict(display['layout_types'][chosen_layout]))

            nx.draw_networkx(G, pos=mypos, node_color=color_map)
            plt.title(label)
            # plt.label(name)
            plt.pause(refresh_rate)
            plt.clf()

            partial.append(a)

            counter -= 1
            if not counter:
                counter = -1

                if snapshot['generate']:
                    plt.savefig(
                        snapshot['location'] + label, format=snapshot['format'], bbox_inches=snapshot['bbox_inches'])
                    counter = fifo_count

                if csv['generate']:
                    savetoCSV(list(map(lambda x: x.dict, partial)),
                              label, dataLoc=csv['location'])
                    counter = fifo_count

            if len(partial) == fifo_count:
                head, *partial = partial
                G.remove_nodes_from([head.dict['alertid']])
                color_map = color_map[1:]

            plt.clf()
