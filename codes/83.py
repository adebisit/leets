from typing import Optional
from dsTypes.linkedList import ListNode

def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head.next is None:
        return head
    current = ListNode(val=head.val)
    head = head.next
    while head is not None:
        if head.val != current.val:
            current.next = ListNode(head.val)
            current = current.next
        head = head.next
    return current