def sort_nums(nums):

    sorted_list = []
    while nums:
        max = -1
        for num in nums:
            if num > max:
                max = num
        sorted_list.append(max)
        nums.remove(max)
    print(sorted_list)


if __name__ == '__main__':
    nums = [24, 55, 78, 64, 25, 12, 22, 11, 1, 2, 44, 3, 122, 23, 34]
    sort_nums(nums)
