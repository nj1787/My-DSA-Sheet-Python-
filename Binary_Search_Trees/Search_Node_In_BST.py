#For Implementation of Binary Tree(Level-wise implementation) Refer To My-DSA-repo-python respository.

#Here I have directly implemented the function.

#Given a Binary Tree in form of a Binary Search Tree, Find whether the given node i.e. k in this case present in the tree or not. Return True
#if the value is present else return False.

def search_node_in_BST(root, k):                  #Here k is the formal argumment passed as number to be searched.
    if root is None:                              #Base Case - Empty Tree
        return False
    if root.data == k:                            #It is possible that root itself contains the value we are searching for. This will change after 
        return True                               #the left and right recursive calls.
    elif root.data > k:                           #Recursive Call - This is where problem gets divided into two parts. From here we decide whether to continue search
        return search_node_in_BST(root.left, k)   #on the left-side of the tree or 
    else:
        return search_node_in_BST(root.right, k)  #on the right-side of the tree. 

#Main
r = take_input()                                  #This function is implemented in the My-DSA-repo-python respository.
print()
print_tree(r)                                     #This function is implemented in the My-DSA-repo-python respository.
print()
result = search_node_in_BST(r, 26)                #result will contain either True or False --> Here 26 is the value to be searched.
print()
print(result)

--------------------------------------------------------------SAMPLE I/O--------------------------------------------------------------------------

Enter Root Data                     #Input
18
Enter Left Child of  18
15
Enter Right Child of  18
21
Enter Left Child of  15
-1
Enter Right Child of  15
-1
Enter Left Child of  21
19
Enter Right Child of  21
26
Enter Left Child of  19
-1
Enter Right Child of  19
-1
Enter Left Child of  26
-1
Enter Right Child of  26
-1                                

18:L 15,R 21                        #Output --> Here L stands for Left Child of Root and R stands for Rigth Child of Root.
15:
21:L 19,R 26
19:
26:


True                               #Output --> True Means Element is Found in the Tree.
