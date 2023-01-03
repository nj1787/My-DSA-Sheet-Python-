#The following is the solution to the problem rotate an array to the left by k elements towards left.

#Optimised Solution
def rotate_arrays(my_list, k):
    result = []
    rev_list = my_list[::-1]
    sublist1 = rev_list[:len(my_list)-k]
    rev_sublist1 = sublist1[::-1]
    sublist2 = rev_list[k + 1:]
    rev_sublist2 = sublist2[::-1]
    result = rev_sublist1 + rev_sublist2
    return result

a = [3, 4, 1, 6, 7, 8, 9]
print(a)
r = rotate_arrays(a, 3)
print(r)


#--------------------------------------------------------------------SAMPLE I/O---------------------------------------------------------------------------#

[3, 4, 1, 6, 7, 8, 9]     #Input

[6, 7, 8, 9, 3, 4, 1]     #Output
