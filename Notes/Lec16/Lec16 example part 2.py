""" Create two dictionaries from IMDB for easy look up
    and ask for an actor or movie name repeatedly and
    print relevant info


    Dictionaries: 
        actors: key: name, value: set of movies
        movies: key: movie, value: set of actors in that movie

"""

def read_values():
    actors = {} #actor dictionary
    movies = {} #movie dictionary

    for line in open("imdb_data.txt"):
        m = line.strip().split("|")
    
        for i in range(len(m)):
            m[i] = m[i].strip() ## strip space of split values

        actor = m[0]
        movie = m[1]
    
        if actor in actors:
            actors[actor].add( movie )
        else:
            actors[actor] = set( [movie] )
     
        if movie in movies:
            movies[movie].add( actor )
        else:
            movies[movie] = set( [actor] )
    return actors, movies

def find_degree(actor, actors, movie):
    if actor == 'Bacon, Kevin':
        return 0
    moviesforbacon = actors['Bacon, Kevin']
    degree1 = set([])
    for movie in moviesforbacon:
        actorset = movies[movie]
        degree1 |= actorset
    degree1 = degree1 - set(['Bacon, Kevin'])
    
    if actor in degree1:
        return 1

if __name__ == "__main__":
    actors, movies = read_values()

    while True:
        actor = raw_input("Actor name (stop to end) => ")
        if actor == 'stop':
            break
        if actor not in actors:
            print "Actor not found"
        else:
            deg = find_degree(actor, actors, movies)
            if deg == None:
                print "Degree is above 1"  #for actors not in list or don't meet the condition
            else:
                print "Degree is", deg
