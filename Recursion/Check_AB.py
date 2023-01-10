def  check_AB(string):
    if len(string) == 1 and string[0] == 'a':
        return True
    elif len(string) == 0:
        return True 
    else:
        if string[0] == 'a':
            if string[1:3] == 'bb' or string[1] == 'a':
                small_output = check_AB(string[3:])
                return small_output
            else:
                small_output = check_AB(string[1:])
                return small_output
        else:
            return False


#Main
s = 'aaaaaa'
print(s)
result = check_AB(s)
print(result)


#----------------------------------------------------------SAMPLE I/O-----------------------------------------------------------------------------------#

a        #Input

True     #Output

abb      #Input

True     #Output

abababa  #Input

False   #Output

abbaaabb #Input

True     #Output
