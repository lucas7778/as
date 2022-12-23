"""
Título do Projeto: Sistema inteligente para levantamento dos fatores de uso de
cargas elétricas nos FPSOs correlacionados às demandas de produção
Número de registro do Projeto: 5900.0117579.21.9

Back-end: X
Módulo: Machine Learning
Caso de uso:

Versão 0.5:
Adicão da classe bp_Perfm para medição de qualidade dos modelos.
Caso de uso:
Data de Início: 01/02/2022
Data de Entrega para Revisão: 01/02/2022
Data de Release: --/--/----
Nome do Responsável: Vitor Hugo Ferreira
Contato: vhferreira@id.uff.br
Desenvolvedor: Daniel Cunha de Araujo Júnior
Contato: dc_junior@id.uff.br
Caso de teste:
Responsável pelo Teste:
Bloco geral de observações importantes:
    Classe bdm_DtMn separada nas classes bp_Perfm e bdm_DtMn (para tomada de
métricas do modelo e manipulações gerais de dados). Cálculo do IQR movido para
o método bp_apred.

Versão 0.6:
Hiperparâmetros adicionados. Classe que atua como gerenciador de modelos
adicionada.
Caso de uso:
Data de Início: 25/02/2022
Data de Entrega para Revisão: 02/03/2022
Data de Release: --/--/----
Nome do Responsável: Vitor Hugo Ferreira
Contato: vhferreira@id.uff.br
Desenvolvedor: Daniel Cunha de Araujo Júnior
Contato: dc_junior@id.uff.br
Caso de teste:
Responsável pelo Teste:
Bloco geral de observações importantes:

Versão 0.7:
Adicionada Grid Search. Classe que retorna valores default adicionada.
Modificações gerais na estrutura do pré-processamento. Ajustes de documentação
e correção de bugs. Desenvolvimentos gerais do pacote.
Caso de uso:
Data de Início: 02/03/2022
Data de Entrega para Revisão: 30/03/2022
Data de Release: --/--/----
Nome do Responsável: Vitor Hugo Ferreira
Contato: vhferreira@id.uff.br
Desenvolvedor: Daniel Cunha de Araujo Júnior
Contato: dc_junior@id.uff.br
Caso de teste:
Responsável pelo Teste:
Bloco geral de observações importantes:

Atualização ao método bp_gets
e bp_apred refletindo alterações no sistema de pré-processamento. Correção de
bug (tentativa de transformação inversa incorreta e/ou conversão para fator de
carga ao se passar processamento especial para variável de saída). Adicionado
método bc_isfit em bc_Check para checar se o modelo pode ser usado para
atividades que requerem treinamento. Adicionado parâmetro bbb_isfit que contém
informações a respeito do status de treinamento do modelo. Método bm_fitgs.
Método bp_eval adicionado a bp_Perfm. Argumento bp_df adicionado ao método
bp_apred. Cálculo do score de validação passado para o método bp_apred. Ajustes
gerais na documentação do módulo.

Versão 0.8:
Controle de entrada base implementado. Ajustes gerais e padronização de
código e documentação.
Caso de uso:
Data de Início: 30/03/2022
Data de Entrega para Revisão: 02/05/2022
Data de Release: --/--/----
Nome do Responsável: Vitor Hugo Ferreira
Contato: vhferreira@id.uff.br
Desenvolvedor: Daniel Cunha de Araujo Júnior
Contato: dc_junior@id.uff.br
Caso de teste:
Responsável pelo Teste: Iahn Igel
Bloco geral de observações importantes:
"""

from typing import Union, Iterable

import pandas as pd
import numpy as np
from machine_learning.bml_check import bc_Check
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    median_absolute_error,
    r2_score,
)

# "from ... import ..." dará problemas de importação circular
import machine_learning.bml_bbox
from machine_learning.bml_dtmn import bdm_DtMn
from machine_learning.bml_log import bl_Log

"""
Define a classe bp_Perfm, que objetiva oferecer utilitários que auxiliam na 
tomada de métricas dos modelos (para utilização interna).

Métodos
----------
 bp_apred: Retorna métricas do modelo.
 bp_eval: A partir de tags passadas retorna o valor da métrica pertinente.
 bp_gets: Toma métricas de uma predição, em relação a uma ground truth.
 bp_mtrct: Retorna um DataFrame contendo as métricas do modelo.
 bp_sr2: Calcula o R-Quadrado entre duas séries.
"""


