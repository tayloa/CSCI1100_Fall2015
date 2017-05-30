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

if __name__ == "__main__":
    actors, movies = read_values()

    while True:
        cmd = raw_input("1 to search actor, 2 to search movie => ")
        if cmd not in ['1','2']:
            break
        if cmd == '1':
            actor = raw_input("Actor name => ")
            if actor in actors:
                print "Actor %s found" %actor
                for movie in actors[actor]:
                    print movie
        elif cmd == '2':
            movie = raw_input("Movie name => ")
            if movie in movies:
                print "Movie %s found" %movie
                for actor in movies[movie]:
                    print actor
        print