#Following is the solution for the problem of Sum of Two Lists. Twp Approaches -> Actual Solution and My Approach.

#Actual Solution
def sum_of_two_lists(list1, list2):
    result = []
    carry = 0
    element_sum = 0
    
    len_list1 = len(list1)
    len_list2 = len(list2)

    i = len_list1 - 1
    j = len_list2 - 1

    while i >= 0 and j >= 0:
        element_sum = list1[i] + list2[j] + carry
        carry = element_sum // 10
        element_sum = element_sum % 10
        result.append(element_sum)
        i = i - 1
        j = j - 1

    while i >= 0:
        element_sum = list1[i] + carry
        carry = element_sum // 10
        element_sum = element_sum % 10
        result.append(element_sum)
        i = i - 1

    while j >= 0:
        element_sum = list2[j] + carry
        carry = element_sum // 10
        element_sum = element_sum % 10
        result.append(element_sum)
        j = j - 1

    while carry != 0:
        element_sum = carry
        carry = element_sum // 10
        element_sum = element_sum % 10
        result.append(element_sum)

    final_ans = result[::-1]

    return final_ans

    
#Main
a = [6, 2, 4]
b = [7, 5, 6]

print(a)
print()
print(b)
print()

result = sum_of_two_lists(a, b)
print(result)

#------------------------------------------------------------------SAMPLE I/O-------------------------------------------------------------------------#
[6, 2, 4]         #Input

[7, 5, 6]         #Input

[1, 3, 8, 0]      #Output

[1]               #Input

[7, 5, 6]         #Input

[7, 5, 7]         #Output


[9, 7, 6, 1]      #Input

[4, 5, 9]         #Input

[1, 0, 2, 2, 0]   #Output
