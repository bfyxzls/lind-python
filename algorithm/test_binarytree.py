from BinaryTree import BinaryTree
from algorithm.ParseTree import inorder, postorder


r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
r.getLeftChild().setRootVal('左1')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('右1')
print(r.getRightChild().getRootVal())
print("---前序---")
r.preorder()

print("---中序---")
inorder(r)

print("---后序---")
postorder(r)
