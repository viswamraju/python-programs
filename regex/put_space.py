import re


def put_space(in_str):
    pattern = re.compile(r"[A-Z][a-z]*")
    words = re.findall(pattern, in_str)
    print(words)
    lower_words = []
    for word in words:
        word = chr(ord(word[0]) + 32) + word[1:]
        lower_words.append(word)

    print(" ".join(lower_words))


if __name__ == '__main__':
    in_str = "BruceWayneIsBatman"
    put_space(in_str)

