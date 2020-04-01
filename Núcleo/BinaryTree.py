# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import math

class NodeBT:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = NodeBT(value)
            return True
        return self.__addInner(value, self.root)
        
    def __addInner(self, value, current):
        if current.value.getMovieDuration() == value.getMovieDuration():
            return False
        elif value.getMovieDuration() < current.value.getMovieDuration():
            if current.left:
                return self.__addInner(value, current.left)
            else:
                current.left = NodeBT(value)
                return True
        elif value.getMovieDuration() > current.value.getMovieDuration():
            if current.right:
                return self.__addInner(value, current.right)
            else:
                current.right = NodeBT(value)
                return True

    def getLevel(self):
        self.treeLevel = 0
        self.__getLevelInner(self.root, 0)
        return self.treeLevel

    def __getLevelInner(self, current, level):
        if not current:
            if level > self.treeLevel:
                self.treeLevel = level
            return True
        self.__getLevelInner(current.left, level+1)
        self.__getLevelInner(current.right, level+1)
        return True

    def drawTree(self):
        fig, ax = plt.subplots(figsize=(10, 7))

        fig.subplots_adjust(top=0.99)
        fig.subplots_adjust(bottom=0)
        fig.subplots_adjust(right=1)
        fig.subplots_adjust(left=0)

        plt.plot(0,0, 10, 10)
        self.__drawTreeInner(ax, self.root, self.getRootPositionX(), self.getLevel())
        plt.show()

    def __drawTreeInner(self, ax, current, parentPositionX, parentPositionY):
        leftChildPosition = self.getLeftChildPosition(parentPositionX, parentPositionY)
        rightChildPosition = self.getRightChildPosition(parentPositionX, parentPositionY)

        if not current.left:
            leftChildPosition = (parentPositionX, parentPositionY)
        if not current.right:
            rightChildPosition = (parentPositionX, parentPositionY)

        movieDuration = self.convertSecondsToTimeFormat(current.value.getMovieDuration())
        movieName = current.value.getMovieName()

        an = ax.annotate("%s\n%s" % (movieDuration, movieName), 
                        xy=leftChildPosition,
                        xytext=(parentPositionX, parentPositionY),
                        va="bottom", ha="center",
                        bbox=dict(boxstyle="round", fc="w"),
                        arrowprops=dict(arrowstyle="->"))

        an = ax.annotate("%s\n%s" % (movieDuration, movieName),
                        xy=rightChildPosition,
                        xytext=(parentPositionX, parentPositionY),
                        va="bottom", ha="center",
                        bbox=dict(boxstyle="round", fc="w"),
                        arrowprops=dict(arrowstyle="->"))
    
        if current.left:
            self.__drawTreeInner(ax, current.left, leftChildPosition[0], leftChildPosition[1])
        if current.right:
            self.__drawTreeInner(ax, current.right, rightChildPosition[0], rightChildPosition[1])
        return True

    def getRootPositionX(self):
        return int(math.pow(2, self.getLevel()-1)) - 1

    def getLeftChildPosition(self, parentPositionX, parentPositionY):
        distanceX = self.distanceXBetweenChildren(parentPositionY)
        x = parentPositionX-distanceX
        y = parentPositionY-1
        return (x,y)

    def getRightChildPosition(self, parentPositionX, parentPositionY):
        distanceX = self.distanceXBetweenChildren(parentPositionY)
        x = parentPositionX+distanceX
        y = parentPositionY-1
        return (x,y)

    def distanceXBetweenChildren(self, parentPositionY):
        return math.pow(2, parentPositionY-2)

    def convertSecondsToTimeFormat(self, seconds):
        hours = int(seconds) // 60 // 60
        minutes = int(seconds) // 60 % 60
        seconds = int(seconds) % 60
        return '%s:%s:%s' % (hours, minutes, int(seconds))

