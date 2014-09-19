#!/usr/bin/env python
import os
from app import create_app, setup_app
from flask import request, g
from flask.ext.script import Manager, Shell
from app.structures.LocationsKDTree import LocationsKDTree
from app.structures.InvertedPointLocationIndex import InvertedPointLocationIndex

env_configuration = os.getenv('FLASK_CONFIG') if os.getenv('FLASK_CONFIG') else 'default'
print os.getenv('FLASK_CONFIG')

app = create_app(env_configuration)

print "Running the " + env_configuration + " configuration ..."
setup_app(env_configuration)
print "Finished running the " + env_configuration + " configuration ..."

manager = Manager(app)

invertedPointLocationIndex = InvertedPointLocationIndex()
invertedPointLocationIndex.build_inverted_location_index()

filmLocationsKDTree = LocationsKDTree()
filmLocationsKDTree.load_point_data()
filmLocationsKDTree.build_kd_tree()

@app.before_request
def before_request():
    print "before request ..."
    g.filmlocationsKDTree = filmLocationsKDTree
    g.invertedPointLocationIndex = invertedPointLocationIndex

def make_shell_context():
    return dict(app=app)

manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()

