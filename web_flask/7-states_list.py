#!/usr/bin/python3
"""
a script that starts a Flask web application
"""

from flask import Flask, abort, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def main():
    ''' Main page Content '''
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(states):
    ''' Close the connection with db '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
