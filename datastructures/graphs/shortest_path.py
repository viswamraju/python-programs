#  Associate weights for each node


def get_shortest_path(edges, src, dst):
    nodes = get_nodes(edges)
    # print(nodes)
    path = shortest_path(nodes, src, dst)
    print(path)


def shortest_path(nodes, src, dst):
    queue = [(src, 0)]
    visited = set(src)
    while queue:
        _ele = queue.pop()
        ele = _ele[0]

        distance = _ele[1]
        if ele == dst:
            return distance
        for neighbour in nodes[ele]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.insert(0, [neighbour, distance + 1])
    return -1


def get_nodes(edges):
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
        ['w', 'x'],
        ['x', 'y'],
        ['z', 'y'],
        ['z', 'v'],
        ['w', 'v']
    ]
    get_shortest_path(edges, 'w', 'z')

