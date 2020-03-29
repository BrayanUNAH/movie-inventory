class Movie:
    def __init__(self, movieName, movieDuration, directorName, category, description):
        self.movieName = movieName
        self.movieDuration = movieDuration  # convertir a segundos
        self.directorName = directorName
        self.category = category
        self.description = description

    def setNewMovieData(self, movieName, movieDuration, directorName, category, description):
        self.__init__(movieName, movieDuration,
                      directorName, category, description)

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
