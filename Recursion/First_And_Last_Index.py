def find_first_index(list1, si, ei, element):
    if si > ei:
        return -1
    if list1[si] == element:
        return si
    else:
        return find_first_index(list1, si + 1, ei, element)

#Not able to build correct logic for Last Index. Mistake was checking with list1[0] instead of list1[si].
def find_last_index(list1, si, ei, element):
    if si > ei:
        return -1
    
    small_output = find_last_index(list1, si + 1, ei, element)

    if small_output == -1:
        if list1[si] == element:
            return si
        else:
            return -1
    else:
        return small_output

def find_first_and_last_index(my_list, ele):
    first_index = find_first_index(my_list, 0, len(my_list) - 1, ele)
    last_index =  find_last_index(my_list, 0, len(my_list) - 1, ele)
    return first_index, last_index
    
    

#Main
a = [2, 3, 1, 4, 5, 6, 5, 1, 4]
print(a)
result = find_first_and_last_index(a, 4)
print()
print(result)



#-------------------------------------------------------------SAMPLE I/O--------------------------------------------------------------------------------#
[2, 3, 1, 4, 5, 6, 5, 1, 4]               #Input

(3, 8)                                    #Output (first index, last index)

[2, 3, 1, 4, 5, 6, 5, 1, 4]               #Input  (searching 9)

(-1, -1)                                  #Output (first index, last index)

[2, 3, 1, 4, 5, 6, 5, 1, 4]               #Input  (searching 2)

(0, 0)                                    #Output (first index, last index)
