#For Implementation of Binary Tree(Level-wise implementation) Refer To My-DSA-repo-python respository.

#Here I have directly implemented the function.

#Given a Binary Search Tree and two integers k1 and k2, find and print the elements which are in range k1 and k2 (both inclusive).
#Print the elements in increasing order.

def print_elements_k1_k2(root, k1, k2):           #Here k1(20) and k2(55) are formal arguments defining the range to print. 
    if root is None:                              #Base Case -> Empty Tree -> Do Nothing
        return
    if root.data > k2:                            #If root is greater than upper limit, no point going to right side of tree
        print_elements_k1_k2(root.left, k1, k2)   #Recursive call to the left side of tree
    elif root.data < k1:                          #If root is lesser than lower limit,  no point going to left side of the tree
        print_elements_k1_k2(root.right, k1, k2)  #Recursive call to the right side of tree
    else:
        print_elements_k1_k2(root.left, k1, k2)   #If root lies in between k1 and k2, first go to left, 
        print(root.data, end=' ')                 #then print main root 
        print_elements_k1_k2(root.right, k1, k2)  #and then got to right.

#Main
r = take_input()
print()
print_tree(r)
print()
print_elements_k1_k2(r, 70, 78)                    #Here lower limit(k1) is 20 and upper limit(k2) is 55.


-------------------------------------------------------------SAMPLE I/O-----------------------------------------------------------------------------------
Enter Root Data                               #Input
51
Enter Left Child of  51
24
Enter Right Child of  51
65
Enter Left Child of  24
-1
Enter Right Child of  24
-1
Enter Left Child of  65
61
Enter Right Child of  65
71
Enter Left Child of  61
55
Enter Right Child of  61
62
Enter Left Child of  71
69
Enter Right Child of  71
78
Enter Left Child of  55
-1
Enter Right Child of  55
-1
Enter Left Child of  62
-1
Enter Right Child of  62
-1
Enter Left Child of  69
-1
Enter Right Child of  69
-1
Enter Left Child of  78
-1
Enter Right Child of  78
-1

51:L 24,R 65                                #Output
24:
65:L 61,R 71
61:L 55,R 62
71:L 69,R 78
55:
62:
69:
78:
  
71 78                                      #Output
