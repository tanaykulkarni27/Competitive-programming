class tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def count_unival(self,root):
        if root == None:
           return 0
        total = self.count_unival(root.left)+self.count_unival(root.right)
        if self.chk_unival(root):
            total+=1
        return total
    def chk_unival(self,root):
        if root == None:
            return True
        if root.left!= None and root.left.data == root.data and root.right!= None and root.right.data == root.data:
            return True

if __name__ == '__main__':
    root = tree(2)
    root.left = tree(2)
    root.right = tree(2)
    root.right.right = tree(2)
    root.right.right.left = tree(2)
    root.right.right.right = tree(2)
    print(root.count_unival(root))
