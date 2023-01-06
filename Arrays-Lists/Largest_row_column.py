def largest_row_column(my_list, r, c):
    if r == 0 and c == 0:
        print('row {} {}'.format(0, -2147483648))
        return
        
    row_sum = 0
    col_sum = 0
    row_sum_list = []
    col_sum_list = []
    
    for i in range(r):
        for j in range(c):
            row_sum += my_list[i][j]
        row_sum_list.append(row_sum)
        row_sum = 0

    for j in range(c):
        for i in range(r):
            col_sum += my_list[i][j]
        col_sum_list.append(col_sum)
        col_sum = 0
    
    max_row_sum = max(row_sum_list)
    max_col_sum = max(col_sum_list)

    index_max_row_sum = row_sum_list.index(max_row_sum)
    index_max_col_sum = col_sum_list.index(max_col_sum)

    if max_row_sum > max_col_sum:
        print("row {} {}".format(index_max_row_sum, max_row_sum))
    elif max_row_sum < max_col_sum:
        print("column {} {}".format(index_max_col_sum, max_col_sum))
    else:
        print("row {} {}".format(index_max_row_sum, max_row_sum))
    
    
#Main
row_col = input().split()
row, col = int(row_col[0]), int(row_col[1])
li = [[int(j) for j in input().split()] for i in range(row)]
print()
largest_row_column(li, row, col)


#-----------------------------------------------------SAMPLE I/O--------------------------------------------------------------------------------------#

4 2                             #Input
1 2
90 100
3 40
-10 200

column 1 342                    #Output

3 3                             #Input
1 1 1
1 1 1
1 1 1

row 0 3                         #Output

0 0                             #Input

row 0 -2147483648               #Ouput
