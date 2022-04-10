def has_path(graph, src, dst):
    if src == dst:
        return True
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst):
            return True
    return False


def has_path_bfs(graph, src, dst):
    queue = [src]

    while queue:
        current = queue.pop()
        if current == dst:
            return True
        for neighbor in graph[current]:
            queue.insert(0, neighbor)
    return False


def depth_first_search(graph, element):
    stack = [element]
    while stack:
        ele = stack.pop()
        print(ele, end=" -> ")
        for neighbor in graph[ele]:
            stack.append(neighbor)


def breadth_first_search(graph, element):
    queue = [element]

    while queue:
        ele = queue.pop()
        print(ele, end=" -> ")

        for neighbor in graph[ele]:
            queue.insert(0, neighbor)


if __name__ == '__main__':
    graph = {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': []
    }
    print(has_path_bfs(graph, 'f', 'j'))
