from APP.separador import Organizador
from PySide2.QtWidgets import QApplication, QDialog, QFileDialog, QLabel,QMainWindow, QMessageBox, QPushButton
import sys


class MAIN(QMainWindow):
    def __init__(self):
        super().__init__()
        self.logica = Organizador()
        self.link = 'False'

        self.label = QLabel('Selecione a "Pasta" que deseja organizar!',self)
        self.label.setGeometry(100,50,400,20)
        self.label.setObjectName('Label')
        self.btn = QPushButton(' ./',self)
        self.btn.setObjectName('Button')
        self.btn.setGeometry(55,120,400,20)
        self.btn.clicked.connect(self.get_dir)

        self.btn_start = QPushButton('Organizar',self)
        self.btn_start.setObjectName('Start')
        self.btn_start.setGeometry(455,120,70,20)
        self.btn_start.clicked.connect(self.start)

        self.config()
    def config(self):
        self.resize(600,200)
        self.setWindowTitle('Organizador')
        self.setObjectName('MAIN')
        with open('./APP/style.css') as CSS:
            self.setStyleSheet(CSS.read())
        self.show()
    def get_dir(self):
        link = QFileDialog(self).getExistingDirectory()
        if link == '':
            self.link = 'False'
            self.btn.setText(' ./')
        else:
            self.link = link
            self.btn.setText(link)

    def start(self):
        if self.link != 'False':
            self.logica.create_directory(self.link)
            x = QMessageBox(self)
            x.setText('Pronto!')
            x.exec_()
            
        else:
            x = QMessageBox(self)
            x.setText('Nem um diretorio selecionado!')
            x.exec_()

        
def run():
    app = QApplication(sys.argv)
    main = MAIN()
    sys.exit(app.exec_())

