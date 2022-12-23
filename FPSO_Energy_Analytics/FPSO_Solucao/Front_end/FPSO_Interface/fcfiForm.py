from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow,\
    QHBoxLayout, QLabel, QDoubleSpinBox, QFrame, QFileDialog, QMessageBox, QInputDialog, QScrollArea
from PyQt5.QtCore import Qt
import sys
import pandas as pd
import os
import numpy as np

class fcfiForm(QMainWindow):
    def __init__(self, saved_eqs, df, objTransf, base) -> None:
        super().__init__()
        uic.loadUi('fcfi2.ui', self)
        self.saved_eqs=saved_eqs
        self.df=df
        self.objTransf=objTransf
        self.base=base
        self.aplicar_PB.clicked.connect(self.calc_up_fcfi)
        self.fill_combobox()


    def calc_up_fcfi(self):
        for eqp in self.saved_eqs.keys():
            base = self.saved_eqs[eqp][1]
            denominador = 1
            numerador = 0
            texto=self.comboBox.currentText()
            if self.saved_eqs[eqp][2] == "Equipamento":
                if self.comboBox.currentText() == base or self.comboBox.currentText() == 'Todas':

                    dfEqp = self.saved_eqs[eqp][0].df.copy()
                    # se houve filtragem no dashboard, o dataframe do eqp precisa ser filtrado
                    if self.objTransf.coord is not None:
                        coords = self.objTransf.getCoord()
                        xmin = coords[0]
                        xmax = coords[1]
                        ymin = coords[2]
                        ymax = coords[3]

                        nomes = self.objTransf.getNames()

                        r1 = dfEqp[nomes[0]] > xmin
                        r2 = dfEqp[nomes[0]] <= xmax
                        r3 = dfEqp[nomes[1]] > ymin
                        r4 = dfEqp[nomes[1]] <= ymax
                        dfEqp = dfEqp[r1 & r2 & r3 & r4]
                        # self.dfFCFI.to_excel('dataframeFCFI.xlsx', index=False)
                        print('dataframe atualizado')

                    if self.media_RB_2.isChecked():
                        numerador = dfEqp[self.saved_eqs[eqp][0].varDep].mean()
                    elif self.quantil_RB_3.isChecked():
                        numerador = dfEqp[self.saved_eqs[eqp][0].varDep].quantile(float(self.quantil_SB_3.value()) / 100)

                    if self.pot_nom_RB.isChecked():
                        denominador = self.saved_eqs[eqp][0].potNominal
                    elif self.pot_pro_RB.isChecked():
                        denominador = self.saved_eqs[eqp][0].potProc
                    elif self.max_RB_3.isChecked():
                        denominador = dfEqp[self.saved_eqs[eqp][0].varDep].max()

                    FC = numerador / denominador

                    ligado = dfEqp.loc[
                        dfEqp[self.saved_eqs[eqp][0].varDep] > self.potOff_SB.value(), self.saved_eqs[eqp][0].varDep].count()

                    total = dfEqp[self.saved_eqs[eqp][0].varDep].count()

                    FI = ligado / total

                    self.saved_eqs[eqp][0].fc = FC
                    self.saved_eqs[eqp][0].fi = FI
        for subsis in self.saved_eqs.keys():
            base = self.saved_eqs[eqp][1]
            denominador = 1
            numerador = 0

            if self.saved_eqs[subsis][2] == "Subsistema":
                if self.comboBox.currentText() == base or self.comboBox.currentText() == 'Todas':

                    dfSubsis = self.saved_eqs[subsis][0].df2.copy()
                    # se houve filtragem no dashboard, o dataframe do eqp precisa ser filtrado
                    if self.objTransf.coord is not None:
                        coords = self.objTransf.getCoord()
                        xmin = coords[0]
                        xmax = coords[1]
                        ymin = coords[2]
                        ymax = coords[3]

                        nomes = self.objTransf.getNames()

                        r1 = dfEqp[nomes[0]] > xmin
                        r2 = dfEqp[nomes[0]] <= xmax
                        r3 = dfEqp[nomes[1]] > ymin
                        r4 = dfEqp[nomes[1]] <= ymax
                        dfSubsis = dfSubsis[r1 & r2 & r3 & r4]
                        # self.dfFCFI.to_excel('dataframeFCFI.xlsx', index=False)
                        print('dataframe atualizado')
                    if self.media_RB_2.isChecked():
                        numerador = dfSubsis[self.saved_eqs[subsis][0].nome].mean()
                    elif self.quantil_RB_3.isChecked():
                        numerador = dfSubsis[self.saved_eqs[subsis][0].nome].quantile(float(self.quantil_SB_3.value()) / 100)

                    if self.pot_nom_RB.isChecked():
                        denominador = self.saved_eqs[subsis][0].pot_nom
                    elif self.pot_pro_RB.isChecked():
                        denominador = self.saved_eqs[subsis][0].pot_proc
                    elif self.max_RB_3.isChecked():
                        denominador = dfSubsis[self.saved_eqs[subsis][0].nome].max()

                    FC = numerador / denominador



                    FC = FC / self.saved_eqs[subsis][0].regime

                    ligado = dfSubsis.loc[dfSubsis[subsis] > self.potOff_SB.value(), subsis].count()

                    total = dfSubsis[self.saved_eqs[subsis][0].nome].count()

                    FI = ligado / total

                    self.saved_eqs[subsis][0].fc = FC
                    self.saved_eqs[subsis][0].fi = FI

        # o reset volta ao estado sem filtragem do dashboard
        self.objTransf.reset()
        self.close()

    # cols é um objeto combobox e dfs um dataframe
    def fill_combobox(self, todas = True):
        self.comboBox.clear()
        #condição que verifica se NÃO houve uma filtragem do dashboard
        if self.objTransf.coord is None:
            lBases=[]

            for i in self.saved_eqs.values():
                lBases.append(i[1])

            lBases = set(lBases)
            lBases = list(lBases)
            if todas:
                lBases.append('Todas')
                lBases.reverse()

            self.comboBox.addItems(lBases)
        else:
            # se houve filtragem, apenas a base de dados filtrada será apresentada para o usuário
            self.comboBox.addItem(self.base)