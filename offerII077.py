# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def merge(self, head1, head2):
        s = h = ListNode(-1)
        while head1 and head2:
            if head1.val < head2.val:
                h.next = head1
                head1 = head1.next
            else:
                h.next = head2
                head2 = head2.next
            h = h.next
        if head1:
            h.next = head1
        if head2:
            h.next = head2
        return s.next
        # 4 -> 2 -> 1
        #     slow  fast
        # 4 -> 2
        #     slow  fast
        # 这种不行哈
        # slow = fast = head
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        # _head2 = fast
        # slow.next = None
    def merge_sort(self, head):
        if not head:
            return None
        if head and not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        _head2 = slow.next
        slow.next = None

        head1 = self.merge_sort(head)
        head2 = self.merge_sort(_head2)
        return self.merge(head1, head2)

    def sortList(self, head):
        return self.merge_sort(head)
