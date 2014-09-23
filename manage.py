#!/usr/bin/env python
import os
from app import create_app, setup_app
from flask import request, g, render_template
from flask.ext.script import Manager, Shell
from app.structures.LocationsKDTree import LocationsKDTree
from app.structures.InvertedPointLocationIndex import InvertedPointLocationIndex

env_configuration = os.getenv('FLASK_CONFIG') if os.getenv('FLASK_CONFIG') else 'default'
print os.getenv('FLASK_CONFIG')

#   Create Flask Application
app = create_app(env_configuration)

print "Running the " + env_configuration + " configuration ..."
setup_app(env_configuration)
print "Finished running the " + env_configuration + " configuration ..."

#   Manager to manage large-scale Flask apps
manager = Manager(app)

#   An inverted index, mapping UTM (Universal Transverse Mercator) lat/lng
#   values geolocating each film, to a LIST of films that were filmed
#   at that location.
#
#   IMPORTANT!:  This is a shared data-structure, built only at startup,
#   that is READ-ONLY by all, and so can be safely shared.
invertedPointLocationIndex = InvertedPointLocationIndex()
invertedPointLocationIndex.build_inverted_location_index()

#   A KD tree, implemented using the scipy package's kdtree implementation
#   under the hood, to allow for fast O(ln) queries of 2D point data.  The
#   points that it stores are geocoded locations coded in UTM to allow them
#   to be treated as 2D points to an approximation.
#
#   IMPORTANT!:  This is a shared data-structure, built only at startup,
#   that is READ-ONLY by all, and so can be safely shared.
filmLocationsKDTree = LocationsKDTree()
filmLocationsKDTree.load_point_data()
filmLocationsKDTree.build_kd_tree()

#   If the request is for the endpoint 'films_near_me,' which is seeking
#   the 7 films closest to a user's location, only then do we bother to
#   load the request with the globally existing KD tree and inverted
#   index.
@app.before_request
def before_request():
    print "before request ..."
    if request.endpoint == 'films_near_me':
        g.filmlocationsKDTree = filmLocationsKDTree
        g.invertedPointLocationIndex = invertedPointLocationIndex

def make_shell_context():
    return dict(app=app)

manager.add_command("shell", Shell(make_context=make_shell_context))

#   This allows us to run all tests via the command:
#   'manage.py test'
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()

