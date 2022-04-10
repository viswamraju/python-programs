def breadth_first_search(graph, element):
    queue = [element]

    while queue:
        ele = queue.pop(0)
        print(ele)

        for neighbor in graph[ele]:
            queue.append(neighbor)


if __name__ == '__main__':
    graph = {
        'a': ['c', 'b'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'f': [],
        'e': []

    }

    breadth_first_search(graph, 'a')
