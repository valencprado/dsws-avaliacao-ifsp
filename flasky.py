import os
import click
from flask_migrate import Migrate
from app import create_app, db
from app.models import Subject, Semester
from flask import render_template
from datetime import datetime, UTC
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

now = datetime.now(UTC)
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Subject=Subject, Semester=Semester)


@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', now=now), 404
