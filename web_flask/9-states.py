#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
from models import storage
from flask import render_template
from models.state import State
from models.city import City
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def states(id=None):
    """ Index to display lists """
    states = storage.all(State)
    cities = storage.all(City)
    cities_l = {}
    states_l = {}
    for key, value in cities.items():
        cities_l[value.name] = value
    for key, value in states.items():
        states_l[value.name] = value
    if id is None:
        return render_template('9-states.html', states_l=states_l, id=id)
    else:
        count = 0
        state_name = ""
        for value in states.values():
            if value.id == id:
                count += 1
                state_name = value.name
        return render_template('9-states.html', state_name=state_name,
                               cities_l=cities_l, id=id, count=count)


@app.teardown_appcontext
def close(states):
    ''' Close the connection with db '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
