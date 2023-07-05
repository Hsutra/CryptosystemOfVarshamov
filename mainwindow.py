from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import decrypt
import encrypt

Form, Window = uic.loadUiType("main.ui")
app = QApplication([])
window = Window()
window.setFixedSize(700, 500)
form = Form()
form.setupUi(window)
window.show()

form.pushButton.clicked.connect(encrypt.show)
form.pushButton_2.clicked.connect(decrypt.show)

if __name__ == '__main__':
    app.exec_()
