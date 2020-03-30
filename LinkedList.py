from BinaryTree import *
from Movie import Movie

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class LinkedList:
    def __init__(self):
        self.first = None

    def push(self, value):
        if not self.first:
            self.first = Node(value)
            return True
        current = self.first
        while current.next:
            current = current.next
        current.next = Node(value)
        return True

    def remove(self, position):
        if not self.first:
            return False
        if position == 0:
            self.first = self.first.next
        currentPosition = 0
        previous = None
        return self.__removeInner(position, currentPosition, self.first, previous)

    def __removeInner(self, position, currentPosition, current, previous):
        if not current:
            return False
        if position == currentPosition:
            previous.next = current.next
            return True
        previous = current
        current = current.next
        currentPosition += 1
        return self.__removeInner(position, currentPosition, current, previous)

    def overwrite(self, position, value):
        if not self.first:
            return False
        if position == 0:
            aux = self.first.next
            self.first = Node(value)
            self.first.next = aux
            return True
        currentPosition = 0
        self.__overwriteInner(position, currentPosition, self.first, None, value)

    def __overwriteInner(self, position, currentPosition, current, previous, value):
        if position == currentPosition:
            previous.next = Node(value)
            previous.next.next = current.next
            return True
        return self.__overwriteInner(position, currentPosition+1, current.next, current, value)

    def getTotalItems(self):
        current = self.first
        total = 0
        while(current):
            total += 1
            current = current.next
        return total

    def search(self, position):
        return self.__searchInner(position, 0, self.first)

    def __searchInner(self, position, currentPosition, current):
        if not current:
            return False
        if position == currentPosition:
            return current
        return self.__searchInner(position, currentPosition+1, current.next)


    def toBinaryTree(self):
        current = self.first
        self.tree = BinaryTree()
        while current:
            self.tree.add(current.value)
            current = current.next
        return True

    def drawBinaryTree(self):
        self.tree.drawTree()
        return True

