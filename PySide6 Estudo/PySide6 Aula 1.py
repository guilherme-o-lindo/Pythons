from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow
from PySide6.QtCore import Qt, QSize
import sys

class MyWindow(QMainWindow):
    def __init__(self, titulo: str): # O que fazer quando o objeto for criado
        super().__init__() # Inicializa a classe QMainWindow
        
        self.titulo = titulo
        self.setWindowTitle(self.titulo) # Define o titulo da janela de acordo com a variável titulo
        self.setFixedSize(QSize(400, 300)) # Define o tamanho da janela
        
        self.showMaximized() # Mostra a janela maximizada, cria a relação com o QApplication
        
        self.button = QPushButton('Clique aqui!') # Cria o botão
        self.setCentralWidget(self.button) # Se torna o widget principal da tela
        self.button.setCheckable(True) # Define se o botão fica 'ligado' ou 'desligado'
        
        self.button.clicked.connect(self.execute_button) # Conecta uma função ao apertar o botão
        
    def execute_button(self):
        print('Botão pressionado com sucesso!')
        
app = QApplication(sys.argv) # Cria o aplicativo
window = MyWindow('Programa legal') # Usa a classe MyWindow e cria o objeto window

app.exec() # Executa o aplicativo em loop