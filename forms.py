# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired

class AnalisarForm(FlaskForm):
    url = StringField('Insira o link do site', validators=[InputRequired()])
    profundidade = SelectField('Selecione a profundidade', choices=[(1, '1'), (2, '2'), (3, '3'), (0, 'Sem profundidade')])
