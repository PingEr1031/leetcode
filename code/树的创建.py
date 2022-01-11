# coding=utf-8

class Node(object):
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    """树"""
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        # 为树增加节点
        node = Node(elem)
        # 树是空的，则将节点 -> 根节点
        if self.root.elem == -1:
            self.root = node
            self.myQueue.append(self.root)
        # 树非空
        else:
            treeNode = self.myQueue[0]
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)
    def pre_order_traversal(self, root):
        result = []

        def traversal(root):
            if root == None:
                return
            result.append(root.val)
            traversal(root.left)
            traversal(root.right)

        traversal(root)
        return result

    def inorder_traversal(self,root):
        res = []
        stack = []
        while stack or root:
            #不断往左子树走，没走一次就将当前节点保存到栈
            if root:
                stack.append(root)
                root = root.left
            # 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
            # 然后转向右边节点，继续上面整个过程
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right
            return res