import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QCheckBox, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Checkbox')
        
        self.check = QCheckBox('Esse é o meu checkbox: ') # Cria o botão de check
        self.setCentralWidget(self.check) # Define o botão de check como o principal widget da janela principal
        
        self.check.stateChanged.connect(self.mostrar_state) # Se o botão mudar de estado, roda a função mostrar_state
        
        self.show()
    def mostrar_state(self):
       if self.check.isChecked(): # Verifica se o botão de check está marcado, caso não, executa o else
           print('A checkbox está marcada!')
       else:
           print('A checkbox não está marcada!')
        
app = QApplication(sys.argv)

window = MainWindow()

app.exec()