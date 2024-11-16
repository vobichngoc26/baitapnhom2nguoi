from PyQt6.QtWidgets import QApplication, QMainWindow

from MainWindowExt import MainWindowExt

app=QApplication([])

qMainWindow=QMainWindow()

HelloworldWindow=MainWindowExt()

HelloworldWindow.setupUi(qMainWindow)

HelloworldWindow.setupSignalAndSlot()

HelloworldWindow.showWindow()

app.exec()