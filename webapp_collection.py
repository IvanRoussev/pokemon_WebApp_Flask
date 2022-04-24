from flask import Flask, render_template, request, jsonify
from pokemon import Pokemon
from collection import Collection
import json

app = Flask(__name__)


@app.route('/')
def homepage():
    """Homepage
    """
    return '<h1> Welcome to Pokemons type in url which collector you would like to pick </h1>'

#Pokemons HTML Output
@app.route('/<collection_name>')
def vaccinated(collection_name):
    """Route is the name of the collectors for example you can use tim and this route will produce an html output

    Args:
        collection_name (str): name of collector

    Returns:
        _type_: html
    """
    pokemon = Collection(collection_name)
    pokemons_list=[] 

    for items in pokemon.pokemons:
            pokemons_list.append(items.to_dict())

    return render_template('home.html', pokemons=pokemons_list, title='Pokemons')


# JSONIFYs output
@app.route('/json/<collection_name>')
def pokemon_page(collection_name):
    """makes a json output to a webpage of all pokemons in that specific collector

    Args:
        collection_name (str): name

    Returns:
        _type_: json output
    """
    pokemon = Collection(collection_name)
    pokemons_list=[] 

    for items in pokemon.pokemons:
            pokemons_list.append(items.to_dict())

    return jsonify(pokemons_list), 200








if __name__=="__main__":
    app.run(debug=True)