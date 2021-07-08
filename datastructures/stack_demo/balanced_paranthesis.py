from stack import Stack


def is_balanced(in_str):
    open_chars = ['{', '[', '(']
    paranthesis_map = {')': '(', '}': '{', ']': '['}

    s = Stack()

    is_balanced = True
    for ch in in_str:
        if ch in open_chars:
            s.push(ch)
        elif ch in list(paranthesis_map.keys()):

            if (s.size() > 0) and s.peek() == paranthesis_map.get(ch):
                s.pop()
            else:
                is_balanced = False
    print(s.size())
    if s.size() != 0:
        is_balanced = False
    return is_balanced


if __name__ == '__main__':
    in_str = "{[]{()}}["
    print(is_balanced(in_str))
