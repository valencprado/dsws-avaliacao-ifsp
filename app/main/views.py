

from flask import redirect, render_template, url_for, session, current_app
from .. import db
from ..models import Subject, Semester
from .forms import SubjectForm
from . import main
from datetime import datetime, UTC

now = datetime.now(UTC)
@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', now=now)
    
    
@main.route('/disciplinas', methods=['GET', 'POST'])
def subjects():
    subjects = Subject.query.all()
    form = SubjectForm()
    form.populate_choices()
    if form.validate_on_submit():
        subject = Subject.query.filter_by(name=form.subject.data).first()
        semester = form.semester.data
        
        if subject is None:
            
            subject = Subject(name=form.subject.data, semester_id=semester)
            db.session.add(subject)
            db.session.commit()
            session['known'] = False
         

           
        else:
            session['known'] = True

        return redirect(url_for('.subjects'))
    return render_template('subjects.html', form=form,
                           known=session.get('known', False), subjects=subjects)

