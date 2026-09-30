import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QComboBox, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ComboBox')
        
        cb = QComboBox() # Cria a caixa de escolha
        cb.addItems(['Brigadeiro', 'Ninho com nutella', 'Beijinho']) # Define os elementos que podem ser escolhidos na caixa
        self.setCentralWidget(cb) # Define a caixa de escolha como o principal widget do main window
        
        # cb.currentTextChanged.connect(self.mostrar_texto_escolhido) # Roda a função mostrar_texto_escolhido quando o elemento selecionado na caixa muda
        cb.activated.connect(lambda index: self.mostrar_texto_escolhido(cb.itemText(index)))
        # actived -- dispara sempre que o usuário clica em algum item da lista
        # .connect -- conecta o evento de disparar (actived) à uma função (nesse caso lambda)
        # lambda index: -- função anônima (não tem nome) de linha unica, recebe o parametro index (indice do item clicado, enviado pelo activated)
        # cb.itemText(index) -- pega o texto do indice que foi passado pelo index
        # self.mostrar_texto_escolhido() -- pega a função que da print no texto escolhido pelo usuário
    
        self.show()
        
    def mostrar_texto_escolhido(self, texto): # O primeiro valor é o self e o segundo é o texto definido pelo usuário
        print(texto)
app = QApplication(sys.argv)

window = MainWindow()

app.exec()