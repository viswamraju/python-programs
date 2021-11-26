"""
Given a list of number find the first duplicate number
"""


def find_first_duplicate1(numbers):     # with o n ^ 2
    duplicate_number_min_index = len(numbers)
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j]:
                if j < duplicate_number_min_index:
                    duplicate_number_min_index = j
                print("found duplicate: {}, index: {}".format(numbers[i], j))
    print(duplicate_number_min_index)

    
def find_all_duplicates(arr):
    """
        Find all duplicate numbers with O(n) time but O(1) space complexity
        
        Logic:
            a = [1, 2, 1, 3, 6]
            
        * Take 0 index element ie 1 abs(a[i]) is 1, a[abs(a[i])] is 2
        * if a[abs(a[i])] is positive change the sign a = [1, -2, 1, 3, 6]  -- first index element ie 1 changing the
        2nd index value to -2
        * go to 1 index abs(a[1]) = 2 , a[abs(a[1])] = 1 and its positive so change the sign.
        
        * come to 2 nd index ie 1 again abs(a[2]) = 1, a[abs(a[2])] = 2 that means if current element is same as
        previous then corresponding value already modified to -ve in previous steps. In this case for 2 sign has
        chnaged to -ve so 1 is already encountered and we consider it as duplicate
    """
    for i in range(len(arr)):
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            print(abs(arr[i]), end=" ")

            
a = [1, 2, 3, 4, 5, 3, 2, 4, 1]
b = [5, 4, 1, 2, 3, 6, 3, 5]
# find_first_duplicate1(a)
find_all_duplicates(b)

