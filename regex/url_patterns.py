import re


def find_urls(string):
    pattern = re.compile(r"(((http|https)://)(www.)?[a-zA-Z0-9./]{2,256})")
    urls = re.findall(pattern, string)
    print(urls)


if __name__ == '__main__':
    string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of http://www.geeksforgeeks.org/'
    find_urls(string)