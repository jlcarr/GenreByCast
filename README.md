# Genre from Cast

A Python script using scikit-learn and IMDB's datasets to predict the genre of a movie from its leading cast using a decision tree model

## Features
* Uses scikit-learn
* Comes with a pre-made model
* Comes with code to train a new model
* Comes with a pre-filtered dataset
* Comes with code to create a differently filtered dataset
* Simple design and usage

### Data used
Inlcuded is a small subset of IMDB's data used to train the pre-made model.


## Installation
Requires Python 2.7
Requires scikit-learn
Requires onehotify library in the same directory
After that its simply a matter of running the appropriate scripts


## Usage
### Actor Code to Name Conversion
IMDB uses a unique identifier code for every actor in their database. This is used to avoid collisions with actors of the same name. For small subsets of their data collisions can be avoided. Included in this project is a pickled set of dictionaries 
Those dicts can be loaded as follows
```python
>>> import pickle
>>> file = open("actors_dicts.p","rb")
>>> name_to_actor, actor_to_name = pickle.load(file)
>>> file.close()
```
After loading, the dicts can be used to convert actor names to their unique identifiers and vice versa
```python
>>> name_to_actor["Kristen Bell"]
'nm0068338'
>>> actor_to_name["nm0000139"]
'Cameron Diaz'
```

### Using the Model Provided
Included in the project is a premade model. It can be loaded into Python using pickle.
```python
>>> import pickle
>>> file = open("genre_by_cast_model.p","rb")
>>> model = pickle.load(file)
>>> file.close()
>>> file = open("genre_encoding.p","rb")
>>> genres_encoder, genres_decoder = pickle.load(file)
>>> file.close()
>>> file = open("actors_encoding.p","rb")
>>> actors_encoder, actors_decoder = pickle.load(file)
>>> file.close()
>>> file = open("actors_dicts.p","rb")
>>> name_to_actor,actor_to_name = pickle.load(file)
>>> actors_encoder, actors_decoder = pickle.load(file)
>>> file.close()
```
After loading it can be used to make predictions
```python
>>> import onehotify
>>> actors_set = [name_to_actor["Seth Rogen"],name_to_actor["Anna Kendrick"]]
>>> predictions = model.predict([onehotify.set_to_onehot(actors_set,actors_encoder)])
>>> [onehotify.onehot_to_set(prediction,genres_decoder) for prediction in predictions]
[set(['Comedy'])]
```

### Creating and Training the Model
You can train your own model, which will be saved to the genre_by_cast.p pickle file, which will hold an scikit-learn DecisionTreeClassifier object. Building your own model is done by change the data in the file training_data.tsv and editing the parameters of the model in create_model.py
Afterwards it can by trained by running the create_model.py scipt

```console
$ python create_model.py
```
