import threading

from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem,\
    QHBoxLayout, QLabel, QDoubleSpinBox, QFrame, QFileDialog, QMessageBox, QInputDialog, QScrollArea, QMessageBox
from PyQt5.QtCore import Qt
import sys
import pandas as pd
import os
import numpy as np

from machine_learning import bml_model
from machine_learning.bml_dtmn import bdm_DtMn
from machine_learning import bml_mman
import dashboard3 as db3
from filterSelection import *
from Plataforma import *
#from warning import *
import pickle
#from waitingThread import RunFunctionDialog
from threading import Event
from concurrent.futures import ThreadPoolExecutor, as_completed

'''
################# Classe que constrói um formulário (janela) para criação/edição de equipamentos #################
Os atributos do contrutor são:
portEqp: valor da porta do servidor web que atenderá ao evento de chamada do dashboard. Esse valor precisa ser controlado
pois múltiplas instâncias de dashboards causam conflito

tree: objeto referente a árvore de equipamentos da app principal

eps: dicionário de equipamentos 

dfTags: dicionário que relaciona tags com unidades de engenharia. Utilizado para colocar unidades de engenharia nos
eixos dos gráficos do dashboard
'''

class EQ_wd(QMainWindow):
    def __init__(self, portEqp, tree=None, eqps=None, dfTags=None, nomeBase=None) -> None:
        super().__init__()
        uic.loadUi('eqp2.ui', self)

        self.dfTags = dfTags
        if self.dfTags is None:
            print('dftags eh none no eqp')
        else:
            print('dftags nao eh none no eqp')
        self.portEqp = portEqp

        self.nomeBase=nomeBase

        # popula a combobox "Modelo" do formulário
        self.models_combobox.addItem("Automático")
        self.models_combobox.addItems(list(bml_mman.bmm_MM.bmm_amdls()))

        # inicialização das variáveis envolvidas para preenchimento do formulário e armazenamento de atributos do
        # equipamento

        self.df_ml = None
        self.df2_ml = None
        self.train_check = False

        # modelos treinados de ML (automático + 7)
        # o modelo automático testa os 7 e retorna aquele com melhor desempenho
        self.predictor_auto = None
        self.predictor_layer = None
        self.predictor_variate = None
        self.predictor_vector = None
        self.predictor_gradient = None
        self.predictor_forest = None
        self.predictor_ridge = None
        self.predictor_tree = None

        #modelo treinado usado para estimativa
        self.current_model = None
        self.current_modelsigla = None

        self.model_saved = False

        self.tree = tree
        self.eqps = eqps

        # a princípio as 2 linhas abaixo, assim com o método self.newDF não tem sentido e devem ser suprimidos
        # self.objTransf = filterSelect1()
        # self.objTransf.itemChanged.connect(self.newDF)

        # inicialização da janela de warning a ser apresentada durante a execução do treinamento de um modelo
        # NÃO ESTÁ FUNCIONANDO !!!!!!!
        self.rfd = None

        ########## EVENTOS ASSOCIADOS À SEÇÃO "Configuração"

        # evento associado à seleção de variáveis de processo na respectiva combobox
        self.var_pro.textActivated.connect(self.change_est_box)


        ########## EVENTOS ASSOCIADOS À SEÇÃO "Machine Learning"

        # Evento associado ao botão "Treinar"
        self.train_ml_pushbutton.clicked.connect(self.run_ml)
        # Evento associado ao botão "Dashboard"
        self.dash_pushbutton.clicked.connect(self.run_dash2)


        ########## EVENTOS ASSOCIADOS À SEÇÃO "Estimativa"

        #Evento associado ao botão "Estimar"
        self.predict_pushbutton.clicked.connect(self.predict_value)


        ########## EVENTOS ASSOCIADOS À SEÇÃO "FC e FI"

        #Evento associado aos radiobuttons "Máxima e Quantil"
        ###DESABILITADO###
        #self.media_RB.toggled.connect(self.RB_selected)

        # Evento associado ao botão "Calcular"
        self.calc_Button.clicked.connect(self.calc_clicked)

        # Evento associado à spinbox associada ao radiobutton "Quantil"
        ### DESABILITADO###
        #self.quantil_SB.valueChanged.connect(self.quanti_SB_changed)


        ########## EVENTOS ASSOCIADOS AO FORMULÁRIO DO EQUIPAMENTO

        # Evento associado ao botão "Salvar"
        self.save_eq_pushbutton.clicked.connect(self.save_eq2)

        # Evento associado ao botão "Remover"
        # A princípio, o botão será desabilitado, pois a funcionalidade foi transferida para o menu de contexto
        #self.remover_pb.clicked.connect(self.remove_eqp)

        self.output_predict.setText("0.0")
        self.fc_Label.setText("0.0")
        self.fi_Label.setText("0.0")

    # Método de suporte para popular um combobox
    def fill_combobox(self, cols, dfs, text=None):
        cols.clear()
        col = list(dfs.columns.values)
        try:
            col.remove('index')
        except exec(Exception) as e:
            pass

        if text is not None:
            col = [text]+col
        cols.addItems(col)

    # Método de suporte, que a princípio não está sendo utilizado
    def clear_ml(self):
        self.var_pro.clear()
        self.var_dep.clear()

        self.models_combobox.unCheckAll()
        self.sel_models_combobox.clear()
        self.current_model = None
        self.model_saved = False
        self.stats_tab.clear()
        self.df_ml = None
        self.df2_ml = None
        self.train_check = False
        self.predictor_auto = None
        self.predictor_layer = None
        self.predictor_variate = None
        self.predictor_vector = None
        self.predictor_gradient = None
        self.predictor_forest = None
        self.predictor_ridge = None
        self.predictor_tree = None
        self.current_modelsigla = None

    def open_data_ml(self):
        self.clear_ml()

        filter = "Planilhas (*.xls *.xlsx *.csv)"
        self.path_ml = QFileDialog.getOpenFileName(self, 'Base de dados', '', filter)[0]
        self.filetype_ml = os.path.splitext(os.path.basename(self.path_ml))[1]

        if self.filetype_ml in ['.xls', '.xlsx', '.csv']:
            if self.filetype_ml in ['.xls', '.xlsx']:
                # dataframe_original
                self.df_ml = pd.read_excel(self.path_ml, engine='openpyxl')

            else:
                # dataframe_original
                self.df_ml = pd.read_csv(self.path_ml)

            self.check_df()

        else:
            QMessageBox.warning(self, "Alerta", "Erro ao abrir o arquivo !")
            self.clear_ml()

    # Método que valida o df e cria do df de trabalho, além de atualizar os combobox de variávei de processo e variáveis
    # dependentes. Parece não fazer muito sentido. Precisa ser avaliado para possível supressão
    def check_df(self):
        if self.df_ml is not None:

            self.df_ml = self.df_ml.replace('Bad', np.nan)
            self.df_ml = self.df_ml.replace(np.nan, 0)
            self.df_ml.iloc[:, 1:] = self.df_ml.iloc[:, 1:].apply(pd.to_numeric)

            # dataframe_trabalho
            self.df2_ml = self.df_ml.copy(deep=True)

            # populando o combobox da 1a linha com as colunas do dataframe_trabalho
            self.fill_combobox(self.var_pro, self.df2_ml, 'Todas')

            # primeira posição apresentada
            self.var_pro.setCurrentIndex(0)

            # populando o combobox da 2a linha com as colunas do dataframe_trabalho
            self.fill_combobox(self.var_dep, self.df2_ml)

        else:
            QMessageBox.warning(self, "Alerta", "Erro ao carregar o dataframe !")

    # carrega um dataframe antigo
    # def load_df(self, df):
    #     self.clear_ml()
    #     self.df_ml = df
    #     self.process_df()

    # muito parecido com o check_df
    # checa se o dataframe foi carregado, cria um dataframe de trabalho(df2_ml) e preenche as comboboxes
    # def process_df(self):
    #     # checa se o dataframe foi carregado
    #     if self.df_ml is not None:
    #         # processa o dataframe
    #         self.df_ml = self.df_ml.replace('Bad', np.nan)
    #         self.df_ml = self.df_ml.replace(np.nan, 0)
    #         self.df_ml.iloc[:, 1:] = self.df_ml.iloc[:, 1:].apply(pd.to_numeric)
    #
    #         # dataframe_trabalho
    #         self.df2_ml = self.df_ml.copy(deep=True)
    #
    #         # populando o combobox da 1a linha com as colunas do dataframe_trabalho
    #         self.fill_combobox(self.var_pro, self.df2_ml, 'Todas')
    #
    #         # primeira posição apresentada
    #         self.var_pro.setCurrentIndex(0)
    #
    #         # populando o combobox da 2a linha com as colunas do dataframe_trabalho
    #         self.fill_combobox(self.var_dep, self.df2_ml)
    #
    #     else:
    #         QMessageBox.warning(self, "Alerta", "Erro ao carregar o dataframe !")


    # método de suporte que não está sendo usado, mas que pode ser muito útil no tratamento do evento do botão "Salvar"
    # itens a serem checkados: Nome, Variáveis de processo, Variável dependente, Pot. nominal, Pot. processo, Fator Pot,
    # Modelo selecionado, estimativa, FC e FI
    def check_train(self):
        train_check = False
        if self.df2_ml is not None:
            if len(self.var_pro.currentData()) != 0 and self.var_dep.currentText() not in self.var_pro.currentData():
                if self.pot_nom.value() != 0:
                    if self.fat_pot != 0:
                        train_check = True
                    else:
                        QMessageBox.warning(self, "Alerta", "Erro: Fator de potência igual a zero !")
                QMessageBox.warning(self, "Alerta", "Erro: Potência nominal igual a zero !")
            QMessageBox.warning(self, "Alerta", "Erro: Variáveis de entrade e/ou saída inválido/os !")
        QMessageBox.warning(self, "Alerta", "Erro dataframe vazio: Necessário carregar dataframe !")
        return train_check

    # método utilizado no run_ml2, para ser lançado como um thread. Ainda não funcional
    def run_models(self, event):
        self.train_check = False
        if self.df2_ml is not None:
            self.sel_models_combobox.clear()
            self.stats_tab.clear()

            self.predict_model = {}
            self.predict_model["Automático"] = None
            for i in list(bml_mman.bmm_MM.bmm_amdls()):
                self.predict_model[str(i)] = None

            if "Todas" in self.var_pro.currentData():
                    col = list(self.df2_ml.columns.values)
                    try:
                        col.remove('index')
                    except Exception as e:
                        pass
                    col.remove(self.var_dep.currentText())
                    self.ml_in = (*col,)
            else:
                self.ml_in = (*self.var_pro.currentData(),)
            self.ml_out = (self.var_dep.currentText(),)

            dataset_raw = self.df2_ml
            output_nominal = (self.pot_nom.value(),)
            output_names = self.ml_out
            input_names = self.ml_in

            for i in self.models_combobox.currentData():
                print(i)
                if event.is_set():
                    return
                if i == 'Automático':

                    # %% Setup de pré-processamentos:

                    setup = {
                        "scale": "minmax",
                        "range": (-1, 1),
                        "special_preprocessing": {},
                        "dataset_split": (0.6, 0.2, 0.2),
                        "dataset_split_type": "granular",
                        "ds_gran_interval": (2, 100),
                        "out_nominal": output_nominal,
                        "nokdd": True,
                        }

                    predictor, comparison = bml_mman.bmm_MM.bmm_auto(
                        bmm_inn=input_names,
                        bmm_outn=output_names,
                        bmm_dsraw=dataset_raw,
                        bmm_setup=setup,
                        bmm_avail='all',
                    )
                    self.predict_model['Automático'] = predictor

                else:
                    setup = {
                        "scale": "minmax",
                        "range": (-1, 1),
                        "special_preprocessing": {},
                        "dataset_split": (0.6, 0.2, 0.2),
                        "dataset_split_type": "granular",
                        "ds_gran_interval": (2, 100),
                        "out_nominal": output_nominal,
                        "nokdd": True,
                    }
                    predictor = bml_mman.bmm_MM.bmm_getm(
                        bmm_tag=i,
                        bmm_inn=input_names,
                        bmm_outn=output_names,
                    )

                    # RECEBENDO O DATASET
                    predictor.bbb_pdata(
                        bbb_dsraw=dataset_raw,
                        bbb_setup=setup,
                    )
                    predictor.bm_fitgs()
                    self.predict_model[i] = predictor

            # for j in self.predict_model.keys():
            #     if self.predict_model[j] is not None:
            #         print(j)
            self.train_check = True
        else:
            QMessageBox.warning(self, "Alerta", "Erro dataframe vazio: Necessário carregar dataframe !")
        return self.train_check

    # método para substituir o run_ml, lançando a thread para o run_models e apresentado uma janela de warning para o
    # esperar. Ainda não funcional
    def run_ml2(self):
        self.rfd = RunFunctionDialog(self.run_models,"Atenção !","Operação em curso ... aguarde      ")
        self.rfd.show()
        if self.rfd.resultado is True:
            for j in self.predict_model.keys():
                if self.predict_model[j] is not None:
                    text = QLabel(
                        f"{self.predict_model[j].bbb_info()}\n\n Estatísticas:\n{self.predict_model[j].bbb_stats()}")
                    scroll = QScrollArea()
                    scroll.setWidget(text)
                    self.stats_tab.addTab(scroll, j)
                    self.sel_models_combobox.addItem(j)

    # Evento associado ao botão "Treinar". Treina os modelos de ML selecionados pelo usuário. Não existe nenhuma warning
    # para o usuário acerca da não seleção de variáveis de processo e variável dependente, assim como dos métodos de ML
    def run_ml(self):
        self.train_check = False
        if self.df2_ml is not None:
            self.sel_models_combobox.clear()
            self.stats_tab.clear()

            if "Todas" in self.var_pro.currentData():
                    col = list(self.df2_ml.columns.values)
                    try:
                        col.remove('index')
                    except Exception as e:
                        pass
                    col.remove(self.var_dep.currentText())
                    self.ml_in = (*col,)
            else:
                self.ml_in = (*self.var_pro.currentData(),)
            self.ml_out = (self.var_dep.currentText(),)

            dataset_raw = self.df2_ml
            if dataset_raw is None:
                print('run_ml dataset is None')
            #output_nominal = (self.pot_nom.value(),)
            output_nominal = (None,)
            output_names = self.ml_out
            input_names = self.ml_in
            print(f'modelos selecionados {self.models_combobox.currentData()}')
            if 'Automático' in self.models_combobox.currentData():

                # %% Setup de pré-processamentos:

                setup = {
                    "scale": "minmax",
                    "range": (-1, 1),
                    "special_preprocessing": {},
                    "dataset_split": (0.6, 0.2, 0.2),
                    "dataset_split_type": "granular",
                    "ds_gran_interval": (2, 100),
                    "out_nominal": output_nominal,
                    "nokdd": True,
                    }

                predictor, comparison = bml_mman.bmm_MM.bmm_auto(
                    bmm_inn=input_names,
                    bmm_outn=output_names,
                    bmm_dsraw=dataset_raw,
                    bmm_setup=setup,
                    bmm_avail='all',
                )

                self.predictor_auto = predictor
                text = QLabel(
                        f"Melhor modelo :{self.predictor_auto.bbb_info()}\n\n Estatísticas:\n{self.predictor_auto.bbb_stats()}")
                scroll = QScrollArea()
                scroll.setWidget(text)
                self.stats_tab.addTab(scroll, "Automático")
                self.sel_models_combobox.addItem('Automático')

            if 'Multilayer Perceptron' in self.models_combobox.currentData():

                # %% Setup de pré-processamentos:

                setup = {
                    "scale": "minmax",
                    "range": (-1, 1),
                    "special_preprocessing": {},
                    "dataset_split": (0.6, 0.2, 0.2),
                    "dataset_split_type": "granular",
                    "ds_gran_interval": (2, 100),
                    "out_nominal": output_nominal,
                    "nokdd": True,
                }
                predictor = bml_mman.bmm_MM.bmm_getm(
                    bmm_tag="Multilayer Perceptron",
                    bmm_inn=input_names,
                    bmm_outn=output_names,
                )

                # RECEBENDO O DATASET
                predictor.bbb_pdata(
                    bbb_dsraw=dataset_raw,
                    bbb_setup=setup,
                )
                #threading.Thread(target=predictor.bm_fitgs).start()
                predictor.bm_fitgs()
                self.predictor_layer = predictor
                text = QLabel(
                    f"{self.predictor_layer.bbb_info()}\n\n Estatísticas:\n{self.predictor_layer.bbb_stats()}")
                scroll = QScrollArea()
                scroll.setWidget(text)
                self.stats_tab.addTab(scroll, "Multilayer Perceptron")
                self.sel_models_combobox.addItem('Multilayer Perceptron')

            if 'Multivariate Regression' in self.models_combobox.currentData():

                # %% Setup de pré-processamentos:

                setup = {
                    "scale": "minmax",
                    "range": (-1, 1),
                    "special_preprocessing": {},
                    "dataset_split": (0.6, 0.2, 0.2),
                    "dataset_split_type": "granular",
                    "ds_gran_interval": (2, 100),
                    "out_nominal": output_nominal,
                    "nokdd": True,
                }
                predictor = bml_mman.bmm_MM.bmm_getm(
                    bmm_tag='Multivariate Regression',
                    bmm_inn=input_names,
                    bmm_outn=output_names,
                )

                # RECEBENDO O DATASET
                predictor.bbb_pdata(
                    bbb_dsraw=dataset_raw,
                    bbb_setup=setup,
                )
                predictor.bm_fitgs()
                self.predictor_variate = predictor
                text = QLabel(
                    f"{self.predictor_variate.bbb_info()}\n\n Estatísticas:\n{self.predictor_variate.bbb_stats()}")
                scroll = QScrollArea()
                scroll.setWidget(text)
                self.stats_tab.addTab(scroll, "Multivariate Regression")
                self.sel_models_combobox.addItem('Multivariate Regression')

            if 'Support-Vector Machine' in self.models_combobox.currentData():

                # %% Setup de pré-processamentos:

                setup = {
                    "scale": "minmax",
                    "range": (-1, 1),
                    "special_preprocessing": {},
                    "dataset_split": (0.6, 0.2, 0.2),
                    "dataset_split_type": "granular",
                    "ds_gran_interval": (2, 100),
                    "out_nominal": output_nominal,
                    "nokdd": True,
                }
                predictor = bml_mman.bmm_MM.bmm_getm(
                    bmm_tag='Support-Vector Machine',
                    bmm_inn=input_names,
                    bmm_outn=output_names,
                )

                # RECEBENDO O DATASET
                predictor.bbb_pdata(
                    bbb_dsraw=dataset_raw,
                    bbb_setup=setup,
                )
                predictor.bm_fitgs()
                self.predictor_vector = predictor
                text = QLabel(
                    f"{self.predictor_vector.bbb_info()}\n\n Estatísticas:\n{self.predictor_vector.bbb_stats()}")
                scroll = QScrollArea()
                scroll.setWidget(text)
                self.stats_tab.addTab(scroll, "Support-Vector Machine")
                self.sel_models_combobox.addItem('Support-Vector Machine')

            if 'Gradient Boosting Regression' in self.models_combobox.currentData():

                # %% Setup de pré-processamentos:

                setup = {
                    "scale": "minmax",
                    "range": (-1, 1),
                    "special_preprocessing": {},
                    "dataset_split": (0.6, 0.2, 0.2),
                    "dataset_split_type": "granular",
                    "ds_gran_interval": (2, 100),
                    "out_nominal": output_nominal,
                    "nokdd": True,
                }
                predictor = bml_mman.bmm_MM.bmm_getm(
                    bmm_tag='Gradient Boosting Regression',
                    bmm_inn=input_names,
                    bmm_outn=output_names,
                )

                # RECEBENDO O DATASET
                predictor.bbb_pdata(
                    bbb_dsraw=dataset_raw,
                    bbb_setup=setup,
                )
                predictor.bm_fitgs()
                self.predictor_gradient = predictor
                text = QLabel(
                    f"{self.predictor_gradient.bbb_info()}\n\n Estatísticas:\n{self.predictor_gradient.bbb_stats()}")
                scroll = QScrollArea()
                scroll.setWidget(text)
                self.stats_tab.addTab(scroll, "Gradient Boosting Regression")
                self.sel_models_combobox.addItem('Gradient Boosting Regression')

            if 'Random Forest Regression' in self.models_combobox.currentData():

                # %% Setup de pré-processamentos:

                setup = {
                    "scale": "minmax",
                    "range": (-1, 1),
                    "special_preprocessing": {},
                    "dataset_split": (0.6, 0.2, 0.2),
                    "dataset_split_type": "granular",
                    "ds_gran_interval": (2, 100),
                    "out_nominal": output_nominal,
                    "nokdd": True,
                }
                predictor = bml_mman.bmm_MM.bmm_getm(
                    bmm_tag='Random Forest Regression',
                    bmm_inn=input_names,
                    bmm_outn=output_names,
                )

                # RECEBENDO O DATASET
                predictor.bbb_pdata(
                    bbb_dsraw=dataset_raw,
                    bbb_setup=setup,
                )
                predictor.bm_fitgs()
                self.predictor_forest = predictor
                text = QLabel(
                    f"{self.predictor_forest.bbb_info()}\n\n Estatísticas:\n{self.predictor_forest.bbb_stats()}")
                scroll = QScrollArea()
                scroll.setWidget(text)
                self.stats_tab.addTab(scroll, "Random Forest Regression")
                self.sel_models_combobox.addItem('Random Forest Regression')

            if 'Ridge Regression' in self.models_combobox.currentData():

                # %% Setup de pré-processamentos:
                print('ridge 1')
                setup = {
                    "scale": "minmax",
                    "range": (-1, 1),
                    "special_preprocessing": {},
                    "dataset_split": (0.6, 0.2, 0.2),
                    "dataset_split_type": "granular",
                    "ds_gran_interval": (2, 100),
                    "out_nominal": output_nominal,
                    "nokdd": True,
                }
                print('ridge 2')
                predictor = bml_mman.bmm_MM.bmm_getm(
                    bmm_tag='Ridge Regression',
                    bmm_inn=input_names,
                    bmm_outn=output_names,
                )
                print('ridge 3')
                # RECEBENDO O DATASET
                predictor.bbb_pdata(
                    bbb_dsraw=dataset_raw,
                    bbb_setup=setup,
                )
                print('ridge 4')
                predictor.bm_fitgs()
                print('ridge 5')
                self.predictor_ridge = predictor
                text = QLabel(
                    f"{self.predictor_ridge.bbb_info()}\n\n Estatísticas:\n{self.predictor_ridge.bbb_stats()}")
                print('ridge 6')
                scroll = QScrollArea()
                print('ridge 7')
                scroll.setWidget(text)
                print('ridge 8')
                self.stats_tab.addTab(scroll, "Ridge Regression")
                print('ridge 9')
                self.sel_models_combobox.addItem('Ridge Regression')
                print('ridge 10')

            if 'Decision Tree Regression' in self.models_combobox.currentData():

                # %% Setup de pré-processamentos:

                setup = {
                    "scale": "minmax",
                    "range": (-1, 1),
                    "special_preprocessing": {},
                    "dataset_split": (0.6, 0.2, 0.2),
                    "dataset_split_type": "granular",
                    "ds_gran_interval": (2, 100),
                    "out_nominal": output_nominal,
                    "nokdd": True,
                }
                predictor = bml_mman.bmm_MM.bmm_getm(
                    bmm_tag='Decision Tree Regression',
                    bmm_inn=input_names,
                    bmm_outn=output_names,
                )

                # RECEBENDO O DATASET
                predictor.bbb_pdata(
                    bbb_dsraw=dataset_raw,
                    bbb_setup=setup,
                )
                predictor.bm_fitgs()
                self.predictor_tree = predictor
                text = QLabel(
                    f"{self.predictor_tree.bbb_info()}\n\n Estatísticas:\n{self.predictor_tree.bbb_stats()}")
                scroll = QScrollArea()
                scroll.setWidget(text)
                self.stats_tab.addTab(scroll, "Decision Tree Regression")
                self.sel_models_combobox.addItem('Decision Tree Regression')

            self.train_check = True

        else:
            QMessageBox.warning(self, "Alerta", "Erro dataframe vazio: Necessário carregar dataframe !")

    # Método associado ao evento de seleção de variávei de processo na respectiva combobox. À medida que as variáveis
    # vão sendo selecionadas, labels e respectivas spinboxes populam a seção "Estimativa". Permite a entrada de valores
    # para as variáveis de processo para que o modelo estime uma saída para a variável dependente
    def change_est_box(self, text):
        index = self.var_pro.findText(text)
        QtItem = self.var_pro.model().item(index)

        if QtItem.checkState() == Qt.Checked:
            label = QLabel(text)
            label.setObjectName('label: ' + text)
            spin = QDoubleSpinBox()
            spin.setMaximum(9000000000.00)
            spin.setObjectName('num: ' + text)

            self.textLayout.addWidget(label)
            self.numLayout.addWidget(spin)

        else:
            label = self.scrollArea.findChild(QLabel, name='label: ' + text)
            spin = self.scrollArea.findChild(QDoubleSpinBox, name='num: ' + text)
            label.deleteLater()
            spin.deleteLater()

    # def rec_var_pro(self,obj):
    #     for var in obj.varProc:
    #         index = self.var_pro.findText(var[0])
    #         QtItem = self.var_pro.model().item(index)
    #         QtItem.setCheckState(Qt.Checked)
    #         label = QLabel(var[0])
    #         label.setObjectName('label: ' + var[0])
    #         spin = QDoubleSpinBox()
    #         spin.setMaximum(9000000000.00)
    #         spin.setObjectName('num: ' + var[0])
    #         spin.setValue(var[1])
    #
    #         self.textLayout.addWidget(label)
    #         self.numLayout.addWidget(spin)

    # método de suporte que armazena uma lista de tuplas com os nomes das variáveis de processo selecionadas e os valores
    # a elas atribuídos
    def feed_ml(self) -> list:
        num_of_vars = self.var_pro.count()
        select = self.var_pro.model().item

        list_of_text_and_vals = []

        for i in range(num_of_vars):
            QtItem = select(i)
            if QtItem.checkState() == Qt.Checked:
                text = QtItem.text()
                spin = self.scrollArea.findChild(QDoubleSpinBox, name='num: ' + text)
                val = spin.value()

                list_of_text_and_vals.append((text, val))

        return list_of_text_and_vals

    # método de suporte parecido com o check_train. pode ser melhorado conforme descrição no outro método. ùtil no
    # evento de Salvar. Atualmente utilizado no "predict_value". Avaliar
    def check_save(self):
        save_check = False
        if self.df2_ml is not None:
            if self.name_eq.text() != '':
                save_check = True
            else:
                QMessageBox.warning(self, "Alerta", "Erro: Defina um nome para o equipamento !")
        else:
            QMessageBox.warning(self, "Alerta", "Erro dataframe vazio: Necessário carregar dataframe !")
        return save_check

    # método de suporte que retorna o modelo a ser usado para predição ou para salvamento no objeto equipamento
    def defcurent_model(self):

        current_modelname = str(self.sel_models_combobox.currentText())
        if current_modelname == 'Automático':
            if not(self.predictor_auto is None):
                self.current_model = self.predictor_auto
            self.current_modelsigla = 'auto'

        elif current_modelname == 'Multilayer Perceptron':
            if not (self.predictor_layer is None):
                self.current_model = self.predictor_layer
            self.current_modelsigla = 'layer'

        elif current_modelname == 'Multivariate Regression':
            if not (self.predictor_variate is None):
                self.current_model = self.predictor_variate
            self.current_modelsigla = 'variate'

        elif current_modelname == 'Support-Vector Machine':
            if not (self.predictor_vector is None):
                self.current_model = self.predictor_vector
            self.current_modelsigla = 'vector'

        elif current_modelname == 'Gradient Boosting Regression':
            if not (self.predictor_gradient is None):
                self.current_model = self.predictor_gradient
            self.current_modelsigla = 'gradient'

        elif current_modelname == 'Random Forest Regression':
            if not (self.predictor_forest is None):
                self.current_model = self.predictor_forest
            self.current_modelsigla = 'forest'

        elif current_modelname == 'Ridge Regression':
            if not (self.predictor_ridge is None):
                self.current_model = self.predictor_ridge
            self.current_modelsigla = 'ridge'

        elif current_modelname == 'Decision Tree Regression':
            if not (self.predictor_tree is None):
                self.current_model = self.predictor_tree
            self.current_modelsigla = 'tree'

    # def save_model(self):
    #     print('a')
    #     self.model_saved = False
    #     try:
    #         if self.check_save() is True:
    #             print('b')
    #             name = self.name_eq.text()
    #             self.defcurent_model()
    #
    #             if os.path.isdir('models') is False:
    #                 os.mkdir(f'./models')
    #
    #             if os.path.isfile(f'./models/{name.strip().lower()}-{self.current_modelsigla}.bbox') is False:
    #                 try:
    #                     local = f'./models/{name.strip().lower()}-{self.current_modelsigla}.bbox'
    #                     bml_mman.bmm_MM.bmm_save(self.current_model, local)
    #                     # self.obj_def = [name, self.feed_ml(), self.var_dep.currentText(),
    #                     #            self.pot_nom.value(), local]
    #                     # self.ml_dict.update({name: self.obj_def})
    #                     self.model_saved = True
    #                 except Exception as e:
    #                     QMessageBox.warning(self, "Alerta", "Erro ao salvar o modelo !")
    #             else:
    #                 QMessageBox.warning(self, "Alerta", "Erro ao salvar o modelo ! (Duplicidade)")
    #     except Exception as e:
    #         print(e)

    # Evento associado ao botão "Salvar"
    def save_eq(self):
        print('aqui')
        print(-1)
        if True:  # self.eq_wd.model_saved is True:
            print(0)
            self.defcurent_model()
            print(1)
            obj_to_save = Eqp_Proc(self.name_eq.text(), self.pot_nom.value(), self.fat_pot.value(),
                                   self.pot_proc.value(), self.df2_ml, self.var_dep.currentText(),
                                   self.feed_ml(), float(self.fc_Label.text()),
                                   float(self.fi_Label.text()), float(self.output_predict.text()))
            print(2)
            obj_to_save.modelo = self.current_model
            print(3)
            obj_to_save.modelo_nome = self.sel_models_combobox.currentText()
            print(4)

            print(5)
            print(self.name_eq.text())
            print(self.eqps.keys())
            if not (self.name_eq.text() in self.eqps.keys()):
                print(6)
                mainItem = QTreeWidgetItem([self.name_eq.text()])
                self.tree.addTopLevelItem(mainItem)
            self.eqps[self.name_eq.text()] = obj_to_save
            self.dump_eq()
            print(7)
        self.close()

    # Evento associado ao botão "Salvar"
    def save_eq2(self):
        print('aqui')
        print(-1)
        teste=self.name_eq.text()
        teste2=self.eqps.keys()

        if self.save_warning_eq():
            if not (self.name_eq.text() in self.eqps.keys()):
                print(0)
                self.defcurent_model()
                print(1)
                obj_to_save = Eqp_Proc(self.name_eq.text(), self.pot_nom.value(), self.fat_pot.value(),
                                       self.pot_proc.value(), self.df2_ml, self.var_dep.currentText(),
                                       self.feed_ml(), float(self.fc_Label.text()),
                                       float(self.fi_Label.text()), float(self.output_predict.text()))
                print(2)
                obj_to_save.modelo = self.current_model
                print(3)
                obj_to_save.modelo_nome = self.sel_models_combobox.currentText()
                print(4)

                print(5)
                print(self.name_eq.text())
                print(self.eqps.keys())
                x = self.nomeBase
                #if not (self.name_eq.text() in self.eqps.keys()):
                print(6)
                # item = self.tree.findItems(self.nomeBase, Qt.MatchExactly, 0)
                # item[0].addChild(QTreeWidgetItem([self.name_eq.text()]))

                self.atualizaTree()

                self.eqps[self.name_eq.text()] = [obj_to_save, self.nomeBase, "Equipamento"]
                #self.dump_eq()
                print(7)

            else:
                self.eqps[self.name_eq.text()][0].potNominal=self.pot_nom.value()
                self.eqps[self.name_eq.text()][0].fP=self.fat_pot.value()
                self.eqps[self.name_eq.text()][0].varDep=self.var_dep.currentText()
                self.eqps[self.name_eq.text()][0].varProc=self.feed_ml()
                #self.eqps[self.name_eq.text()][0].df
                self.eqps[self.name_eq.text()][0].potProc=self.pot_proc.value()
                self.eqps[self.name_eq.text()][0].fc=float(self.fc_Label.text())
                self.eqps[self.name_eq.text()][0].fi=float(self.fi_Label.text())
                self.eqps[self.name_eq.text()][0].outpredict=float(self.output_predict.text())
                self.eqps[self.name_eq.text()][0].modelo_nome=self.sel_models_combobox.currentText()
                self.eqps[self.name_eq.text()][0].modelo=self.current_model
            self.dump_eq()
            self.close()


    def atualizaTree(self):
        lBases = []
        tipo = "Equipamento"
                
        for i in self.eqps.values():
            lBases.append(i[1])
        lBases=set(lBases)
        if self.nomeBase in lBases:
            listaItens = self.tree.findItems(self.nomeBase, Qt.MatchExactly, 0)
            listaItens[0].addChild(QTreeWidgetItem([self.name_eq.text(),tipo]))
        else:
            item = QTreeWidgetItem([self.nomeBase])
            self.tree.addTopLevelItem(item)
            item.addChild(QTreeWidgetItem([self.name_eq.text(),tipo]))

    def save_warning_eq(self):
        if self.name_eq.text() =="":
            QMessageBox.warning(self, "Alerta", "É preciso associar um nome ao equipamento ...")
            return False
        elif self.var_dep.currentText() is None:
            QMessageBox.warning(self, "Alerta", "É preciso associar uma variável dependente ao equipamento ...")
            return False
        elif len(self.var_pro.currentData()) == 0:
            QMessageBox.warning(self, "Alerta", "É preciso associar variáveis de processo ao equipamento ...")
            return False
        elif self.sel_models_combobox.currentText() == "":
            QMessageBox.warning(self, "Alerta", "É preciso treinar um modelo do equipamento ...")
            return False
        else:
            return True



    # Evento associado ao botão "Remover"
    def remove_eqp(self):
        del self.eqps[self.name_eq.text()]
        self.tree.clear()
        for i in self.eqps.keys():
            mainItem = QTreeWidgetItem([i])
            self.tree.addTopLevelItem(mainItem)
        self.dump_eq()
        self.close()

    # Método de suporte para salvar em arquivo do sistema o dicionário de equipamentos
    def dump_eq(self):
        try:
            with open('eqs.pickle', 'wb') as fp:
                pickle.dump(self.eqps, fp)
        except Exception as e:
            print(e)

    # Evento associado ao botão Dashboard
    def run_dash2(self):
        try:
            if self.df2_ml is None:
                QMessageBox.warning(
                    self, "Alerta",
                    "É preciso abrir um arquivo de dados antes de exibir a análise")
            else:
                if len(self.var_pro.currentData()) != 0:
                    l = ['index', self.var_dep.currentText()]
                    for i in self.var_pro.currentData():
                        l.append(i)
                    print(l)

                    t = db3.DashThread(self.df2_ml[l], dataTags=self.dfTags, port=self.portEqp.getPorta())
                    self.portEqp.proxima()
                    t.start()
        except Exception as e:
            print(e)

    # Evento associado ao botão "Estimar"
    def predict_value(self):
        try:
            if self.check_save() is True:
                self.defcurent_model()
                x_dict = {}
                for i in self.feed_ml():
                    x_dict[i[0]] = [float(i[1])]
                x = pd.DataFrame.from_dict(x_dict)
                y = self.current_model.bbb_pred(
                    bbb_x=x,
                    bbb_noneg=True,  # automaticamente zera valores negativos
                    bbb_fator=True,
                    # retorna a predição como fator do output_nominal (não faz nada se um valor nominal não tiver sido passado na montagem no modelo)
                )

                self.output_predict.setText(str(y.iloc[0][0]))
            else:
                QMessageBox.warning(self, "Alerta", "Erro, não foi possível fazer a previsão com os valores inseridos !")
        except Exception as e:
            print(e)

    # Evento associado à seleção dos radiobuttons "Máxima" ou "Quantil". Os nomes das variáveis relativas a esses
    # radiobuttons, assim como o nome do método estão tuins
    ###DEASBILITADO###
    def RB_selected(self):
        if self.media_RB.isChecked():
            self.potRef_SB.setValue(self.df2_ml[self.var_dep.currentText()].max())
        elif self.quantil_RB.isChecked():
            self.potRef_SB.setValue(self.df2_ml[self.var_dep.currentText()].quantile(float(self.quantil_SB.value())/100))

    #Evento associado ao botão calcular
    def calc_clicked(self):
        denominador=1
        numerador=0
        if self.media_RB.isChecked():
            numerador= self.df2_ml[self.var_dep.currentText()].mean()
        elif self.quantil_RB.isChecked():
            numerador=self.df2_ml[self.var_dep.currentText()].quantile(float(self.quantil_SB.value())/100)

        if self.pot_nom_RB.isChecked():
            denominador=float(self.pot_nom.value())
        elif self.pot_pro_RB.isChecked():
            denominador = float(self.pot_proc.value())
        elif self.max_RB.isChecked():
            denominador = self.df2_ml[self.var_dep.currentText()].max()
        FC=numerador/denominador
        print(numerador)
        print(denominador)
        self.fc_Label.setText(str(FC))

        ligado=self.df2_ml.loc[self.df2_ml[self.var_dep.currentText()]>self.potOff_SB.value(),self.var_dep.currentText()].count()
        total=self.df2_ml[self.var_dep.currentText()].count()
        FI=ligado/total
        self.fi_Label.setText(str(FI))

    # Evento associado à spinbox associada ao radiobutton "Quantil"
    ### DESABILITADO ###
    def quanti_SB_changed(self):
        self.potRef_SB.setValue(self.df2_ml[self.var_dep.currentText()].quantile(float(self.quantil_SB.value()) / 100))

    #Sem sentido. Avaliar a supressão
    # def newDF(self):
    #     print(self.objTransf.getCoord())

    #Método de suporte que permite à app principal alterar o df a ser utilizado no equipamento. Foi criado pois o
    # carregamento do df gravado dava erro no machine learning.
    def setDataframe(self, df):
        self.df_ml=df
        self.check_df()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wd = EQ_wd()
    wd.show()
    app.exec_()
