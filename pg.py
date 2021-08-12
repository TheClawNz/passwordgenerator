import random
import string
import pyperclip
from PyQt5 import QtWidgets
from passwordgenerator import Ui_MainWindow

class Arayuz(QtWidgets.QMainWindow, Ui_MainWindow): 
    length = 5
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        # Toplama vb
        self.buttonGenerate.clicked.connect(self.generate)
        self.buttonCopy.clicked.connect(self.copy)  

    # Herhangi bir rakam butonuna basıldığında çalışacak fonksiyon
    def generate(self):
        self.password.setText(generatePassword(int(self.spinBox.text())))

    def copy(self):
        pyperclip.copy(str(self.password.text())) 
 
def generatePassword(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    letters = random.sample(lower + upper + num + symbols, length)
     
    return "".join(letters)