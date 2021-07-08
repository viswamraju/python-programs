import re


def print_upper_lower_letters(in_str):
    upper_letters = re.findall(r"[A-Z]", in_str)
    lower_letters = re.findall(r"[a-z]", in_str)
    numerical_chars = re.findall(r"[0-9]", in_str)
    special_chars = re.findall(r"[,.!?]", in_str)
    word_chars = re.findall(r"\w+", in_str)
    non_word_chars = re.findall(r"\W+", in_str)
    print(upper_letters)
    print(lower_letters)
    print(numerical_chars)
    print(special_chars)
    print(word_chars)
    print(non_word_chars)



if __name__ == '__main__':
    in_str = "ThisIsGeeksforGeeks !, 123"
    print_upper_lower_letters(in_str)
