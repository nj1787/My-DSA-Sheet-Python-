def wave_print(my_list, r, c):
    for j in range(c):
        for i in range(r):
            if j % 2 == 0:
                print(my_list[i][j], end=' ')
            else:
                print(my_list[r-1-i][j], end=' ')   

#Main
row_col = input().split()
row, col = int(row_col[0]), int(row_col[1])
li = [[int(j) for j in input().split()] for i in range(row)]
wave_print(li, row, col)
print()



#---------------------------------------------------------------------Sample I/O------------------------------------------------------------------------#
3 3                         #Input
10 20 30
40 50 60
70 80 90

10 40 70 80 50 20 30 60 90  #Output
  
5 3                                     #Input 
1 2 3 
4 5 6 
7 8 9 
10 11 12 
13 14 15

1 4 7 10 13 14 11 8 5 2 3 6 9 12 15     #Output
