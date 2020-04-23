#!/usr/bin/python3
""" script that starts a Flask web application """
from models import storage
from models.state import State
from os import environ
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_session(error):
    """ remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ display a HTML page: (inside the tag BODY) """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    return render_template("7-states_list.html", states=states)


@app.route('/cities_by_states')
def cities_by_states():
    """all cities by states"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    result = []
    for state in states:
        result.append([state, sorted(state.cities, key=lambda k: k.name)])
    return render_template("8-cities_by_states.html", states=result)


if __name__ == "__main__":
    """ Main Function """
    app.run(host="0.0.0.0", port=5000)
