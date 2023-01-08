def check_list_sorted(my_list):
    if len(my_list) == 0 or len(my_list) == 1:
        return True
    elif my_list[0] > my_list[1]:
        return False
    else:
        return check_list_sorted(my_list[1:])
 
def check_list_sorted_optimised(list1, si):
    l = len(list1)
    if si == l - 1 or si == l:
        return True
    if list1[si] < list1[si + 1]:
        return check_list_sorted_optimised(list1, si + 1)
    else:
        return False


#Main
a = [1, 1, 6, 4, 5]
print(a)
print()
result = check_list_sorted(a)
print(result)
b = [1, 2, 6, 4, 5, 6, 7, 8, 9]
print(a)
result2 = check_list_sorted_optimised(b, 0)
print(result2)




#--------------------------------------------------------------SAMPLE I/O---------------------------------------------------------------------------------#

[1, 2, 3, 4, 5]       #Input

True                  #Output

[1, 2, 3, 4, 5, 6, 7, 8, 9]    #Input for Optimised 

True                           #Output for Optimised

[1, 2, 6, 4, 5, 6, 7, 8, 9]    #Input for Optimised

False                          #Outpuut for Optimised
