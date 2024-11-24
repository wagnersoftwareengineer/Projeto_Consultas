from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class AgendarConsultaForm(FlaskForm):
    nome_paciente = StringField('Nome do Paciente', validators=[DataRequired()])
    email_paciente = StringField('Email do Paciente', validators=[DataRequired(), Email()])
    data = StringField('Data da Consulta (dd/mm)', validators=[DataRequired()])
    hora = StringField('Hora da Consulta (hh:mm)', validators=[DataRequired()])
    submit = SubmitField('Agendar')
