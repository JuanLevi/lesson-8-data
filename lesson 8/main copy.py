class Node():
    def __init__(self,v):
        self.root=v
        self.right=None
        self.left=None
    
    def InOrder(self,root):
        if root:
            self.InOrder(root.left)
            print(root.root)
            self.InOrder(root.right)
    

    def PreOrder(self,root):
        if root:
            print(root.root)
            self.PreOrder(root.left)
            self.PreOrder(root.right)

    def PostOrder(self,root):
        if root:
            self.PostOrder(root.left)
            self.PostOrder(root.right)
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

node.InOrder(node)
print('...')
node.PreOrder(node)
print('...')
node.PostOrder(node)