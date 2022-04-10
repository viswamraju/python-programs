def undirected_path(edges, src, dst):
    visited = set()
    graph = convert_edges_to_nodes(edges)
    return has_path(graph, src, dst, visited)


def has_path(graph, src, dst, visited):
    if src == dst:
        return True
    if src in visited:
        return False
    visited.add(src)

    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst, visited):
            return True
    return False


def convert_edges_to_nodes(edges):
    nodes_dict = dict()

    for edge in edges:
        src, dst = edge
        if src not in nodes_dict:
            nodes_dict[src] = []
        if dst not in nodes_dict:
            nodes_dict[dst] = []
        nodes_dict[src].append(dst)
        nodes_dict[dst].append(src)
    return nodes_dict


if __name__ == '__main__':
    edges = [
        ['i', 'j'],
        ['k', 'i'],
        ['m', 'k'],
        ['k', 'l'],
        ['o', 'n']
    ]

print(undirected_path(edges, 'j', 'm'))
