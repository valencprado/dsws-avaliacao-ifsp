from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired

class SubjectForm(FlaskForm):
    subject = StringField('Cadastre a nova disciplina e o semestre associado', validators=[DataRequired()])
    semester = RadioField('Selecione semestre', choices=[])
    submit = SubmitField('Cadastrar')
    
    def populate_choices(self):
        from ..models import Semester
        self.semester.choices = [(semester.id, semester.name) for semester in Semester.query.all()]

