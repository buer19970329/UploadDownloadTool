import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import gui

if __name__ == "__main__":
    app =  QApplication(sys.argv)
    ex = gui.App()
    ex.show()
    sys.exit(app.exec_())