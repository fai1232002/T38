import spacy
nlp = spacy.load('en_core_web_md')

movie_list = {}
with open('movies.txt', 'r', encoding='utf-8') as file:
    for movie in file.readlines():
        movie = movie.strip()
        movie_list[movie[:movie.find(' :')]] = movie[movie.find(':')+1:]

movie_user = {'Planet Hulk':'Will he save their world or destroy it? When the Hulk becomes too dangerous for the '
                            'Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet '
                            'where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he '
                            'is sold into slavery and trained as a gladiator.'}
movie_user_d = nlp(movie_user['Planet Hulk'])

max_k = ''
max_s = 0
for movie_k in movie_list.keys():
    movie_d = nlp(movie_list[movie_k])
    print(f'{movie_k} {movie_d.similarity(movie_user_d)}')
    if movie_d.similarity(movie_user_d) > max_s:
        max_s = movie_d.similarity(movie_user_d)
        max_k = movie_k

print(f'Next movie recommendation is {max_k} & is similarity is {max_s}')
