#!/usr/bin/python3
""" script that starts a Flask web application """
from models import storage
from models.state import State
from flask import Flask, render_template
from os import environ
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


@app.route('/cities_by_states/')
def cities_by_states():
    """List all cities by states"""
    states = storage.all("State").values()
    result = []
    for state in sorted(states, key=lambda x: x.name):
        result.append([state, state.cities])
    return render_template("8-cities_by_states.html", result=result)


if __name__ == "__main__":
    """ Main Function """
    app.run(host="0.0.0.0", port=5000)
