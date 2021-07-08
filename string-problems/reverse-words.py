def reverse_words(in_str):
    words = in_str.split()
    no_words = len(words)
    out_words = []
    for i in range(no_words-1, -1, -1):
        out_words.append(words[i])
    print(" ".join(out_words))


if __name__ == '__main__':
    in_str = "geeks quiz practice code"
    reverse_words(in_str)