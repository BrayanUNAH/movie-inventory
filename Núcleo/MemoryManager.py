# -*- coding: 'utf-8' -*-

from Núcleo.LinkedList import LinkedList
from Núcleo.Movie import Movie
import json
import os

class MemoryManager:
    def __init__(self):
        self.memoryPath = 'Memory\\memory.json'
        os.makedirs('Memory', exist_ok=True)

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


