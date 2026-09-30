from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(
    'mysql+pymysql://root:@localhost/meu_banco_legal' 
    # mysql é o banco que será usado e o pymysql é o driver Python que será usado para conectar ao banco
    # root é o usuário atual
    # @localhost é o servidor
    # meu_banco_legal é o banco
    # padrão: mysql+pymysql://usuario:senha@host/banco
)

Base = declarative_base()

class Usuario(Base): # mapeia a tabela 'usuario' do banco para um objeto Python
    __tablename__ = 'usuario' # tabela usuario do meu_banco_legal
    
    ID = Column(Integer, primary_key=True) # coluna ID (chave primária)
    Nome = Column(String(40)) # coluna nome
    Email = Column(String(90)) # coluna email
    Telefone = Column(Integer, nullable=True) # coluna telefone

Session = sessionmaker(bind=engine)
session = Session()

session.add(Usuario(Nome='Guilherme', Email='guilhermezinho@gmail.com', Telefone=121231)) # adiciona o novo usuario
session.commit() # # salva as alterações no banco de dados