import sys
from PyQt5.QtWidgets import QApplication
from pg import Arayuz

application = QApplication(sys.argv)
passwordGenerator = Arayuz()

sys.exit(application.exec_())