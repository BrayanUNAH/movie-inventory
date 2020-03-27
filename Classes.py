class Movie:
    def __init__(self, movieName, movieDuration, directorName, category, description):
        self.movieName = movieName
        self.movieDuration = movieDuration #convertir a segundos
        self.directorName = directorName
        self.category = category
        self.description = description

    def setNewMovieData(self, movieName, movieDuration, directorName, category, description):
        self.__init__(movieName, movieDuration, directorName, category, description)

    def getMovieName(self): 
        return self.movieName

    def getMovieDuration(self):
        return self.movieDuration
    
    def getDirectorName(self):
        return self.directorName
    
    def getCategory(self):
        return self.category
    
    def getDescription(self):
        return self.description
    

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.first = None

    def push(self, data):
        if not self.first:
            self.first = Node(data)
            return True
        current = self.first
        while current.next:
            current = current.next
        current.next = Node(data)
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

        
        