class bp_Perfm:
    """
    Classe de utilitários para tomada de métricas dos modelos.

    Métodos públicos:
        bp_apred, bp_eval, bp_gets, bp_mtrct

    """

    @staticmethod
    def bp_gets(
        bp_ypred: list,
        bp_ytrue: list,
        bp_log: bool = True,
        **kwargs,
    ):
        """Toma métricas de uma predição, em relação a uma ground truth."""

        if bp_log or kwargs != {}:
            bl_Log.bl_regmt("bp_gets", **kwargs)

        bp_pred = bp_ypred
        bp_gt = bp_ytrue

        bp_stats = []
        bp_e = [0.0 for k in range(len(bp_pred))]
        for k in range(len(bp_e)):
            bp_e[k] = bp_pred[k] - bp_gt[k]

        bp_abse = [None for k in range(len(bp_pred))]
        for k in range(len(bp_abse)):
            bp_abse[k] = abs(bp_e[k])

        for k in range(len(bp_pred)):
            bp_stats.append(bp_pred[k])
            bp_stats.append(bp_gt[k])
            bp_stats.append(bp_e[k])
            bp_stats.append(bp_abse[k])

        return bp_stats

    @staticmethod
    def bp_sr2(
        bp_p: Iterable,
        bp_t: Iterable,
        **kwargs,
    ):
        """Calcula o R-Quadrado entre duas séries, bp_p e bp_t."""

        bl_Log.bl_regmt("bp_sr2", **kwargs)

        bp_r2 = np.corrcoef(bp_t, bp_p)[0, 1] ** 2

        if np.isnan(bp_r2):
            bp_r2 = r2_score(bp_t, bp_p)

            if bp_r2 < 0:
                bp_r2 = 0

        return bp_r2

    @staticmethod
    def bp_apred(
        bp_bbox,
        bp_df: str = "val",
        **kwargs,
    ):
        """
        Retorna métricas do modelo.

        :param bp_bbox: Modelo
        :param bp_df: "trn", "val", "tst" ou DataFrame com variáveis a serem
        utilizadas para comparação (deve conter valores para todas as variáveis
        utilizadas pelo modelo (input e output). Caso o modelo não contenha
        particão de testes e "tst" seja selecionado, retornará None.

        :return: Dicionário com métricas tomadas.
        """

        # checar entrada
        #######################################################################
        bl_Log.bl_regmt("bp_apred", **kwargs)

        bp_model = bp_bbox.bbb_model
        bp_prepy = bp_bbox.bbb_prepy
        bbb_outn = bp_bbox.bbb_outn

        bp_cout = bc_Check.bc_type(
            bc_var=bp_df, bc_dtype=[str, pd.DataFrame], bc_vname="bp_df"
        )
        if bp_cout["error"]:
            bp_bbox.bbb_addlg(bp_cout["log"])
            return

        if isinstance(bp_df, pd.DataFrame):

            # checar se o dataframe não está vazio
            bp_cout = bc_Check.bc_dslen(
                bc_ds=bp_df,
                bc_dlen=(1, np.inf),
                bc_vname="bp_df",
            )
            if bp_cout["error"]:
                bp_bbox.bbb_addlg(bp_cout["log"])
                return

            # checar se as colunas são pertinentes
            bp_cout = bc_Check.bc_dscol(
                bc_ds=bp_df,
                bc_vars=bp_bbox.bbb_cvar,
                bc_vname="bp_df",
            )
            if bp_cout["error"]:
                bp_bbox.bbb_addlg(bp_cout["log"])
                return

            # fazer o processamento inicial do dataframe
            bp_data, bp_dinf = bdm_DtMn.bdm_ids(
                bdm_dsraw=bp_df,
                bdm_cvar=bp_bbox.bbb_cvar,
            )
            del bp_dinf

        else:
            if bp_df == "trn":
                bp_data = bp_bbox.bbb_trnds
            elif bp_df == "tst":
                bp_data = bp_bbox.bbb_tstds
            else:
                bp_data = bp_bbox.bbb_valds

        # checar se o dataframe não está vazio
        bp_cout = bc_Check.bc_dslen(
            bc_ds=bp_data,
            bc_dlen=(1, np.inf),
            bc_vname="bp_df",
        )
        if bp_cout["error"]:
            bp_bbox.bbb_addlg(bp_cout["log"])
            return

        #######################################################################

        # Nomes das colunas, em dois niveis (nome do parametro e metrica)
        bp_lbls = [
            bp_bbox.bbb_pcoly,
            ["Predicao", "Ground Truth", "Erro", "Erro Abs."],
        ]

        bp_index = pd.MultiIndex.from_product(
            bp_lbls, names=["Outputs", "Metrics"]
        )

        # separando input e output do dataframe passado
        bp_x, bp_y = bdm_DtMn.bdm_splxy(bp_data, bp_bbox.bbb_inn, bbb_outn)

        # tomando as predições
        bp_preds = bp_model.predict(bp_x)
        bp_preds = bp_preds.reshape((len(bp_preds), len(bp_bbox.bbb_pcoly)))

        bp_normy = bp_bbox.bbb_trnsy(bbb_y=bp_y)

        if bp_bbox.bbb_inv:
            bp_preds = bp_prepy.inverse_transform(bp_preds)
        else:
            bp_y = bp_normy

        # tomar métricas
        bp_mae = mean_absolute_error(bp_preds, bp_y)
        bp_mdae = median_absolute_error(bp_preds, bp_y)
        bp_r2 = bp_Perfm.bp_sr2(
            np.squeeze(bp_preds),
            np.squeeze(bp_y.to_numpy()),
        )

        bp_allst = []

        for j in range(len(bp_preds)):

            if type(bp_y) == np.ndarray:
                bp_ytrue = bp_y[j]
            else:
                bp_ytrue = bp_y.iloc[j]

            bp_allst.append(
                bp_Perfm.bp_gets(
                    bp_ypred=bp_preds[j],
                    bp_ytrue=bp_ytrue,
                    bp_log=False,
                )
            )
        bl_Log.bl_regmt("bp_gets", **kwargs)

        bp_sdf = pd.DataFrame(
            data=bp_allst,
            columns=bp_index,
        )
        bp_sdf.index.name = "Medicao"

        bp_smry = bp_sdf.describe()
        bp_smry.index.name = "Estatisticas"
        bp_smry.loc["IQR", :] = bp_smry.loc["75%"] - bp_smry.loc["25%"]

        bp_gtl = [
            bp_label
            for bp_label in bp_smry.columns
            if "Ground Truth" in bp_label
        ]
        bp_gtl = bp_gtl[0]

        # bp_range = bp_smry.loc["max", bp_gtl] - bp_smry.loc["min", bp_gtl]
        if bp_bbox.bbb_onom[0] is None:
            bp_range = bp_bbox.bbb_dsinf[bp_bbox.bbb_outn[0]]["max"]

        else:
            bp_range = bp_bbox.bbb_onom[0]

        if bp_range == 0:
            bp_range = 1

        # media e mediana do erro absoluto dividido pelo intervalo
        # encontrado nas ground truths
        bp_maep = 100 * bp_mae / bp_range
        bp_mdaep = 100 * bp_mdae / bp_range

        # bp_maep = None
        # bp_mdaep = None

        bp_out = {
            "sdf": bp_sdf,
            "smry": bp_smry,
            "r2": bp_r2,
            "mae": bp_mae,
            "mdae": bp_mdae,
            "maep": bp_maep,
            "mdaep": bp_mdaep,
        }

        return bp_out

    @staticmethod
    def bp_eval(
        bp_model=None,
        bp_metrc: str = "mae",
        bp_log: bool = True,
        **kwargs,
    ):
        """
        A partir de tags passadas retorna o valor da métrica pertinente.

        :param bp_model: Modelo.
        :param bp_metrc: Métrica desejada.

        :return: Valor da métrica.
        """

        if bp_log or kwargs != {}:
            bl_Log.bl_regmt("bp_eval", **kwargs)

        if bp_metrc == "r2":
            bp_value = bp_model.bbb_r2

        elif bp_metrc == "mae":
            bp_value = bp_model.bbb_mae

        elif bp_metrc == "mdae":
            bp_value = bp_model.bbb_mdae

        elif bp_metrc == "maep":
            bp_value = bp_model.bbb_maep

        elif bp_metrc == "mdaep":
            bp_value = bp_model.bbb_mdaep

        else:
            return None

        return bp_value

    @staticmethod
    def bp_mtrct(bp_model=None, **kwargs) -> pd.DataFrame:
        """Retorna um DataFrame contendo as métricas do modelo."""

        bl_Log.bl_regmt("bp_mtrct", **kwargs)

        bp_df = []
        bp_metrct = {
            "r2": bp_model.bbb_r2,
            "mae": bp_model.bbb_mae,
            "mdae": bp_model.bbb_mdae,
            "maep": bp_model.bbb_maep,
            "mdaep": bp_model.bbb_mdaep,
        }

        bp_df.append([bp_metrct[bp_m] for bp_m in bp_metrct])

        bp_rows = [bp_i.upper().replace("P", " %") for bp_i in bp_metrct]

        bp_df = pd.DataFrame(data=bp_df, columns=bp_rows, index=["Valor"])
        bp_df.columns.name = "Metricas"

        return bp_df.T
