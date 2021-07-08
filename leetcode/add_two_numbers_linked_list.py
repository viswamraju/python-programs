class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1, l2):
    carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1 + v2 + carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(8)))
    l2 = ListNode(5, ListNode(6, ListNode(9)))

    l3 = add_two_numbers(l1, l2)

    node = l3
    while node:
        print(node.val)
        node = node.next



