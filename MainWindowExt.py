from MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.Exit.clicked.connect(self.processExit)
        self.Clear.clicked.connect(self.processClear)
        self.Cong.clicked.connect(self.processCong)
        self.Tru.clicked.connect(self.processTru)
        self.Nhan.clicked.connect(self.processNhan)
        self.Chia.clicked.connect(self.processChia)
    def processExit(self):
        self.MainWindow.close()
    def processClear(self):
        self.Hesoa.setText("")
        self.Hesob.setText("")
        self.ketqua.setText("")
        self.Hesoa.setFocus()
    def processCong(self):
        a=float(self.lineEdita.text())
        b=float(self.lineEditb.text())
        result=a+b
        self.lineEditkq.setText(f"{a}+{b}={result}")
    def processTru(self):
        a=float(self.lineEdita.text())
        b=float(self.lineEditb.text())
        result=a-b
        self.lineEditkq.setText(f"{a}-{b}={result}")
    def processNhan(self):
        a=float(self.lineEdita.text())
        b=float(self.lineEditb.text())
        result=a*b
        self.lineEditkq.setText(f"{a}*{b}={result}")
    def processChia(self):
        try:
            a = float(self.lineEdita.text())
            b = float(self.lineEditb.text())
            if b==0:
                self.lineEditkq.setText("Error!")
            else:
                result=a/b
                self.lineEditkq.setText(f"{a}/{b}={result}")
        except:
            self.lineEditkq.setText("Input data not valid")
