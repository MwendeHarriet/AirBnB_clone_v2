#!/usr/bin/python3
"""This script starts flask application"""


from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception):
    """Function removes session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_state():
    """Function list all states by name"""
    my_objects = list(storage.all(State).values())
    my_objects.sort(key=lambda x: x.name)
    return render_template('7-states_list.html', my_objects=my_objects)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
