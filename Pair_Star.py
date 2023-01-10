def pair_star(string):
    if len(string) == 1:
        return string[0]
    small_output = pair_star(string[1:])
    if string[0] == small_output[0]:
        return string[0] + '*' + small_output
    else:
        return string[0] + small_output

#Main
s = "aa"
print(s)
result = pair_star(s)
print(result)


#--------------------------------------------------------SAMPLE I/O---------------------------------------------------------------------------------------#

aa     #Input
a*a    #Output

aaaa      #Input
a*a*a*a   #Output

hello     #Input
hel*lo    #Output
