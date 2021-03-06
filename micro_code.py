## 输入某二叉树的前序遍历和中序遍历的结果，
# 请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，
# 则重建二叉树并返回。

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0 or pre == None :
            return None
        root = TreeNode(pre[0])
        ## 获取左子树的前序遍历
        child_map = self.getChildRoot(pre, tin)
        ## 分别获取左子树和右子树的前序遍历和中序遍历
        pre_left = child_map['pre_left']
        tin_left = child_map['tin_left']
        ## 递归调用,获取左子树
        root.left = self.reConstructBinaryTree(pre_left, tin_left)
        
        pre_right = child_map['pre_right']
        tin_right = child_map['tin_right']
        root.right = self.reConstructBinaryTree(pre_right, tin_right)
        return root
        
        
    ## 找到子树
    def getChildRoot(self, pre, tin) :
        child = {}
        root = pre[0]
        pre_left = []
        tin_left = []
        pre_right = []
        tin_right = []
        ## 中序遍历是否遍历到了根
        flag = False
        for i in tin :
            if i != root and flag != True:
                tin_left.append(i)
            elif i == root :
                flag = True
                continue
            else :
                tin_right.append(i)

        for i in pre :
            if i in tin_left:
                pre_left.append(i)
            elif i != root :
                pre_right.append(i)
        child['pre_left'] = pre_left
        child['pre_right'] = pre_right
        child['tin_left'] = tin_left
        child['tin_right'] = tin_right
        return child


## test
# pre = [1,2,4,7,3,5,6,8]
# tin = [4,7,2,1,5,3,8,6]
# s = Solution()
# root = s.reConstructBinaryTree(pre, tin)

# print(root)



class Node :
    def __init__(self, data, left = None, right = None) :
        self.data = data
        self.left = left
        self.right = right

def printSpreadNode(root) :
    list = []
    list.append(root)
    n = 1
    while len(list) > 0 :
        tempList = []
        for i in list :
            print("第" + str(n) + "层 : " + str(i.data))
            if i.left is not None :
                tempList.append(i.left)
            if i.right is not None :
                tempList.append(i.right)
            list = tempList
        n = n + 1

# root = Node(1)
# root.left = Node(2, Node(4), Node(5))
# root.right = Node(3, Node(6), Node(7))

# printSpreadNode(root)


class Solution2:
    def StrToInt(self, s):
        try :
            return int(s)
        except :
            return 0

# s = Solution2()
# print(s.StrToInt('123'))


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def Merge(self, pHead1, pHead2):
        # write code here
        if (pHead1 == None) :
            return pHead2
        if (pHead2 == None) :
            return pHead1
        all_val_list = self.getAllList(pHead1, pHead2)
        self.sort(all_val_list)
        return self.constructList(all_val_list)

    def constructList(self, list) :
        head = ListNode(list[0])
        p = head
        for i in range(1, len(list)) :
            p.next = ListNode(list[i])
            p = p.next
        return head

    def sort(self, list) :
        ## -- 冒泡排序 -- 
        for i in range(0, len(list)) :
            for j in range(len(list) - i, len(list)) :
                if list[j] > list[j + 1] :
                    ## 交换
                    list[j], list[j + 1] = list[j + 1], list[j]
        return list 

    ## 获取所有的值  
    def getAllList(self, pHead1, pHead2) :
        list = []
        p1 = pHead1
        while (p1 != None) :
            list.append(p1.val)
            p1 = pHead1.next
        p1 = pHead2 
        while (p2 != None) :
            list.append(p2.val)
            p2 = pHead2.val
        return list

        

p1 = ListNode(1)
p1.next = ListNode(3)
p1.next.next = ListNode(5)

p2 = ListNode(2)
p2.next = ListNode(4)
p2.next.next = ListNode(6)

s = Solution()
print(s.Merge(p1, p2))
        
        

