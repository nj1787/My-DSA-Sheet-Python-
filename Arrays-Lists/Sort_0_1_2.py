#The following are the two approaches that I have used to solve the problem of sorting an array/lists consisting only of 0, 1 and 2.

def sort_0_1_2_brute_force(my_list):
    d = {}
    result = []
    
    for ele in my_list:
        d[ele] = d.get(ele, 0) + 1

    zeros = d[0]
    ones = d[1]
    twos = d[2]

    for i in range(zeros):
        result.append(0)

    for j in range(ones):
        result.append(1)

    for k in range(twos):
        result.append(2)

    return result
 
    
def sort_0_1_2_optimized(my_list):
    i = 0
    j = 0
    k = len(my_list) - 1

    while j <= k:
        if my_list[j] == 1:
            j = j + 1
        elif my_list[j] == 0:
            my_list[j], my_list[i] = my_list[i], my_list[j]
            i = i + 1
            j = j + 1
        else:
            my_list[k], my_list[j] = my_list[j], my_list[k]
            k = k - 1
        


#Main
a = [2, 2, 0, 1, 1]
print(a)
print()
b = [1, 1, 0, 2, 1, 1, 0]
print(b)
print()
r = sort_0_1_2_brute_force(a)
print(r)
print()
sort_0_1_2_optimized(b)
print(b)


#------------------------------------------------------------SAMPLE I/O--------------------------------------------------------------------------------#
[2, 2, 0, 1, 1]                 #Input Brute Force

[1, 1, 0, 2, 1, 1, 0]           #Input Optimized

[0, 1, 1, 2, 2]                 #Output Brute Force

[0, 0, 1, 1, 1, 1, 2]           #Output Optimized
