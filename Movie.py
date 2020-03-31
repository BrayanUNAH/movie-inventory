# -*- coding: 'utf-8' -*-
class Movie:
    def __init__(self, movieName, movieDuration, directorName, category, description):
        self.movieName = movieName
        self.movieDuration = movieDuration  # convertir a segundos
        self.directorName = directorName
        self.category = category
        self.description = description


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

    def getVariableList(self):
        return [self.movieName,
                self.movieDuration,  # convertir a segundos
                self.directorName,
                self.category,
                self.description]

    def getVariablesDict(self):
        variableDict = {0: self.movieName,
                        1: self.movieDuration,
                        2: self.directorName,
                        3: self.category,
                        4: self.description
                        }
        return variableDict
        
