from dsTypes.linkedList import *

def arrayToLinkedList(array):
    dummy = ListNode()
    current = dummy
    for value in array:
        current.next= ListNode(value)
        current = current.next
    return dummy.next()

if __name__ == "__main__":
    array = [2, 6, 10]
    linkedList = arrayToLinkedList(array)
    print(linkedList)
