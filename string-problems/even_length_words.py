def print_even_length_words(in_str):
    for word in in_str.split():
        if len(word) % 2 == 0:
            print(word)


if __name__ == '__main__':
    in_str = "This is a python language"
    print_even_length_words(in_str)