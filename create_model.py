"""
test

"""


import onehotify

print "Opening and reading training data file"
file = open("training_data.tsv","r")
data = file.read()
file.close()
print "Done reading file\n"

print "Parsing tsv"
data = data.splitlines()
data = [x.split("\t") for x in data[1:]]
print "Done parsing tsv\n"


print "Gathering genres and actors set"
genres = set([y for x in data for y in x[3].split(",")])
actors = set([x[1] for x in data])
print "done gathering genres and actors set\n"


print "Generating one-hot encodings"
genres_encoder, genres_decoder = onehotify.categories_to_onehot_encoders(genres)
actors_encoder, actors_decoder = onehotify.categories_to_onehot_encoders(actors)
print "Denerating one-hot encodings\n"


print "Generating movie_to_actors and movie_to_genres mappings"
movie_to_actors = {}
movie_to_genres = {}
for x in data:
	if x[0] not in movie_to_actors:
		movie_to_actors[x[0]] = set()
	movie_to_actors[x[0]].add(x[1])
	if x[0] not in movie_to_genres:
		movie_to_genres[x[0]] = set()
	movie_to_genres[x[0]].update(set(x[3].split(",")))
print "Done generating movie_to_actors and movie_to_genres mappings\n"


print "Setting up training data"
X_training_data = []
y_training_data = []
for movie in movie_to_genres.keys():
	actors_onehot = onehotify.set_to_onehot(movie_to_actors[movie],actors_encoder)
	genres_onehot = onehotify.set_to_onehot(movie_to_genres[movie],genres_encoder)
	X_training_data.append(actors_onehot)
	y_training_data.append(genres_onehot)
print "Done Setting up training data\n"




from sklearn import ensemble

print "Creating and training model"
model = ensemble.RandomForestClassifier()
model.fit(X_training_data, y_training_data)
print "Done creating and training model\n"




import pickle

print "Saving model"
file = open("genre_by_cast_model.p","wb")
pickle.dump(model,file)
file.close()
file = open("genre_encoding.p","wb")
pickle.dump((genres_encoder, genres_decoder), file)
file.close()
file = open("actors_encoding.p","wb")
pickle.dump((actors_encoder, actors_decoder), file)
file.close()
print "Done saving model\n"



