def check_list_sorted(my_list):
    if len(my_list) == 0 or len(my_list) == 1:
        return True
    elif my_list[0] > my_list[1]:
        return False
    else:
        return check_list_sorted(my_list[1:])


#Main
a = [1, 1, 6, 4, 5]
print(a)
print()
result = check_list_sorted(a)
print(result)




#--------------------------------------------------------------SAMPLE I/O---------------------------------------------------------------------------------#

[1, 2, 3, 4, 5]       #Input

True                  #Output
