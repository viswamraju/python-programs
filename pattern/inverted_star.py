def inverted_star1(n):
    """
    * * * * *
     * * * *
      * * *
       * *
        *
    :param n:
    :return:
    """
    tmp_str = ""
    for i in range(n):
        tmp_str += " " * i + "* " * (n-i) + "\n"

    print(tmp_str)


def inverted_star2(n):
    """
    * * * * *
      * * * *
        * * *
          * *
            *
    :param n:
    :return:
    """
    tmp_str = ""
    for i in range(n):
        tmp_str += "  " * i + "* " * (n-i) + "\n"

    print(tmp_str)


if __name__ == '__main__':
    inverted_star1(10)
