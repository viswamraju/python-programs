# Find a pair of whose sum equals to given target
# works for sorted   O(N)

# def find_pair(nums, target):
#     low = 0
#     high = len(nums) - 1
#     while low < high:
#         if nums[low] + nums[high] > target:
#             high = high - 1
#         elif nums[low] + nums[high] < target:
#             low = low + 1
#         else:
#             print(low, high)
#             break
#
#
# l1 = [1, 2, 3, 9]
# l2 = [1, 2, 4, 4]
# find_pair(l2, 8)

# ------------------------------------------------------------------------

# Find a pair of whose sum equals to given target
# not sorted   time complexity O(N), space complexity O(N)

def find_pair(nums, target):
    tmp_dict = dict()
    for _ in nums:
        required_value = target - _
        if required_value in tmp_dict:
            print("found pair")
            break
        else:
            tmp_dict[required_value] = _
    

l1 = [1, 2, 3, 9]
l2 = [1, 2, 4, 4]
find_pair(l1, 8)
