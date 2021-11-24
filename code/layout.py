import networkx as nx


def bipartite(G: nx.Graph, d):
    align = d['align']
    center = None if not d['center']['chosen'] else "array-like"
    return nx.drawing.layout.bipartite_layout(G, nodes=G.nodes, align=align['options'][align['chosen']], scale=d['scale'],
                                              center=center, aspect_ratio=d['aspect_ratio'])


def circular(G, d):
    center = None if not d['center']['chosen'] else "array-like"
    return nx.drawing.layout.circular_layout(
        G, scale=d['scale'], center=center)


def graphviz(G, d):
    prog = d['prog']
    root = None if d['root'] == "None" else d['root']
    return nx.drawing.nx_agraph.graphviz_layout(
        G, prog=prog['options'][prog['chosen']], root=root)


def kamada_kawai(G, d):
    center = None if not d['center']['chosen'] else "array-like"
    return nx.drawing.layout.kamada_kawai_layout(
        G, scale=d['scale'], center=center)


def random(G, d):
    center = None if not d['center']['chosen'] else "array-like"
    return nx.drawing.layout.random_layout(
        G, center=center, seed=d['seed'])


def shell(G, d):
    center = None if not d['center']['chosen'] else "array-like"
    return nx.drawing.layout.shell_layout(
        G, scale=d['scale'], center=center, rotate=d['rotate'])


def spectral(G, d):
    center = None if not d['center']['chosen'] else "array-like"
    return nx.drawing.layout.spectral_layout(
        G, scale=d['scale'], center=center)


def spiral(G, d):
    center = None if not d['center']['chosen'] else "array-like"
    return nx.drawing.layout.spiral_layout(
        G, scale=d['scale'], center=center, equidistant=d['equidistant'])


def spring(G, d):
    center = None if not d['center']['chosen'] else "array-like"
    return nx.drawing.layout.spring_layout(
        G, scale=d['scale'], center=center, k=d['k'], seed=d['seed'], iterations=d['iterations'], threshold=d['threshold'])


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
