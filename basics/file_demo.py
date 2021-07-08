def read1():
    with open('fff.txt') as f:
        print(f.read().splitlines())


def read2():
    lines = []
    with open('fff.txt') as f:
        for line in f:
            lines.append(line.strip())
        print(lines)


def read3():
    with open('fff.txt') as f:
        print([line.strip() for line in f.readlines()])

print("my name is viswam".title())
