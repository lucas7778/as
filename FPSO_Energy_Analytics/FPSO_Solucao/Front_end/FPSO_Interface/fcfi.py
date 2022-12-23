from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow,\
    QHBoxLayout, QLabel, QDoubleSpinBox, QFrame, QFileDialog, QMessageBox, QInputDialog, QScrollArea
from PyQt5.QtCore import Qt
import sys
import pandas as pd
import os
import numpy as np


class FcFi_wd(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('fcfi.ui', self)
        self.saved_eqs = {}
    def calc_clicked(self):
        try:
            if float(self.potRef_SB.value()) != float(0):
                for i in self.saved_eqs.keys():
                    df = self.saved_eqs[i].df
                    FC = df[self.saved_eqs[i].varDep].mean() / self.potRef_SB.value()
                    self.saved_eqs[i].fc = FC
            else:
                if self.media_RB.isChecked() and float(self.potRef_SB.value()) == float(0):
                    for i in self.saved_eqs.keys():
                        df = self.saved_eqs[i].df
                        FC = df[self.saved_eqs[i].varDep].mean() / df[self.saved_eqs[i].varDep].max()
                        self.saved_eqs[i].fc = FC

                elif self.quantil_RB.isChecked() and float(self.potRef_SB.value()) == float(0):
                    for i in self.saved_eqs.keys():
                        df = self.saved_eqs[i].df
                        FC = df[self.saved_eqs[i].varDep].mean() / df[self.saved_eqs[i].varDep].quantile(float(self.quantil_SB.value()) / 100)
                        self.saved_eqs[i].fc = FC

            for i in self.saved_eqs.keys():
                df = self.saved_eqs[i].df
                ligado = df.loc[
                    df[self.saved_eqs[i].varDep] > self.potOff_SB.value(), self.saved_eqs[
                        i].varDep].count()
                total = df[self.saved_eqs[i].varDep].count()
                FI = ligado / total
                self.saved_eqs[i].fi = FI

        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wd = FcFi_wd()
    wd.show()
    app.exec_()
