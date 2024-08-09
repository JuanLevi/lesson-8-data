class Node():
    def __init__(self,v):
        self.root=v
        self.right=None
        self.left=None
    
def InOrder(root):
    if root:
        InOrder(root.left)
        print(root.root)
        InOrder(root.right)
    

def PreOrder(root):
    if root:
        print(root.root)
        PreOrder(root.left)
        PreOrder(root.right)

def PostOrder(root):
    if root:
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.root)


node=Node(10)
node.left=Node(11)
node.right=Node(2)
node.left.left=Node(4)
node.left.right=Node(99)
node.right.left=Node(41)
node.right.right=Node(18)

'''
print(node.root)
print(node.right.right.root)
'''

InOrder(node)
print('...')
PreOrder(node)
print('...')
PostOrder(node)