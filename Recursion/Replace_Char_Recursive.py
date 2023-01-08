def replace_char_recursive(string, old, new):
    if len(string) == 1 and string[0] == old:
        return new
    elif len(string) == 1 and string[0] != old:
        return string[0]
    else:
        if string[0] == old:
            return new + replace_char_recursive(string[1:], old, new)
        else:
            return string[0] + replace_char_recursive(string[1:], old, new)

#Main
s = 'bbcba'
print(s)
print()
result = replace_char_recursive(s, 'a', 'x')
print(result)




#------------------------------------------------------------SAMPLE I/O------------------------------------------------------------------------------------#

bbcba       #Input

bbcbx       #Output

a           #Input

x           #Output

bccbbw      #Input

bccbbw      #Output
