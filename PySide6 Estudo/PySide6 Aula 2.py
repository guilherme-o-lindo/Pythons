from PySide6.QtWidgets import (QApplication, QPushButton, QMainWindow, 
                               QLabel, QLineEdit, QVBoxLayout, QWidget)
import sys

class MyWindow(QMainWindow):
    def __init__(self, titulo: str): # O que fazer quando o objeto for criado
        super().__init__() # Inicializa a classe QMainWindow
        
        self.show() # Mostra a janela
        
        # LABEL
        self.lbl = QLabel('Escreva algo!') # Serve para mostrar informações, não é interativo
        self.txt = QLineEdit() # Permite o usuário digitar algo na interface
        #self.txt.textChanged.connect(self.lbl.setText) # Quando o texto mudar, define o label como o texto alterado
        
        # BUTTON
        self.button = QPushButton('Clique aqui!') # Cria o botão
        self.button.setCheckable(False) # Define se o botão fica 'ligado' ou 'desligado'
        
        self.button.clicked.connect(self.execute) # Conecta uma função ao apertar o botão
        
        # LAYOUT
        layout = QVBoxLayout() # Organiza os widgets em coluna, cuida do posicionamento deles automaticamente
        layout.addWidget(self.txt) # Adiciona o widget
        layout.addWidget(self.lbl) # Adiciona o widget
        layout.addWidget(self.button) # Adiciona o widget
        
        # CONTAINER
        container = QWidget() # Cria uma janela simples
        container.setLayout(layout) # Coloca o layout com os widgets na janela
        
        self.setCentralWidget(container) # Mostra o container/janela como o widget central do app
        
    def execute(self):
        print('Botão pressionado com sucesso!')
        
        self.lbl.setText(self.txt.text()) # Pega o label e faz com que apareça escrito o texto do txt
        
app = QApplication(sys.argv) # Cria o aplicativo
window = MyWindow('Programa legal') # Usa a classe MyWindow e cria o objeto window

app.exec() # Executa o aplicativo em loop