# tem uma estranha dependência do openpyxl
#import MyWidgets
import time

from PyQt5 import QtWidgets
import io
import os
import sys
from datetime import datetime
import threading
import concurrent.futures
import openpyxl     # previne usar a biblioteca errada para abrir o arquivo .xlsx

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QApplication, QInputDialog, QLabel, QTreeWidgetItem, \
    QScrollArea, QAction, QMenu, QAbstractItemView
from PyQt5 import QtGui
from PyQt5.uic import loadUi
import pandas as pd
import numpy as np
import dashboard3 as db
import eq
import subsis
from subsistema import *
import pickle
from Plataforma import *
from fcfi import *

from filterSelection import *

from fcfiForm import *

from machine_learning import bml_model
from machine_learning.bml_dtmn import bdm_DtMn
from machine_learning import bml_mman

from fpso_interface3 import fpso_eq, fpso_rede
from powerflow.bpf_NetManager import bpf_NetManager

pd.set_option('display.max_columns', None)


class Circuit:
    def __init__(self):
        self.params = ('', 0.0, 0.0)
        self.dados = {
            'gen_bus': {},
            'load_bus': {},
            'trafo': {},
            'trafo3w': {},
            'load': {},
            'process_load': {}
        }

    def bpf_nunet(self, name, f_hz, sn_mva):
        self.params = (name, f_hz, sn_mva)

    def bpf_modfy(self, bpf_type=None, bpf_data=None):
        if bpf_type == 'equipment':
            if not bpf_data['bpf_drop']:
                self.dados[bpf_data['bpf_equip']][bpf_data['bpf_infos']['name']] = bpf_data
            else:
                self.dados[bpf_data['bpf_equip']].pop(bpf_data['bpf_infos']['name'])

    def bpf_get(self, bpf_type=None, bpf_param=None, bpf_elem=None):
        if bpf_type is not None and bpf_param is None and bpf_elem is not None:
            return self.dados[bpf_type][bpf_elem]
        if bpf_type is not None and bpf_param is not None and bpf_elem is None:
            return list(self.dados[bpf_type].keys())
        if bpf_elem is not None:
            return self.dados[bpf_type][bpf_elem]['bpf_infos'][bpf_param]

    def bpf_runpf(self, ml_eqps):
        rede = bpf_NetManager()
        print(self.params)
        rede.bpf_nunet(name=self.params[0], f_hz=self.params[1], sn_mva=self.params[2])
        ml_loads = []
        subsys_log_header1 = '\nRESULTADOS NOS SUBSISTEMAS:\n\n'
        subsys_log_header2 = f'{"NOME DO SUBSISTEMA":>20}     ' \
                            f'{"POTÊNCIA ATIVA (MW)":>20}\n\n'
        subsys_log_result = ''
        subsys_dict = {}
        for tipo in self.dados.keys():
            for nome in self.dados[tipo].keys():
                eqp_data = self.dados[tipo][nome]
                print(eqp_data)
                rede.bpf_modfy(bpf_type='equipment', bpf_data=eqp_data)
                if tipo in ['load', 'process_load']:
                    if tipo == 'process_load':
                        nome_modelo = eqp_data['bpf_infos']['ml_model']
                        if not (nome_modelo in ml_eqps.keys()):
                            return "ERRO: Modelo '" + nome_modelo + "' inexistente ou não carregado"
                        pot_ativa = ml_eqps[nome_modelo][0].outpredict * 0.001
                        ml_loads.append([nome, pot_ativa])
                    else:
                        pot_ativa = eqp_data['bpf_infos']['p_mw']
                    sub_id = eqp_data['bpf_infos']['sub_id']
                    if sub_id != '':
                        subsys_dict[sub_id] = subsys_dict.get(sub_id, 0.0) + pot_ativa
        print(ml_loads)
        all_log = rede.bpf_runpf(ml_loads=ml_loads)
        all_log += subsys_log_header1 + subsys_log_header2
        for sub in subsys_dict.keys():
            pot_ativa = f'{subsys_dict[sub]:.4f}'
            all_log += f'{sub:>20}  ' \
                       f'{pot_ativa:>20}\n'
        return all_log


