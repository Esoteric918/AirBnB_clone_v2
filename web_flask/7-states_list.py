#!/usr/bin/python3
"""Start Flask app"""
from models import storage
from flask import Flask, app, render_template
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def state_list():
    """states list"""
    state = storage.all(State)
    return render_template("7-states_list.html", State=state)


@app.teardown_appcontext
def teardown_db(exception):
    """teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
