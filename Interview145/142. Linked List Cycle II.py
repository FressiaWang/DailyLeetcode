"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position 
(0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.
算法思路：

首先，判定环的存在：
a. 有环的话，快指针和慢指针必然相遇，通过指针相等退出循环；
b. 无环时，快指针将访问非法域，导致异常，从而被try...except...捕获，进而返回None.

判定有环后，利用上一步的信息（相遇的点），判定入口：
a. 设起点q到入口点r的距离为H步，入口r到第一次见面点m的为D步。一圈为C步，设第一次相遇时，Fast相对于r点转了n圈。如下图所示;
b. 则第一次相遇时，Slow运动了(H+D)步，Fast运动了(H + nC + D), 由于Fast指针是慢指针Slow的两倍速度, 从而有距离公式：

                      2(H+D) = H + nC + D,
经过简单的移位运算，有：

                       H = nC -D
c. 这表明，当我们让Slow重新从q点处、Fast继续从相遇见的m点处，以相等的速度移动时，两个指针会在入口r点相遇。
即Slow从q点移动H步，而Fast相当于会从m点移动n圈(会回到m处)，再后退D步。最终都在r点遇见。

https://leetcode.com/problems/linked-list-cycle-ii/discuss/258948/%2B-python
"""
class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        try: ##如果有尾部，必然出错，进入except。
            Slow = head.next ## 保证Slow和 Fast同时移动
            Fast = head.next.next
            while Slow!=Fast: ## Fast一直是Slow的两倍速度，这点很关键。
                Slow = Slow.next
                Fast = Fast.next.next
        except:
            return None       
        Slow = head ##让Slow从头开始，Fast保持上一步的位置
        while Slow != Fast:
            Slow = Slow.next
            Fast = Fast.next
        return Slow
