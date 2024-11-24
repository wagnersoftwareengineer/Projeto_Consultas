import pytest
from app import app, db
from app.models import Paciente, Consulta

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_agendar_consulta(client):
    response = client.post('/agendar', data={
        'nome_paciente': 'Teste Paciente',
        'email_paciente': 'teste@exemplo.com',
        'data_hora': '2024-12-31 14:00:00'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Consulta agendada com sucesso!' in response.data