# Sistema de Gerenciamento de Consultas Médicas

Este é um projeto de exemplo desenvolvido em Flask, que permite o agendamento de consultas médicas e a listagem de consultas agendadas. Foi criado como parte de um exercício acadêmico para consolidar conhecimentos em desenvolvimento web com Python.


projeto_consultas/
│
├── app/
│   ├── __init__.py         # Inicializa o aplicativo Flask
│   ├── forms.py            # Formulários para o agendamento
│   ├── models.py           # Modelos de banco de dados (Paciente, Consulta)
│   ├── routes.py           # Rotas para interação com o sistema
│   └── templates/          # Arquivos HTML 
│       ├── base.html       # Layout base do sistema
│       ├── agendar_consulta.html # Tela de agendamento
│       └── listar_consultas.html # Tela de listagem
│
├── static/                 # Arquivos estáticos (CSS, imagens)
│   └── style.css           # Estilos personalizados ( Apliquei poucos recursos , mas pode alterar tranquilamente)
│
├── requirements.txt        # Dependências do projeto
├── run.py                  # Script principal para rodar o servidor
└── consultas.db            # Banco de dados SQLite (gerado automaticamente mas podemos aplicar um PostgreSQL ou MySQL , fica ao critério e ao Setup )


---
##Tabelas de Dados

Tabela: Paciente

- id: Identificador único (integer, primary key)
- nome: Nome completo do paciente (string, obrigatório)
- email: Endereço de e-mail (string, único, obrigatório)

Tabela: Consulta
- id: Identificador único (integer, primary key)
- data_hora: Data e hora da consulta (datetime, obrigatório)
- paciente_id: ID do paciente (foreign key para Paciente)

---
## **Funcionalidades**

- **Agendamento de Consultas**: Permite registrar um paciente e agendar uma consulta especificando a data e o horário.
- **Listagem de Consultas**: Exibe as consultas já agendadas, organizadas por data e horário.
- **Banco de Dados**: Armazena informações de pacientes e consultas em um banco SQLite.

---

## **Tecnologias Utilizadas**

- **Backend**: Python 3.11, Flask
- **Frontend**: HTML5, CSS (com Bootstrap)
- **Banco de Dados**: SQLite
- **Outras Bibliotecas**:
  - Flask-WTF (Formulários)
  - SQLAlchemy (ORM)
  - Flask-Bootstrap (Estilo)

---

## **Instalação**

### **Pré-requisitos**
- Python 3.11 instalado no sistema
- Pip para gerenciar pacotes

### **Passos**

- Navegue até o diretório do projeto
- Crie e ative um ambiente virtual

python -m venv venv

- pip install -r requirements.txt
- Inicie o servidor
python run.py

Será acessível via : http://127.0.0.1:5000/
