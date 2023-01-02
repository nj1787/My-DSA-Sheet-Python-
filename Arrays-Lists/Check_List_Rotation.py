#Following is the code for the problem to check whether given array/list is rotated or not.
#If yes, then return the index from which it is rotated else return 0.

def check_list_rotated(my_list):
    if len(my_list) == 0:
        return 0
    org_list = sorted(my_list)
    first_org = org_list[0]
    index_org_list = org_list.index(first_org)
    index_given_list = my_list.index(first_org)
    diff = abs(index_given_list - index_org_list)
    return diff

#Main
a = [5, 6, 1, 2, 3, 4]
print(a)
result = check_list_rotated(a)
print(result)



#-------------------------------------------------------------Sample I/O----------------------------------------------------------------------------------#

[5, 6, 1, 2, 3, 4]  #Input

2                   #Output

[3, 6, 8, 9, 10]    #Input

0                   #Output

[10, 20, 30, 1]     #Input

3                   #Output
