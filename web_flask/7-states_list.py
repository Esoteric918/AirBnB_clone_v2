#!/usr/bin/python3
"""Start Flask app"""
from models import storage
from flask import Flask, app, render_template
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def stateList():
    """states list"""
    storage.reload()
    state = storage.all(State)
    return render_template("7-states_list.html", States=state)


@app.teardown_appcontext
def teardown_db(context):
    """teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
