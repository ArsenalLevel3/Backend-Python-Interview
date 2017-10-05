#!/usr/bin/env python
# _*_ coding: utf-8 _*_


from __future__ import print_function
import SinglyLinkedList


def reverseLinkedList(myLinkedList):
    previous = None
    current = myLinkedList.head
    while(current != None):
        temp = current.next
        current.next = previous
        previous = current
        current = temp
    myLinkedList.head = previous


if __name__ == '__main__':
    myLinkedList = SinglyLinkedList.LinkedList()
    for i in range(10, 0, -1):
        myLinkedList.insertAtStart(i)

    print('Original:', end=' ')
    myLinkedList.printLinkedList()
    print()
    print('Reversed:', end=' ')
    reverseLinkedList(myLinkedList)
    myLinkedList.printLinkedList()
