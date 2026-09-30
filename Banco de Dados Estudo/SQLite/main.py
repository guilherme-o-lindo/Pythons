from sqlalchemy import create_engine # create_engine cria uma conexão para se conectar ao banco ou um novo banco de dados vazio
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey

from sqlalchemy.orm import sessionmaker, declarative_base
# sessionmaker → cria uma "fábrica de sessões"
#   - Sessão = área de trabalho temporária
#   - É nela que você adiciona, altera ou deleta registros
#   - Só depois você "confirma" as mudanças com session.commit()

# declarative_base → cria a base para definir classes
#   - Cada classe que você criar com essa base herdada virará automaticamente uma tabela no banco
#   - Os atributos da classe viram colunas da tabela
#   - Os objetos da classe viram registros (linhas) na tabela

db = create_engine('sqlite:///banco_legal.db')
# sqlite indica qual tipo de banco de dados vai usar (nesse caso o SQLite)
# as /// indica que estará no  mesmo lugar desse script (main.py)
# banco_legal.db é o nome do banco

Session = sessionmaker(bind=db) # Chama a função sessionmaker que retorna uma função para criar um objeto sessão e liga ao banco de dados
session = Session() # Chama a função e cria uma instância base da qual você herda para definir suas tabelas

Base = declarative_base() # É a classe que permite transformar uma classe python em uma tabela

# Tabela
class Usuário(Base): # Vai herdar de Base
    __tablename__ = 'Usuários'
    
    Id = Column('ID', Integer, primary_key=True) # cria uma coluna, a nomeia e depois passa o tipo de registro que ela deve receber, e primary_key indica o que vai diferenciar um registro de outro
    Nome = Column('NOME', String)
    Idade = Column('IDADE', Integer)
    Email = Column('EMAIL', String)
    Senha = Column('SENHA', String)
    Ativo = Column('ATIVO', Boolean)
    
    def __init__(self, Nome, Idade, Email, Senha, Ativo=True):
        self.Nome = Nome
        self.Idade = Idade
        self.Email = Email
        self.Senha = Senha
        self.Ativo = Ativo
    
class Livro(Base):
    __tablename__ = 'Livros'
    
    Id = Column('ID', Integer, primary_key=True)
    Titulo = Column('TÍTULO', String)
    Paginas = Column('PÁGINAS', Integer)
    Dono = Column('DONO', ForeignKey('Usuários.ID')) # Pega a variável id da tabela usuários, impedindo colocar um valor diferente dentro de Usuários.Id
    
    def __init__(self, Titulo, Paginas, Dono):
        self.Titulo = Titulo
        self.Paginas = Paginas
        self.Dono = Dono

Base.metadata.create_all(bind=db) # Cria as tabelas definidas pelo declarative_base

# C - Create
#usuario = Usuário(Nome='Guilherme', Idade=15, Email='guilherme.silva@gmail.com', Senha='senha123') # Cria o usuário Guilherme
#session.add(usuario) # Adiciona o Guilherme à sessão atual
#session.commit() # Envia a sessão atual com o Guilherme nela ao banco de dados banco_legal

# R - Read
lista_usuários = session.query(Usuário).all() # Indica qual tabela vai pegar, nesse caso a tabela usuário com todos os usuários
#primeiro_item_usuários = session.query(Usuário).first() # Pega somente o primeiro usuário, nesse caso
#usuario_Guilherme = session.query(Usuário).filter_by(Id=3).first()
#print(usuario_Guilherme.Id)
#print(usuario_Guilherme.Nome)
#for Guilherme in lista_usuários:
#    print(Guilherme.Id)

#print(lista_usuários)
#print(primeiro_item_usuários)

# U - Update
#usuario_Guilherme.Nome = 'João Bosco'
#session.add(usuario_Guilherme)
#session.commit()

# D - Delete
#session.delete(usuario_Guilherme)
#session.commit()