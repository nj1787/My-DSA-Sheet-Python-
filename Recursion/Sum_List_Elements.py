def sum_of_list_elements(list1):
    if len(list1) == 0:
        return 0
    small_output = sum_of_list_elements(list1[1:])
    return list1[0] + small_output


#Main
a = [1, 2]
print(a)
print()
result = sum_of_list_elements(a)
print(result)


#-----------------------------------------------------------SAMPLE I/O-------------------------------------------------------------------------------------#

[1, 1, 6, 4, 5]                     #Input

17                                  #Output

[]                                  #Input

0                                   #Output

[1]                                 #Input

1                                   #Output
  
[1, 2]                              #Input

3                                   #Output
