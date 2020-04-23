#!/usr/bin/python3
""" script that starts a Flask web application """
from models import storage
from models.state import State
from os import getenv
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_state(id=""):
    """ displays a HTML page:(inside the tag BODY) with list of cities """
    states = storage.all("State")
    if id_d == "all":
        return render_template("9-states.html", state="all", name="States",
                               states=states.values())
    else:
        flag = False
        for k, v in states.items():
            if k == id_d:
                flag = True
                break
        if flag:
            result = v.cities
            return render_template("9-states.html", state="1",
                                   name="State: {}".format(v.name),
                                   states=result)
        else:
            return render_template("9-states.html", state="",
                                   name="Not found!",
                                   states=states)


@app.teardown_appcontext
def close_session(error):
    """ remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    """ Main Function """
    app.run(host="0.0.0.0", port=5000)
