import sys
def max_sum(lst):
    max_sum = float('-inf')
    start, end = 0, 0
    print(max_sum)
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if sum(lst[i:j]) > max_sum:
                start = i
                end = j
                max_sum = sum(lst[i:j])
    print(lst[start:end+1])


def max_sub_array(lst):

    current_sum = 0
    max_sum = -sys.maxsize
    start = 0
    end = 0
    poi = 0
    for i in range(len(lst)):
        current_sum += lst[i]

        if max_sum < current_sum:
            max_sum = current_sum
            start = poi
            end = i
        if current_sum < 0:
            current_sum = 0
            poi = i + 1

    print(max_sum)
    print(lst[start: end])


if __name__ == '__main__':
    lst = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    lst2 = [5, 4, -1, 7, 8]
    max_sub_array(lst)
