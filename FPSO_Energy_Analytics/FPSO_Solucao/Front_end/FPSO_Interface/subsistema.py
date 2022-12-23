from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtGui
from PyQt5.uic import loadUi

class Subsistema_Window(QMainWindow):
    def __init__(self):
        super(Subsistema_Window, self).__init__()
        loadUi("subsistema_interface2.ui", self)
        self.setWindowTitle("FPDA - Subsistemas")
        self.add_icon.setPixmap(QtGui.QPixmap("assets/add.png").scaled(16, 16))
        self.minus_icon.setPixmap(QtGui.QPixmap("assets/minus.png").scaled(16, 16))

        self.loaded_obj = []
        self.temp = None
        self.global_v = False

        self.sbclose_button.clicked.connect(self.close_sb)
        self.subvalidate_button.clicked.connect(self.consolidar)

        self.sb_listWidget.itemDoubleClicked.connect(self.fill_listWidget2)

    def displayInfo(self):
        self.show()

    def close_sb(self):
        self.close()

    def check_consolidar(self):
        if len(self.subcol_combobox.currentData()) != 0 and self.subnewsystem_editline.text() != '':
            v = True
            if len(self.loaded_obj) != 0:
                for i in range(len(self.loaded_obj)):

                    if self.loaded_obj[i][0] == self.subnewsystem_editline.text():
                        v = False
        else:
            v = False
        return v

    def consolidar(self):
        try:
            if self.check_consolidar() is True:
                self.temp = (self.subnewsystem_editline.text(), self.subcol_combobox.currentData(), self.subcol_combobox_2.currentData())
                self.loaded_obj.append(self.temp)
                self.fill_listwidget()
                self.reset_sbcombobox()
                self.subnewsystem_editline.clear()
                self.global_v = True
            else:
                self.global_v = False
                QMessageBox.warning(self, "Alerta", "Nome do subsistema não informado ou em duplicidade !")

        except Exception as e:
            QMessageBox.warning(self, "Alerta", "Nome do subsistema não informado ou em duplicidade !")

    def fill_listwidget(self):
        try:
            self.sb_listWidget.clear()
            for i in range(len(self.loaded_obj)):
                self.sb_listWidget.addItem(self.loaded_obj[i][0])

        except Exception as e:
            pass


    def fill_listWidget2(self, item):
        try:
            self.sb_listWidget2.clear()
            selected = item.text()
            for i in range(len(self.loaded_obj)):
                if self.loaded_obj[i][0] == selected:
                    for j in self.loaded_obj[i][1]:
                        self.sb_listWidget2.addItem('+ '+str(j))
                    for k in self.loaded_obj[i][2]:
                        self.sb_listWidget2.addItem('- ' + str(k))

        except Exception as e:
            pass

    def closeEvent(self, event):
        self.close_sb()

    def reset_sbcombobox(self):
        try:
            self.subcol_combobox.unCheckAll()
            self.subcol_combobox_2.unCheckAll()
        except Exception as e:
            pass