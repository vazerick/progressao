import sys
import sass

# import do PyQt5

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt

# import das janelas

from ui.main import Ui_MainWindow as Main


class gui:

    def __init__(self):
# declarações da interface gráfica
        print("Gerando a interface gráfica")

        self.app = QApplication(sys.argv)

# janela principal
        self.wMain = QMainWindow()
        self.ui = Main()
        self.ui.setupUi(self.wMain)        
        
# seta a mesma folha de estilos e bloqueio para todas as janelas

        tema = sass.compile(filename="ui/style.scss")
        print("Gera o tema", tema)

        for janela in [
            self.wMain            
        ]:
            janela.setStyleSheet(tema)
            janela.setWindowModality(Qt.ApplicationModal)       

# inicializa a janela
        self.wMain.show()
