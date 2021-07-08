def a():
    lst = []
    for i in [1, 2, 3, 4]:
        lst.append(lambda: i)
    print([f() for f in lst])


a()
