from app import app
from app import app, db

# Aqui vou gerar o banco com os dados e tabelas, para o projeto.
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)