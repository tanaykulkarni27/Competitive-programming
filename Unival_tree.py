def read_str():
    return str(input())
def read_int():
    return int(input())
def read_str_array():
    return [str(i) for i in input().split()]
def read_int_array():
    return [int(i) for i in input().split()]
class tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def count(self,root):
        if root == None:
            return 0
        else:
            total = self.count(root.right) +self.count(root.left)
            if self.chk_node(root):
                total+=1
            return total
    def chk_node(self,root):
        if root == None:
            return False
        elif root.left == None and root.right == None:
            return True
        elif root.left != None and root.left.data == root.data  and root.right != None and root.right.data == root.data:
            return True
        else:
            return False
if __name__ == '__main__':
    root = tree(3)
    root.left = tree(2)
    root.right = tree(3)
    root.right.right = tree(2)
    root.right.right.left = tree(2)
    root.right.right.right = tree(2)
    print(root.count(root))
