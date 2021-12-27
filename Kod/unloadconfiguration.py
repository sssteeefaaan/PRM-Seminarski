from comparefunctions import funcs
from operator import add
from functools import reduce
from xmlparser import downloadXMLFiles, checkDir


def unloadAttributes(attributes={}):
    meta = list(filter(lambda x: x[1] != 0 or x[0] == "alertid", [(attributes[x].get("xml_parser", ""), attributes[x].get("c", 0), funcs.get(
        attributes[x].get("h", {}).get("options", {})[attributes[x].get("h", {}).get("chosen", 0)], "")) for x in attributes if attributes[x].get("use", False)]))
    if meta[0][0] != "alertid":
        raise BaseException("alerid MUST BE USED!")

    if reduce(add, list(map(lambda x: x[1], meta)), 0) != 1:
        raise BaseException("dotProduct(c, eigen) MUST BE 1!")

    return zip(*meta)


def unloadDataSource(dataSource={}):
    if dataSource.get('download_location', ""):
        download_location = dataSource['download_location']
    else:
        print(
            f"Missing download_location in data_source... download_location will be set to default value 'downloads/'!")
        download_location = 0.5

    if dataSource.get('files', ""):
        files = dataSource['files']
    else:
        print(
            f"Missing files in data_source... files will be set to default value '[]'!")
        files = []

    if dataSource.get('urls', ""):
        urls = dataSource['urls']
    else:
        print(
            f"Missing urls in data_source... urls will be set to default value '[]'!")
        urls = []

    return files + downloadXMLFiles(urls, downloadLoc=download_location)


def unloadDisplay(display={}):
    if display.get('t', ""):
        t = display['t']
    else:
        print(
            f"Missing t in display... t will be set to default value '{0.5}'!")
        t = 0.5

    if display.get('window_name', ""):
        window_name = display['window_name']
    else:
        print(f"Missing window_name in display... window_name will be set to default value 'Vizualizacija klasterizacije IDS alerta'!")
        window_name = "Vizualizacija klasterizacije IDS alerta"

    if display.get('refresh_rate', ""):
        refresh_rate = display['refresh_rate']
    else:
        print(
            f"Missing refresh_rate in display... refresh_rate will be set to default value '{0.0001}'!")
        refresh_rate = 0.0001

    if display.get('pause_key', ""):
        pause_key = display['pause_key']
    else:
        print(
            f"Missing pause_key in display... pause_key will be set to default value ' '!")
        pause_key = " "

    if display.get('unpause_key', ""):
        unpause_key = display['unpause_key']
    else:
        print(
            f"Missing unpause_key in display... unpause_key will be set to default value 'escape'!")
        unpause_key = "escape"

    if display.get('fifo_count', ""):
        fifo_count = display['fifo_count']
    else:
        print(
            f"Missing fifo_count in display... fifo_count will be set to default value '{50}'!")
        fifo_count = 50

    if display.get('node_colors', ""):
        node_colors = display['node_colors']
    else:
        print(f"Missing node_colors in display... node_colors will be set to default value '#1f78b4'!")
        node_colors = ["#1f78b4"]

    if display.get('layout', "") and display['layout'].get('chosen', "") and display['layout'].get('options', "") and display['layout']['options'].get(display['layout']['chosen'], ""):
        name = display['layout']['chosen']
        layout = {"name": name} | display['layout']['options'][name]
    else:
        print(f"Layout in display is corrupted... layout will be set to default value 'spring'!")
        layout = {
            "name": "spring",
            "scale": 1,
            "k": 1,
            "seed": 100,
            "iterations": 50,
            "threshold": 0.0001
        }

    if display.get('arrows', ""):
        arrows = display['arrows'] if display['arrows'] != "None" else None
    else:
        print(f"Missing arrows in display... arrors will be set to default value 'None'!")
        arrows = None

    if display.get('arrow_style', "") and display['arrow_style'].get('options', "") and display['arrow_style'].get('chosen', "") and display['arrow_style']['options'].get(display['arrow_style']['chosen']):
        arrow_style = display['arrow_style']['options'][display['arrow_style']['chosen']]
    else:
        print(f"arrow_style in display is corrupted... arrow_style will be set to default value 'curve_filled_B (-|>)'!")
        arrow_style = "-|>"

    if display.get('arrow_size', ""):
        arrow_size = display['arrow_size']
    else:
        print(f"Missing arrow_size in display... arrow_size will be set to default value '10'!")
        arrow_size = 10

    if display.get('with_labels', ""):
        with_labels = display['with_labels']
    else:
        print(f"Missing with_labels in display... with_labels will be set to default value 'true'!")
        with_labels = True

    if display.get('node_size', ""):
        node_size = display['node_size']
    else:
        print(
            f"Missing node_size in display... node_size will be set to default value '200'!")
        node_size = 200

    if display.get('node_shape', "") and display['node_shape'].get('options', "") and display['node_shape'].get('chosen', "") and display['node_shape']['options'].get(display['node_shape']['chosen']):
        node_shape = display['node_shape']['options'][display['node_shape']['chosen']]
    else:
        print(f"node_shape in display is corrupted... node_shape will be set to default value 'circle (o)'!")
        node_shape = "o"

    if display.get('style', ""):
        style = display['style']
    else:
        print(f"Missing style in display... style will be set to default value 'solid'!")
        style = "solid"

    if display.get('font_size', ""):
        font_size = display['font_size']
    else:
        print(
            f"Missing font_size in display... font_size will be set to default value '10'!")
        font_size = 10

    if display.get('font_color', ""):
        font_color = display['font_color']
    else:
        print(f"Missing font_color in display... font_color will be set to default value 'k (black)'!")
        font_color = "k"

    if display.get('font_weight', ""):
        font_weight = display['font_weight']
    else:
        print(f"Missing font_weight in display... font_weight will be set to default value 'normal'!")
        font_weight = "normal"

    if display.get('font_family', ""):
        font_family = display['font_family']
    else:
        print(f"Missing font_family in display... font_family will be set to default value 'sans-serif'!")
        font_family = "sans-serif"

    return {
        "t": t,
        "window_name": window_name,
        "refresh_rate": refresh_rate,
        "pause_key": pause_key,
        "unpause_key": unpause_key,
        "fifo_count": fifo_count,
        "node_colors": node_colors,
        "layout": layout,
        "arrows": arrows,
        "arrow_style": arrow_style,
        "arrow_size": arrow_size,
        "with_labels": with_labels,
        "node_size": node_size,
        "node_shape": node_shape,
        "style": style,
        "font_size": font_size,
        "font_color": font_color,
        "font_weight": font_weight,
        "font_family": font_family
    }


def unloadOptional(optional={}):
    if optional.get('snapshot', ""):
        snapshot = optional['snapshot']
    else:
        print(f"Missing snapshot in optional... snapshot will be set to default value!")
        snapshot = {
            "generate": True,
            "location": "snapshot/",
            "format": "png",
            "bbox_inches": "tight",
            "dpi": 500
        }

    if optional.get('csv', ""):
        csv = optional['csv']
    else:
        print(f"Missing csv in optional... csv will be set to default value!")
        csv = {
            "generate": True,
            "location": "data/"
        }

    if snapshot['generate']:
        checkDir(snapshot['location'])

    return (snapshot, csv)
