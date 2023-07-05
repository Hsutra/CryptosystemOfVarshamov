from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QFileDialog
import ast
import main

Form, Window = uic.loadUiType("decrypt.ui")
app = QApplication([])
window = Window()
window.setFixedSize(700, 500)
form = Form()
form.setupUi(window)
def show():
    window.show()
def downvector():
    filename = QFileDialog.getOpenFileName(None, "Open File", ".", "Text Files (*.txt);;All Files (*)")
    path = filename[0]
    file = open(path, 'r')
    vector = file.readline()
    form.plainTextEdit_3.setPlainText(f"{vector}\n")
    file.close()
def downcodes():
    filename = QFileDialog.getOpenFileName(None, "Open File", ".", "Text Files (*.txt);;All Files (*)")
    path = filename[0]
    file = open(path, 'r')
    codewords = file.readline()
    form.plainTextEdit_3.appendPlainText(f"{codewords}")
    file.close()

def downtext():
    filename = QFileDialog.getOpenFileName(None, "Open File", ".", "Text Files (*.txt);;All Files (*)")
    path = filename[0]
    file = open(path, 'r')
    form.plainTextEdit.setPlainText(file.read())
    file.close()

def decrypt():
    cryptogram = form.plainTextEdit.toPlainText()
    codes = form.plainTextEdit_3.toPlainText()
    m = int(form.plainTextEdit_4.toPlainText())
    e = int(form.plainTextEdit_5.toPlainText())
    splitcodes = codes.splitlines()
    vector = main.str_to_int(splitcodes[0])
    codewords = ast.literal_eval(splitcodes[2])
    crypt = main.decrypt(cryptogram, vector, codewords, m, e)
    form.plainTextEdit_2.setPlainText(f"{crypt}")

form.pushButton.clicked.connect(downvector)
form.pushButton_2.clicked.connect(downtext)
form.pushButton_3.clicked.connect(decrypt)
form.pushButton_4.clicked.connect(downcodes)

if __name__ == '__main__':
    show()
    app.exec_()

