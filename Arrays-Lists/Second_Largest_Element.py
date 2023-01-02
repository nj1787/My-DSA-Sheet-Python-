#Following code gave me a TLE(Time Limit Exceeded) on my Coding Ninjas Learning Portal. 
#However, the output is correct for any kind of test case and edge cases.

def second_largest_element(my_list):
    largest = my_list[0]
    second_largest = -2147483648
    i = 1
    while i < len(my_list):
        if my_list[i] > largest:
            second_largest = my_list[i]
            largest = my_list[i]
            i = i + 1
        elif my_list[i] == largest:
            i = i + 1
        elif my_list[i] > second_largest:
            second_largest = my_list[i]
            i = i + 1
    return second_largest

             

#Main
a = [6, 6, 6, 6, 6, 6, 6]
print(a)
result = second_largest_element(a)
print(result)
