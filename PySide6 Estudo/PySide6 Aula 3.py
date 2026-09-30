import sys
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # MAIN WINDOW
        self.setWindowTitle('Jimmy Neutron')       
        
        # IMAGEM
        widget = QLabel() # Cria um label, que pode exibir texto ou imagem
        
        widget.setPixmap(QPixmap(r"C:\Users\User\Documents\PySide6 Estudo\Jimmy Neutron.png")) # Define o conteudo do label como uma imagem, no caso o JImmy Neutron.png
        widget.setScaledContents(True) # Faz a imagem redimensionar junto com o tamanho do QLabel, como o QLabel estará como widget principal, o tamanho da imagem será o tamanho da janela
        
        # LAYOUT & CONTAINER
        layout = QVBoxLayout()
        layout.addWidget(widget)
        
        container = QWidget() # Cria um container (widget para organizar outros widgets), com possibilidades de colocar varios widgets dentro dele (layout)
        container.setLayout(layout) # Adiciona o layout ao container
        self.setCentralWidget(container) # Torna o container o widget principal da janela principal
        
        self.show()
        
app = QApplication(sys.argv)

window = MainWindow()

app.exec()