class Demo(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("fpso_interface5.ui", self)
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowTitle("FPDA")

        # a princípio a linha abaixo será excluída
        self.threads = []

        #inicialização do dataframe da app principal
        self.df = None

        # objeto responsável por fazer a comunicação entre o dashboard e a app principal
        # este objeto recebe as coordenadas de um "box_select" do gráfico de dispersão para análise de fator de carga
        # quando isso é feito ele emite um sinal que dispara "self.newDF", que altera o dataframe para cálculo de FC e
        # FI em batelada
        self.objTransf=filterSelect1()
        #self.novaCoord=False

        #A princípio não há mais necessidade de tratamento deste sinal
        #self.objTransf.itemChanged.connect(self.newDF)

        # Menu-> Arquivo-> Abrir
        self.actionAbrir.triggered.connect(self.open_data)
        # Associação ao ícone
        self.actionAbrir.setIcon(QtGui.QIcon("imgs/db_icon.png"))
        self.actionML.setIcon(QtGui.QIcon("imgs/ml_icon.png"))

        # Menu-> Relatórios-> FC e FI
        self.actionFC_e_FI_Relatorio.triggered.connect(self.fc_fi_rel)

       
        # replace_combobox relacionada ao botão "Substituir valores"(replace_button) +++++ 4a linha
        self.operations = ['Valor Médio', 'Valor Posterior', 'Valor Anterior']
        self.replace_combobox.addItems(self.operations)
        # botão "Substituir valores" associado ao replace_combobox
        self.replace_button.clicked.connect(self.replace_values2)


        # remove_button relacionado ao botão 1 "Eliminar colunas"(remove_button) +++++ 2a linha
        self.remove_button.clicked.connect(self.remove_update_combobox)

        self.manter_button.clicked.connect(self.keep_update_combobox)

        # relacionado ao remove_combobox
        self.reset2.clicked.connect(self.Reset2)

        # limiar_button relacionado ao botão 2 "Eliminar colunas"(limiar_button) (limiar_spin) +++++ 3a linha
        self.limiar_button.clicked.connect(self.remove_update_filter)

        # relacionado ao sub_combobox, sub_lineEdit1 e sub_lineEdit2 ++++++ 1a linha
        self.sub_button.clicked.connect(self.replace_line2)

        # relacionado ao sub_combobox
        self.reset1.clicked.connect(self.Reset1)

        # Botão eliminar linhas
        self.limiar_linhas_button.clicked.connect(self.elimLinhas)

        # Botão "Base original" +++++ 5a linha
        self.reset_button.clicked.connect(self.clear_infobase)

        # Botão "Exibir análise" +++++ 6a linha
        self.run_dash_button.clicked.connect(self.run_dash2)

        # Botão "Visualizar dataframe" +++++ 5a linha
        self.df_show_button.clicked.connect(self.excel_show)
        self.tags_button.clicked.connect(self.tags_show)
        # inicialização da porta do dash, quando acionado pela app principal
        self.port = 8050
        # objeto que controla as portas do dashboard acionado na tela de equipamento
        self.portEqp = db.Porta()

        ############ subsistema : Essa parte do código será substituída ###################
        #self.sbWindow = Subsistema_Window()
        #self.sb_button.clicked.connect(self.subsistema_show)
        #self.sbWindow.subvalidate_button.clicked.connect(self.addSubsistema)


        # criação de um novo subsistema
        ########## apontar o método que vai tratar o evento de criar o subsistema ###################
        self.actionSubsistema.triggered.connect(self.new_sub)

        #Inicialização da variável que receberá as unidades referentes as tags do sistema. Será utilizada no dashboard
        # para que as unidades aparecçam nos eixos dos gráficos
        self.dfTag = None

        # criação de um novo equipamento
        self.actionML.triggered.connect(self.new_eq)
        # edição de um equipamento existente, a partir de um duploclick em um item da árvore
        self.eq_treewidget.doubleClicked.connect(self.open_eq_sub)

        # ----------adicionando o menu de contexto na árvore de equipamentos--------------------------------------
        self.eq_treewidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.eq_treewidget.customContextMenuRequested.connect(self._show_context_menu)
        # ----------------------------------------------------------------

        # ----------adicionando o menu de contexto nas estatísticas--------------------------------------
        self.est_label.setContextMenuPolicy(Qt.CustomContextMenu)
        self.est_label.customContextMenuRequested.connect(self._show_context_menu2)
        # ----------------------------------------------------------------

        # inicialização de do dicionário que armazena os equipamentos de processo (Plataforma.py -> classe: Eqp_Proc
        self.saved_eqs = {}

        # a princípio, duas janelas para fazer a mesma coisa
        # inicialização da janela com formulário para criação de equipamentos
        self.eq_wd = None
        # inicialização da janela com formulário para edição de equipamentos
        self.eqpForm = None
        # inicialização da janela com formulário para edição de subsistemas
        self.subForm = None

        # método que recupera o dicionário de equipamentos de um arquivo local (eqs.pickle) e que tem um argumento
        # default treeLoad=True, que faz a árvore de equipamentos ser atualizada
        self.load_eq2()

        # Cálculo do FC e FI em batelada
        self.actionFC_e_FI.triggered.connect(self.run_fcfi2)
        #self.fcfi_wd = None
        #inicialização da janela de configuração para cálculo de FC e FI em batelada
        self.fcfiForm = None

################################ INÍCIO DO CÓDIGO DA ABA FLUXO DE POTÊNCIA ##################################

        self.circuito = Circuit()
        self.fp_nome_lineEdit.setText('Rede: <Vazia>')
        self.fp_res_textEdit.setFontFamily('Courier New')
        self.fp_cadastra_eq = fpso_eq(self)
        self.fp_cria_rede = fpso_rede(self)
        self.nome_arquivo_rede = ''
        self.prefixo_eq_to_ind = {
            'Barra*: ': 1,
            'Barra : ': 2,
            'Trafo : ': 3,
            'Trafo*: ': 4,
            'Carga : ': 5,
            'Carga*: ': 6,
        }
        self.tipos_de_eq = [
            '',
            'Barra de geração',
            'Barra de carga',
            'Trafo de 2 enrolamentos',
            'Trafo de 3 enrolamentos',
            'Carga Estática',
            'Carga dep. de Processo'
        ]
        self.eq_types = [
            '',
            'gen_bus',
            'load_bus',
            'trafo',
            'trafo3w',
            'load',
            'process_load'
        ]

        ''' Eventos associados à janela de fluxo de potencia'''

        self.fp_criar_flu_PB.clicked.connect(self.criar_fluxo)
        self.fp_abrir_flu_PB.clicked.connect(self.abrir_fluxo)
        self.fp_cad_eq_PB.clicked.connect(self.cadastrar_eq)
        self.fp_rodar_PB.clicked.connect(self.rodar_fluxo)

        # edição de um equipamento existente, a partir de um duploclick em um item da árvore
        self.fp_eq_rede_treewidget.doubleClicked.connect(self.abrir_eq_rede)

        # ----------adicionando o menu de contexto na árvore de equipamentos--------------------------------------
        self.fp_eq_rede_treewidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.fp_eq_rede_treewidget.customContextMenuRequested.connect(self._mostrar_menu_contexto_rede)

    def criar_fluxo(self):
        """ Abrir aba para a criação de um novo arquivo """
        self.fp_eq_rede_treewidget.clear()
        self.circuito = Circuit()
        self.fp_nome_lineEdit.setText('Rede: <Vazia>')
        self.fp_cria_rede.show()
        self.fp_cria_rede.dados_rede = ("", 0.0, 0.0)

    def salvar_rede_criada(self):
        print(self.fp_cria_rede.dados_rede)
        self.fp_nome_lineEdit.setText('Rede: ' + self.fp_cria_rede.dados_rede[0])
        self.circuito.bpf_nunet(
            name=self.fp_cria_rede.dados_rede[0],
            f_hz=self.fp_cria_rede.dados_rede[1],
            sn_mva=self.fp_cria_rede.dados_rede[2]
        )
        circuit_filter = "Circuitos (*.pickle)"
        self.nome_arquivo_rede = QFileDialog.getSaveFileName(self, 'Circuito', '', circuit_filter)[0]
        if self.nome_arquivo_rede != '':
            try:
                with open(self.nome_arquivo_rede, 'wb') as fp:
                    pickle.dump(self.circuito, fp)
            except Exception as e:
                print(e)

    def salvar_rede_alterada(self):
        if self.nome_arquivo_rede != '':
            try:
                with open(self.nome_arquivo_rede, 'wb') as fp:
                    pickle.dump(self.circuito, fp)
            except Exception as e:
                print(e)

    def abrir_fluxo(self):
        """ Abrir aba para selecionar um novo arquivo"""
        self.fp_eq_rede_treewidget.clear()
        self.circuito = Circuit()
        self.fp_nome_lineEdit.setText('Rede: <Vazia>')
        circuit_filter = "Circuitos (*.pickle)"
        self.nome_arquivo_rede = QFileDialog.getOpenFileName(self, 'Circuito', '', circuit_filter)[0]
        if self.nome_arquivo_rede != '':
            try:
                with open(self.nome_arquivo_rede, 'rb') as fp:
                    self.circuito = pickle.load(fp)
                self.fp_nome_lineEdit.setText('Rede: ' + self.circuito.params[0])
                self.exibir_arvore_eq()
            except Exception as e:
                print(e)

    def exibir_arvore_eq(self):
        barras = self.circuito.bpf_get(bpf_type='gen_bus', bpf_param='name')
        barras.extend(self.circuito.bpf_get(bpf_type='load_bus', bpf_param='name'))
        is_gen = True
        for barra in barras:
            if is_gen:
                self.exibir_barra_geracao('Barra*: ' + barra)
                is_gen = False
            else:
                self.exibir_barra_carga('Barra : ' + barra)
        tipos = ['trafo', 'trafo3w', 'load', 'process_load']
        prefixos = ['Trafo : ', 'Trafo*: ', 'Carga : ', 'Carga*: ']
        for t in range(4):
            tipo = tipos[t]
            pref = prefixos[t]
            eqpts = self.circuito.bpf_get(bpf_type=tipo, bpf_param='name')
            for eq in eqpts:
                atrib_barra = 'hv_bus'
                if tipo in ['load', 'process_load']:
                    atrib_barra = 'bus'
                subsis = ''
                if tipo in ['load', 'process_load']:
                    subsis = self.circuito.bpf_get(bpf_type=tipo, bpf_elem=eq, bpf_param='sub_id')
                barra = self.circuito.bpf_get(bpf_type=tipo, bpf_elem=eq, bpf_param=atrib_barra)
                self.fp_cadastra_eq.orig_name = ''
                self.exibir_eqp_pendurado(pref + eq, [barra], 'Subsis: ' + subsis, False)

    def cadastrar_eq(self):
        if self.nome_arquivo_rede == '':
            QMessageBox.warning(self, "Alerta", "Nenhuma rede foi criada ou aberta ...")
            return
        """ Abre a janela .ui secundaria"""
        self.fp_cadastra_eq.fp_eq_combobox.setCurrentText('')
        self.fp_cadastra_eq.fp_eq_combobox.setEnabled(True)
        self.fp_cadastra_eq.stackedWidget.setCurrentIndex(0)
        self.fp_cadastra_eq.limpar_eq()
        self.fp_cadastra_eq.show()

    def exibir_barra_geracao(self, nome):
        if self.fp_eq_rede_treewidget.topLevelItemCount() > 0:
            QMessageBox.warning(self, "Alerta", "Apenas uma barra de geração deve ser criada")
            self.fp_cadastra_eq.raise_()
            return False
        mainItem = QTreeWidgetItem([nome])
        self.fp_eq_rede_treewidget.addTopLevelItem(mainItem)
        mainItem.setToolTip(0, nome)
        return True

    def exibir_barra_carga(self, nome):
        if len(self.fp_eq_rede_treewidget.findItems(nome, Qt.MatchExactly, 0)) > 0:
            QMessageBox.warning(self, "Alerta", "Nome usado")
            self.fp_cadastra_eq.raise_()
            return False
        mainItem = QTreeWidgetItem([nome])
        self.fp_eq_rede_treewidget.addTopLevelItem(mainItem)
        mainItem.setToolTip(0, nome)
        return True

    def exibir_eqp_pendurado(self, nome, barras, subsistema, force):
        if self.fp_cadastra_eq.orig_name == '':
            existing = self.fp_eq_rede_treewidget.findItems(nome, Qt.MatchExactly, 0)
        else:
            nome_ext = nome[:8] + self.fp_cadastra_eq.orig_name
            existing = self.fp_eq_rede_treewidget.findItems(nome_ext, Qt.MatchExactly, 0)
        if len(existing) > 0:
            if force:
                for item in existing:
                    parent = item.parent()
                    parent.removeChild(item)
            else:
                QMessageBox.warning(self, "Alerta", "Nome usado")
                self.fp_cadastra_eq.raise_()
                return False
        itemsBarra = []
        for barra in barras:
            itemBarra = self.fp_eq_rede_treewidget.findItems('Barra*: ' + barra, Qt.MatchExactly, 0)
            if len(itemBarra) == 0:
                itemBarra = self.fp_eq_rede_treewidget.findItems('Barra : ' + barra, Qt.MatchExactly, 0)
                if len(itemBarra) == 0:
                    QMessageBox.warning(self, "Alerta", "Barra inexistente")
                    self.fp_cadastra_eq.raise_()
                    return False
            itemsBarra.append(itemBarra[0])
        for itemBarra in itemsBarra:
            item = QTreeWidgetItem([nome])
            itemBarra.addChild(item)
            item.setToolTip(0, nome)
        if len(subsistema) > 8:
            items_sub = self.fp_eq_rede_treewidget.findItems(subsistema, Qt.MatchExactly, 0)
            if len(items_sub) == 0:
                item_sub = QTreeWidgetItem([subsistema])
                self.fp_eq_rede_treewidget.addTopLevelItem(item_sub)
                item_sub.setToolTip(0, subsistema)
            else:
                item_sub = items_sub[0]
            item = QTreeWidgetItem([nome])
            item_sub.addChild(item)
            item.setToolTip(0, nome)
        return True

    # Evento de duplo click em um item da árvore de equipamentos
    def abrir_eq_rede(self, Qtindex):
        # referência do item selecionado na árvore
        item = self.fp_eq_rede_treewidget.itemFromIndex(Qtindex)
        print(item.text(0))
        self.abrir_ou_editar_eq_rede(item)

    def abrir_ou_editar_eq_rede(self, item):
        if item.text(0)[:8] == 'Subsis: ':
            return
        index_fp = self.prefixo_eq_to_ind[item.text(0)[:8]]
        self.fp_cadastra_eq.fp_eq_combobox.setCurrentText(self.tipos_de_eq[index_fp])
        self.fp_cadastra_eq.fp_eq_combobox.setEnabled(False)
        self.fp_cadastra_eq.stackedWidget.setCurrentIndex(index_fp)
        self.fp_cadastra_eq.preencher_eq(index_fp, item.text(0)[8:])
        self.fp_cadastra_eq.show()

    # construção do menu de contexto da árvore de equipamentos
    def _mostrar_menu_contexto_rede(self, position):
        acao1 = QAction("Remover")
        acao1.triggered.connect(self.remover_eq_rede)

        acao2 = QAction("Editar")
        acao2.triggered.connect(self.editar_eq_rede)

        menu = QMenu(self.fp_eq_rede_treewidget)
        menu.addAction(acao1)
        menu.addAction(acao2)
        menu.exec_(self.fp_eq_rede_treewidget.mapToGlobal(position))

    # método que trata a ação de remover o equipamento, a partir do menu de contexto
    def remover_eq_rede(self):
        column = self.fp_eq_rede_treewidget.currentColumn()
        text = self.fp_eq_rede_treewidget.currentItem().text(column)
        print("remover " + text)
        if text[:8] == 'Subsis: ':
            return
        alteracao_rede = {
            'bpf_equip': self.eq_types[self.prefixo_eq_to_ind[text[:8]]],
            'bpf_drop': True,
            'bpf_infos':
                {
                    'name': text[8:]
                }
        }
        self.circuito.bpf_modfy(bpf_type='equipment', bpf_data=alteracao_rede)
        self.fp_eq_rede_treewidget.clear()
        self.exibir_arvore_eq()

    # método que trata a ação de editar o equipamento, a partir do menu de contexto
    def editar_eq_rede(self):
        item = self.fp_eq_rede_treewidget.currentItem()
        print("editar " + item.text(0))
        self.abrir_ou_editar_eq_rede(item)

    def rodar_fluxo(self):
        if self.nome_arquivo_rede == '':
            QMessageBox.warning(self, "Alerta", "Nenhuma rede foi criada ou aberta")
            return
        """ Escrever no campo resultados """
        print(self.saved_eqs.keys())
        pf_res = self.circuito.bpf_runpf(ml_eqps=self.saved_eqs)
        self.fp_res_textEdit.setText(pf_res)  # resultado

################################ FIM DO CÓDIGO DA ABA FLUXO DE POTÊNCIA ###############################

    # Evento: Menu-> Arquivo-> Abrir ou ícone
    def open_data(self):
        filter = "Planilhas (*.xls *.xlsx *.csv)"
        self.path = QFileDialog.getOpenFileName(self, 'Base de dados', '', filter)[0]
        self.nomeBase = os.path.splitext(os.path.basename(self.path))[0]
        print(self.nomeBase)
        self.filetype = os.path.splitext(os.path.basename(self.path))[1]

        # limpa os combobox das 1a e 2a linhas
        self.sub_combobox.clear()
        self.remove_combobox.clear()
        # ??????????????
        self.sub_combobox.setCurrentIndex(0)
        self.remove_combobox.setCurrentIndex(0)

        # zera o valor do limiar_spin na 3a linha
        self.limiar_spin.setValue(0)

        if self.filetype in ['.xls', '.xlsx', '.csv']:
            if self.filetype in ['.xls', '.xlsx']:
                # dataframe_original
                self.df = pd.read_excel(self.path, engine='openpyxl')

            else:
                # dataframe_original
                self.df = pd.read_csv(self.path)

            self.df = self.df.replace('Bad', np.nan)
            self.df.iloc[:, 1:] = self.df.iloc[:, 1:].apply(pd.to_numeric)
            #self.df.fillna(0)

            # dataframe_trabalho
            self.df2 = self.df.copy(deep=True)
            self.dfFCFI = self.df.copy(deep=True)

            # relacionada à tela de subsistema que será refatorada
            ###desabilitado###
            #self.clear_sb()

            # populando o combobox da 1a linha com as colunas do dataframe_trabalho
            self.fill_combobox(self.sub_combobox, self.df2, 'Todas')


            # inserindo a opção "Todas" na primeira posição
            #self.sub_combobox.insertItem(0, 'Todas')
            # primeira posição apresentada
            self.sub_combobox.setCurrentIndex(0)

            # populando o combobox da 2a linha com as colunas do dataframe_trabalho
            self.fill_combobox(self.remove_combobox, self.df2)

            # atualiza a label com o número de colunas do df de trabalho (self.df2)
            self.counter_cols()
            # atualiza a label com o path do arquivo gerador do df de trabalho
            self.name_base_label.setText(self.path)
            # preenche a área de texto da app com as estatísticas e info do df de trabalho
            self.estatic_show()

            # relacionado a tela de subsistema que será refatorada
            ###desabilitado###
            #self.remove_from_loaded_obj()

        else:
            self.name_base_label.setText('Nenhuma')
            self.est_label.setText("Estatísticas da base de dados.")
            self.corr_label.setText("Correlação da base de dados.")
            self.col_label.setText('')
            self.df = None
            ###desabilitado###
            #self.clear_sb()
            #self.sbWindow.subcol_combobox.clear()

    # Menu-> Relatórios-> FC e FI
    def fc_fi_rel(self):
        try:
            if len(self.saved_eqs)==0:
                QMessageBox.warning(self, "Alerta", "Nenhum equipamento foi criado ainda ...")
            else:
                filter = "Arquivo texto (*.txt)"
                path = 'nada'
                path = QFileDialog.getSaveFileName(self, 'Salvar relatório de FCs e FIs como ...', 'relatorio', filter)[0]
                if not (path == ''):
                    with open(path, 'w') as arquivo:
                        arquivo.write('Relatório de FCs e FIs: ' + datetime.now().__str__() + '\n\n')
                    with open(path, 'a') as arquivo:
                        for eqp_sub in self.saved_eqs.keys():
                            
                            temp = eqp_sub + '    FC = '+str(self.saved_eqs[eqp_sub][0].fc)+'    FI = '+str(self.saved_eqs[eqp_sub][0].fi)+ '\n\n'
                            arquivo.write(temp)
                        
        except Exception as e:
            pass



    # construção do menu de contexto da árvore de equipamentos
    def _show_context_menu(self, position):
        acao1 = QAction("Remover")
        acao1.triggered.connect(self.removeEqp2)

        acao2 = QAction("Editar")
        acao2.triggered.connect(self.editaEqp)

        menu = QMenu(self.eq_treewidget)
        menu.addAction(acao1)
        menu.addAction(acao2)
        menu.exec_(self.eq_treewidget.mapToGlobal(position))

    # construção do menu de contexto para as estatísticas
    def _show_context_menu2(self, position):
        acao1 = QAction("Exportar")
        acao1.triggered.connect(self.exportar)
        menu = QMenu(self.est_label)
        menu.addAction(acao1)
        menu.exec_(self.est_label.mapToGlobal(position))

    # método que trata a ação de remover o equipamento, a partir do menu de contexto
    def removeEqp(self):
        column = self.eq_treewidget.currentColumn()
        text = self.eq_treewidget.currentItem().text(column)

        # a condição abaixo faz com que as ações do menu de contexto não sejam executadas para as bases de dados
        if text in self.saved_eqs.keys():
            del self.saved_eqs[text]
            self.eq_treewidget.clear()
            self.load_eq2()
            self.dump_eq()

    def removeEqp2(self):
        column = self.eq_treewidget.currentColumn()
        text = self.eq_treewidget.currentItem().text(column)
        item = self.eq_treewidget.currentItem()

        # a condição abaixo distingue a ação nos eqp da ação na base de dados
        if text in self.saved_eqs.keys():
            self.eq_treewidget.currentItem().parent().removeChild(item)
            del self.saved_eqs[text]
            self.dump_eq()
        else:
            children=item.takeChildren()
            for i in children:
                del self.saved_eqs[i.text(0)]
            self.dump_eq()
            item2 = self.eq_treewidget.takeTopLevelItem(self.eq_treewidget.indexOfTopLevelItem(item))



    # método que trata a ação de editar o equipamento, a partir do menu de contexto
    def editaEqp(self):
        column = self.eq_treewidget.currentColumn()
        text = self.eq_treewidget.currentItem().text(column)
        print("right-clicked item is " + text)
        if text in self.saved_eqs.keys():
            qtindex = self.eq_treewidget.currentIndex()
            self.open_eq_sub(qtindex)

    def exportar(self):
        filter = "Arquivo texto (*.txt)"
        path='nada'
        path = QFileDialog.getSaveFileName(self, 'Salvar estatísticas como ...','estatísticas', filter)[0]
        if not (path == ''):
            with open(path,'w') as arquivo:
                arquivo.write('Estatísticas: '+self.nomeBase+'\n\n')
            with open(path,'a') as arquivo:
                arquivo.write(self.est_label.text()+'\n\n')
                arquivo.write('Correlações da Base de dados de trabalho: '+self.nomeBase+'\n\n')
                arquivo.write(self.corr_label.text())

       

    # cols é um objeto combobox e dfs um dataframe
    def fill_combobox(self, cols, dfs, text=None):
        cols.clear()
        col = list(dfs.columns.values)
        col.remove('index')
        if text != None:
            col = [text]+col
        cols.addItems(col)

    # conta o numero de colunas do dataframe_trabalho ?????????
    def counter_cols(self):
        self.col_label.setText(str(len(self.df2.columns)-1))

    # apresentação das estatísticas
    def estatic_show(self):
        pd.options.display.max_rows = 150
        pd.options.display.max_columns = 150
        self.est_label.setText('Estatísticas da base de dados.')
        self.corr_label.setText('Correlação da base de dados.')
        try:
            # a princípio isso é uma variável local e não um atributo da classe principal
            # não precisa do self

            # if 'Todas' in self.filtro_combobox.currentData():
            #     self.df3 = self.df2.copy()
            #     self.df3 = self.df3.drop('index', axis=1)
            # else:
            #     col = self.filtro_combobox.currentData()
            #     self.df3 = self.df2.loc[:,col]
            #self.df3 = self.df3.drop('index', axis=1)


            self.df3 = self.df2.copy()
            self.df3 = self.df3.drop('index', axis=1)
            corr = self.df3.corr()
            desc = self.df3.describe(include=[np.number])

            # as estatísticas estão sendo apresentadas como labels e não como uma Text Edit .... avaliar
            self.est_label.setText(str(desc))
            self.corr_label.setText(str(corr))
        # parece tratar o caso de dataframes não numéricos: usa o info() ao invés do describe()
        except Exception as e:
            if type(e).__name__ == "ValueError":
                self.df3 = self.df2.copy()
                self.df3 = self.df3.drop('index', axis=1)
                buffer = io.StringIO()

                desc = self.df3.info(buf=buffer)
                s = buffer.getvalue()
                self.est_label.setText(s)

    # Evento do botão 1 "Eliminar colunas"(remove_button) +++++ 2a linha
    def remove_update_combobox(self):
        if len(self.remove_combobox.currentData()) == 0:
            QMessageBox.warning(self, "Alerta", "Nenhuma coluna foi selecionada ...")
            return
        try:
            col_selected = self.remove_combobox.currentData()
            # elimina a coluna( por enquanto apenas uma) do dataframe_trabalho
            self.df2 = self.df2.drop(col_selected, axis=1)
            self.dfFCFI = self.df.copy(deep=True)

            ###desabilitado###
            #self.remove_from_loaded_obj()

            # atualiza os comboboxes das 1a e 2a linhas
            self.fill_combobox(self.remove_combobox, self.df2)
            self.fill_combobox(self.sub_combobox, self.df2, 'Todas')


            #self.sub_combobox.insertItem(0, 'Todas')
            self.sub_combobox.setCurrentIndex(0)

            # atualiza o label (label_2) com o número de colunas
            self.counter_cols()
            # atualiza as estatísticas com o novo dataframe_trabalho
            self.estatic_show()

        except Exception as e:
            if type(e).__name__ == "AttributeError":
                pass

    # Evento do botão  "Manter"(manter_button) +++++ 2a linha
    def keep_update_combobox(self):
        if len(self.remove_combobox.currentData()) == 0:
            QMessageBox.warning(self, "Alerta", "Nenhuma coluna foi selecionada ...")
            return
        try:
            col_selected = self.remove_combobox.currentData()
            col_selected = ['index']+col_selected
            # elimina a coluna( por enquanto apenas uma) do dataframe_trabalho
            self.df2 = self.df2[col_selected]
            self.dfFCFI = self.df.copy(deep=True)
            # atualiza os comboboxes das 1a e 2a linhas

            ###desabilitado###
            #self.remove_from_loaded_obj()

            self.fill_combobox(self.remove_combobox, self.df2)
            self.fill_combobox(self.sub_combobox, self.df2, 'Todas')

            # self.sub_combobox.insertItem(0, 'Todas')
            self.sub_combobox.setCurrentIndex(0)

            # atualiza o label (label_2) com o número de colunas
            self.counter_cols()
            # atualiza as estatísticas com o novo dataframe_trabalho
            self.estatic_show()
        except Exception as e:
            if type(e).__name__ == "AttributeError":
                pass

    # Evento do botão 2 "Eliminar colunas"(limiar_button) (limiar_spin) +++++ 3a linha
    def remove_update_filter(self):
        try:
            if self.df is None:
                QMessageBox.warning(self, "Alerta", "Nenhum arquivo carregado ...")
            else:
                pfilter = self.limiar_spin.value() / 100

                for col in list(self.df2.columns.values):
                    if self.df2[col].isna().sum() / len(self.df2.index) > pfilter:
                        self.df2 = self.df2.drop(col, axis=1)
                        self.dfFCFI = self.df.copy(deep=True)

                ###desabilitado###
                #self.remove_from_loaded_obj()

                self.fill_combobox(self.remove_combobox, self.df2)
                self.fill_combobox(self.sub_combobox, self.df2,'Todas')
                #self.sub_combobox.insertItem(0, 'Todas')
                self.sub_combobox.setCurrentIndex(0)
                self.counter_cols()
                self.estatic_show()

        except Exception as e:
            if type(e).__name__ == "ValueError":
                self.est_label.setText("Estatísticas da base de dados.")
                self.corr_label.setText("Correlação da base de dados.")

    # Evento do botão "Substituir valores" associado ao replace_combobox ++++ 4a linha
    def replace_values2(self):
        try:

            if self.replace_combobox.currentText() == self.operations[0]:
                for col in list(self.df2.columns.values):
                    if col != 'index':
                        # substituindo 0 pela média. Era para substituir valores faltantes
                        self.df2[col] = self.df2[col].fillna(self.df2[col].mean())
                        self.dfFCFI = self.df.copy(deep=True)

            elif self.replace_combobox.currentText() == self.operations[1]:
                for col in list(self.df2.columns.values):
                    if col != 'index':
                        # substitui o 0 por NaN (faltante) e depois substitui NaN pelo anterior
                        self.df2[col] = self.df2[col].fillna(method='bfill')
                        self.dfFCFI = self.df.copy(deep=True)

            elif self.replace_combobox.currentText() == self.operations[2]:
                for col in list(self.df2.columns.values):
                    if col != 'index':
                        self.df2[col] = self.df2[col].fillna(method='ffill')
                        self.dfFCFI = self.df.copy(deep=True)

            self.estatic_show()
        except Exception as e:
            if type(e).__name__ == "AttributeError":
                QMessageBox.warning(self, "Alerta", "Nenhum arquivo carregado ...")

    def elimLinhas(self):
        try:
            # número de variáveis
            total = len(self.df2.iloc[1, :]) - 1 # pois é necessário desconsiderar a colunda 'indice'
            print(len(self.df2))
            pct = self.limiar_linhas_spin.value()
            pctTot = pct * total / 100
            if self.elim_comboBox.currentText() == '=':
                # verifica se a percentagem do número de ocorrências de um determinado valor supera a percentagem indicada pelo usuários
                ind = self.df2[self.df2[self.df2 == self.val_linhas_spin.value()].count(axis=1) > pctTot].index
            elif self.elim_comboBox.currentText() == '>':
                # para fazer a comparação com o '>' é necessário excluir a coluna 'índice'
                ind = self.df2[self.df2[self.df2.iloc[:, 1:] > self.val_linhas_spin.value()].count(axis=1) > pctTot].index
            else:
                ind = self.df2[self.df2[self.df2.iloc[:, 1:] < self.val_linhas_spin.value()].count(axis=1) > pctTot].index
            self.df2 = self.df2.drop(ind)
            print(len(self.df2))
            self.estatic_show()
        except Exception as e:
            print(e)

    # Evento do botão "Base original" +++++ 5a linha
    def clear_infobase(self):
        try:
            if self.df is None:
                QMessageBox.warning(self, "Alerta", "Nenhum arquivo carregado ...")
            else:
                self.df2 = self.df.copy(deep=True)
                self.dfFCFI = self.df.copy(deep=True)
                ###desabilitado###
                #self.clear_sb()

                self.fill_combobox(self.sub_combobox, self.df2, 'Todas')
                #self.sub_combobox.insertItem(0, 'Todas')
                self.sub_combobox.setCurrentIndex(0)
                self.fill_combobox(self.remove_combobox, self.df2)
                self.counter_cols()
                self.estatic_show()
                ###desabilitado###
                #self.remove_from_loaded_obj()
        except Exception as e:
            if type(e).__name__ == "AttributeError":
                # print('No dateframe loaded.')
                pass

    # Evento do botão "Exibir análise" +++++ 6a linha
    def run_dash2(self):
        if self.df is None:
            QMessageBox.warning(
                self, "Alerta",
                "É preciso abrir um arquivo de dados antes de exibir a análise")
        else:
            t = db.DashThread(self.df2, self.objTransf, dataTags=self.dfTag,  port=self.port)
            self.port += 1
            t.start()

    # Evento do botão "Visualizar dataframe" +++++ 5a linha
    def show_excel(self):
        try:
            # desenecessária a cópia do dataframe de trabalho
            self.df4 = self.df2.copy()
            self.df4.to_excel('dataframe_de_trabalho.xlsx', index=False)

            os.system('start excel.exe dataframe_de_trabalho.xlsx')
        except Exception as e:
            if type(e).__name__ == "AttributeError":
                pass

    # Thread para chamar a função acima
    def excel_show(self):
        try:
            if self.df is None:
                QMessageBox.warning(self, "Alerta", "Nenhum arquivo carregado ...")
            else:
                threading.Thread(target=self.show_excel).start()
        except Exception as e:
            pass

    # Evento do botão "Substituir por"
    def replace_line2(self):

        if len(self.sub_combobox.currentData()) == 0:
            QMessageBox.warning(self, "Alerta", "Nenhuma coluna foi selecionada ...")
            return

        value1 = self.sub_lineEdit1.text()
        value2 = self.sub_lineEdit2.text()

        if self.isanumber(self.sub_lineEdit1.text()) == True:
            value1 = float(self.sub_lineEdit1.text())

        if self.isanumber(self.sub_lineEdit2.text()) == True:
            value2 = float(self.sub_lineEdit2.text())

        # permite que os valores faltantes (designados por null) sejam substituídos por qualquer valor
        if value1 == 'null':
            value1 = np.nan

        try:
            if 'Todas' in self.sub_combobox.currentData():
                self.df2.iloc[:, 1:] = self.df2.iloc[:, 1:].replace(value1, value2)
            else:
                col = self.sub_combobox.currentData()
                self.df2[col] = self.df2[col].replace(value1, value2)
            self.dfFCFI = self.df.copy(deep=True)
            self.estatic_show()

        except Exception as e:
            print(e)
            if type(e).__name__ == "AttributeError":
                print('No dateframe loaded.')
                pass

    # método suporte para a função acima
    def isanumber(self, value):
        try:
            float(value)
        except ValueError:
            return False
        else:
            return True

    # Evento do botão Reset da seção "Substituir valores"
    def Reset1(self):
        if self.df is None:
            QMessageBox.warning(self, "Alerta", "Nenhuma coluna disponível ...")
        else:
            self.sub_combobox.unCheckAll()

    # Evento do botão Reset da seção "Manipular colunas"
    def Reset2(self):
        if self.df is None:
            QMessageBox.warning(self, "Alerta", "Nenhuma coluna disponível ...")
        else:
            self.remove_combobox.unCheckAll()



    # Evento do botão "Carregar unidades" que antes era "Visualizar tags"
    # Não há mais visualização de tags, apenas atualização do dfTags com
    # as unidades de engenharia. Mudar o nome do método é uma boa alternativa
    def tags_excel(self):
        filter = "Planilhas (*.xls *.xlsx *.csv)"
        #dfTag = None
        path = QFileDialog.getOpenFileName(self, 'Base de dados', '', filter)[0]
        filetype = os.path.splitext(os.path.basename(path))[1]
        if filetype in ['.xls', '.xlsx', '.csv']:
            if filetype in ['.xls', '.xlsx']:
                # dataframe_original
                self.dfTag = pd.read_excel(path, engine='openpyxl')

            else:
                # dataframe_original
                self.dfTag = pd.read_csv(path)
        if self.dfTag is None:
            print('dftag eh none no main')
        else:
            print('dftag nao e none no main')



    # Thread para lançar o método acima
    def tags_show(self):
        try:
            if self.df is None:
                QMessageBox.warning(self, "Alerta", "Nenhum arquivo carregado ...")
            else:
                threading.Thread(target=self.tags_excel).start()
        except Exception as e:
            pass

    # relacionado à tela de subsistema que será refatorada
    def subsistema_show(self):
        try:
            self.fill_combobox(self.sbWindow.subcol_combobox, self.df2)
            self.fill_combobox(self.sbWindow.subcol_combobox_2, self.df2)
        except Exception as e:
            pass
        self.sbWindow.displayInfo()

    # relacionado à tela de subsistema que será refatorada
    def addSubsistema(self):
        try:
            if self.sbWindow.global_v is True:
                df1 = self.df2[self.sbWindow.temp[1]]
                df2 = self.df2[self.sbWindow.temp[2]]
                dftrab = df1.sum(axis=1).subtract(df2.sum(axis=1))
                self.df2[self.sbWindow.temp[0]] = dftrab
                self.dfFCFI = self.df.copy(deep=True)

                self.fill_combobox(self.remove_combobox, self.df2)
                self.fill_combobox(self.sub_combobox, self.df2, 'Todas')

                self.sub_combobox.setCurrentIndex(0)

                # atualiza o label (label_2) com o número de colunas
                self.counter_cols()
                # atualiza as estatísticas com o novo dataframe_trabalho
                self.estatic_show()

        except Exception as e:
            pass

    # relacionado à tela de subsistema que será refatorada
    def clear_sb(self):
        self.sbWindow.loaded_obj.clear()
        self.sbWindow.subnewsystem_editline.clear()
        self.sbWindow.sb_listWidget.clear()
        self.sbWindow.sb_listWidget2.clear()

    # relacionado à tela de subsistema que será refatorada
    def remove_from_loaded_obj(self):
        try:
            templist = []
            for i in range(len(self.sbWindow.loaded_obj)):
                if self.sbWindow.loaded_obj[i][0] not in list(self.df2.columns):
                    templist.append(self.sbWindow.loaded_obj[i])
            if len(templist) != 0:
                for sub in templist:
                    self.sbWindow.loaded_obj.remove(sub)

                self.sbWindow.sb_listWidget2.clear()

                self.sbWindow.fill_listwidget()

        except Exception as e:
            pass


    # Esse método é chamado pelo "getDataframe" para abrir uma janela de seleção de arquivo, caso nenhuma base tenha
    # sido carregada. o getDataframe está relacionado ao evento de criação de um novo equipamento. A sugestão é associar
    # o new_eq a esse evento, com o trecho de código que está comentado
    def new_eq(self):
        # try:
        #     self.eq_wd = eq.EQ_wd(self.portEqp, tree=self.eq_treewidget,eqps= self.saved_eqs, dfTags=self.dfTag)
        #     self.eq_wd.open_data_ml()
        #     if self.eq_wd.df_ml is None:
        #         self.eq_wd.close()
        #         return
        #     #self.eq_wd.save_eq_pushbutton.clicked.connect(self.save_eq)
        #     self.eq_wd.show()
        # except Exception as e:
        #     print(e)

        try:
            if self.df is None:
                self.open_data()
                return

            # chamar um formulário de equipamento para preenchimento
            self.eqpForm = eq.EQ_wd(self.portEqp, tree=self.eq_treewidget, eqps=self.saved_eqs, dfTags=self.dfTag, nomeBase=self.nomeBase)
            self.eqpForm.setDataframe(self.df2)
            self.eqpForm.show()
        except Exception as e:
            print(e)

    # Evento associado ao botão Subsistema
    def new_sub(self):
        if self.df is None:
            self.open_data()
            return
        try:
            self.subForm = subsis.SubsisWd(eqps=self.saved_eqs, df2=self.df2,  portEqp= self.portEqp, dfTags=self.dfTag, nomeBase=self.nomeBase, tree=self.eq_treewidget)
            self.subForm.show()
        except:
            QMessageBox.warning(self, "Alerta", "Necessário carregar base e criar equipamentos")
            return

    # método para gravar o dicionário de equipamentos em um arquivo de sistema
    def dump_eq(self):
        try:
            with open('eqs.pickle', 'wb') as fp:
                pickle.dump(self.saved_eqs, fp)
        except Exception as e:
            print(e)


    # método para carregar o dicionário de equipamentos, a partir de um arquivo do sistema
    # por default também atualiza a árvore de equipamentos. Essa é uma implementação DIFERENTE para organização
    #
    def load_eq2(self, treeLoad=True):
        try:

            if len(self.saved_eqs)==0:
                with open('eqs.pickle', 'rb') as fp:
                    self.saved_eqs = pickle.load(fp)

            if treeLoad:
                #header = ["Equipamentos"]

                treeDict={}
                lBases=[]
                leqps=self.saved_eqs.keys()

                #montando uma lista com as bases gravadas
                for i in self.saved_eqs.values():
                    lBases.append(i[1])
                #tirando as bases repetidas
                y2=sorted(set(lBases))

                # montando um dicionário que associa a cada base (key) uma lista de equipamentos (values)
                for bases in y2:
                    # armazenando a lista de values( equipamentos associados a uma base)
                    temp = []
                    for eqps, basesN in zip(leqps, lBases):
                        if bases == basesN:
                            temp.append(eqps)
                    temp=sorted(temp)
                    #montando o dicionário
                    treeDict[bases] = temp.copy()

                headers = ["Nome", "Tipo"]
                self.eq_treewidget.setHeaderLabels(headers)

                for bases in treeDict.keys():
                    # 1 nível,  o nome da base
                    tree_widget_item = QTreeWidgetItem([bases])
                    # adicionando em segundo nível os equipamentos pertencentes àquela base
                    for equip in treeDict[bases]:
                        if self.saved_eqs[equip][2]=="Subsistema":
                            tipo="Subsistema"
                        else:
                            tipo="Equipamento"
                        tree_widget_item.addChild(QTreeWidgetItem([equip, tipo]))
                    # colocando o conjunto na árvore de equipamentos
                    self.eq_treewidget.addTopLevelItem(tree_widget_item)
                    # for equip in treeDict[bases]:
                    #     tree_widget_item.addChild(QTreeWidgetItem([equip, "Equipamento"]))
                # headers = ["Nome", "Tipo"]
                # self.eq_treewidget.setHeaderLabels(headers)
                self.eq_treewidget.resizeColumnToContents(0)
        except Exception as e:
            if not os.path.exists('eqs.pickle'):
                QMessageBox.warning(self, "Alerta", "Nenhum equipamento foi criado ainda....")
                return
            print(e)




    # Evento de duplo click em um item da árvore de equipamentos

    def open_eq_sub(self, Qtindex):

        # if self.df is None:
        #     self.open_data()
        #     return

        # column = self.eq_treewidget.currentColumn()
        # text = self.eq_treewidget.currentItem().text(column)
        #
        # if text in self.saved_eqs.keys():
        #     qtindex = self.eq_treewidget.currentIndex()
        #     self.open_eq_sub(qtindex)


        # referência do item selecionado na árvore
        column = self.eq_treewidget.currentColumn()
        item = self.eq_treewidget.itemFromIndex(Qtindex)
        text = item.text(0)
        #tipo = self.saved_eqs[item.text(0)][2]

        # a condição abaixo não permite a ação de duplo click na base de dados
        if text in self.saved_eqs.keys():
            tipo = self.saved_eqs[text][2]
            if tipo == "Equipamento":
                self.open_eq2(Qtindex)
            else:
                self.open_sub2(Qtindex)


    def open_eq2(self, Qtindex):
        try:
            # if self.df is None:
            #     self.open_data()
            #     return

            # referência do item selecionado na árvore
            item = self.eq_treewidget.itemFromIndex(Qtindex)
            print(item.text(0))

            # resgatar obj do dicionário de persistência
            objEqp = self.saved_eqs[item.text(0)][0]

            # chamar um formulário de equipamento para preenchimento
            self.eqpForm = eq.EQ_wd(self.portEqp, tree=self.eq_treewidget, eqps=self.saved_eqs, dfTags=self.dfTag, nomeBase=self.saved_eqs[item.text(0)][1])

            ##### solução temporária. A princípio cada eqp vai guardar o seu próprio df #######3
            #self.eqpForm.setDataframe(self.df2)
            self.eqpForm.setDataframe(objEqp.df)

            # preencher os campos do formulário com os dados do objEqp

            ############################ Seção Configuração ##############################
            self.eqpForm.name_eq.setText(objEqp.nome)
            # não permite a edição do nome
            self.eqpForm.name_eq.setEnabled(False)
            self.eqpForm.pot_nom.setValue(objEqp.potNominal)
            self.eqpForm.pot_proc.setValue(objEqp.potProc)
            print('load_obj_eq 2')
            self.eqpForm.fat_pot.setValue(objEqp.fP)

            #self.eqpForm.df2_ml = objEqp.df
            #self.eqpForm.setDataframe(self.df2)
            # populando o combobox da 1a linha com as colunas do dataframe_trabalho
            self.eqpForm.fill_combobox(self.eqpForm.var_pro, objEqp.df, 'Todas')

            # primeira posição apresentada
            self.eqpForm.var_pro.setCurrentIndex(0)

            # populando o combobox da 2a linha com as colunas do dataframe_trabalho
            self.eqpForm.fill_combobox(self.eqpForm.var_dep, objEqp.df)

            # marcando as variáveis que foram usadas para descrever o equipamento e, com elas, populando
            # a seção Estimativa

            indexDep = self.eqpForm.var_dep.findText(objEqp.varDep)
            self.eqpForm.var_dep.setCurrentIndex(indexDep)
            #QtItem = self.eqpForm.var_dep.model().item(indexDep)
            #QtItem.setCheckState(Qt.Checked)


            for var in objEqp.varProc:
                index = self.eqpForm.var_pro.findText(var[0])
                QtItem = self.eqpForm.var_pro.model().item(index)
                QtItem.setCheckState(Qt.Checked)
                label = QLabel(var[0])
                label.setObjectName('label: ' + var[0])
                spin = QDoubleSpinBox()
                spin.setMaximum(9000000000.00)
                spin.setObjectName('num: ' + var[0])
                spin.setValue(var[1])

                self.eqpForm.textLayout.addWidget(label)
                self.eqpForm.numLayout.addWidget(spin)

            ############################ Seção Machine Learning ##############################

            # a lista de modelos de ML é carregada na chamada do construtor do formulário (eqpForm) em models_combobox

            # resgatando o modelo do objEqp
            self.eqpForm.current_model = objEqp.modelo


            # marcando o modelo gravado em models_combobox
            indexMod = self.eqpForm.models_combobox.findText(objEqp.modelo_nome)
            QtItem = self.eqpForm.models_combobox.model().item(indexMod)
            QtItem.setCheckState(Qt.Checked)

            # populando a tab Modelos com ao informação do modelo e respectivas estatísticas
            text = QLabel(
                f"{self.eqpForm.current_model.bbb_info()}\n\n Estatísticas:\n{self.eqpForm.current_model.bbb_stats()}")
            scroll = QScrollArea()
            scroll.setWidget(text)
            print('load_obj_eq 5')
            self.eqpForm.stats_tab.clear()
            print('load_obj_eq 6')
            self.eqpForm.stats_tab.addTab(scroll, objEqp.modelo_nome)
            print('load_obj_eq 7')
            self.eqpForm.sel_models_combobox.addItem(objEqp.modelo_nome)
            print('load_obj_eq 8')
            self.eqpForm.output_predict.setText(str(objEqp.outpredict))
            print('load_obj_eq 9')
            ############################ Seção FC e FI ##############################

            self.eqpForm.fc_Label.setText(str(objEqp.fc))
            print('load_obj_eq 10')
            self.eqpForm.fi_Label.setText(str(objEqp.fi))
            print('load_obj_eq 11')
            self.eqpForm.show()
            print('load_obj_eq 12')
        except Exception as e:
            print(e)



    # Evento de duplo click em um item da árvore de subsistemas
    def open_sub2(self, Qtindex):
        try:
            # if self.df is None:
            #     self.open_data()
            #     return

            # referência do item selecionado na árvore
            item = self.eq_treewidget.itemFromIndex(Qtindex)

            # resgatar obj do dicionário de persistência
            objSub = self.saved_eqs[item.text(0)][0]

            # chamar um formulário de subsistema para preenchimento
            self.subForm = subsis.SubsisWd(eqps=self.saved_eqs, portEqp=self.portEqp, tree=self.eq_treewidget,
                                           dfTags=self.dfTag, nomeBase=self.saved_eqs[item.text(0)][1], novo=False)

            self.subForm.df2=objSub.df2


           # preencher os campos do formulário com os dados do objEqp

            ############################ Seção Configuração ##############################
            self.subForm.name_sub.setText(objSub.nome)
            # não permite a edição do nome
            self.subForm.name_sub.setEnabled(False)
            self.subForm.pot_nom.setValue(objSub.pot_nom)
            self.subForm.pot_proc.setValue(objSub.pot_proc)

            self.subForm.var_procs=objSub.varProcs
            self.subForm.current_model=objSub.modelo

            ############### A princípio não é necessário ... Popula dropdown de modelos do ML
            self.subForm.models_combobox.clear()
            self.subForm.models_combobox.addItem("Automático")
            self.subForm.models_combobox.addItems(list(bml_mman.bmm_MM.bmm_amdls()))

            # marca o modelo que foi gravado
            index = self.subForm.models_combobox.findText(objSub.nome_modelo)
            QtItem = self.subForm.models_combobox.model().item(index)
            QtItem.setCheckState(Qt.Checked)

            for var in objSub.eqpsSelected:
                index = self.subForm.eq_combobox.findText(var)
                QtItem = self.subForm.eq_combobox.model().item(index)
                QtItem.setCheckState(Qt.Checked)

            for var in objSub.varProcs:
                label = QLabel(var[0])
                label.setObjectName('label: ' + var[0])
                spin = QDoubleSpinBox()
                spin.setMaximum(9000000000.00)
                spin.setObjectName('num: ' + var[0])
                spin.setValue(var[1])

                self.subForm.textLayout.addWidget(label)
                self.subForm.numLayout.addWidget(spin)

            

            # populando a tab Modelos com ao informação do modelo e respectivas estatísticas
            text = QLabel(
                f"{objSub.modelo.bbb_info()}\n\n Estatísticas:\n{objSub.modelo.bbb_stats()}")
            scroll = QScrollArea()
            scroll.setWidget(text)

            self.subForm.stats_tab.clear()

            self.subForm.stats_tab.addTab(scroll, objSub.nome_modelo)

            self.subForm.sel_models_combobox.addItem(objSub.nome_modelo)

            self.subForm.output_predict.setText(str(objSub.output))


            ############################ Seção FC e FI ##############################

            self.subForm.reg_deno_SB.setValue(objSub.regime[0])
            self.subForm.reg_num_SB.setValue(objSub.regime[1])

            self.subForm.fc_Label.setText(str(objSub.fc))

            self.subForm.fi_Label.setText(str(objSub.fi))

            self.subForm.show()

        except Exception as e:
            print(e)

    # evento associado ao botão "FC e FI" para cálculo em batelada
    def run_fcfi2(self):
        if self.df is None:
            self.open_data()
            return
        print('fcfi_1')
        self.fcfiForm=fcfiForm(self.saved_eqs,self.dfFCFI,self.objTransf, self.nomeBase)
        print('fcfi_2')
        self.fcfiForm.show()
        #self.fcfiForm.calc_up_fcfi()
        print('fcfi_3')
        self.dump_eq()
        print('fcfi_4')
if __name__ == '__main__':
    app = QApplication([])
    window = Demo()
    window.show()
    app.exec_()
