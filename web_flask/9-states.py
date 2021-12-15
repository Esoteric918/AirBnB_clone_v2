#!/usr/bin/python3
"""flask app for states"""


from flask import Flask, render_template
from flask.scaffold import F
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/cities_by_states")
def states(id=None):
    """list of states"""
    storage.reload()
    states = storage.all(State)

    if id:
        states = states.get('State.{}'.format(id))
    return render_template('9-states.html', State.states)


@app.teardown_appcontext
def teardown(context):
    """teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
