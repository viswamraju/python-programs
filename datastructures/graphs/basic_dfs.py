def depth_first_search_rec(graph, element):
    stack = [element]

    while stack:
        ele = stack.pop()
        print(ele)
        for neighbor in graph[ele]:
            depth_first_search_rec(graph, neighbor)


def depth_first_search_without_rec(graph, element):
    stack = [element]

    while stack:
        ele = stack.pop()
        print(ele)
        for neighbor in graph[ele]:
            stack.append(neighbor)


if __name__ == '__main__':
    graph = {
        'a': ['c', 'b'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'f': [],
        'e': []

    }
    depth_first_search_rec(graph, 'a')
    print("###############")
    depth_first_search_without_rec(graph, 'a')
