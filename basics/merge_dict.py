d1 = {'A1': 20, 'B1': 25, 'C1': 40, 'D1': 50}
d2 = {"X1": 100, "Y1": 200, "b1": 25, "A1": 22, "D1": "Hello"}


def merge_dicts():
    for key, value in d2.items():
        d1[key] = value
    print(d1)


def merge_dicts2():
    d1.update(d2)
    print(d1)


merge_dicts2()
