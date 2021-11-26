def find_first_repeating_number_1(numbers):   # with o (n ^ 2)
    repeating_number_found = False
    repeating_number = -1
    for i in range(len(numbers)):
        print(numbers[i])
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j]:
                print("duplicate found, {}".format(numbers[i]))
                repeating_number_found = True
                repeating_number = numbers[i]
                break
        if repeating_number_found:
            break
    print(repeating_number)
    

def find_first_repeating_number_2(numbers):     # with o (n)
    repeat_numbers = dict()
    repeat_number = -1
    for i in range(len(numbers)):
        if numbers[i] in repeat_numbers:
            
            repeat_number = numbers[i]
            print("repeating number found: {}".format(numbers[i]))
        else:
            repeat_numbers[numbers[i]] = 1
    print(repeat_numbers)
    print(repeat_number)
    
    
arr = [10, 5, 3, 4, 3, 5, 6]
# find_first_repeating_number_1(arr)
find_first_repeating_number_2(arr)
