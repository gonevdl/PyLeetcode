"""
请编写一个函数，用于 删除单链表中某个特定节点 。在设计函数时需要注意，你无法访问链表的头节点head ，
只能直接访问 要被删除的节点 。

题目数据保证需要删除的节点 不是末尾节点 。

head = [4,5,1,9], node = 5
输出：[4,1,9]
解释：指定链表中值为5的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-node-in-a-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        q = node
        while node.next is not None:
            p = node.next
            node.val = p.val
            node = node.next
            q = node.next



l2 = ListNode(9)
l22 = l2
l2.next = ListNode(9)
l2 = l2.next
l222 = l2
l2.next = ListNode(4)
l2 = l2.next

Solution().deleteNode(l222)
print("hello")
