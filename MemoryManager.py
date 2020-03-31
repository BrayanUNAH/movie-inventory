# -*- coding: 'utf-8' -*-
from LinkedList import LinkedList
from Movie import Movie
import json
import os

class MemoryManager:
    def __init__(self):
        self.memoryPath = 'memory\\memory.json'
        os.makedirs('memory', exist_ok=True)

    def saveLinkedList(self, linkedList, totalItems):
        memoryFile = open(self.memoryPath, 'w')
        dictTosave = {}
        for item in range(totalItems):
            auxDict = {item: linkedList.search(item).value.getVariablesDict()}
            dictTosave.update(auxDict)
        jsonFile = json.dumps(dictTosave)
        memoryFile.write(jsonFile)
        memoryFile.close()

    def loadLinkedList(self):
        memoryFile = open(self.memoryPath, 'r')
        jsonLinkedList = json.load(memoryFile)
        linkedList = LinkedList()
        for item in jsonLinkedList.values():
            movie = []
            for value in item.values():
                movie.append(value)      
            linkedList.push(Movie(movie[0], movie[1], movie[2], movie[3], movie[4]))
        memoryFile.close()
        return linkedList

"""ll = LinkedList()
movie1 = Movie("lkjd", "2", "kdf", "kfldj", "dkfj")
movie2 = Movie("lkjd", "4", "kdf", "kfldj", "dkfj")
movie3 = Movie("lkjd", "1", "kdf", "kfldj", "dkfj")
ll.push(movie1)
ll.push(movie2)
ll.push(movie3)

memory = MemoryManager()
memory.saveLinkedList(ll, ll.getTotalItems())
memory.loadLinkedList()"""

