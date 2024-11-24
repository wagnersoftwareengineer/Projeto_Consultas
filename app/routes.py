from flask import render_template, redirect, url_for, flash
from app import app, db
from app.models import Paciente, Consulta
from app.forms import AgendarConsultaForm
from datetime import datetime

@app.route("/", methods=["GET", "POST"])
@app.route("/agendar", methods=["GET", "POST"])
def agendar_consulta():
    form = AgendarConsultaForm()
    if form.validate_on_submit():
        # Obter os valores diretamente do formulário
        data_str = form.data.data  # Data no formato 'YYYY-MM-DD'
        hora_str = form.hora.data  # Hora no formato 'HH:MM'

        # Combinar data e hora em um único objeto datetime
        data_hora = datetime.strptime(f"{data_str} {hora_str}", "%Y-%m-%d %H:%M")

        # Processar o restante do código para salvar no banco de dados
        paciente = Paciente.query.filter_by(email=form.email_paciente.data).first()
        if not paciente:
            paciente = Paciente(nome=form.nome_paciente.data, email=form.email_paciente.data)
            db.session.add(paciente)
            db.session.commit()
        nova_consulta = Consulta(data_hora=data_hora, paciente=paciente)
        db.session.add(nova_consulta)
        db.session.commit()

        flash('Consulta agendada com sucesso!', 'success')
        return redirect(url_for('listar_consultas'))
    return render_template('agendar_consulta.html', form=form)

@app.route("/consultas")
def listar_consultas():
    consultas = Consulta.query.all()
    return render_template('listar_consultas.html', consultas=consultas)
