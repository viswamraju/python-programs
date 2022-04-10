import sys


def largest_component(graph):
    visited = set()
    max_count = 0
    for node in graph:
        node_count = explore_and_get_count(graph, node, visited)
        if node_count > max_count:
            max_count = node_count
    return max_count


def smallest_component(graph):
    visited = set()
    min_count = sys.maxsize
    for node in graph:
        node_count = explore_and_get_count(graph, node, visited)
        if node_count > 0 and node_count < min_count:
            min_count = node_count
    return min_count


def explore_and_get_count(graph, current, visited):
    if current in visited:
        return 0
    visited.add(current)
    size = 1
    for neighbor in graph[current]:
        size += explore_and_get_count(graph, neighbor, visited)

    return size


if __name__ == '__main__':
    graph = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    }
    # print(largest_component(graph))
    print(smallest_component(graph))
