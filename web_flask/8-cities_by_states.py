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


@app.route('/cities_by_states')
def cities_by_states():
    """ Index to display lists """
    states = storage.all(State)
    cities = storage.all(City)
    cities_list = {}
    states_list = {}
    for key, value in cities.items():
        cities_list[value.name] = value
    for key, value in states.items():
        states_list[value.name] = value
    return render_template('8-cities_by_states.html', states_list=states_list,
                           cities_list=cities_list)


@app.teardown_appcontext
def close(states):
    ''' Close the connection with db '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
