def connected_graphs_count(graph):
    visited = set()
    count = 0
    for node in graph:
        # count += traverse(graph, node, visited)
        if traverse_v1(graph, node, visited):
            count += 1
    print(count)


def traverse(graph, node, visited):
    if node in visited:
        return 0
    stack = [node]

    while stack:
        ele = stack.pop()
        visited.add(ele)
        for neighbor in graph[ele]:
            if neighbor not in visited:
                stack.append(neighbor)
    return 1


def traverse_v1(graph, current, visited):
    if current in visited:
        return False
    visited.add(current)

    for neighbor in graph[current]:
        traverse_v1(graph, neighbor, visited)
    return True


if __name__ == '__main__':
    graph = {
        3: [],
        4: [6],
        6: [4, 5, 7, 8],
        8: [6],
        7: [6],
        5: [6],
        1: [2],
        2: [1]
    }
    connected_graphs_count(graph)
