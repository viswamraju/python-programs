def pair_of_nums(nums, target):
    tmp_dict = dict()

    for i, num in enumerate(nums):
        print(tmp_dict)
        req_val = target - num
        if num in tmp_dict:
            return i, tmp_dict[num]
        else:
            tmp_dict[req_val] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(pair_of_nums(nums, target))