import networkx as nx


def bipartite(G: nx.Graph, d):
    align = d['align']
    return nx.drawing.layout.bipartite_layout(
        G, nodes=G.nodes, align=align['options'][align['chosen']],
        scale=d['scale'],
        aspect_ratio=d['aspect_ratio'])


def circular(G, d):
    return nx.drawing.layout.circular_layout(
        G, scale=d['scale'])


def graphviz(G, d):
    prog = d['prog']
    root = None if d['root'] == "None" else d['root']
    return nx.drawing.nx_agraph.pygraphviz_layout(
        G, prog=prog['options'][prog['chosen']], root=root)


def kamada_kawai(G, d):
    return nx.drawing.layout.kamada_kawai_layout(
        G, scale=d['scale'])


def random(G, d):
    return nx.drawing.layout.random_layout(
        G, seed=d['seed'])


def shell(G, d):
    return nx.drawing.layout.shell_layout(
        G, scale=d['scale'], rotate=d['rotate'])


def spectral(G, d):
    return nx.drawing.layout.spectral_layout(
        G, scale=d['scale'])


def spiral(G, d):
    return nx.drawing.layout.spiral_layout(
        G, scale=d['scale'],  equidistant=d['equidistant'])


def spring(G, d):
    return nx.drawing.layout.spring_layout(
        G, scale=d['scale'], k=d['k'], seed=d['seed'], iterations=d['iterations'], threshold=d['threshold'])


layout_types = {
    "bipartite": bipartite,
    "circular": circular,
    "graphviz": graphviz,
    "kamada_kawai": kamada_kawai,
    "random": random,
    "shell": shell,
    "spectral": spectral,
    "spiral": spiral,
    "spring": spring
}
