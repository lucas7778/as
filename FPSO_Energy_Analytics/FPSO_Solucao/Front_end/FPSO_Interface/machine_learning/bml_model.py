"""
Título do Projeto: Sistema inteligente para levantamento dos fatores de uso de
cargas elétricas nos FPSOs correlacionados às demandas de produção
Número de registro do Projeto: 5900.0117579.21.9

Back-end: X
Módulo: Machine Learning
Caso de uso:

Versão 0.0:
Data de início: 30/11/2021 12:08:56
Data de Entrega para Revisão: 15/12/2021
Data de Release: --/--/----

Nome do Responsável: Vitor Hugo Ferreira
Contato: vhferreira@id.uff.br
Desenvolvedor: Daniel Cunha de Araujo Júnior
Contato: dc_junior@id.uff.br

Versão 0.1:
Alterações gerais de métodos e padronização e formatação do código.
Caso de uso:
Data de Início: 15/12/2021
Data de Entrega para Revisão: 15/01/2022
Data de Release: --/--/----
Nome do Responsável: Vitor Hugo Ferreira
Contato: vhferreira@id.uff.br
Desenvolvedor: Daniel Cunha de Araujo Júnior
Contato: dc_junior@id.uff.br
Caso de teste:
Responsável pelo Teste:
Bloco geral de observações importantes:
    Formatação geral dos nomes de atributos. Adicionadas docstrings faltantes.
Alteração do método fit() de todos os modelos. Adicionadas opções de
hiperparâmetros.

Versão 0.2:
Alterações gerais de métodos e padronização e formatação do código.
Caso de uso:
Data de Início: 16/01/2022
Data de Entrega para Revisão: 18/01/2022
Data de Release: --/--/----
Nome do Responsável: Vitor Hugo Ferreira
Contato: vhferreira@id.uff.br
Desenvolvedor: Daniel Cunha de Araujo Júnior
Contato: dc_junior@id.uff.br
Caso de teste:
Responsável pelo Teste:
Bloco geral de observações importantes:
    Padronização dos nomes de variáveis e argumentos dos métodos. Ajustes nas
docstrings refletindo as alterações.

Versão 0.3:
Alterações gerais de métodos e padronização e formatação do código.
Caso de uso:
Data de Início: 24/01/2022
Data de Entrega para Revisão: 24/01/2022
Data de Release: --/--/----
Nome do Responsável: Vitor Hugo Ferreira
Contato: vhferreira@id.uff.br
Desenvolvedor: Daniel Cunha de Araujo Júnior
Contato: dc_junior@id.uff.br
Caso de teste:
Responsável pelo Teste:
Bloco geral de observações importantes:
    Ajustes de cabeçalho: Ajustes de nome do responsável (alteração de Daniel
Araujo para Vitor Hugo Ferreira), incluída. Data de Entrega para Revisão.

Versão 0.4:
Novos métodos adicionados e ajustes gerais de métodos e padronização do código.
Caso de uso:
Data de Início: 28/01/2022
Data de Entrega para Revisão: 28/01/2022
Data de Release: --/--/----
Nome do Responsável: Vitor Hugo Ferreira
Contato: vhferreira@id.uff.br
Desenvolvedor: Daniel Cunha de Araujo Júnior
Contato: dc_junior@id.uff.br
Caso de teste:
Responsável pelo Teste:
Bloco geral de observações importantes:
    Adicionado suporte a multi-output para a Support Vector Machine (SVM).
Adicionado suporte a multi-output para o Gradient Boosting Regressor (GBR).
Ajustes nas docstrings de bml_model.py (erro de digitação).

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
    Métodos de bdm_DtMn convertidos para métodos estáticos. Classe bdm_DtMn
separada nas classes bp_Perfm e bdm_DtMn (para tomada de métricas do modelo e
manipulações gerais de dados). Cálculo do IQR movido parao método bp_apred.
Instanciamento da classe bdm_DtMn em bbb_BBox removido. Método bbb_cstat
removido (a lógica agora faz parte do processamento de bm_fit).

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
    Adicionado o hiperparâmetro alpha para o modelo Ridge. Adicionado o
hiperparâmetro max_depth para o modelo GBR. Adicionados hiperparâmetros para o
modelo RFR (n_estimators, max_depth, max_leaf_nodes, criterion). Adicionado
controle de entrada para o hiperparâmetro "criterion" no modelo RFR. Adicionado
hiperparâmetros para o modelo DTR (max_depth, max_leaf_nodes, criterion).
Adicionado controle de entrada para todos os modelos (somente uma variável de
saída). Adicionado o parâmetro bbb_param, que contém um dicionário com os
hiperparâmetros definidos. Formatação dos nomes dos hiperparâmetros para o
modelo GBR segundo padronização. Formatação dos nomes dos hiperparâmetros para
o modelo RFR segundo padronização. Formatação dos nomes dos hiperparâmetros
para o modelo DTR segundo padronização.

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
    Método bm_fitgs adicionado aos modelos (executa Grid Search). Método
bbb_fit adicionado a classe bbb_BBox. Métodos bm_fit e bm_fitgs ambos extendem
o método bbb_fit. Hiperparâmetro incorreto removido de bm_grid em
bm_DTR.bm_fitgs. Processamento de bm_grid passado para o método bbb_fit.
Ajustes nas docstrings de bml_model e bml_bbox. Docstrings para os parâmetros
de bbb_BBox adicionada. Ajustes gerais na documentação do módulo.

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
    Argumento **kwargs adicionado aos métodos de bml_bbox e bml_model. Valores
default adicionados para argumentos bm_name/bbb_name e bm_inn/bbb_inn.
Padronização das keywords dos dicionários de bm_grid (equivalente a
padronização de bm_fit). Método bc_ds adicionado a bc_Check, que checa a
pertinência do dataset passado para o modelo. Progresso parcial no tratamento
de erros.
"""

