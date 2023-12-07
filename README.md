Common Methods
a typical implementation will likely include methods for inserting and removing nodes, and for searching or traversing the tree.


Basic Operation Of Tree Data Structure:
Create – create a tree in the data structure.
Insert − Inserts data in a tree.
Search − Searches specific data in a tree to check whether it is present or not.
Traversal:
Preorder Traversal – perform Traveling a tree in a pre-order manner in the data structure.
In order Traversal – perform Traveling a tree in an in-order manner.
Post-order Traversal –perform Traveling a tree in a post-order manner.



simple way of rep a tree node in python: 
class BinaryTreeNode:
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild=None


Insert an Element in a Binary Search Tree

The current node can be an empty node
The element to be inserted can be greater than the element at the current node
The element to be inserted can be less than the element at the current node

search an element in a Binary search Tree
 binary search tree cannot have duplicate elements, we can search any element in a binary search tree using the following rules that are based on the properties of the binary search trees. We will start from the root and follow these properties
 1. If the current node is empty, we will say that the element is not present 
2. If the element in the current node is greater than the element to be searched, we will search the element in its left subtree as the left subtree of any node contains all the elements lesser than the current node.
3. If the element in the current node is less than the element to be searched, we will search the element in its right subtree as the right subtree of any node contains all the elements greater  than the current node.
4. If the element at the current node is equal to the element to be searched, we will return True.


How to delete an element in a Binary search Tree
(https://jackskylord.medium.com/binary-search-trees-3031846c02e9)

We will start by creating a while loop that will loop until the node that we are currently at is None/Null. If the input value is less than the current node value then we will want to set the parent node to the current node and will want to set the current node to the left child of the current node.We do this because the current node is greater than the input value, and thus our only chance in finding a match is to go to the left child (input value is less than the current node value)

