# config.py

import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')  # Chave secreta para o Flask
    CSRF_SECRET_KEY = os.getenv('CSRF_SECRET_KEY')  # Chave secreta para CSRF
