#!/usr/bin/python3
""" script that starts a Flask web application """
from models import storage, State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_state(id=""):
    """ displays a HTML page:(inside the tag BODY) with list of cities """
    state_obj = storage.all("State")
    city_obj = storage.all("City")
    states = list()
    cities = list()
    for state, value in state_obj.items():
        states.append(value)
    for city, value in city_obj.items():
        cities.append(value)

    state_id = "State.{}".format(id)
    if id is not None and state_id not in state_obj:
        states = None
    return render_template("9-states.html",
                           states=states,
                           cities=cities,
                           id=id)


@app.teardown_appcontext
def close_session(error):
    """ remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    """ Main Function """
    app.run(host="0.0.0.0", port=5000)
