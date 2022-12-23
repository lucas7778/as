import threading

from PyQt5.QtCore import QEventLoop
from PyQt5.QtGui import QShowEvent
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import uic
import sys

from powerflow.bpf_NetManager import bpf_NetManager

class fpso_eq(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.second = uic.loadUi('fpso_fp_eq_interface.ui', self).__init__
        self.parent_win = parent
        self.orig_name = ''

        ''' Eventos associados a janela "Tipos de equipamentos" '''

        ''' Eventos referentes a troca de aba de equipamento '''
        self.stackedWidget.setCurrentIndex(0)
        self.fp_eq_combobox.currentIndexChanged.connect(self.alterar_janela)

        ''' Eventos referentes às abas de equipamento'''
        self.fp_eq_ok_bg_PB.clicked.connect(self.confirmar_bg_eq)
        self.fp_eq_cancel_bg_PB.clicked.connect(self.cancelar_bg_eq)

        self.fp_eq_ok_bc_PB.clicked.connect(self.confirmar_bc_eq)
        self.fp_eq_cancel_bc_PB.clicked.connect(self.cancelar_bc_eq)

        self.fp_eq_ok_t2_PB.clicked.connect(self.confirmar_t2_eq)
        self.fp_eq_cancel_t2_PB.clicked.connect(self.cancelar_t2_eq)

        self.fp_eq_ok_t3_PB.clicked.connect(self.confirmar_t3_eq)
        self.fp_eq_cancel_t3_PB.clicked.connect(self.cancelar_t3_eq)

        self.fp_eq_ok_ce_PB.clicked.connect(self.confirmar_ce_eq)
        self.fp_eq_cancel_ce_PB.clicked.connect(self.cancelar_ce_eq)

        self.fp_eq_ok_cp_PB.clicked.connect(self.confirmar_cp_eq)
        self.fp_eq_cancel_cp_PB.clicked.connect(self.cancelar_cp_eq)

        ''' Populando as combobox '''  # Modificar lista com nomes
        ''' Trafo de 2 enrolamentos '''
        self.fp_barra_a_t2_combobox.addItem('1')
        self.fp_barra_b_t2_combobox.addItem('2')

        ''' Trafo de 3 enrolamentos '''
        self.fp_barra_a_t3_combobox.addItem('3')
        self.fp_barra_m_t3_combobox.addItem('4')
        self.fp_barra_b_t3_combobox.addItem('5')

        ''' Carga estática '''
        self.fp_barra_ce_combobox.addItem('6')

        ''' Carga dep. de processo '''
        self.fp_barra_ce_combobox.addItem('7')
        self.fp_model_cp_combobox.addItem('8')

    ''' Método para a mudança de janela dependendo do selecionado na combobox '''

    def alterar_janela(self):
        index_fp = self.fp_eq_combobox.currentIndex()
        self.stackedWidget.setCurrentIndex(index_fp)

    ''' Métodos referentes à barra de gereção '''

    def preencher_combo_barra(self, combo, nome_barra):
        barras = self.parent_win.circuito.bpf_get(bpf_type='gen_bus', bpf_param='name')
        barras.extend(self.parent_win.circuito.bpf_get(bpf_type='load_bus', bpf_param='name'))
        for i in range(combo.count() - 1, -1, -1):
            combo.removeItem(i)
        combo.addItem('')
        combo.addItems(barras)
        if nome_barra not in barras:
            nome_barra = ''
        if nome_barra == '':
            combo.setCurrentIndex(0)
        else:
            idx = barras.index(nome_barra)
            combo.setCurrentIndex(idx + 1)

    def preencher_combo_modelo(self, combo, nome_modelo):
        model_tree = self.parent_win.eq_treewidget
        modelos = []
        for i in range(0, model_tree.topLevelItemCount()):
            item_i = model_tree.topLevelItem(i)
            for j in range(0, item_i.childCount()):
                modelos.append(item_i.child(j).text(0))
        for i in range(combo.count() - 1, -1, -1):
            combo.removeItem(i)
        combo.addItem('')
        combo.addItems(modelos)
        if not (nome_modelo in modelos):
            nome_modelo = ''
        if nome_modelo == '':
            combo.setCurrentIndex(0)
        else:
            idx = modelos.index(nome_modelo)
            combo.setCurrentIndex(idx + 1)

    def limpar_eq(self):
        self.orig_name = ''

        # Barra de geração
        self.fp_nome_bg_lineEdit.setEnabled(True)
        self.fp_nome_bg_lineEdit.setText('')
        self.fp_tensao_bg_SB.setValue(0.0)
        self.fp_tensao_bg_SB.setMaximum(9999.99)
        self.fp_pot_bg_SB.setValue(0.0)
        self.fp_pot_bg_SB.setMaximum(9999.99)
        self.fp_servico_bg_RB.setChecked(False)

        # Barra de carga
        self.fp_nome_bc_lineEdit.setEnabled(True)
        self.fp_nome_bc_lineEdit.setText('')
        self.fp_tensao_bc_SB.setValue(0.0)
        self.fp_tensao_bc_SB.setMaximum(9999.99)
        self.fp_servico_bc_RB.setChecked(False)

        # Trafo de 2 enrolamentos
        # self.fp_nome_t2_lineEdit.setEnabled(True)
        self.fp_nome_t2_lineEdit.setText('')
        self.preencher_combo_barra(self.fp_barra_a_t2_combobox, '')
        self.preencher_combo_barra(self.fp_barra_b_t2_combobox, '')
        self.fp_pot_t2_SB.setValue(0.0)
        self.fp_pot_t2_SB.setMaximum(9999.99)
        self.fp_tensao_a_t2_SB.setValue(0.0)
        self.fp_tensao_a_t2_SB.setMaximum(9999.99)
        self.fp_tensao_b_t2_SB.setValue(0.0)
        self.fp_tensao_b_t2_SB.setMaximum(9999.99)
        self.fp_servico_t2_RB.setChecked(False)

        # Trafo de 3 enrolamentos
        # self.fp_nome_t3_lineEdit.setEnabled(True)
        self.fp_nome_t3_lineEdit.setText('')
        self.preencher_combo_barra(self.fp_barra_a_t3_combobox, '')
        self.preencher_combo_barra(self.fp_barra_m_t3_combobox, '')
        self.preencher_combo_barra(self.fp_barra_b_t3_combobox, '')
        self.fp_pot_a_t3_SB.setValue(0.0)
        self.fp_pot_a_t3_SB.setMaximum(9999.99)
        self.fp_pot_m_t3_SB.setValue(0.0)
        self.fp_pot_m_t3_SB.setMaximum(9999.99)
        self.fp_pot_b_t3_SB.setValue(0.0)
        self.fp_pot_b_t3_SB.setMaximum(9999.99)
        self.fp_tensao_a_t3_SB.setValue(0.0)
        self.fp_tensao_a_t3_SB.setMaximum(9999.99)
        self.fp_tensao_m_t3_SB.setValue(0.0)
        self.fp_tensao_m_t3_SB.setMaximum(9999.99)
        self.fp_tensao_b_t3_SB.setValue(0.0)
        self.fp_tensao_b_t3_SB.setMaximum(9999.99)
        self.fp_servico_t3_RB.setChecked(False)

        # Carga estática
        # self.fp_nome_ce_lineEdit.setEnabled(True)
        self.fp_nome_ce_lineEdit.setText('')
        self.preencher_combo_barra(self.fp_barra_ce_combobox, '')
        self.fp_pot_ce_SB.setValue(0.0)
        self.fp_pot_ce_SB.setMaximum(9999.99)
        self.fp_fatp_ce_SB.setValue(0.0)
        self.fp_fatp_ce_SB.setMaximum(9999.99)
        self.fp_subsis_ce_lineEdit.setText('')
        self.fp_servico_ce_RB.setChecked(False)

        # Carga de processo
        # self.fp_nome_cp_lineEdit.setEnabled(True)
        self.fp_nome_cp_lineEdit.setText('')
        self.preencher_combo_barra(self.fp_barra_cp_combobox, '')
        self.preencher_combo_modelo(self.fp_model_cp_combobox, '')
        self.fp_fatp_cp_SB.setValue(0.0)
        self.fp_fatp_cp_SB.setMaximum(9999.99)
        self.fp_subsis_cp_lineEdit.setText('')
        self.fp_servico_cp_RB.setChecked(False)

    def preencher_eq(self, index_tipo_eq, nome):
        self.orig_name = nome
        if index_tipo_eq == 1:  # Barra de geração
            self.fp_nome_bg_lineEdit.setText(nome)
            self.fp_nome_bg_lineEdit.setEnabled(False)
            self.fp_tensao_bg_SB.setValue(
                self.parent_win.circuito.bpf_get(
                    bpf_type='gen_bus', bpf_elem=nome, bpf_param='vn_kv'
                )
            )
            self.fp_pot_bg_SB.setValue(
                self.parent_win.circuito.bpf_get(
                    bpf_type='gen_bus', bpf_elem=nome, bpf_param='p_mw'
                )
            )
            self.fp_servico_bg_RB.setChecked(
                self.parent_win.circuito.bpf_get(
                    bpf_type='gen_bus', bpf_elem=nome, bpf_param='in_service'
                )
            )
        elif index_tipo_eq == 2:  # Barra de carga
            self.fp_nome_bc_lineEdit.setText(nome)
            self.fp_nome_bc_lineEdit.setEnabled(False)
            self.fp_tensao_bc_SB.setValue(
                self.parent_win.circuito.bpf_get(
                    bpf_type='load_bus', bpf_elem=nome, bpf_param='vn_kv'
                )
            )
            self.fp_servico_bg_RB.setChecked(
                self.parent_win.circuito.bpf_get(
                    bpf_type='load_bus', bpf_elem=nome, bpf_param='in_service'
                )
            )
        elif index_tipo_eq == 3:  # Trafo de 2 enrolamentos
            self.fp_nome_t2_lineEdit.setText(nome)
            # self.fp_nome_t2_lineEdit.setEnabled(False)
            self.preencher_combo_barra(
                self.fp_barra_a_t2_combobox, self.parent_win.circuito.bpf_get(
                    bpf_type='trafo', bpf_elem=nome, bpf_param='hv_bus'
                )
            )
            self.preencher_combo_barra(
                self.fp_barra_b_t2_combobox, self.parent_win.circuito.bpf_get(
                    bpf_type='trafo', bpf_elem=nome, bpf_param='lv_bus'
                )
            )
            self.fp_tensao_a_t2_SB.setValue(
                self.parent_win.circuito.bpf_get(
                    bpf_type='trafo', bpf_elem=nome, bpf_param='vn_hv_kv'
                )
            )
            self.fp_tensao_b_t2_SB.setValue(
                self.parent_win.circuito.bpf_get(
                    bpf_type='trafo', bpf_elem=nome, bpf_param='vn_lv_kv'
                )
            )
            self.fp_pot_t2_SB.setValue(
                self.parent_win.circuito.bpf_get(
                    bpf_type='trafo', bpf_elem=nome, bpf_param='sn_mva'
                )
            )
            self.fp_servico_t2_RB.setChecked(
                self.parent_win.circuito.bpf_get(
                    bpf_type='trafo', bpf_elem=nome, bpf_param='in_service'
                )
            )
        elif index_tipo_eq == 4:  # Trafo de 3 enrolamentos
            self.fp_nome_t3_lineEdit.setText(nome)
            # self.fp_nome_t3_lineEdit.setEnabled(False)
            self.preencher_combo_barra(
                self.fp_barra_a_t3_combobox, self.parent_win.circuito.bpf_get(
                    bpf_type='trafo3w', bpf_elem=nome, bpf_param='hv_bus'
                )
            )
            self.preencher_combo_barra(
                self.fp_barra_m_t3_combobox, self.parent_win.circuito.bpf_get(
                    bpf_type='trafo3w', bpf_elem=nome, bpf_param='mv_bus'
                )
            )
            self.preencher_combo_barra(
                self.fp_barra_b_t3_combobox, self.parent_win.circuito.bpf_get(
                    bpf_type='trafo3w', bpf_elem=nome, bpf_param='lv_bus'
                )
            )
            self.fp_tensao_a_t3_SB.setValue(
                self.parent_win.circuito.bpf_get(
                    bpf_type='trafo3w', bpf_elem=nome, bpf_param='vn_hv_kv'
                )
            )
            self.fp_tensao_m_t3_SB.setValue(
                self.parent_win.circuito.bpf_get(
                    bpf_type='trafo3w', bpf_elem=nome, bpf_param='vn_mv_kv'
                )
            )
            self.fp_tensao_b_t3_SB.setValue(
                self.parent_win.circuito.bpf_get(
                    bpf_type='trafo3w', bpf_elem=nome, bpf_param='vn_lv_kv'
                )
            )
            self.fp_pot_a_t3_SB.setValue(
                self.parent_win.circuito.bpf_get(
                    bpf_type='trafo3w', bpf_elem=nome, bpf_param='sn_hv_mva'
                )
            )
            self.fp_pot_m_t3_SB.setValue(
                self.parent_win.circuito.bpf_get(
                    bpf_type='trafo3w', bpf_elem=nome, bpf_param='sn_mv_mva'
                )
            )
            self.fp_pot_b_t3_SB.setValue(
                self.parent_win.circuito.bpf_get(
                    bpf_type='trafo3w', bpf_elem=nome, bpf_param='sn_lv_mva'
                )
            )
            self.fp_servico_t3_RB.setChecked(
                self.parent_win.circuito.bpf_get(
                    bpf_type='trafo3w', bpf_elem=nome, bpf_param='in_service'
                )
            )
        elif index_tipo_eq == 5:  # Carga estática
            self.fp_nome_ce_lineEdit.setText(nome)
            # self.fp_nome_ce_lineEdit.setEnabled(False)
            self.preencher_combo_barra(
                self.fp_barra_ce_combobox, self.parent_win.circuito.bpf_get(
                    bpf_type='load', bpf_elem=nome, bpf_param='bus'
                )
            )
            self.fp_pot_ce_SB.setValue(
                self.parent_win.circuito.bpf_get(
                    bpf_type='load', bpf_elem=nome, bpf_param='p_mw'
                )
            )
            self.fp_fatp_ce_SB.setValue(
                self.parent_win.circuito.bpf_get(
                    bpf_type='load', bpf_elem=nome, bpf_param='pf'
                )
            )
            self.fp_subsis_ce_lineEdit.setText(
                self.parent_win.circuito.bpf_get(
                    bpf_type='load', bpf_elem=nome, bpf_param='sub_id'
                )
            )
            self.fp_servico_ce_RB.setChecked(
                self.parent_win.circuito.bpf_get(
                    bpf_type='load', bpf_elem=nome, bpf_param='in_service'
                )
            )
        elif index_tipo_eq == 6:  # Carga de processo
            self.preencher_combo_barra(self.fp_barra_cp_combobox, '')
            self.preencher_combo_modelo(self.fp_model_cp_combobox, '')
            self.fp_fatp_cp_SB.setValue(0.0)
            self.fp_subsis_cp_lineEdit.setText('')
            self.fp_servico_cp_RB.setChecked(False)

            self.fp_nome_cp_lineEdit.setText(nome)
            # self.fp_nome_cp_lineEdit.setEnabled(False)
            self.preencher_combo_barra(
                self.fp_barra_cp_combobox, self.parent_win.circuito.bpf_get(
                    bpf_type='process_load', bpf_elem=nome, bpf_param='bus'
                )
            )
            self.preencher_combo_modelo(
                self.fp_model_cp_combobox, self.parent_win.circuito.bpf_get(
                    bpf_type='process_load', bpf_elem=nome, bpf_param='ml_model'
                )
            )
            self.fp_fatp_cp_SB.setValue(
                self.parent_win.circuito.bpf_get(
                    bpf_type='process_load', bpf_elem=nome, bpf_param='pf'
                )
            )
            self.fp_subsis_cp_lineEdit.setText(
                self.parent_win.circuito.bpf_get(
                    bpf_type='process_load', bpf_elem=nome, bpf_param='sub_id'
                )
            )
            self.fp_servico_cp_RB.setChecked(
                self.parent_win.circuito.bpf_get(
                    bpf_type='process_load', bpf_elem=nome, bpf_param='in_service'
                )
            )

    def confirmar_bg_eq(self):
        """ Dados: fp_nome_bg_lineEdit = Nome dado pelo usuario; fp_tensao_bg_SB = tensão em kV fornecida;
        fp_pot_bg_SB = potencia em MW fornecida; fp_servico_bg_RB = se o radio button está selecionado """
        barra_geracao = (self.fp_nome_bg_lineEdit.text(), self.fp_tensao_bg_SB.value(), self.fp_pot_bg_SB.value(),
                         self.fp_servico_bg_RB.isChecked())
        alteracao_rede = {
            'bpf_equip': 'gen_bus',
            'bpf_drop': False,
            'bpf_infos':
                {
                    'name': barra_geracao[0],
                    'vn_kv': barra_geracao[1],
                    'in_service': barra_geracao[3],
                    'p_mw': barra_geracao[2],
                }
        }
        if self.orig_name == '':
            if not self.parent_win.exibir_barra_geracao('Barra*: ' + barra_geracao[0]):
                return
        else:
            new_name = alteracao_rede['bpf_infos']['name']
            alteracao_rede['bpf_infos']['name'] = self.orig_name
            alteracao_rede['bpf_drop'] = True
            self.parent_win.circuito.bpf_modfy(bpf_type='equipment', bpf_data=alteracao_rede)
            alteracao_rede['bpf_infos']['name'] = new_name
            alteracao_rede['bpf_drop'] = False
        self.parent_win.circuito.bpf_modfy(bpf_type='equipment', bpf_data=alteracao_rede)
        self.parent_win.salvar_rede_alterada()
        self.stackedWidget.setCurrentIndex(0)  # Resetando pra pagina 0
        self.fp_eq_combobox.setCurrentIndex(0) # Resetando a combobox
        self.close()

    def cancelar_bg_eq(self):
        self.stackedWidget.setCurrentIndex(0)  # Resetando pra pagina 0
        self.fp_eq_combobox.setCurrentIndex(0)  # Resetando a combobox
        self.close()

    ''' Eventos referentes à barra de carga '''

    def confirmar_bc_eq(self):
        """ Dados: fp_nome_bc_lineEdit = Nome dado pelo usuario; fp_tensao_bc_SB = tensão em kV fornecida;
        fp_servico_bc_RB = se o radio button está selecionado """
        barra_carga = (self.fp_nome_bc_lineEdit.text(), self.fp_tensao_bc_SB.value(), self.fp_servico_bc_RB.isChecked())
        alteracao_rede = {
            'bpf_equip': 'load_bus',
            'bpf_drop': False,
            'bpf_infos':
                {
                    'name': barra_carga[0],
                    'vn_kv': barra_carga[1],
                    'in_service': barra_carga[2],
                }
        }
        if self.orig_name == '':
            if not self.parent_win.exibir_barra_carga('Barra : ' + barra_carga[0]):
                return
        else:
            new_name = alteracao_rede['bpf_infos']['name']
            alteracao_rede['bpf_infos']['name'] = self.orig_name
            alteracao_rede['bpf_drop'] = True
            self.parent_win.circuito.bpf_modfy(bpf_type='equipment', bpf_data=alteracao_rede)
            alteracao_rede['bpf_infos']['name'] = new_name
            alteracao_rede['bpf_drop'] = False
        self.parent_win.circuito.bpf_modfy(bpf_type='equipment', bpf_data=alteracao_rede)
        self.parent_win.salvar_rede_alterada()
        self.stackedWidget.setCurrentIndex(0)  # Resetando pra pagina 0
        self.fp_eq_combobox.setCurrentIndex(0) # Resetando a combobox
        self.close()

    def cancelar_bc_eq(self):
        self.stackedWidget.setCurrentIndex(0)  # Resetando pra pagina 0
        self.fp_eq_combobox.setCurrentIndex(0) # Resetando a combobox
        self.close()

    ''' Eventos referentes ao trafo de 2 enrolamentos '''

    def confirmar_t2_eq(self):
        """ Dados: fp_nome_t2_lineEdit = Nome dado pelo usuario; fp_pot_t2_SB = potencia nominal aparente em MVA;
        fp_barra_a_t2_combobox = Barra de alta tensão selecionada, fp_barra_b_t2_combobox = barra de baixa tensão;
        fp_tensao_a_t2_SB = tensão do lado de alta fornecida; fp_tensao_b_t2_SB = tensão do lado de baixa;
        fp_servico_t2_RB = se o radio button está selecionado """
        trafo_2 = (self.fp_nome_t2_lineEdit.text(), self.fp_pot_t2_SB.value(), self.fp_barra_a_t2_combobox.currentText(),
                   self.fp_barra_b_t2_combobox.currentText(), self.fp_tensao_a_t2_SB.value(),
                   self.fp_tensao_b_t2_SB.value(), self.fp_servico_t2_RB.isChecked())
        alteracao_rede = {
            'bpf_equip': 'trafo',
            'bpf_drop': False,
            'bpf_infos':
                {
                    'name': trafo_2[0],
                    'hv_bus': trafo_2[2],
                    'lv_bus': trafo_2[3],
                    'vn_hv_kv': trafo_2[4],
                    'vn_lv_kv': trafo_2[5],
                    'sn_mva': trafo_2[1],
                    'in_service': trafo_2[6],
                }
        }
        if self.orig_name == '':
            if not self.parent_win.exibir_eqp_pendurado('Trafo : ' + trafo_2[0], [trafo_2[2]], '', False):
                return
        else:
            if not self.parent_win.exibir_eqp_pendurado('Trafo : ' + trafo_2[0], [trafo_2[2]], '', True):
                return
            new_name = alteracao_rede['bpf_infos']['name']
            alteracao_rede['bpf_infos']['name'] = self.orig_name
            alteracao_rede['bpf_drop'] = True
            self.parent_win.circuito.bpf_modfy(bpf_type='equipment', bpf_data=alteracao_rede)
            alteracao_rede['bpf_infos']['name'] = new_name
            alteracao_rede['bpf_drop'] = False
        self.parent_win.circuito.bpf_modfy(bpf_type='equipment', bpf_data=alteracao_rede)
        self.parent_win.salvar_rede_alterada()
        self.stackedWidget.setCurrentIndex(0)  # Resetando pra pagina 0
        self.fp_eq_combobox.setCurrentIndex(0)  # Resetando a combobox
        if self.orig_name != '':
            self.parent_win.fp_eq_rede_treewidget.clear()
            self.parent_win.exibir_arvore_eq()
        self.close()

    def cancelar_t2_eq(self):
        self.stackedWidget.setCurrentIndex(0)  # Resetando pra pagina 0
        self.fp_eq_combobox.setCurrentIndex(0)  # Resetando a combobox
        self.close()

    ''' Métodos referentes ao trafo de 3 enrolamentos '''

    def confirmar_t3_eq(self):
        """ Dados: fp_nome_t3_lineEdit = Nome dado pelo usuario; fp_barra_a_t3_combobox = Barra de alta tensão;
        fp_barra_m_t3_combobox = barra de media tensão; fp_barra_b_t3_combobox = barra de baixa tensão;
        fp_tensao_a_t2_SB = tensão do lado de alta; fp_tensao_m_t2_SB = tensão do lado de média;
        fp_tensao_b_t2_SB = tensão do lado de baixa; fp_servico_t3_RB = se o radio button está selecionado """

        trafo_3 = (self.fp_nome_t3_lineEdit.text(), self.fp_barra_a_t3_combobox.currentText(),
                   self.fp_barra_m_t3_combobox.currentText(), self.fp_barra_b_t3_combobox.currentText(),
                   self.fp_tensao_a_t3_SB.value(), self.fp_tensao_m_t3_SB.value(), self.fp_tensao_b_t3_SB.value(),
                   self.fp_pot_a_t3_SB.value(), self.fp_pot_m_t3_SB.value(), self.fp_pot_b_t3_SB.value(),
                   self.fp_servico_t3_RB.isChecked())
        alteracao_rede = {
            'bpf_equip': 'trafo3w',
            'bpf_drop': False,
            'bpf_infos':
                {
                    'name': trafo_3[0],
                    'hv_bus': trafo_3[1],
                    'mv_bus': trafo_3[2],
                    'lv_bus': trafo_3[3],
                    'vn_hv_kv': trafo_3[4],
                    'vn_mv_kv': trafo_3[5],
                    'vn_lv_kv': trafo_3[6],
                    'sn_hv_mva': trafo_3[7],
                    'sn_mv_mva': trafo_3[8],
                    'sn_lv_mva': trafo_3[9],
                    'in_service': trafo_3[10],
                }
        }
        if self.orig_name == '':
            if not self.parent_win.exibir_eqp_pendurado('Trafo*: ' + trafo_3[0], [trafo_3[1]], '', False):
                return
        else:
            if not self.parent_win.exibir_eqp_pendurado('Trafo*: ' + trafo_3[0], [trafo_3[1]], '', True):
                return
            new_name = alteracao_rede['bpf_infos']['name']
            alteracao_rede['bpf_infos']['name'] = self.orig_name
            alteracao_rede['bpf_drop'] = True
            self.parent_win.circuito.bpf_modfy(bpf_type='equipment', bpf_data=alteracao_rede)
            alteracao_rede['bpf_infos']['name'] = new_name
            alteracao_rede['bpf_drop'] = False
        self.parent_win.circuito.bpf_modfy(bpf_type='equipment', bpf_data=alteracao_rede)
        self.parent_win.salvar_rede_alterada()
        self.stackedWidget.setCurrentIndex(0)  # Resetando pra pagina 0
        self.fp_eq_combobox.setCurrentIndex(0)  # Resetando a combobox
        if self.orig_name != '':
            self.parent_win.fp_eq_rede_treewidget.clear()
            self.parent_win.exibir_arvore_eq()
        self.close()

    def cancelar_t3_eq(self):
        self.stackedWidget.setCurrentIndex(0)  # Resetando pra pagina 0
        self.fp_eq_combobox.setCurrentIndex(0)  # Resetando a combobox
        self.close()

    ''' Métodos referentes à carga estática '''

    def confirmar_ce_eq(self):
        """ Dados: fp_nome_ce_lineEdit = Nome dado pelo usuario; fp_barra_ce_combobox = Barra selecionada;
        fp_pot_ce_SB = potencia ativa fornecida; fp_fatp_ce_SB = fator de potencia forncecido;
       fp_subsis_ce_lineEdit = subsistema selecionado; fp_servico_ce_RB = se o radio button está selecionado """
        carga_est = (self.fp_nome_ce_lineEdit.text(), self.fp_barra_ce_combobox.currentText(),
                     self.fp_pot_ce_SB.value(), self.fp_fatp_ce_SB.value(), self.fp_subsis_ce_lineEdit.text(),
                     self.fp_servico_ce_RB.isChecked())
        alteracao_rede = {
            'bpf_equip': 'load',
            'bpf_drop': False,
            'bpf_infos':
                {
                    'name': carga_est[0],
                    'bus': carga_est[1],
                    'p_mw': carga_est[2],
                    'pf': carga_est[3],
                    'in_service': carga_est[5],
                    'sub_id': carga_est[4],
                }
        }
        if self.orig_name == '':
            if not self.parent_win.exibir_eqp_pendurado(
                    'Carga : ' + carga_est[0], [carga_est[1]], 'Subsis: ' + carga_est[4], False):
                return
        else:
            if not self.parent_win.exibir_eqp_pendurado(
                    'Carga : ' + carga_est[0], [carga_est[1]], 'Subsis: ' + carga_est[4], True):
                return
            new_name = alteracao_rede['bpf_infos']['name']
            alteracao_rede['bpf_infos']['name'] = self.orig_name
            alteracao_rede['bpf_drop'] = True
            self.parent_win.circuito.bpf_modfy(bpf_type='equipment', bpf_data=alteracao_rede)
            alteracao_rede['bpf_infos']['name'] = new_name
            alteracao_rede['bpf_drop'] = False
        self.parent_win.circuito.bpf_modfy(bpf_type='equipment', bpf_data=alteracao_rede)
        self.parent_win.salvar_rede_alterada()
        self.stackedWidget.setCurrentIndex(0)  # Resetando pra pagina 0
        self.fp_eq_combobox.setCurrentIndex(0)  # Resetando a combobox
        if self.orig_name != '':
            self.parent_win.fp_eq_rede_treewidget.clear()
            self.parent_win.exibir_arvore_eq()
        self.close()

    def cancelar_ce_eq(self):
        self.stackedWidget.setCurrentIndex(0)  # Resetando pra pagina 0
        self.fp_eq_combobox.setCurrentIndex(0)  # Resetando a combobox
        self.close()

    ''' Métodos referentes à carga dep. de processo '''

    def confirmar_cp_eq(self):
        """ Dados: fp_nome_cp_lineEdit = Nome dado pelo usuario; fp_barra_cp_combobox = Barra selecionada;
        fp_model_cp_combobox = modelo selecionado; fp_fatp_cp_SB = fator de potencia forncecido;
       fp_subsis_cp_lineEdit = subsistema selecionado; fp_servico_cp_RB = se o radio button está selecionado """
        carga_proc = (self.fp_nome_cp_lineEdit.text(), self.fp_barra_cp_combobox.currentText(),
                      self.fp_model_cp_combobox.currentText(), self.fp_fatp_cp_SB.value(),
                      self.fp_subsis_cp_lineEdit.text(), self.fp_servico_cp_RB.isChecked())
        # declara os dados de outra Carga de Processo (sem subsistema)
        alteracao_rede = {
            'bpf_equip': 'process_load',
            'bpf_drop': False,
            'bpf_infos':
                {
                    'name': carga_proc[0],
                    'bus': carga_proc[1],
                    'ml_model': carga_proc[2],
                    'pf': carga_proc[3],
                    'in_service': carga_proc[5],
                    'sub_id': carga_proc[4],
                }
        }
        if self.orig_name == '':
            if not self.parent_win.exibir_eqp_pendurado(
                    'Carga*: ' + carga_proc[0], [carga_proc[1]], 'Subsis: ' + carga_proc[4], False):
                return
        else:
            if not self.parent_win.exibir_eqp_pendurado(
                    'Carga*: ' + carga_proc[0], [carga_proc[1]], 'Subsis: ' + carga_proc[4], True):
                return
            new_name = alteracao_rede['bpf_infos']['name']
            alteracao_rede['bpf_infos']['name'] = self.orig_name
            alteracao_rede['bpf_drop'] = True
            self.parent_win.circuito.bpf_modfy(bpf_type='equipment', bpf_data=alteracao_rede)
            alteracao_rede['bpf_infos']['name'] = new_name
            alteracao_rede['bpf_drop'] = False
        self.parent_win.circuito.bpf_modfy(bpf_type='equipment', bpf_data=alteracao_rede)
        self.parent_win.salvar_rede_alterada()
        self.stackedWidget.setCurrentIndex(0)  # Resetando pra pagina 0
        self.fp_eq_combobox.setCurrentIndex(0)  # Resetando a combobox
        if self.orig_name != '':
            self.parent_win.fp_eq_rede_treewidget.clear()
            self.parent_win.exibir_arvore_eq()
        self.close()

    def cancelar_cp_eq(self):
        self.stackedWidget.setCurrentIndex(0)  # Resetando pra pagina 0
        self.fp_eq_combobox.setCurrentIndex(0)  # Resetando a combobox
        self.close()


class fpso_rede(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.second = uic.loadUi('cria_rede.ui', self).__init__
        self.parent_win = parent

        self.fp_rede_ok_PB.clicked.connect(self.confirmar_rede)
        self.fp_rede_cancel_PB.clicked.connect(self.cancelar_rede)
        self.dados_rede = ("", 0.0, 0.0)
        self.fp_freq_rede_SB.setMaximum(9999.99)
        self.fp_pot_rede_SB.setMaximum(9999.99)


    def confirmar_rede(self):
        """ Dados: fp_nome_rede_LineEdit = Nome da rede; fp_freq_rede_SB = frequência em Hz;
        fp_pot_rede_SB = potencia aparente em MVA """
        self.dados_rede = (
            self.fp_nome_rede_LineEdit.text(), self.fp_freq_rede_SB.value(), self.fp_pot_rede_SB.value()
        )
        self.parent_win.salvar_rede_criada()
        self.close()

    def cancelar_rede(self):
        self.close()
