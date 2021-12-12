#!/usr/bin/python3
"""Start Flask app"""
from models import storage
from flask import Flask, app, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """states list"""
    res = []
    storage.reload()

    for v in storage.all("States").values():
        res.append([v.id, v.name])
    return render_template("7-states_list.html", states=res)


@app.teardown_appcontext
def teardown_db(exception):
    """teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
