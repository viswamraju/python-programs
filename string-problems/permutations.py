from itertools import permutations


def all_permutations(in_str):
    perm_list = permutations(in_str)

    for item in perm_list:
        print("".join(item))


def perm(string):
    if len(string) == 1:
        return [string]

    perms = []
    for c in string:
        remaining_chrs = [_ for _ in string if _ != c]
        res = perm(remaining_chrs)

        for _ in res:
            perms.append([c] + _)
    return perms


if __name__ == '__main__':
    in_str = "ABC"
    # all_permutations(in_str)
    print(perm('ABC'))
