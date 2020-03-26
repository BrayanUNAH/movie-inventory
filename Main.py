from Classes import *

movie1 = Movie("pelicula1", 1, "Don Juan", "acción", "Hola mundo1")
movie2 = Movie("pelicula2", 2, "Urrutia", "terror", "Hola mundo2")
movie3 = Movie("pelicula3", 3, "Andrade", "drama", "Hola mundo3")
movie4 = Movie("pelicula4", 4, "Felipe", "comedia", "Hola mundo4")

ll = LinkedList()
ll.push(movie1)
ll.push(movie2)
ll.push(movie3)
ll.push(movie4)

ll.remove(1)
print(ll.search(3))

ll.printInventary()
