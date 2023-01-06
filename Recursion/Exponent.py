def power_optimised(base, power):
    if power == 0:
        return 1
    elif power % 2 == 0:
        return power_optimised(base * base, power // 2)
    else:
        return base * power_optimised(base * base, power // 2)

def power(b, e):
    if e == 0:
        return 1
    return b*power(b, e - 1)


#Main
base = int(input('Enter Base Value '))
exponent = int(input('Enter Exponent Value '))
result = power(base, exponent)
print(result)

b = int(input('Enter Base Value '))
p = int(input('Enter Exponent Value '))
result_optimised = power_optimised(b, p)
print(result_optimised)


#----------------------------------------------------------SAMPLE I/O-------------------------------------------------------------------------------------#
Enter Base Value 3              #Input
Enter Exponent Value 3          #Input

27                              #Output

Enter Base Value 5              #Input
Enter Exponent Value 6          #Input

15625                           #Output
