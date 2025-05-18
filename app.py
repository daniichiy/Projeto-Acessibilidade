# app.py

from flask import Flask
from config import Config
from routes import index

# Criando o aplicativo Flask
app = Flask(__name__)

# Carregar a configuração
app.config.from_object(Config)

# Definindo a rota
app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])

# Rodar o servidor Flask
if __name__ == "__main__":
    app.run(debug=True)
