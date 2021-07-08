def find_index(str1, str2):
    return str1.find(str2)


def find_index_1(str1, str2):
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str2[j] != str1[i + j]:
                break
        else:
            return i
    return -1


if __name__ == '__main__':
    str1 = "hello"
    str2 = "lli"
    print(find_index_1(str1, str2))
