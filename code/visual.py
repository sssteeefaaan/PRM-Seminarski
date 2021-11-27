import networkx as nx
import matplotlib.pyplot as plt
from alert import Alert
from compareFuncs import F
from xmlparser import parseXML, savetoCSV
import datetime as dt
from layout import layout_types
from unload import *
from os import _exit


def on_key(event, figure=None, pause_key=" ", unpause_key="escape"):
    if event.key == pause_key:
        figure.canvas.start_event_loop(0)
    if event.key == unpause_key:
        figure.canvas.stop_event_loop()

def on_close(event):
    _exit(1)

def visualize(attributes={}, data_source={}, display={}, optional={}):

    (attr, c, h) = unloadAttributes(attributes)
    files = unloadDataSource(data_source)
    disp = unloadDisplay(display)
    (snapshot, csv) = unloadOptional(optional)

    G = nx.Graph()
    color_map = []

    mng = plt.get_current_fig_manager()
    mng.set_window_title(disp['window_name'])
    fig = plt.figure(1)

    fig.canvas.mpl_connect('key_release_event', lambda event: on_key(event, figure=fig, pause_key=disp['pause_key'], unpause_key=disp['unpause_key']))
    fig.canvas.mpl_connect('close_event', on_close)

    i = 0
    id = 0
    mypos = None
    partial = []
    for file in files:

        name = file.replace(".xml", "").split("/")[-1]
        parsedData = parseXML(file)

        for row in parsedData:

            label = dt.datetime.now().strftime("%d. %B %Y @ %H-%M-%S-%f ms")
            row['alertid'] = id = id + 1
            a = Alert(attr, row)

            G.add_nodes_from([(a.dict['alertid'])])

            max = [0, a]

            for node in partial:
                weight = F(a.vector, node.vector, c, h)
                if weight >= disp['t']:
                    G.add_weighted_edges_from([(node.dict['alertid'], a.dict['alertid'], weight)])

                    if weight > max[0]:
                        max = [weight, node]

            if max[1].dict['alertid'] == a.dict['alertid']:
                color_map.append(disp['node_colors'][i])
                i = (i + 1) % len(disp['node_colors'])
            else:
                color_map.append(max[1].color)

            a.color = color_map[-1]

            mypos = layout_types[disp['layout']['name']](G, dict(disp['layout']))

            nx.draw_networkx(G,
                             pos=mypos,
                             node_color=color_map,
                             arrows=disp['arrows'],
                             arrowstyle=disp['arrow_style'],
                             arrowsize=disp['arrow_size'],
                             with_labels=disp['with_labels'],
                             node_size=disp['node_size'],
                             node_shape=disp['node_shape'],
                             style=disp['style'],
                             font_size=disp['font_size'],
                             font_color=disp['font_color'],
                             font_weight=disp['font_weight'],
                             font_family=disp['font_family'])

            plt.title(label)
            # plt.label(name)
            plt.pause(disp['refresh_rate'])

            partial.append(a)

            if not id % disp['fifo_count']:
                if snapshot['generate']:
                    plt.savefig(
                        fname=snapshot['location'] +
                        label + '.' + snapshot['format'],
                        format=snapshot['format'],
                        bbox_inches=snapshot['bbox_inches'])  # ,
                    # dpi=snapshot['dpi'])

                if csv['generate']:
                    savetoCSV(list(map(lambda x: x.dict, partial)),
                              label, dataLoc=csv['location'])

            if len(partial) == disp['fifo_count']:
                head, *partial = partial
                G.remove_nodes_from([head.dict['alertid']])
                color_map = color_map[1:]

            plt.clf()
