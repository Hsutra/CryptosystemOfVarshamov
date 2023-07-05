from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox
import ast
import main

Form, Window = uic.loadUiType("encrypt.ui")
app = QApplication([])
window = Window()
window.setFixedSize(700, 500)
form = Form()
form.setupUi(window)

def show():
    window.show()

def error(text):
    err = QMessageBox()
    err.setWindowTitle("Ошибка")
    err.setText(text)
    err.setIcon(QMessageBox.Warning)
    err.exec_()

def genvectors():
    if form.plainTextEdit.toPlainText() == '' or form.plainTextEdit_2.toPlainText() == '' or form.plainTextEdit_3.toPlainText() == '':
        error("Вы не заполнили все поля!")
    elif int(form.plainTextEdit_3.toPlainText()) < int(form.plainTextEdit.toPlainText()):
        error("Число а не должно быть больше длины кода n")
    elif int(form.plainTextEdit_2.toPlainText()) < 0 or int(form.plainTextEdit_2.toPlainText()) > 9:
        error("Разрадность p должна быть от 0 до 9")
    else:
        file = open("closedvector.txt", "w")
        file2 = open("openvector.txt", "w")
        vector = main.genvector(int(form.plainTextEdit_3.toPlainText()), int(form.plainTextEdit_2.toPlainText()))
        secKey = main.gensec(vector)
        vectorB = main.genopenvector(vector, secKey[0], secKey[1])
        file.write(f"{vector}\n{secKey}")
        file2.write(f"{vectorB}")
        file.close()
        file2.close()

def gencodes():
    if form.plainTextEdit.toPlainText() == '' or form.plainTextEdit_2.toPlainText() == '' or form.plainTextEdit_3.toPlainText() == '':
        error("Вы не заполнили все поля!")
    elif int(form.plainTextEdit_3.toPlainText()) < int(form.plainTextEdit.toPlainText()):
        error("Число а не должно быть больше длины кода n")
    elif int(form.plainTextEdit_2.toPlainText()) < 0 or int(form.plainTextEdit_2.toPlainText()) > 9:
        error("Разрадность p должна быть от 0 до 9")
    else:
        file = open("codes.txt", "w")
        codes = main.gencodes(int(form.plainTextEdit_3.toPlainText()), int(form.plainTextEdit_2.toPlainText()), int(form.plainTextEdit.toPlainText()))
        file.write(f"{codes}")
        file.close()

def downvector():
    filename = QFileDialog.getOpenFileName(None, "Open File", ".", "Text Files (*.txt);;All Files (*)")
    path = filename[0]
    file = open(path, 'r')
    vector = file.readline()
    form.plainTextEdit_5.setPlainText(f"{vector}")
    file.close()
def downcodes():
    filename = QFileDialog.getOpenFileName(None, "Open File", ".", "Text Files (*.txt);;All Files (*)")
    path = filename[0]
    file = open(path, 'r')
    codewords = file.readline()
    form.plainTextEdit_5.appendPlainText(f"{codewords}")
    file.close()

def downtext():
    filename = QFileDialog.getOpenFileName(None, "Open File", ".", "Text Files (*.txt);;All Files (*)")
    path = filename[0]
    file = open(path, 'r')
    form.plainTextEdit_4.setPlainText(file.read())
    file.close()

def encrypt():
    plaintext = form.plainTextEdit_4.toPlainText()
    codes = form.plainTextEdit_5.toPlainText()
    if not codes:
        error("Загрузите кодовые слова и ключ")
    elif not plaintext:
        error("Введите или загрузите текст!!")
    else:
        codes = codes.splitlines()
        vector = main.str_to_int(codes[0])
        print(vector)
        codewords = ast.literal_eval(codes[2])
        file = open("Cryptogram.txt", "w")
        crypt = main.encrypt(plaintext, vector, codewords)
        file.write(f"{crypt}")
        err = QMessageBox()
        err.setWindowTitle("Успех")
        err.setText("Сообщение было зашифровано!")
        err.exec_()
        file.close()

form.pushButton.clicked.connect(genvectors)
form.pushButton_2.clicked.connect(downvector)
form.pushButton_3.clicked.connect(downtext)
form.pushButton_4.clicked.connect(encrypt)
form.pushButton_5.clicked.connect(gencodes)
form.pushButton_6.clicked.connect(downcodes)

if __name__ == '__main__':
    show()
    app.exec_()