# deve ser importado e executado antes de sklearn
# from sklearnex import patch_sklearn

# patch_sklearn()

from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR
from sklearn.linear_model import (
    LinearRegression,
    Ridge,
)
from sklearn.ensemble import (
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.tree import DecisionTreeRegressor
from sklearn.multioutput import MultiOutputRegressor
import numpy as np
import pandas as pd

from machine_learning.bml_bbox import bbb_BBox
from machine_learning.bml_dtmn import bdm_DtMn
from machine_learning.bml_check import bc_Check
from machine_learning.bml_perfm import bp_Perfm
from machine_learning.bml_log import bl_Log

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

"""
Define as classes referentes aos modelos oferecidos pelo pacote:
    bm_MLP: Multilayer Perceptron
    bm_MVR: Multivariate Regression
    bm_SVM: Support-Vector Machine
    bm_GBR: Gradient Boosting Regression
    bm_RFR: Random Forest Regression
    bm_RDG: Ridge Regression
    bm_DTR: Decision Tree Regression

Métodos
----------
        bm_fit: treina o modelo e calcula métricas quanto a qualidade das 
            predições.
        bm_fitgs: treina o modelo utilizando Grid Search e calcula métricas 
            quanto a qualidade das predições.
"""


# %% Multilayer Perceptron
class bm_MLP(bbb_BBox):
    """
    Modelo caixa-preta do tipo Multilayer Perceptron.

    Classe derivada de bbb_BBox, estendendo funcionalidades para atender a
    especificidade do modelo. Estende as funcionalidades __init__() e bbb_fit
    para fins de construção do objeto e especificação de hiperparâmetros,
    respectivamente.

    Métodos públicos:
        bm_fit
        bm_fitgs
    """

    def __init__(
        self,
        bm_name: str = "Multilayer Perceptron",
        bm_inn: tuple = ("days_since_start",),
        bm_outn: tuple = None,
        **kwargs,
    ):
        """
        :param bm_name: Nome do modelo a ser criado.
        :param bm_inn: Tupla contendo o nome das variáveis de entrada.
        :param bm_outn: Tupla contendo o nome da variável de saída.
        """

        bbb_BBox.__init__(
            self,
            bbb_name=bm_name,
            bbb_inn=bm_inn,
            bbb_outn=bm_outn,
            **kwargs,
        )
        # self.bbb_regmt(bbb_methd="__init__", **kwargs)
        self.bbb_mtype = "Multilayer Perceptron"

    def bm_fit(
        self,
        bm_hlyr: int = None,
        bm_actvn: str = "relu",
        bm_lrate: float = 0.001,
        bm_maxit: int = 1500,
        bm_tol: float = 1e-4,
        bm_bsize: int = 200,
        bm_ninc: int = 50,
        **kwargs,
    ):
        """
        Treina o modelo com a partição de treino do dataset e toma as métricas
        de validação.

        :param bm_hlyr: Quantidade de neurônios da camada oculta.
        (int)
        :param bm_actvn: Função de ativação utilizada. Deve ser uma string
        pertencente à {"identity", "logistic", "tanh", "relu"}
        :param bm_lrate: Learning Rate inicial. (float)
        :param bm_maxit: Número máximo de epochs. (int)
        :param bm_tol: Menor melhoria necessária que deve ser encontrada em
        'bm_ninc' iterações. Se não for, será considerado que o modelo
        convergiu. (float)
        :param bm_bsize: Número de batch. (int)
        :param bm_ninc: Máximo de iterações sem no mínimo bm_tol de melhoria.
        """

        # checar entrada
        #######################################################################
        self.bbb_regmt(bbb_methd="bm_fit", **kwargs)

        bm_cout = bc_Check.bc_isdp(self)
        if bm_cout["error"]:
            self.bbb_addlg(bm_cout["log"])
            return

        bm_dflt = bdm_DtMn.bdm_fdflt(self.bm_fit)

        # ajustes de parâmetros default
        if bm_hlyr is None:
            bm_hlyr = 2 * len(self.bbb_pcolx) + 1

        bm_dflt["bm_hlyr"] = 2 * len(self.bbb_pcolx) + 1

        self.bbb_param = {
            "bm_hlyr": bm_hlyr,
            "bm_actvn": bm_actvn,
            "bm_lrate": bm_lrate,
            "bm_maxit": bm_maxit,
            "bm_tol": bm_tol,
            "bm_bsize": bm_bsize,
            "bm_ninc": bm_ninc,
        }

        bm_schk = bc_Check.bc_schek(bc_mtype=self.bbb_mtype, bc_subs=bm_dflt)

        for bm_p in self.bbb_param:
            bm_cout = bm_schk[bm_p](self.bbb_param[bm_p])
            if bm_cout["error"]:
                self.bbb_param[bm_p] = bm_cout["subs"]
                self.bbb_addlg(bm_cout["log"])

        # # bm_bsize
        # bm_cout = bc_Check.bc_naint(
        #     bc_var=bm_bsize,
        #     bc_subs=min(200, len(self.bbb_trnds), len(self.bbb_valds)),
        #     bc_vname="bm_bsize",
        # )
        # if bm_cout["error"]:
        #     bm_bsize = bm_cout["subs"]
        #     self.bbb_addlg(bm_cout["log"])

        #######################################################################

        bm_p = bdm_DtMn.bdm_tdict(
            bdm_mtype=self.bbb_mtype,
            bdm_dict=self.bbb_param,
        )
        # bm_p['epsilon'] = 1e-7

        bm_model = MLPRegressor(**bm_p)
        bbb_BBox.bbb_fit(self, bm_model, **kwargs)

    def bm_fitgs(self, bm_grid: list = None, bm_score: str = "mae", **kwargs):
        """
        Treina o modelo com a partição de treino do dataset e toma as
        métricas de validação, definindo hiperparâmetros conforme resultado da
        Grid Search.

        :param bm_grid: Grid de busca.
        :param bm_score: Métrica para decidir o melhor conjunto de
            hiperparâmetros.
        """

        # checar entrada
        #######################################################################
        self.bbb_regmt(bbb_methd="bm_fitgs", **kwargs)

        bm_cout = bc_Check.bc_isdp(self)
        if bm_cout["error"]:
            self.bbb_addlg(bm_cout["log"])
            return

        bm_dflt = bdm_DtMn.bdm_fdflt(self.bm_fit)

        # ajustes de parâmetros default
        bm_dflt["bm_hlyr"] = 2 * len(self.bbb_pcolx) + 1

        if bm_grid is not None:

            bm_schk = bc_Check.bc_schek(
                bc_mtype=self.bbb_mtype,
                bc_subs=bm_dflt,
            )

            for (bm_i, bm_dict) in enumerate(bm_grid):

                for bm_arg in bm_dflt:
                    if bm_arg not in bm_dict:
                        bm_grid[bm_i][bm_arg] = [bm_dflt[bm_arg]]

                for bm_key in bm_dict:
                    for (bm_j, bm_param) in enumerate(bm_dict[bm_key]):
                        bm_cout = bm_schk[bm_key](bm_param)

                        if bm_cout["error"]:
                            bm_grid[bm_i][bm_key][bm_j] = bm_cout["subs"]
                            self.bbb_addlg(bm_cout["log"])

            # Remover redundâncias
            for (bm_i, bm_dict) in enumerate(bm_grid):
                for bm_j in bm_dict:
                    if len(bm_dict[bm_j]) != len(set(bm_dict[bm_j])):
                        bm_grid[bm_i][bm_j] = list(set(bm_grid[bm_i][bm_j]))
                        bbb_s = (
                            "Redundâncias removidas em bm_grid["
                            + str(bm_i)
                            + ']["'
                            + bm_j
                            + '"]'
                        )
                        self.bbb_addlg(bbb_s)
        else:
            bm_grid = [
                {
                    "bm_hlyr": [
                        2 * len(self.bbb_pcolx) + 1,
                        10,
                        50,
                        100,
                        200,
                    ],
                    "bm_actvn": ["relu", "tanh"],
                    "bm_lrate": [0.005, 0.001],
                    "bm_maxit": [750],
                    "bm_bsize": [200],
                    "bm_tol": [1e-4],
                    "bm_ninc": [50],
                    # "bm": [1e-7],
                }
            ]
        #######################################################################

        bm_model = MLPRegressor()
        bbb_BBox.bbb_fit(self, bm_model, bm_grid, bbb_sscr=bm_score, **kwargs)


# %% Support Vector Machine
class bm_SVM(bbb_BBox):
    """
    Modelo caixa-preta do tipo Support Vector Machine.

    Classe derivada de bbb_BBox, estendendo funcionalidades para atender a
    especificidade do modelo. Estende as funcionalidades __init__() e bbb_fit
    para fins de construção do objeto e especificação de hiperparâmetros,
    respectivamente.

    Métodos públicos:
        bm_fit
        bm_fitgs
    """

    def __init__(
        self,
        bm_name: str = "Support-Vector Machine",
        bm_inn: tuple = ("days_since_start",),
        bm_outn: tuple = None,
        **kwargs,
    ):
        """
        :param bm_name: Nome do modelo a ser criado.
        :param bm_inn: Tupla contendo o nome das variáveis de entrada.
        :param bm_outn: Tupla contendo o nome da variável de saída.
        """

        bbb_BBox.__init__(
            self,
            bbb_name=bm_name,
            bbb_inn=bm_inn,
            bbb_outn=bm_outn,
            **kwargs,
        )
        # self.bbb_regmt(bbb_methd="__init__", **kwargs)
        self.bbb_mtype = "Support-Vector Machine"

        # checar entrada
        #######################################################################
        # bc_Check.bc_outn(self.bbb_outn, self.bbb_mtype)
        #######################################################################

    def bm_fit(
        self,
        bm_krnel: str = "linear",
        bm_epsil: float = 0.005,
        bm_c: int = 5,
        **kwargs,
    ):
        """
        Treina o modelo com a partição de treino do dataset e toma as métricas
        de validação.

        Parametros
        ----------
        :param bm_krnel: str, optional
            Kernel a ser utilizado. Deve pertencer ao conjunto {"linear", "rbf"
            , "poly"}
        :param bm_epsil: float, int, optional
            Tolerância ao erro. Padronizado em 0.005.
        :param bm_c: float, int , optional
            Peso aplicado a tolerâncias não respeitadas. Padronizado em 5.
        """

        # checar entrada
        #######################################################################
        self.bbb_regmt(bbb_methd="bm_fit", **kwargs)

        bm_cout = bc_Check.bc_isdp(self)
        if bm_cout["error"]:
            self.bbb_addlg(bm_cout["log"])
            return

        bm_dflt = bdm_DtMn.bdm_fdflt(self.bm_fit)

        self.bbb_param = {
            "bm_krnel": bm_krnel,
            "bm_epsil": bm_epsil,
            "bm_c": bm_c,
        }
        bm_schk = bc_Check.bc_schek(bc_mtype=self.bbb_mtype, bc_subs=bm_dflt)

        for bm_p in self.bbb_param:
            bm_cout = bm_schk[bm_p](self.bbb_param[bm_p])
            if bm_cout["error"]:
                self.bbb_param[bm_p] = bm_cout["subs"]
                self.bbb_addlg(bm_cout["log"])
        #######################################################################

        bm_p = bdm_DtMn.bdm_tdict(
            bdm_mtype=self.bbb_mtype,
            bdm_dict=self.bbb_param,
        )

        if len(self.bbb_outn) > 1:
            bm_model = MultiOutputRegressor(SVR(**bm_p))
        else:
            bm_model = SVR(**bm_p)

        bbb_BBox.bbb_fit(self, bm_model, **kwargs)

    def bm_fitgs(
        self,
        bm_grid: list = None,
        bm_score: str = "mae",
        **kwargs,
    ):
        """
        Treina o modelo com a partição de treino do dataset e toma as
        métricas de validação, definindo hiperparâmetros conforme resultado da
        Grid Search.

        :param bm_grid: Grid de busca.
        :param bm_score: Métrica para decidir o melhor conjunto de
            hiperparâmetros.
        """

        # checar entrada
        #######################################################################
        self.bbb_regmt(bbb_methd="bm_fitgs", **kwargs)

        bm_cout = bc_Check.bc_isdp(self)
        if bm_cout["error"]:
            self.bbb_addlg(bm_cout["log"])
            return

        if bm_grid is not None:

            bm_dflt = bdm_DtMn.bdm_fdflt(self.bm_fit)
            bm_schk = bc_Check.bc_schek(self.bbb_mtype)

            for (bm_i, bm_dict) in enumerate(bm_grid):

                for bm_arg in bm_dflt:
                    if bm_arg not in bm_dict:
                        bm_grid[bm_i][bm_arg] = [bm_dflt[bm_arg]]

                for bm_key in bm_dict:
                    for (bm_j, bm_param) in enumerate(bm_dict[bm_key]):
                        bm_cout = bm_schk[bm_key](bm_param)
                        if bm_cout["error"]:
                            bm_grid[bm_i][bm_key][bm_j] = bm_cout["subs"]
                            self.bbb_addlg(bm_cout["log"])

            # Remover redundâncias
            for (bm_i, bm_dict) in enumerate(bm_grid):
                for bm_j in bm_dict:
                    if len(bm_dict[bm_j]) != len(set(bm_dict[bm_j])):
                        bm_grid[bm_i][bm_j] = list(set(bm_grid[bm_i][bm_j]))
                        bbb_s = (
                            "Redundâncias removidas em bm_grid["
                            + str(bm_i)
                            + ']["'
                            + bm_j
                            + '"]'
                        )
                        self.bbb_addlg(bbb_s)
        else:
            bm_grid = [
                {
                    "bm_krnel": ["rbf", "poly"],
                    "bm_c": [3, 1.5, 1],
                    "bm_epsil": [0.1, 0.5],
                }
            ]

        #######################################################################

        if len(self.bbb_outn) > 1:
            bm_model = MultiOutputRegressor(SVR())
        else:
            bm_model = SVR()

        bbb_BBox.bbb_fit(self, bm_model, bm_grid, bbb_sscr=bm_score, **kwargs)


# %% Multivariate Regression
class bm_MVR(bbb_BBox):
    """
    Modelo caixa-preta do tipo Multivariate Regression

    Classe derivada de bbb_BBox, estendendo funcionalidades para atender a
    especificidade do modelo. Estende as funcionalidades __init__() e bbb_fit
    para fins de construção do objeto e especificação de hiperparâmetros,
    respectivamente.

    Métodos públicos:
        bm_fit
        bm_fitgs
    """

    def __init__(
        self,
        bm_name: str = "Multivariate Regression",
        bm_inn: tuple = ("days_since_start",),
        bm_outn: tuple = None,
        **kwargs,
    ):
        """
        :param bm_name: Nome do modelo a ser criado.
        :param bm_inn: Tupla contendo o nome das variáveis de entrada.
        :param bm_outn: Tupla contendo o nome da variável de saída.
        """

        bbb_BBox.__init__(
            self,
            bbb_name=bm_name,
            bbb_inn=bm_inn,
            bbb_outn=bm_outn,
            **kwargs,
        )
        # self.bbb_regmt(bbb_methd="__init__", **kwargs)
        self.bbb_mtype = "Multivariate Regression"

    def bm_fit(self, **kwargs):
        """Treina o modelo com a partição de treino do dataset e toma as métricas
        de validação."""

        bm_cout = bc_Check.bc_isdp(self)
        if bm_cout["error"]:
            self.bbb_addlg(bm_cout["log"])
            return

        self.bbb_param = {}

        bm_model = LinearRegression()

        bbb_BBox.bbb_fit(self, bm_model, **kwargs)

    def bm_fitgs(
        self,
        bm_grid: list = None,
        bm_score: str = "mae",
        **kwargs,
    ):
        """
        Treina o modelo com a partição de treino do dataset e toma as
        métricas de validação, definindo hiperparâmetros conforme resultado da
        Grid Search.

        :param bm_grid: Grid de busca.
        :param bm_score: Métrica para decidir o melhor conjunto de
            hiperparâmetros.
        """

        bm_cout = bc_Check.bc_isdp(self)
        if bm_cout["error"]:
            self.bbb_addlg(bm_cout["log"])
            return

        self.bm_fit(**kwargs)


# %% Gradient Boosting Regressor
class bm_GBR(bbb_BBox):
    """
    Modelo caixa-preta do tipo Gradient Boosting Regressor.

    Classe derivada de bbb_BBox, estendendo funcionalidades para atender a
    especificidade do modelo. Estende as funcionalidades __init__() e bbb_fit
    para fins de construção do objeto e especificação de hiperparâmetros,
    respectivamente.

    Métodos públicos:
        bm_fit
        bm_fitgs
    """

    def __init__(
        self,
        bm_name: str = "Gradient Boosting Regression",
        bm_inn: tuple = ("days_since_start",),
        bm_outn: tuple = None,
        **kwargs,
    ):
        """
        :param bm_name: Nome do modelo a ser criado.
        :param bm_inn: Tupla contendo o nome das variáveis de entrada.
        :param bm_outn: Tupla contendo o nome da variável de saída.
        """

        bbb_BBox.__init__(
            self,
            bbb_name=bm_name,
            bbb_inn=bm_inn,
            bbb_outn=bm_outn,
            **kwargs,
        )
        # self.bbb_regmt(bbb_methd="__init__", **kwargs)
        self.bbb_mtype = "Gradient Boosting Regression"

        # checar entrada
        #######################################################################
        # bc_Check.bc_outn(self.bbb_outn, self.bbb_mtype)
        #######################################################################

    def bm_fit(
        self,
        bm_bmdl=None,
        bm_nesti: int = 100,
        bm_lr: float = 0.1,
        bm_crite: str = "friedman_mse",
        bm_mdep: int = 3,
        **kwargs,
    ):
        """
        Treina o modelo com a partição de treino do dataset e toma as métricas
        de validação.

        :param bm_bmdl: bbb_BBox, default=None
            Modelo base.
        :param bm_nesti: int. default=100
            Numero de estimadores. Por padrão é igual a 100.
        :param bm_lr: float. default=0.1
            O quanto a contribuição de cada árvore diminui.
        :param bm_crite: string. default="friedman_mse".
            Função para definir a qualidade de uma divisão. Deve pertencer ao
            conjunto {"squared_error", "friedman_mse", "mse", "mae"}.
        :param bm_mdep: Profundidade máxima de cada árvore gerada.
        """

        # checar entrada
        #######################################################################
        self.bbb_regmt(bbb_methd="bm_fit", **kwargs)

        bm_cout = bc_Check.bc_isdp(self)
        if bm_cout["error"]:
            self.bbb_addlg(bm_cout["log"])
            return

        bm_dflt = bdm_DtMn.bdm_fdflt(self.bm_fit)

        self.bbb_param = {
            "bm_bmdl": bm_bmdl,
            "bm_nesti": bm_nesti,
            "bm_lr": bm_lr,
            "bm_crite": bm_crite,
            "bm_mdep": bm_mdep,
        }
        bm_schk = bc_Check.bc_schek(bc_mtype=self.bbb_mtype, bc_subs=bm_dflt)

        for bm_p in self.bbb_param:
            if bm_p == "bm_bmdl":
                bm_cout = bc_Check.bc_class(
                    bm_bmdl, [bbb_BBox, type(None)], "bm_bmdl", bc_subs=None
                )
                if bm_cout["error"]:
                    self.bbb_param[bm_p] = bm_cout["subs"]
                    self.bbb_addlg(bm_cout["log"])
            else:
                bm_cout = bm_schk[bm_p](self.bbb_param[bm_p])
                if bm_cout["error"]:
                    self.bbb_param[bm_p] = bm_cout["subs"]
                    self.bbb_addlg(bm_cout["log"])
        #######################################################################

        bm_p = bdm_DtMn.bdm_tdict(
            bdm_mtype=self.bbb_mtype,
            bdm_dict=self.bbb_param,
        )

        if bm_bmdl is not None:
            bm_p["init"] = bm_bmdl.bbb_model

        if len(self.bbb_outn) > 1:
            bm_model = MultiOutputRegressor(GradientBoostingRegressor(**bm_p))
        else:
            bm_model = GradientBoostingRegressor(**bm_p)

        bbb_BBox.bbb_fit(self, bm_model, **kwargs)

    def bm_fitgs(
        self,
        bm_grid: list = None,
        bm_score: str = "mae",
        **kwargs,
    ):
        """
        Treina o modelo com a partição de treino do dataset e toma as
        métricas de validação, definindo hiperparâmetros conforme resultado da
        Grid Search.

        :param bm_grid: Grid de busca.
        :param bm_score: Métrica para decidir o melhor conjunto de
            hiperparâmetros.
        """

        # checar entrada
        #######################################################################
        self.bbb_regmt(bbb_methd="bm_fitgs", **kwargs)

        bm_cout = bc_Check.bc_isdp(self)
        if bm_cout["error"]:
            self.bbb_addlg(bm_cout["log"])
            return

        if bm_grid is not None:

            bm_dflt = bdm_DtMn.bdm_fdflt(self.bm_fit)
            bm_schk = bc_Check.bc_schek(self.bbb_mtype)

            for (bm_i, bm_dict) in enumerate(bm_grid):

                for bm_arg in bm_dflt:
                    if bm_arg not in bm_dict:
                        bm_grid[bm_i][bm_arg] = [bm_dflt[bm_arg]]

                for bm_key in bm_dict:
                    for (bm_j, bm_param) in enumerate(bm_dict[bm_key]):
                        bm_cout = bm_schk[bm_key](bm_param)
                        if bm_cout["error"]:
                            bm_grid[bm_i][bm_key][bm_j] = bm_cout["subs"]
                            self.bbb_addlg(bm_cout["log"])

            # Remover redundâncias
            for (bm_i, bm_dict) in enumerate(bm_grid):
                for bm_j in bm_dict:
                    if len(bm_dict[bm_j]) != len(set(bm_dict[bm_j])):
                        bm_grid[bm_i][bm_j] = list(set(bm_grid[bm_i][bm_j]))
                        bbb_s = (
                            "Redundâncias removidas em bm_grid["
                            + str(bm_i)
                            + ']["'
                            + bm_j
                            + '"]'
                        )
                        self.bbb_addlg(bbb_s)

        else:
            bm_grid = [
                {
                    "bm_nesti": [10, 50, 100],
                    "bm_lr": [0.1, 0.2],
                    "bm_crite": ["friedman_mse"],
                }
            ]

        #######################################################################

        if len(self.bbb_outn) > 1:
            bm_model = MultiOutputRegressor(GradientBoostingRegressor())
        else:
            bm_model = GradientBoostingRegressor()

        bbb_BBox.bbb_fit(self, bm_model, bm_grid, bbb_sscr=bm_score, **kwargs)


# %% Random Forest Regressor
class bm_RFR(bbb_BBox):
    """
    Modelo caixa-preta do tipo Random Forest Regressor.

    Classe derivada de bbb_BBox, estendendo funcionalidades para atender a
    especificidade do modelo. Estende as funcionalidades __init__() e bbb_fit
    para fins de construção do objeto e especificação de hiperparâmetros,
    respectivamente.

    Métodos públicos:
        bm_fit
        bm_fitgs
    """

    def __init__(
        self,
        bm_name: str = "Random Forest Regression",
        bm_inn: tuple = ("days_since_start",),
        bm_outn: tuple = None,
        **kwargs,
    ):
        """
        :param bm_name: Nome do modelo a ser criado.
        :param bm_inn: Tupla contendo o nome das variáveis de entrada.
        :param bm_outn: Tupla contendo o nome da variável de saída.
        """

        bbb_BBox.__init__(
            self,
            bbb_name=bm_name,
            bbb_inn=bm_inn,
            bbb_outn=bm_outn,
            **kwargs,
        )
        # self.bbb_regmt(bbb_methd="__init__", **kwargs)
        self.bbb_mtype = "Random Forest Regression"

    def bm_fit(
        self,
        bm_nesti: int = 100,
        bm_mdep: int = None,
        bm_mleaf: int = None,
        bm_crite: str = "squared_error",
        **kwargs,
    ):
        """
        Treina o modelo com a partição de treino do dataset e toma as métricas
        de validação.

        :param bm_nesti: Número de árvores a serem geradas.
        :param bm_mdep: Profundidade máxima de cada nó da árvore.
        :param bm_mleaf: Número máximo de "folhas" (nós de saída) de cada
            árvore.
        :param bm_crite: Critério de melhora.
        """

        # checar entrada
        #######################################################################
        self.bbb_regmt(bbb_methd="bm_fit", **kwargs)

        bm_cout = bc_Check.bc_isdp(self)
        if bm_cout["error"]:
            self.bbb_addlg(bm_cout["log"])
            return

        bm_dflt = bdm_DtMn.bdm_fdflt(self.bm_fit)

        self.bbb_param = {
            "bm_nesti": bm_nesti,
            "bm_mdep": bm_mdep,
            "bm_mleaf": bm_mleaf,
            "bm_crite": bm_crite,
        }
        bm_schk = bc_Check.bc_schek(bc_mtype=self.bbb_mtype, bc_subs=bm_dflt)

        for bm_p in self.bbb_param:
            bm_cout = bm_schk[bm_p](self.bbb_param[bm_p])
            if bm_cout["error"]:
                self.bbb_param[bm_p] = bm_cout["subs"]
                self.bbb_addlg(bm_cout["log"])
        #######################################################################

        bm_p = bdm_DtMn.bdm_tdict(
            bdm_mtype=self.bbb_mtype,
            bdm_dict=self.bbb_param,
        )

        bm_model = RandomForestRegressor(**bm_p)

        bbb_BBox.bbb_fit(self, bm_model, **kwargs)

    def bm_fitgs(
        self,
        bm_grid: list = None,
        bm_score: str = "mae",
        **kwargs,
    ):
        """
        Treina o modelo com a partição de treino do dataset e toma as
        métricas de validação, definindo hiperparâmetros conforme resultado da
        Grid Search.

        :param bm_grid: Grid de busca.
        :param bm_score: Métrica para decidir o melhor conjunto de
            hiperparâmetros.
        """

        # checar entrada
        #######################################################################
        self.bbb_regmt(bbb_methd="bm_fitgs", **kwargs)

        bm_cout = bc_Check.bc_isdp(self)
        if bm_cout["error"]:
            self.bbb_addlg(bm_cout["log"])
            return

        if bm_grid is not None:

            bm_dflt = bdm_DtMn.bdm_fdflt(self.bm_fit)
            bm_schk = bc_Check.bc_schek(self.bbb_mtype)

            for (bm_i, bm_dict) in enumerate(bm_grid):

                for bm_arg in bm_dflt:
                    if bm_arg not in bm_dict:
                        bm_grid[bm_i][bm_arg] = [bm_dflt[bm_arg]]

                for bm_key in bm_dict:
                    for (bm_j, bm_param) in enumerate(bm_dict[bm_key]):
                        bm_cout = bm_schk[bm_key](bm_param)
                        if bm_cout["error"]:
                            bm_grid[bm_i][bm_key][bm_j] = bm_cout["subs"]
                            self.bbb_addlg(bm_cout["log"])

            # Remover redundâncias
            for (bm_i, bm_dict) in enumerate(bm_grid):
                for bm_j in bm_dict:
                    if len(bm_dict[bm_j]) != len(set(bm_dict[bm_j])):
                        bm_grid[bm_i][bm_j] = list(set(bm_grid[bm_i][bm_j]))
                        bbb_s = (
                            "Redundâncias removidas em bm_grid["
                            + str(bm_i)
                            + ']["'
                            + bm_j
                            + '"]'
                        )
                        self.bbb_addlg(bbb_s)

        else:
            bm_grid = [
                {
                    "bm_nesti": [50],
                    "bm_mdep": [3, 5],
                    "bm_crite": ["absolute_error", "squared_error"],
                }
            ]
        #######################################################################

        bm_model = RandomForestRegressor()
        bbb_BBox.bbb_fit(self, bm_model, bm_grid, bbb_sscr=bm_score, **kwargs)


# %% Ridge
class bm_RDG(bbb_BBox):
    """
    Modelo caixa-preta do tipo Ridge Regression.

    Classe derivada de bbb_BBox, estendendo funcionalidades para atender a
    especificidade do modelo. Estende as funcionalidades __init__() e bbb_fit
    para fins de construção do objeto e especificação de hiperparâmetros,
    respectivamente.

    Métodos públicos:
        bm_fit
        bm_fitgs
    """

    def __init__(
        self,
        bm_name: str = "Ridge Regression",
        bm_inn: tuple = ("days_since_start",),
        bm_outn: tuple = None,
        **kwargs,
    ):
        """
        :param bm_name: Nome do modelo a ser criado.
        :param bm_inn: Tupla contendo o nome das variáveis de entrada.
        :param bm_outn: Tupla contendo o nome da variável de saída.
        """

        bbb_BBox.__init__(
            self,
            bbb_name=bm_name,
            bbb_inn=bm_inn,
            bbb_outn=bm_outn,
            **kwargs,
        )
        # self.bbb_regmt(bbb_methd="__init__", **kwargs)
        self.bbb_mtype = "Ridge Regression"

    def bm_fit(self, bm_alpha: float = 1.0, **kwargs):
        """
        Treina o modelo com a partição de treino do dataset e toma as métricas
        de validação.

        :param bm_alpha: Controla a força da regularização. Deve ser do tipo
        float e maior que 0.
        """

        # checar entrada
        #######################################################################
        self.bbb_regmt(bbb_methd="bm_fit", **kwargs)

        bm_cout = bc_Check.bc_isdp(self)
        if bm_cout["error"]:
            self.bbb_addlg(bm_cout["log"])
            return

        bm_dflt = bdm_DtMn.bdm_fdflt(self.bm_fit)

        self.bbb_param = {"bm_alpha": bm_alpha}
        bm_schk = bc_Check.bc_schek(
            bc_mtype=self.bbb_mtype,
            bc_subs=bm_dflt,
        )

        for bm_p in self.bbb_param:
            bm_cout = bm_schk[bm_p](self.bbb_param[bm_p])
            if bm_cout["error"]:
                self.bbb_param[bm_p] = bm_cout["subs"]
                self.bbb_addlg(bm_cout["log"])
        #######################################################################

        bm_p = bdm_DtMn.bdm_tdict(
            bdm_mtype=self.bbb_mtype,
            bdm_dict=self.bbb_param,
        )

        bm_model = Ridge(**bm_p)
        bbb_BBox.bbb_fit(self, bm_model, **kwargs)

    def bm_fitgs(
        self,
        bm_grid: list = None,
        bm_score: str = "mae",
        **kwargs,
    ):
        """
        Treina o modelo com a partição de treino do dataset e toma as
        métricas de validação, definindo hiperparâmetros conforme resultado da
        Grid Search.

        :param bm_grid: Grid de busca.
        :param bm_score: Métrica para decidir o melhor conjunto de
            hiperparâmetros.
        """

        # checar entrada
        #######################################################################
        self.bbb_regmt(bbb_methd="bm_fitgs", **kwargs)

        bm_cout = bc_Check.bc_isdp(self)
        if bm_cout["error"]:
            self.bbb_addlg(bm_cout["log"])
            return

        if bm_grid is not None:

            bm_dflt = bdm_DtMn.bdm_fdflt(self.bm_fit)
            bm_schk = bc_Check.bc_schek(self.bbb_mtype)

            for (bm_i, bm_dict) in enumerate(bm_grid):

                for bm_arg in bm_dflt:
                    if bm_arg not in bm_dict:
                        bm_grid[bm_i][bm_arg] = [bm_dflt[bm_arg]]

                for bm_key in bm_dict:
                    for (bm_j, bm_param) in enumerate(bm_dict[bm_key]):
                        bm_cout = bm_schk[bm_key](bm_param)
                        if bm_cout["error"]:
                            bm_grid[bm_i][bm_key][bm_j] = bm_cout["subs"]
                            self.bbb_addlg(bm_cout["log"])

            # Remover redundâncias
            for (bm_i, bm_dict) in enumerate(bm_grid):
                for bm_j in bm_dict:
                    if len(bm_dict[bm_j]) != len(set(bm_dict[bm_j])):
                        bm_grid[bm_i][bm_j] = list(set(bm_grid[bm_i][bm_j]))
                        bbb_s = (
                            "Redundâncias removidas em bm_grid["
                            + str(bm_i)
                            + ']["'
                            + bm_j
                            + '"]'
                        )
                        self.bbb_addlg(bbb_s)

        else:
            bm_grid = [{"bm_alpha": [0.0, 0.1, 0.25, 0.5, 1]}]
        #######################################################################

        bm_model = Ridge()
        bbb_BBox.bbb_fit(self, bm_model, bm_grid, bbb_sscr=bm_score, **kwargs)


# %% Decision Tree Regressor
class bm_DTR(bbb_BBox):
    """
    Modelo caixa-preta do tipo Decision Tree Regressor.

    Classe derivada de bbb_BBox, estendendo funcionalidades para atender a
    especificidade do modelo. Estende as funcionalidades __init__() e bbb_fit
    para fins de construção do objeto e especificação de hiperparâmetros,
    respectivamente.

    Métodos públicos:
        bm_fit
        bm_fitgs
    """

    def __init__(
        self,
        bm_name: str = "Decision Tree Regression",
        bm_inn: tuple = ("days_since_start",),
        bm_outn: tuple = None,
        **kwargs,
    ):
        """
        :param bm_name: Nome do modelo a ser criado.
        :param bm_inn: Tupla contendo o nome das variáveis de entrada.
        :param bm_outn: Tupla contendo o nome da variável de saída.
        """

        bbb_BBox.__init__(
            self,
            bbb_name=bm_name,
            bbb_inn=bm_inn,
            bbb_outn=bm_outn,
            **kwargs,
        )
        # self.bbb_regmt(bbb_methd="__init__", **kwargs)
        self.bbb_mtype = "Decision Tree Regression"

    def bm_fit(
        self,
        bm_mdep: int = None,
        bm_mleaf: int = None,
        bm_crite: str = "friedman_mse",
        **kwargs,
    ):
        """
        Treina o modelo com a partição de treino do dataset e toma as métricas
        de validação.

        :param bm_mdep: Profundidade máxima da árvore.
        :param bm_mleaf: Número máximo de "folhas" (nós de saída) da
            árvore.
        :param bm_crite: Critério de melhora.
        """

        # checar entrada
        #######################################################################
        self.bbb_regmt(bbb_methd="bm_fit", **kwargs)

        bm_cout = bc_Check.bc_isdp(self)
        if bm_cout["error"]:
            self.bbb_addlg(bm_cout["log"])
            return

        bm_dflt = bdm_DtMn.bdm_fdflt(self.bm_fit)

        self.bbb_param = {
            "bm_mdep": bm_mdep,
            "bm_mleaf": bm_mleaf,
            "bm_crite": bm_crite,
        }
        bm_schk = bc_Check.bc_schek(
            bc_mtype=self.bbb_mtype,
            bc_subs=bm_dflt,
        )

        for bm_p in self.bbb_param:
            bm_cout = bm_schk[bm_p](self.bbb_param[bm_p])
            if bm_cout["error"]:
                self.bbb_param[bm_p] = bm_cout["subs"]
                self.bbb_addlg(bm_cout["log"])
        #######################################################################

        self.bbb_param = {
            "bm_mdep": bm_mdep,
            "bm_mleaf": bm_mleaf,
            "bm_crite": bm_crite,
        }

        bm_p = bdm_DtMn.bdm_tdict(
            bdm_mtype=self.bbb_mtype,
            bdm_dict=self.bbb_param,
        )

        bm_model = DecisionTreeRegressor(**bm_p)
        bbb_BBox.bbb_fit(self, bm_model, **kwargs)

    def bm_fitgs(
        self,
        bm_grid: list = None,
        bm_score: str = "mae",
        **kwargs,
    ):
        """
        Treina o modelo com a partição de treino do dataset e toma as
        métricas de validação, definindo hiperparâmetros conforme resultado da
        Grid Search.

        :param bm_grid: Grid de busca.
        :param bm_score: Métrica para decidir o melhor conjunto de
            hiperparâmetros.
        """

        #######################################################################
        bm_cout = bc_Check.bc_isdp(self)
        if bm_cout["error"]:
            self.bbb_addlg(bm_cout["log"])
            return

        if bm_grid is not None:

            bm_dflt = bdm_DtMn.bdm_fdflt(self.bm_fit)
            bm_schk = bc_Check.bc_schek(self.bbb_mtype)

            for (bm_i, bm_dict) in enumerate(bm_grid):

                for bm_arg in bm_dflt:
                    if bm_arg not in bm_dict:
                        bm_grid[bm_i][bm_arg] = [bm_dflt[bm_arg]]

                for bm_key in bm_dict:
                    for (bm_j, bm_param) in enumerate(bm_dict[bm_key]):
                        bm_cout = bm_schk[bm_key](bm_param)
                        if bm_cout["error"]:
                            bm_grid[bm_i][bm_key][bm_j] = bm_cout["subs"]
                            self.bbb_addlg(bm_cout["log"])

            # Remover redundâncias
            for (bm_i, bm_dict) in enumerate(bm_grid):
                for bm_j in bm_dict:
                    if len(bm_dict[bm_j]) != len(set(bm_dict[bm_j])):
                        bm_grid[bm_i][bm_j] = list(set(bm_grid[bm_i][bm_j]))
                        bbb_s = (
                            "Redundâncias removidas em bm_grid["
                            + str(bm_i)
                            + ']["'
                            + bm_j
                            + '"]'
                        )
                        self.bbb_addlg(bbb_s)

        else:
            bm_grid = [
                {
                    "bm_mdep": [1, 3, 5],
                    "bm_crite": ["absolute_error", "friedman_mse"],
                }
            ]
        #######################################################################

        bm_model = DecisionTreeRegressor()
        bbb_BBox.bbb_fit(self, bm_model, bm_grid, bbb_sscr=bm_score, **kwargs)
