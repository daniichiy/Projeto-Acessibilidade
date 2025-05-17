from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv
import datetime

load_dotenv()  # Carregar variáveis do arquivo .env

# Carregar a URL de conexão do banco
DATABASE_URL = os.getenv("DATABASE_URL")

# Criar uma base para definir os modelos
Base = declarative_base()

# Definir a tabela 'relatorios'
class Relatorio(Base):
    __tablename__ = 'relatorios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_arquivo = Column(String(255), nullable=False)
    caminho_arquivo = Column(String, nullable=False)
    data_criacao = Column(DateTime, default=datetime.datetime.utcnow)
    total_imagens = Column(Integer)
    imagens_sem_alt = Column(Integer)

# Criar a conexão com o banco
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def criar_tabela():
    """Cria as tabelas no banco, se não existirem"""
    Base.metadata.create_all(engine)

def salvar_relatorio(nome_arquivo, caminho_arquivo, total_imagens, imagens_sem_alt):
    """Salva o relatório no banco de dados"""
    session = SessionLocal()
    novo_relatorio = Relatorio(
        nome_arquivo=nome_arquivo,
        caminho_arquivo=caminho_arquivo,
        total_imagens=total_imagens,
        imagens_sem_alt=imagens_sem_alt
    )
    session.add(novo_relatorio)
    session.commit()  # Salva no banco
    session.close()

def buscar_relatorios():
    """Consulta todos os relatórios no banco"""
    session = SessionLocal()
    relatorios = session.query(Relatorio).order_by(Relatorio.data_criacao.desc()).all()
    session.close()
    return relatorios
