def check_parenthesis(in_str):
    stack = []
    match_chars = {'{': '}', '(': ')', '[': ']'}
    for ch in in_str:
        if ch in match_chars:
            stack.append(ch)
        else:
            if not stack or match_chars[stack.pop()] != ch:
                return False
    return len(stack) == 0


if __name__ == '__main__':
    # in_str = '()'
    # in_str = "()[]{}"
    # in_str = "(]"
    # in_str = "([)]"
    in_str = "{[]}"
    print(check_parenthesis(in_str))
