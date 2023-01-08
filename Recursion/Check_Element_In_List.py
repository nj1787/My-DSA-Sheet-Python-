def check_element_present(my_list, element):
    if len(my_list) == 0:
        return False
    elif len(my_list) == 1 and my_list[0] == element:
        return True
    elif my_list[0] == element:
        return True
    else:
        return check_element_present(my_list[1:], element)



#Main
a = [9, 8, 10]
print(a)
print()
result1 = check_element_present(a, 2)
print(result1)
print()
result2 = check_element_present(a, 8)
print(result2)
print()


#-----------------------------------------------------SAMPLE I/O-------------------------------------------------------------------------------------------#

[9, 8, 10]          #Input

False               #Output result1

True                #Output result2
