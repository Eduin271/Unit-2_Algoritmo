class BinarySearchTree(object): # A binary search tree class
 
         class __Node(object): # A node in a binary search tree

                def __init__( # Constructor takes a key that is
                        self, # used to determine the position
                                key, # inside the search tree,
                                data, # the data associated with the key
                                left=None, # and a left and right child node
                                right=None): # if known
                        self.key = key # Copy parameters to instance
                        self.data = data # attributes of the object
                        self.leftChild = left
                        self.rightChild = right

                def __str__(self): # Represent a node as a string
                        return "{" + str(self.key) + ", " + str(self.data) + "}"
                
                def __init__(self): # The tree organizes nodes by their
                        self.__root = None # keys. Initially, it is empty.

                def isEmpty(self): # Check for empty tree
                        return self.__root is None
                
                def root(self): # Get the data and key of the root

                        if self.isEmpty(): # If the tree is empty, raise

                                raise Exception("No root node in empty tree")
                        return (        # Otherwise return root data and its

                                self.__root.data, self.__root.key)