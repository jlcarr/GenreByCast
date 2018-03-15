actors_names_set = ["Kate Winslet"]


from sklearn import tree
import pickle
import onehotify

print "Loading model"
file = open("genre_by_cast_model.p","rb")
model = pickle.load(file)
file.close()
file = open("genre_encoding.p","rb")
genres_encoder, genres_decoder = pickle.load(file)
file.close()
file = open("actors_encoding.p","rb")
actors_encoder, actors_decoder = pickle.load(file)
file.close()
file = open("actors_dicts.p","rb")
name_to_actor,actor_to_name = pickle.load(file)
file.close()
print "Done loading model\n"




actors_set = [name_to_actor[name] for name in actors_names_set]

predictions = model.predict([onehotify.set_to_onehot(actors_set,actors_encoder)])
print "Prediction: "+str([onehotify.onehot_to_set(prediction,genres_decoder) for prediction in predictions])




