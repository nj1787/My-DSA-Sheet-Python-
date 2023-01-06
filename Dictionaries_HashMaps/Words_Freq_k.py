def print_words_freq_k(string, key):
    word_list = string.split()
    d = {}
    
    for word in word_list:
        d[word] = d.get(word, 0) + 1
    
    for k in d.keys():
        if d[k] == key:
            print(k)
        else:
            continue

#Main
s = "this is a word string having many many word"
print(s)
print()
print_words_freq_k(s, 1)


#------------------------------------------------------------SAMPLE I/O------------------------------------------------------------------------------------#

this is a word string having many many word     #Output

this                                            #Output
is
a
string
having

this is a word string having many many word    #Output (for key = 2)

word                                           #Output
many
