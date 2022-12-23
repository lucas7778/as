from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog, QMessageBox, QLabel,\
    QDoubleSpinBox, QScrollArea, QTreeWidgetItem
from PyQt5 import uic
import pandas as pd
from machine_learning import bml_mman
import sys
from Plataforma import Subsistema
import pickle
from PyQt5.QtCore import Qt
import dashboard3 as db3

class SubsisWd(QMainWindow):
    def __init__(self, eqps=None,  df2=None, portEqp= None, tree=None, dfTags = None, nomeBase = None, novo=True):

        super().__init__()
        uic.loadUi('subsis.ui', self)
        #self.show()
        self.eqps = eqps
        self.portEqp=portEqp
        #self.subsistemas = dict()
        if df2 is not None:
            self.df2 = df2.copy()
        #self.saved_subs = None
        self.tree = tree
        self.dfTags = dfTags
        self.nomeBase = nomeBase
        self.novo=novo

        # popula a combobox de equipamentos
        it=[]
        for i in self.eqps.keys():
            if self.eqps[i][1]== self.nomeBase and self.eqps[i][2] =="Equipamento":
                it.append(i)
        self.eq_combobox.addItems(it)

        # Popula dropdown de modelos do ML
        self.models_combobox.clear()
        self.models_combobox.addItem("Automático")
        self.models_combobox.addItems(list(bml_mman.bmm_MM.bmm_amdls()))

        #self.eq_combobox.addItems(list(self.eqps.keys()))  # adicionar a lista de equipamentos
        self.aplicar_pushButton.clicked.connect(self.aplic_button)
        # Controle do layout de estimativas
        self.var_procs = dict()

        ''' Eventos associados à seção de "Machine Learning" '''
        #self.models_combobox.clear()
        self.train_ml_pushbutton.clicked.connect(self.run_ml)
        self.dash_pushbutton.clicked.connect(self.run_dash)

        ''' Eventos associados à seção "Estimar" '''
        self.predict_pushbutton.clicked.connect(self.predict_value)

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

        # modelo treinado usado para estimativa
        self.current_model = None
        self.current_modelsigla = None
        

        ''' Eventos associados à seção "FC e FI" '''
        self.media_RB.toggled.connect(self.me_qt_rb_selected)
        self.quantil_SB.valueChanged.connect(self.quantil_sb_changed)
        self.FC_num = None
        self.FC_dem = None
        self.FC = None
        self.FI = None


        self.max_RB.toggled.connect(self.pot_rb_selected)

        self.reg_num_SB.valueChanged.connect(self.reg_sb_changed)
        self.reg_deno_SB.valueChanged.connect(self.reg_sb_changed)

        self.calc_button.clicked.connect(self.calc_clicked)

        ''' Eventos associados ao formulário '''
        self.save_sub_pushbutton.clicked.connect(self.save_subsis)



    ''' Método assiciado ao botão "aplicar". A aplicação popula respectivas spinboxes e seção "Estimativa" referente /
     aos equipamentos selecionados '''
    def aplic_button(self):

        # Checa se dados fornecidos estão corretos
        if self.name_sub.text() == "":
            QMessageBox.warning(self, "Alerta", "Erro: Defina um nome para o subsistema")
            return

        if not self.eq_combobox.currentData():
            QMessageBox.warning(self, "Alerta", "Erro: Escolha os equipamentos do subsistema")
            return





        # Lista de variáveis dependentes e soma das potências nominal e de processo
        var_dep = list()
        pot_nom = 0
        pot_proc = 0
        eqps_selected = self.eq_combobox.currentData()

        for eq in eqps_selected:
            if self.eqps[eq][1] == self.nomeBase and self.eqps[eq][2] == "Equipamento":
                var_dep.append(self.eqps[eq][0].varDep)
                pot_nom += self.eqps[eq][0].potNominal
                pot_proc += self.eqps[eq][0].potProc
            else:
                index = self.eq_combobox.findText(eq)
                QtItem = self.eq_combobox.model().item(index)
                QtItem.setCheckState(Qt.Unchecked)
                eqps_selected.remove(eq)

        # Setando campos da interface com valores de potência obtidos
        self.pot_nom.setValue(pot_nom)
        self.pot_proc.setValue(pot_proc)
        # Cria nova coluna no dataframe de trabalho que representa o subsistema
        self.df2[self.name_sub.text()] = self.df2[var_dep].sum(axis=1)


        # Preenche área de estimativas
        # Checa se já existem dados no layout

        self.limpaLayout(self.textLayout)
        self.limpaLayout(self.numLayout)

        # if len(self.var_procs.keys()) != 0:
        #     # Se existem dados, primeiro é feita remoção para serem adicionados na sequência
        #     for var in self.var_procs.keys():
        #         label = self.scrollArea.findChild(QLabel, name='label: ' + var)
        #         spin = self.scrollArea.findChild(QDoubleSpinBox, name='num: ' + var)
        #         label.deleteLater()
        #         spin.deleteLater()
        #         self.novo=True

        var_procs = dict()
        for eq in eqps_selected:
            for var_proc in self.eqps[eq][0].varProc:
                if var_proc[0] not in var_procs.keys():
                    var_procs[var_proc[0]] = var_proc[1]

        self.var_procs = var_procs
        for var in self.var_procs.keys():
            label = QLabel(var)
            label.setObjectName('label: ' + var)
            spin = QDoubleSpinBox()
            spin.setMaximum(9000000000.00)
            spin.setValue(self.var_procs[var])
            spin.setObjectName('num: ' + var)

            self.textLayout.addWidget(label)
            self.numLayout.addWidget(spin)

        pass

    def limpaLayout(self, layout):
        for i in reversed(range(layout.count())):
            widgetToRemove = layout.itemAt(i).widget()
            # remove it from the layout list
            layout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)

    ''' Método associado ao botão "Treinar"'''
    def run_ml(self):
        if not self.models_combobox.currentData():
            QMessageBox.warning(self, "Alerta", "Erro: Escolha um método de Machine Learning")
            return

        self.sel_models_combobox.clear()
        self.stats_tab.clear()

        output_nominal = (None,)
        output_names = (self.name_sub.text(),)
        dataset_raw = self.df2
        #input_names = tuple(self.var_procs.keys())
        input_names = tuple(self.feed_ml2(tuplas=False))

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

        pass

    # Evento associado ao botão Dashboard
    def run_dash(self):
        try:
            if len(self.feed_ml2(tuplas=False)) != 0:
                l = ['index', self.name_sub.text()]
                for i in self.feed_ml2(tuplas=False):
                    l.append(i)
                print(l)

                t = db3.DashThread(self.df2[l], dataTags=self.dfTags, port=self.portEqp.getPorta())
                self.portEqp.proxima()
                t.start()
        except Exception as e:
            print(e)

    ''' Evento associado ao botão "Estimar" '''
    def predict_value(self):
        try:
            self.defcurent_model()
            x_dict = {}
            for i in self.feed_ml2():
                x_dict[i[0]] = [float(i[1])]
            x = pd.DataFrame.from_dict(x_dict)
            y = self.current_model.bbb_pred(
                bbb_x=x,
                bbb_noneg=True,  # automaticamente zera valores negativos
                bbb_fator=True,
                # retorna a predição como fator do output_nominal (não faz nada se um valor nominal não tiver sido passado na montagem no modelo)
            )

            self.output_predict.setText(str(y.iloc[0][0]))
        except:
            QMessageBox.warning(self, "Alerta", "Erro: Número de equipamentos redundantes igual a zero !")

        pass

    ''' Evento associado à seleção dos radiobuttons "Média" e "Quantil" '''
    def me_qt_rb_selected(self):
        if self.media_RB.isChecked():
            self.FC_num = self.df2[self.name_sub.text()].mean()
        elif self.quantil_RB.isChecked():
            self.FC_num = self.df2[self.name_sub.text()].quantile(float(self.quantil_SB.value())/100)

    ''' Evento associado à spinbox associada ao radiobutton "Quantil" '''
    def quantil_sb_changed(self):

        pass

    ''' Evento associado à seleção dos radiobuttons de "Potência nominal", "Potência de processo" e "Máxima" '''
    def pot_rb_selected(self):
        if self.pot_nom_RB.isChecked():
            self.FC_dem = self.pot_nom.value()

        elif self.pot_pro_RB.isChecked():
            self.FC_dem = self.pot_proc.value()

        elif self.max_RB.isChecked():
            self.FC_dem = self.df2[self.name_sub.text()].max()

        pass

    ''' Eventos associados às spinboxes de regimes de uso '''
    def reg_sb_changed(self):

        pass

    ''' Evento associado ao botão calcular'''
    def calc_clicked(self):
        self.me_qt_rb_selected()
        self.pot_rb_selected()

        FC = self.FC_num / self.FC_dem
        self.fc_Label.setText(str(FC))
        try:
            FI = 0
            for equip in self.eq_combobox.currentData():
                FI = FI + (self.df2[self.eqps[equip][0].varDep] > 0).sum() / len(self.df2.index)

            FI = FI / self.reg_deno_SB.value()
            self.fi_Label.setText(str(FI))
        except ZeroDivisionError:
            QMessageBox.warning(self, "Alerta", "Erro: Número de equipamentos redundantes igual a zero !")
        pass

    def save_subsis(self):
        print('save')
        if self.save_warning_sub():
            try:
                self.defcurent_model()
                reg = (self.reg_deno_SB.value(), self.reg_num_SB.value())
                if not (self.name_sub.text() in self.eqps.keys()):
                    #self.defcurent_model()
                    #reg = (self.reg_deno_SB.value(), self.reg_num_SB.value())
                    subsistema = Subsistema(nome=self.name_sub.text(),
                                        eqpsSelected=self.eq_combobox.currentData(),
                                        pot_nom=self.pot_nom.value(),
                                        pot_proc=self.pot_proc.value(),
                                        output=float(self.output_predict.text()),
                                        fc=float(self.fc_Label.text()),
                                        fi=float(self.fi_Label.text()),
                                        modelo=self.current_model,
                                        nome_modelo=self.sel_models_combobox.currentText(),
                                        df2 = self.df2,
                                        varProcs=self.feed_ml2(),
                                        regime=reg)
                    #subsistema.modelo = self.current_model
                    #self.subsistemas[self.name_sub.text()] = subsistema
                    # mainItem = QTreeWidgetItem([self.name_sub.text()])
                    # self.tree.addTopLevelItem(mainItem)
                    # self.dump_sub()
                    self.atualizaTree()
                    self.eqps[self.name_sub.text()] = [subsistema, self.nomeBase, "Subsistema"]
                else:
                    self.eqps[self.name_sub.text()][0].eqpsSelected = self.eq_combobox.currentData()
                    self.eqps[self.name_sub.text()][0].pot_nom = self.pot_nom.value()
                    self.eqps[self.name_sub.text()][0].pot_proc = self.pot_proc.value()
                    self.eqps[self.name_sub.text()][0].output = float(self.output_predict.text())
                    self.eqps[self.name_sub.text()][0].fc = float(self.fc_Label.text())
                    self.eqps[self.name_sub.text()][0].fi = float(self.fi_Label.text())
                    self.eqps[self.name_sub.text()][0].modelo = self.current_model
                    self.eqps[self.name_sub.text()][0].nome_modelo = self.sel_models_combobox.currentText()
                    self.eqps[self.name_sub.text()][0].df2=self.df2
                    self.eqps[self.name_sub.text()][0].varProcs = self.feed_ml2()
                    self.eqps[self.name_sub.text()][0].regime=reg

                self.dump_eq()
                self.close()

            except:
                QMessageBox.warning(self, "Alerta", "Erro ao salvar equipamento")
            pass

    def atualizaTree(self):
        lBases = []
        tipo = "Subsistema"

        for i in self.eqps.values():
            lBases.append(i[1])
        lBases = set(lBases)
        if self.nomeBase in lBases:
            listaItens = self.tree.findItems(self.nomeBase, Qt.MatchExactly, 0)
            listaItens[0].addChild(QTreeWidgetItem([self.name_sub.text(), tipo]))
        else:
            item = QTreeWidgetItem([self.nomeBase])
            self.tree.addTopLevelItem(item)
            item.addChild(QTreeWidgetItem([self.name_sub.text(), tipo]))

    def save_warning_sub(self):
        if self.name_sub.text() =="":
            QMessageBox.warning(self, "Alerta", "É preciso associar um nome ao equipamento ...")
            return False
        elif len(self.eq_combobox.currentData()) == 0:
            QMessageBox.warning(self, "Alerta", "É preciso associar variáveis de processo ao equipamento ...")
            return False
        elif self.sel_models_combobox.currentText() == "":
            QMessageBox.warning(self, "Alerta", "É preciso treinar um modelo do equipamento ...")
            return False
        else:
            return True


    def defcurent_model(self):
        current_modelname = str(self.sel_models_combobox.currentText())

        if current_modelname == 'Automático':
            if not(self.predictor_auto is None):
                self.current_model = self.predictor_auto
            self.current_modelsigla = 'auto'

        if current_modelname == 'Multilayer Perceptron':
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

    def feed_ml(self) -> list:

        list_of_text_and_vals = []

        for var in self.var_procs.keys():
            spin = self.scrollArea.findChild(QDoubleSpinBox, name='num: ' + var)
            val = spin.value()
            list_of_text_and_vals.append((var, val))

        return list_of_text_and_vals

    def feed_ml2(self,tuplas=True) -> list:
        list_of_text_and_vals = []

        for i in reversed(range(self.textLayout.count())):
            texto = self.textLayout.itemAt(i).widget().text()
            num = self.numLayout.itemAt(i).widget().value()
            if tuplas:
                list_of_text_and_vals.append((texto, num))
            else:
                list_of_text_and_vals.append(texto)

        return list_of_text_and_vals

    # Método de suporte para salvar em arquivo do sistema o dicionário de equipamentos/subsistema
    def dump_eq(self):
        try:
            with open('eqs.pickle', 'wb') as fp:
                pickle.dump(self.eqps, fp)
        except Exception as e:
            print(e)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    wd = SubsisWd()
    wd.show()
    app.exec_()
