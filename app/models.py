
from . import db


class Semester(db.Model):
    __tablename__ = 'semesters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    subjects = db.relationship('Subject', backref='semester', lazy='dynamic')

    def __repr__(self):
        return '<Semester %r>' % self.name


class Subject(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    semester_id = db.Column(db.Integer, db.ForeignKey('semesters.id'))

    def __repr__(self):
        return '<Subject %r>' % self.name