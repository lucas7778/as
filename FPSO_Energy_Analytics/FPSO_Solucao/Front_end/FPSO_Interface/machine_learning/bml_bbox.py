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
Separação do ferramental gráfico (a solução utilizará o desenvolvido pelo
Front-end). Adicionada opção de devolver a predição em função da carga nominal
(fator de carga). Simplificação do método bbb_cstat: será chamado de forma
automática ao terminar o bm_fit() (em uma atualização futura bbb_cstat passará
a fazer parte da classe bdm_DtMn ao invés de bbb_BBox). Adicionado o método
bbb_stats, que retorna todas métricas calculadas.

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
    Padronização dos nomes de variáveis e argumentos dos métodos de bbb_BBox.
Ajustes nas docstrings refletindo as alterações. Adicionado o parâmetro
bbb_normt para ajuste de estratégia de normalização.

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
    Adicionados métodos para salvar modelos.

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
    Adicionado controle de entrada para o método bbb_sstat. Adicionada a
funcionalidade de salvar as tabelas em formato excel. Adicionado o parâmetro
bbb_normt à classe bbb_BBox (guarda informações sobre normalização), junto com
getter apropriado. Removido o parâmetro bdm_normt da classe bdm_DtMn. Métodos
de bdm_DtMn convertidos para métodos estáticos. Classe bdm_DtMn separada nas
classes bp_Perfm e bdm_DtMn (para tomada de métricas do modelo e manipulações
gerais de dados). Cálculo do IQR movido parao método bp_apred. Instanciamento
da classe bdm_DtMn em bbb_BBox removido. Método bbb_cstat removido (a lógica
agora faz parte do processamento de bm_fit). Ajustes nas propriedades bbb_sdf e
bbb_smry. Ajustes nos métodos refletindo alterações. Valor padrão de bbb_form
alterado para False. (os dataframes de estatísticas serão retornados/salvos em
formato numérico por padrão).

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
    Método bbb_save removido devido a problemas de importação circular (e
também redundância).

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
    Adicionado controle de entrada para o argumento bbb_fator no método
bbb_pred. Adicionado atributo bbb_prepx, que guarda o objeto utilizado para
pré-processamento de inputs. Adicionados argumentos para pré-processamento no
método bbb_pdata. Alterado o formato padrão dos dados (treinamento, predição
etc) de NumPy para DataFrame, conforme padronização do projeto. Parâmetro
bbb_normt removido. Passagem de parâmetros bbb_onom, bbb_dsspl movida de
__init__ para o método bbb_pdata. Adicionado atributo bbb_prepy, que guarda o
objeto utilizado para pré/pós-processamento de outputs. Adicionados atributos
bbb_pcolx e bbb_pcoly, que guardam listas contendo os nomes das colunas para
apresentação do pré-processamento. Adicionados métodos bbb_trnsx e bbb_trnsy
que permitem visualização dos dados após o pré-processamento. Controle de
entrada de bbb_pred alterado refletindo alterações na estratégia de
pré-processamento. Alterações nos métodos envolvendo atividades de
préprocessamento refletindo alterações no fluxo de dados: leitura inicial do
dataframe passado, preprocessamento, predição/treinamento. Atualização no
método de particionamento do DataFrame para treinamento, validação e teste:
métodos bdm_dfpar, bdm_dfsim, bdm_dfgrn, bdm_gdiv adicionados, possibilitando a
divisão das partições de forma granular (cada partição cobrirá o mesmo
horizonte de tempo que o DataFrame original).Alteração no valor padrão de
bbb_setup em bbb_pdata. Adicionado parâmetro bbb_noneg no método bbb_pred,
que controla a conversão de valores negativos das previsões para 0. Correção de
bug (tentativa de transformação inversa incorreta e/ou conversão para fator de
carga ao se passar processamento especial para variável de saída).
Adicionado argumento bbb_fread ao método bbb_pred, que verifica se é necessário
fazer o procedimento inicial de leitura (chamar o método bdm_ids).
Adicionado método bc_isfit em bc_Check para checar se o modelo pode ser usado
para atividades que requerem treinamento. Adicionado parâmetro bbb_isfit que
contém informações a respeito do status de treinamento do modelo. Método
bm_fitgs adicionado aos modelos (executa Grid Search). Método bbb_fit
adicionado a classe bbb_BBox. Métodos bm_fit e bm_fitgs ambos extendem o método
bbb_fit. Argumento bbb_sscr adicionado ao método bbb_BBox.bbb_fit, que controla
a métrica utilizada na Grid Search. Parâmetro bbb_gsr adicionado a classe
bbb_BBox (DataFrame que contém os resultados da GridSearch). Parâmetro bbb_isdp
adicionado a classe bbb_BBox: informa se o modelo está pronto para ser
treinado. Funcionalidade para salvar resultados da Grid Search adicionada ao
Método bbb_sstat. bbb_info passa a informar se foi realizado um treinamento
normal ou com Grid Search. Processamento de bm_grid passado para o método
bbb_fit. Padronização de variáveis em bbb_BBox. Ajustes nas docstrings de
bml_model e bml_bbox. Docstrings para os parâmetros de bbb_BBox adicionada.
Método bbb_BBox.bbb_testm adicionado, que retorna métricas sobre o dataset de
teste. Ajustes gerais na documentação do módulo.

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
    Bug corrigido em bbb_fit (o for loop declarado na linha 728 agora acessa a
variável correta). Variável bbb_log que contém o log interno
de utilização do modelo adicionada. Método bbb_addl, que adiciona informações
ao log, adicionado. Type hints parcialmente adicionadas. Argumento **kwargs
adicionado aos métodos de bml_bbox e bml_model. Valores default adicionados
para argumentos bm_name/bbb_name e bm_inn/bbb_inn. Método bc_ds adicionado a
bc_Check, que checa a pertinencia do dataset passado para o modelo. Progresso
parcial no tratamento de erros. Padronização das keywords dos dicionários de
bm_grid (equivalente a padronização de bm_fit). Progresso parcial no tratamento
de erros. Método bc_array atualizado. Error catching geral adicionado em
bbb_fit, bbb_pdata, bbb_trnsx, bbb_trnsy, bbb_pred, bbb_sstat. Progresso
parcial no tratamento de erros de bbb_setup. Variável bbb_compt, que segura os
resultados de bmm_auto, adicionada à classe BBox. Atualizações nos métodos
bbb_stats e bbb_sstat, refletindo adição de bbb_compt. Classe BBox atualizada
para sempre imprimir registros novos do log. Progresso parcial no controle de
entrada (rotinas para checagem do dataset e partições atualizadas). Variável
bbb_isbc adicionada a classe bbb_BBox, que reporta se o modelo foi instanciado
corretamente. Ajustes no controle de entrada no método __init__ de BBox.
Progresso parcial na adição de type hints. Adição do controle de entrada do
método bbb_pdata concluido. Documentação atualizada.
"""

import os
import warnings
from math import isclose
from datetime import datetime
from typing import Union, Optional

import numpy as np
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import (
    MinMaxScaler,
    LabelBinarizer,
    StandardScaler,
    Binarizer,
    KBinsDiscretizer,
)
from sklearn.exceptions import FitFailedWarning
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

from machine_learning.bml_dtmn import bdm_DtMn
from machine_learning.bml_check import bc_Check
from machine_learning.bml_perfm import bp_Perfm
from machine_learning.bml_log import bl_Log

"""
Define a superclasse bbb_BBox, classe base que define métodos
e atributos comuns a todos os modelos.

Métodos
----------
    bbb_info: Retorna informações a respeito da instância
    bbb_fit: Treina o modelo (uso interno)
    bbb_pdata: Prepara o dataset
    bbb_pred: Recebe x (input) e retorna y (output),  
    bbb_sdf: Retorna a comparação das predições com as Ground Truths
    bbb_smry: Retorna o estatísticas descritivas do modelo
    bbb_sstat: Salva as tabelas geradas em bbb_save
    bbb_stats: Retorna as estatísticas do modelo
    bbb_testm: Retorna as estatísticas comparando com a partição de testes
    bbb_trnsx: Transforma x conforme as opções de pré-processamento.
    bbb_trnsy: Transforma x conforme as opções de pré-processamento.
"""

# %% Superclasse bml_BBox


class bbb_BBox:
    """
    Superclasse base de predição baseada em Machine Learning.

    Atributos públicos:
        bbb_cvar, bbb_dm, bbb_ds, bbb_dsinf, bbb_dsspl, bbb_inn, bbb_name,
        bbb_onom, bbb_outn, bbb_trnds, bbb_tstds, bbb_valds, bbb_model,
        bbb_mtype, bbb_r2

        bbb_sdf, bbb_smry

    Métodos públicos:
        bbb_info, bbb_pdata, bbb_pred, bbb_sstat, bbb_stats

    """

    def __init__(
        self,
        bbb_name: str = "BBox Model",
        bbb_inn: tuple = ("days_since_start",),
        bbb_outn: tuple = None,
        **kwargs,
    ):
        """
        :param bbb_name: Nome do modelo a ser criado.
        :param bbb_inn: Tupla contendo o nome das variáveis de entrada.
        :param bbb_outn: Tupla contendo o nome da variável de saída.
        """

        try:

            self.__bbb_isbc = True
            self.__bbb_log = ""

            # checar entrada
            #######################################################################
            # self.bbb_regmt(bbb_methd="__init__", **kwargs)

            bbb_cout = bc_Check.bc_type(
                bc_var=bbb_name,
                bc_dtype=[type(None), str],
                bc_vname="bbb_name",
                bc_subs="Model",
            )
            if bbb_cout["error"]:
                bbb_name = bbb_cout["subs"]
                self.bbb_addlg(bbb_cout["log"])

            bbb_cout = bc_Check.bc_array(
                bc_var=bbb_inn,
                bc_atype=[tuple],
                bc_dtype=[str],
                bc_vname="bbb_inn/bbb_outn",
            )
            if bbb_cout["error"]:
                self.bbb_addlg(bbb_cout["log"])
                self.__bbb_isbc = False

            bbb_cout = bc_Check.bc_array(
                bc_var=bbb_outn,
                bc_atype=[tuple],
                bc_dtype=[str],
                bc_vname="bbb_outn",
                bc_dlen=1,
            )
            if bbb_cout["error"]:
                self.bbb_addlg(bbb_cout["log"])
                self.__bbb_isbc = False

            #######################################################################

            if self.__bbb_isbc is True:
                self.__bbb_name = bbb_name if bbb_name is not None else "bbb_BBox"
                self.__bbb_inn = bbb_inn
                self.__bbb_outn = bbb_outn
                self.__bbb_cvar = bbb_inn + bbb_outn
            else:
                self.__bbb_name = None
                self.__bbb_inn = None
                self.__bbb_outn = None
                self.__bbb_cvar = None

            self.__bbb_onom = None

            self.__bbb_mtype = None
            self.__bbb_model = None

            self.__bbb_ds = None
            self.__bbb_dsinf = None

            self.__bbb_setup = None
            self.__bbb_inv = True
            self.__bbb_dsspl = None
            self.__bbb_sprep = None

            self.__bbb_prepx = None
            self.__bbb_prepy = None
            self.__bbb_pcolx = None
            self.__bbb_pcoly = None

            self.__bbb_trnds = None
            self.__bbb_valds = None
            self.__bbb_tstds = None

            self.__bbb_param = None

            self.__bbb_r2 = None
            self.__bbb_mae = None
            self.__bbb_mdae = None
            self.__bbb_maep = None
            self.__bbb_mdaep = None

            self.__bbb_sdf = None
            self.__bbb_smry = None

            self.__bbb_gsp = None
            self.__bbb_gsr = None

            self.__bbb_compt = None

            self.__bbb_isfit = False

            self.__bbb_isdp = False

            if self.__bbb_isbc:
                self.bbb_addlg("Modelo instanciado com exito.")
            else:
                self.bbb_addlg("O modelo não foi instanciado com exito.")

        except Exception as ex:
            self.bbb_addlg(str(ex))

    # getters e setters

    # bbb_name
    @property
    def bbb_name(self):
        """Nome da instância."""
        return self.__bbb_name

    # bbb_inn
    @property
    def bbb_inn(self):
        """Tupla contendo o nome dos inputs."""
        return self.__bbb_inn

    # bbb_outn
    @property
    def bbb_outn(self):
        """Nome do output."""
        return self.__bbb_outn

    # bbb_onom
    @property
    def bbb_onom(self):
        """Valor nominal do output."""
        return self.__bbb_onom

    @bbb_onom.setter
    def bbb_onom(self, o):
        self.__bbb_onom = o

    # bbb_cvar
    @property
    def bbb_cvar(self):
        """Tupla contendo os nomes de todas as variáveis utilizadas pela
        instância."""
        return self.__bbb_cvar

    # bbb_mtype
    @property
    def bbb_mtype(self):
        """Nome do modelo (Técnica de Machine Learning utilizada)."""
        return self.__bbb_mtype

    @bbb_mtype.setter
    def bbb_mtype(self, m):
        self.__bbb_mtype = m

    # bbb_model
    @property
    def bbb_model(self):
        """Objeto do modelo."""
        return self.__bbb_model

    @bbb_model.setter
    def bbb_model(self, m):
        self.__bbb_model = m

    # dataset
    @property
    def bbb_ds(self):
        """Base de dados utilizada pelo modelo."""
        return self.__bbb_ds

    # ds_info
    @property
    def bbb_dsinf(self):
        """Descrição da base de dados utilizada."""
        return self.__bbb_dsinf

    # bbb_setup
    @property
    def bbb_setup(self):
        """Opções de pré-processamento da base de dados."""
        return self.__bbb_setup

    @bbb_setup.setter
    def bbb_setup(self, s):
        self.__bbb_setup = s

    # bbb_inv
    @property
    def bbb_inv(self):
        """True se as transformações de pré-processamento de y são
        revertíveis, caso contrário, False."""
        return self.__bbb_inv

    # bbb_dsspl
    @property
    def bbb_dsspl(self):
        """Percentis para partições de treinamento, validação e teste da base
        de dados, respectivamente."""
        return self.__bbb_dsspl

    @bbb_dsspl.setter
    def bbb_dsspl(self, s):
        self.__bbb_dsspl = s

    # bbb_sprep
    @property
    def bbb_sprep(self):
        """Opções especiais de pré-processamento."""
        return self.__bbb_sprep

    @bbb_sprep.setter
    def bbb_sprep(self, s):
        self.__bbb_sprep = s

    # bbb_prepx
    @property
    def bbb_prepx(self):
        """Variável que guarda as transformações de inputs."""
        return self.__bbb_prepx

    @bbb_prepx.setter
    def bbb_prepx(self, p):
        self.__bbb_prepx = p

    # bbb_prepy
    @property
    def bbb_prepy(self):
        """Variável que guarda as transformações de outputs."""
        return self.__bbb_prepy

    @bbb_prepy.setter
    def bbb_prepy(self, p):
        self.__bbb_prepy = p

    # bbb_pcolx
    @property
    def bbb_pcolx(self):
        """Nomes das colunas do DataFrame de input (processado)."""
        return self.__bbb_pcolx

    @bbb_pcolx.setter
    def bbb_pcolx(self, p):
        self.__bbb_pcolx = p

    # bbb_pcoly
    @property
    def bbb_pcoly(self):
        """Nomes das colunas do DataFrame de saída (processado)."""
        return self.__bbb_pcoly

    @bbb_pcoly.setter
    def bbb_pcoly(self, p):
        self.__bbb_pcoly = p

    # bbb_trnds
    @property
    def bbb_trnds(self):
        """Partição de treinamento do dataset."""
        return self.__bbb_trnds

    # bbb_valds
    @property
    def bbb_valds(self):
        """Partição de validação do dataset"""
        return self.__bbb_valds

    # bbb_tstds
    @property
    def bbb_tstds(self):
        """Partição de teste do dataset."""
        return self.__bbb_tstds

    # bbb_param
    @property
    def bbb_param(self):
        """Hiperparâmetros do modelo."""
        return self.__bbb_param

    @bbb_param.setter
    def bbb_param(self, p):
        self.__bbb_param = p

    # bbb_r2
    @property
    def bbb_r2(self):
        """Score R^2 sobre o dataset de validação."""
        return self.__bbb_r2

    @property
    def bbb_valsc(self):
        """R^2 (Depreciado)"""
        return self.bbb_r2

    @bbb_r2.setter
    def bbb_r2(self, score):
        self.__bbb_r2 = score

    # bbb_mae
    @property
    def bbb_mae(self):
        """Média do Erro Absoluto (MAE) sobre o dataset de validação."""
        return self.__bbb_mae

    @bbb_mae.setter
    def bbb_mae(self, score):
        self.__bbb_mae = score

    # bbb_mdae
    @property
    def bbb_mdae(self):
        """Mediana do Erro Absoluto sobre o dataset de validação."""
        return self.__bbb_mdae

    @bbb_mdae.setter
    def bbb_mdae(self, score):
        self.__bbb_mdae = score

    # bbb_maep
    @property
    def bbb_maep(self):
        """MAE sobre o dataset de validação em percentual."""
        return self.__bbb_maep

    @bbb_maep.setter
    def bbb_maep(self, score):
        self.__bbb_maep = score

    # bbb_mdaep
    @property
    def bbb_mdaep(self):
        """Mediana do Erro Abs. sobre o dataset de validação em percentual."""
        return self.__bbb_mdaep

    @bbb_mdaep.setter
    def bbb_mdaep(self, score):
        self.__bbb_mdaep = score

    # stats_df
    @property
    def bbb_sdf(self):
        """Comparação das predições com a partição de validação."""
        return self.__bbb_sdf

    @bbb_sdf.setter
    def bbb_sdf(self, df):
        self.__bbb_sdf = df

    # bbb_smry
    @property
    def bbb_smry(self):
        """Sumário da comparação com a partição de validação."""
        return self.__bbb_smry

    @bbb_smry.setter
    def bbb_smry(self, smry):
        self.__bbb_smry = smry

    @property
    def bbb_mtrct(self):
        """Tabela apresentando as métricas do modelo."""
        return bp_Perfm.bp_mtrct(self)

    # bbb_gsp
    @property
    def bbb_gsp(self):
        """Parâmetros da Grid Search (se executada)."""
        return self.__bbb_gsp

    # bbb_gsr
    @property
    def bbb_gsr(self):
        """DataFrame contendo resultados da Grid Search."""
        return self.__bbb_gsr

    # bbb_compt
    @property
    def bbb_compt(self):
        """Dataframe contendo comparação dos modelos gerados por bmm_auto."""
        return self.__bbb_compt

    @bbb_compt.setter
    def bbb_compt(self, c):
        self.__bbb_compt = c

    # bbb_isfit
    @property
    def bbb_isfit(self):
        """O modelo já foi treinado? (True ou False)."""
        return self.__bbb_isfit

    @bbb_isfit.setter
    def bbb_isfit(self, f):
        self.__bbb_isfit = f

    # bbb_ispd
    @property
    def bbb_isdp(self):
        """O modelo já teve os dados preparados? (True ou False)"""
        return self.__bbb_isdp

    @bbb_isdp.setter
    def bbb_isdp(self, p):
        self.__bbb_isdp = p

    # bbb_isbc
    @property
    def bbb_isbc(self):
        """O modelo foi instanciado corretamente? (True ou False)"""
        return self.__bbb_isbc

    # bbb_log
    @property
    def bbb_log(self):
        """Log de utilização do modelo."""
        return self.__bbb_log

    # métodos

    def bbb_info(self, **kwargs):
        """Retorna informações a respeito do modelo instanciado."""

        try:

            self.bbb_regmt(bbb_methd="bbb_info", **kwargs)

            if not self.__bbb_isbc:
                return "Modelo não instanciado corretamente."

            bbb_str = "Name: " + str(self.bbb_name) + "\n\n"

            if self.__bbb_mtype is not None:
                bbb_str += "Model Type: " + self.__bbb_mtype

            bbb_str += "\nStatus: "
            if not self.bbb_isfit:
                bbb_str += "Unbuilt"
            else:
                bbb_str += "Trained"
                if self.bbb_gsr is not None:
                    bbb_str += " (Grid Search)"

            if self.bbb_isfit:
                bbb_str += "\n\nMetrics:"
                bbb_str += "\n\t" + str(self.bbb_mtrct).replace("\n", "\n\t")

            bbb_str += "\n\n\nOutput:\n"
            for bbb_name in self.__bbb_outn:
                bbb_str += "\t" + bbb_name + "\n"

            bbb_str += "\n\nInputs:\n"
            for bbb_name in self.__bbb_inn:
                bbb_str += "\t" + bbb_name + "\n"

            if self.bbb_isfit and self.__bbb_mtype != "Multivariate Regression":
                bbb_str += "\n\nParams:\n"
                bbb_str += "\n\t" + str(
                    pd.DataFrame.from_dict(
                        self.bbb_param,
                        columns=["Value"],
                        orient="index",
                    )
                ).replace("\n", "\n\t")

                bbb_str += "\n\n"

        except Exception as ex:
            self.bbb_addlg(str(ex))
            return

        return bbb_str

    def bbb_pdata(
        self,
        bbb_dsraw: pd.DataFrame = None,
        bbb_setup: dict = None,
        **kwargs,
    ):
        """
        Prepara o dataset: normalização, binning, split de treinamento,
        validação e teste etc.

        :param bbb_dsraw: DataFrame a ser lido.
        :param bbb_setup: Dicionário contendo as opções de pré-processamento.
        """

        # checar entrada
        #######################################################################
        try:

            self.bbb_regmt(bbb_methd="bbb_pdata", **kwargs)

            bbb_cout = bc_Check.bc_isbc(self)
            if bbb_cout["error"]:
                self.bbb_addlg(bbb_cout["log"])
                return

            bbb_mdsln = (20, np.inf)
            # checar dataframe
            bbb_cout = bc_Check.bc_ds(
                bc_model=self,
                bc_vars=self.bbb_cvar,
                bc_dataf=bbb_dsraw,
                bc_clen=True,
                bc_dlen=(2 * bbb_mdsln[0], 2 * bbb_mdsln[1]),
                bc_vname="bbb_dsraw",
            )
            if bbb_cout["error"]:
                self.bbb_addlg(bbb_cout["log"])
                if bbb_cout["subs"] is None:
                    return
                else:
                    bbb_dsraw = bbb_cout["subs"]

            bbb_dstp = {
                "scale": "minmax",
                "range": (-1, 1),
                "special_preprocessing": {},
                "dataset_split": (0.6, 0.2, 0.2),
                "dataset_split_type": "granular",
                "ds_gran_interval": (2, 100),
                "out_nominal": tuple([None for i in range(len(self.bbb_outn))]),
                "nokdd": False,
            }

            if bbb_setup is None:
                self.bbb_addlg(
                    "Convertendo para opções padrão de preparo do dataset."
                )
                bbb_setup = {**bbb_dstp}

            else:
                bbb_setup = {**bbb_setup}
                # checar opção de escala
                if "scale" in bbb_setup:
                    bbb_cout = bc_Check.bc_inset(
                        bc_var=bbb_setup["scale"],
                        bc_dval=["minmax", "standard", "none"],
                        bc_subs="minmax",
                        bc_vname='bbb_setup["scale"]',
                    )
                    if bbb_cout["error"]:
                        bbb_setup["scale"] = bbb_cout["subs"]
                        self.bbb_addlg(bbb_cout["log"])
                else:
                    bbb_setup["scale"] = "minmax"
                    # self.bbb_addlg("Convertendo scale para padrão.")

                # checar range
                if "range" in bbb_setup:
                    bbb_cout = bc_Check.bc_range(
                        bc_var=bbb_setup["range"],
                        bc_subs=(-1, 1),
                    )
                    if bbb_cout["error"]:
                        bbb_setup["range"] = bbb_cout["subs"]
                        self.bbb_addlg(bbb_cout["log"])

                elif bbb_setup["scale"] == "minmax":
                    bbb_setup["range"] = (-1, 1)

                # checar sprep
                if "special_preprocessing" in bbb_setup:
                    bbb_setup["special_preprocessing"] = {
                        **bbb_setup["special_preprocessing"]
                    }
                    bbb_cout = bc_Check.bc_svar(
                        bc_var=bbb_setup["special_preprocessing"],
                        bc_cvars=self.bbb_cvar,
                    )
                    if bbb_cout["error"]:
                        bbb_setup["special_preprocessing"] = bbb_cout["subs"]
                        self.bbb_addlg(bbb_cout["log"])

                else:
                    bbb_setup["special_preprocessing"] = {}

                # checar split de dataset
                if "dataset_split" in bbb_setup:
                    bbb_cout = bc_Check.bc_dsspl(
                        bc_var=bbb_setup["dataset_split"],
                        bc_vname='bbb_setup["dataset_split"]',
                        bc_subs=bbb_dstp["dataset_split"],
                    )
                    if bbb_cout["error"]:
                        bbb_setup["dataset_split"] = bbb_dstp["dataset_split"]
                        self.bbb_addlg(bbb_cout["log"])
                else:
                    bbb_setup["dataset_split"] = bbb_dstp["dataset_split"]

                # checar tipo de split
                if "dataset_split_type" in bbb_setup:
                    bbb_cout = bc_Check.bc_inset(
                        bc_var=bbb_setup["dataset_split_type"],
                        bc_vname='bbb_setup["dataset_split_type"]',
                        bc_dval=["simple", "granular"],
                        bc_subs=bbb_dstp["dataset_split_type"],
                    )
                    if bbb_cout["error"]:
                        bbb_setup["dataset_split_type"] = bbb_cout["subs"]
                        self.bbb_addlg(bbb_cout["log"])
                else:
                    bbb_setup["dataset_split_type"] = bbb_dstp[
                        "dataset_split_type"
                    ]

                # checar ds_gran_interval
                if "ds_gran_interval" in bbb_setup:
                    bbb_cout = bc_Check.bc_range(
                        bc_var=bbb_setup["ds_gran_interval"],
                        bc_subs=bbb_dstp["ds_gran_interval"],
                        bc_vname='bbb_dstp["ds_gran_interval"]',
                        bc_rngtp=[int],
                    )
                    if bbb_cout["error"]:
                        self.bbb_addlg(bbb_cout["log"])
                        bbb_setup["ds_gran_interval"] = bbb_cout["subs"]
                else:
                    bbb_setup["ds_gran_interval"] = bbb_dstp["ds_gran_interval"]

                # checar out nominal
                if "out_nominal" in bbb_setup:
                    if bbb_setup["out_nominal"] is None:
                        bbb_setup["out_nominal"] = tuple(
                            [None for i in range(len(self.bbb_outn))]
                        )
                    else:
                        bbb_cout = bc_Check.bc_array(
                            bc_var=bbb_setup["out_nominal"],
                            bc_atype=[tuple],
                            bc_dtype=[
                                int,
                                float,
                                type(None),
                                np.float64,
                                np.int64,
                            ],
                            bc_vname='bbb_setup["out_nominal"]',
                            bc_dlen=len(self.bbb_outn),
                            bc_subs=tuple(
                                [None for i in range(len(self.bbb_outn))]
                            ),
                        )
                        if bbb_cout["error"]:
                            bbb_setup["out_nominal"] = bbb_cout["subs"]
                            self.bbb_addlg(bbb_cout["log"])

                else:
                    bbb_setup["out_nominal"] = tuple(
                        [None for i in range(len(self.bbb_outn))]
                    )

                # checar opção de não usar kdd
                if "nokdd" in bbb_setup:
                    bbb_cout = bc_Check.bc_inset(
                        bc_var=bbb_setup["nokdd"],
                        bc_vname='bbb_setup["nokdd"]',
                        bc_dval=[False, True],
                        bc_subs=bbb_dstp["nokdd"],
                    )
                    if bbb_cout["error"]:
                        self.bbb_addlg(bbb_cout["log"])
                        bbb_setup["nokdd"] = bbb_dstp["nokdd"]
                else:
                    bbb_setup["nokdd"] = bbb_dstp["nokdd"]

            #######################################################################

            # try:
            self.bbb_setup = bbb_setup

            for i in self.bbb_outn:
                if i in self.bbb_setup["special_preprocessing"]:
                    self.__bbb_inv = False
                    break

            self.bbb_dsspl = bbb_setup["dataset_split"]
            self.bbb_onom = bbb_setup["out_nominal"]
            self.__bbb_sprep = bbb_setup["special_preprocessing"]

            self.__bbb_ds, self.__bbb_dsinf = bdm_DtMn.bdm_ids(
                bdm_dsraw=bbb_dsraw,
                bdm_cvar=self.bbb_cvar,
            )

            # checagem intermediária
            ###################################################################

            # checar se o dataset continua tendo tamanho suficiente
            bbb_cout = bc_Check.bc_dslen(
                bc_ds=self.__bbb_ds,
                bc_dlen=(3 * bbb_mdsln[0], 3 * bbb_mdsln[1]),
                bc_vname="bbb_ds",
            )
            if bbb_cout["error"]:
                self.bbb_addlg(bbb_cout["log"])
                self.__bbb_ds = None
                return

            # checar se o dataset tem entradas/saídas constantes
            bbb_cout = bc_Check.bc_dsvar(
                bc_ds=self.__bbb_ds,
                bc_outn=self.bbb_outn,
                bc_vname="bbb_ds",
            )
            self.bbb_addlg(bbb_cout["log"])
            if bbb_cout["error"]:
                self.__bbb_ds = None
                return
            ###################################################################

            bbb_dfs = bdm_DtMn.bdm_dfpar(
                bdm_df=self.bbb_ds,
                bdm_dsspl=self.bbb_setup["dataset_split"],
                bdm_type=self.bbb_setup["dataset_split_type"],
                bdm_dint=self.bbb_setup["ds_gran_interval"],
            )

            self.__bbb_trnds, self.__bbb_valds, self.__bbb_tstds = bbb_dfs

            # checar partições
            ###################################################################

            bbb_names = ["bbb_trnds", "bbb_valds", "bbb_tstds"]
            for (bbb_num, bbb_par) in enumerate(bbb_dfs):

                # checar se o dataset continua tendo tamanho suficiente
                if bbb_names[bbb_num] != "bbb_tstds":
                    bbb_cout = bc_Check.bc_dslen(
                        bc_ds=bbb_par,
                        bc_dlen=(bbb_mdsln[0], bbb_mdsln[1]),
                        bc_vname=bbb_names[bbb_num],
                    )
                    if bbb_cout["error"]:
                        self.bbb_addlg(bbb_cout["log"])
                        self.__bbb_ds = None
                        return

                # checar se o dataset tem entradas/saídas constantes
                bbb_cout = bc_Check.bc_dsvar(
                    bc_ds=bbb_par,
                    bc_outn=self.bbb_outn,
                    bc_vname=bbb_names[bbb_num],
                )
                self.bbb_addlg(bbb_cout["log"])
                if bbb_cout["error"]:
                    self.__bbb_ds = None
                    return

            ###################################################################

            self.bbb_prepx, self.bbb_pcolx = bdm_DtMn.bdm_gettr(
                bdm_vars=self.bbb_inn,
                bdm_scale=self.bbb_setup["scale"],
                bdm_range=self.bbb_setup["range"],
                bdm_sprep=self.bbb_setup["special_preprocessing"],
                bdm_trnds=self.bbb_trnds,
            )

            self.bbb_prepy, self.bbb_pcoly = bdm_DtMn.bdm_gettr(
                bdm_vars=self.bbb_outn,
                bdm_scale=self.bbb_setup["scale"],
                bdm_range=self.bbb_setup["range"],
                bdm_sprep=self.bbb_setup["special_preprocessing"],
                bdm_trnds=self.bbb_trnds,
            )

            if len(self.bbb_pcoly) != 1:
                raise ValueError(
                    "As opções de pré-processamento"
                    + "apresentam como consequência mais de uma saída."
                )

            self.bbb_prepy = self.bbb_prepy.transformers[0][1]

            self.__bbb_isdp = True
            self.bbb_addlg(bbb_s="Modelo preparado para treinamento.")

        except Exception as ex:
            self.bbb_addlg(str(ex))
            return

    def bbb_fit(self, bbb_model, bbb_grid=None, bbb_sscr="mae", **kwargs):
        """Treina o modelo (uso interno)."""

        try:
            # checar entrada
            #######################################################################
            # self.bbb_regmt(bbb_methd="bbb_fit", **kwargs)

            bbb_cout = bc_Check.bc_isdp(self)
            if bbb_cout["error"]:
                self.bbb_addlg(bbb_cout["log"])
                return
            #######################################################################

            bbb_fdict = {
                "r2": "r2",
                "mae": "neg_mean_absolute_error",
                "mdae": "neg_median_absolute_error",
            }
            bbb_sscr = bbb_fdict[bbb_sscr]

            bbb_m = Pipeline(
                steps=[
                    ("preprocess", self.bbb_prepx),
                    ("m", bbb_model),
                ]
            )

            if bbb_grid is not None:

                self.__bbb_gsp = bbb_grid
                bbb_tgrid = []

                for bbb_d in bbb_grid:
                    bbb_td = bdm_DtMn.bdm_tdict(
                        bdm_mtype=self.bbb_mtype,
                        bdm_dict=bbb_d,
                    )
                    if (
                        self.bbb_mtype == "Gradient Boosting Regression"
                        and "init" in bbb_td
                    ):
                        for (bm_i, bm_j) in enumerate(bbb_td["init"]):
                            bbb_td["init"][bm_i] = bm_j.bbb_model
                    bbb_tgrid.append(bbb_td)

                bbb_pgrid = [{} for i in bbb_tgrid]

                for (i, j) in enumerate(bbb_tgrid):
                    for key in j:
                        bbb_pgrid[i]["m__" + key] = j[key]

                bbb_m = GridSearchCV(
                    estimator=bbb_m,
                    param_grid=bbb_pgrid,
                    scoring=bbb_sscr,
                    cv=3,
                )
                # print(bbb_m.get_params().keys())

            # tomar a partição de treinamento
            try:
                bm_x, bm_y = bdm_DtMn.bdm_splxy(
                    self.bbb_trnds, self.bbb_inn, self.bbb_outn
                )
                self.bbb_prepx.fit(bm_x)
                bm_y = self.bbb_prepy.fit_transform(bm_y)

                bbb_m.fit(bm_x, bm_y)

            except FitFailedWarning as bbb_err:
                self.bbb_elog(FitFailedWarning, bbb_err)
                self.bbb_addlg("Erro durante treinamento, abortando bbb_fit")
                return

            if bbb_grid is not None:
                self.bbb_model = bbb_m.best_estimator_
                bbb_gsr = pd.DataFrame(bbb_m.cv_results_)
                self.__bbb_gsr = bdm_DtMn.bdm_stdgr(self, bbb_gsr)

                self.bbb_param = bdm_DtMn.bdm_tdict(
                    bdm_mtype=self.bbb_mtype,
                    bdm_dict=self.bbb_model["m"].get_params(),
                    bdm_inv=True,
                )
            else:
                self.bbb_model = bbb_m

            # marcar o modelo como treinado
            self.bbb_isfit = True

            # tomando métricas
            # bp_sdf, bp_smry, bp_r2, bp_mae, bp_mdae, bp_maep, bp_mdaep

            bbb_t = bp_Perfm.bp_apred(bp_bbox=self)

            self.bbb_sdf = bbb_t["sdf"]
            self.bbb_smry = bbb_t["smry"]
            self.bbb_r2 = bbb_t["r2"]
            self.bbb_mae = bbb_t["mae"]
            self.bbb_mdae = bbb_t["mdae"]
            self.bbb_maep = bbb_t["maep"]
            self.bbb_mdaep = bbb_t["mdaep"]

            self.bbb_addlg("Modelo treinado.")

        except Exception as ex:
            self.bbb_addlg(str(ex))
            return

    def bbb_trnsx(
        self,
        bbb_x: pd.DataFrame = None,
        **kwargs,
    ) -> Optional[pd.DataFrame]:
        """Transforma um DataFrame de inputs (bbb_x) conforme as opções de
        pré-processamento selecionadas em bbb_pdata."""

        try:

            # checar entrada
            #######################################################################
            self.bbb_regmt(bbb_methd="bbb_trnsx", **kwargs)

            # checar se o modelo foi treinado
            bbb_cout = bc_Check.bc_isfit(self)
            if bbb_cout["error"]:
                self.bbb_addlg(bbb_cout["log"])
                return

            # checar dataframe
            bbb_cout = bc_Check.bc_ds(
                bc_model=self,
                bc_vars=self.bbb_inn,
                bc_dataf=bbb_x,
                bc_clen=False,
                bc_vname="bbb_x",
            )
            if bbb_cout["error"]:
                self.bbb_addlg(bbb_cout["log"])
                return

            #######################################################################

            bbb_x, x_inf = bdm_DtMn.bdm_ids(
                bdm_dsraw=bbb_x,
                bdm_cvar=self.bbb_inn,
            )
            del x_inf

            tx = pd.DataFrame(
                self.bbb_prepx.transform(bbb_x),
                columns=self.bbb_pcolx,
                index=bbb_x.index,
            )

        except Exception as ex:
            self.bbb_addlg(str(ex))
            return

        return tx

    def bbb_trnsy(
        self,
        bbb_y: pd.DataFrame = None,
        **kwargs,
    ) -> Optional[pd.DataFrame]:
        """Transforma um DataFrame de outputs (bbb_y) conforme as opções de
        pré-processamento selecionadas em bbb_pdata."""

        try:

            # checar entrada
            #######################################################################
            self.bbb_regmt(bbb_methd="bbb_trnsy", **kwargs)

            bbb_cout = bc_Check.bc_isfit(self)
            if bbb_cout["error"]:
                self.bbb_addlg(bbb_cout["log"])
                return

            # checar dataframe
            bbb_cout = bc_Check.bc_ds(
                bc_model=self,
                bc_vars=self.bbb_outn,
                bc_dataf=bbb_y,
                bc_clen=False,
                bc_vname="bbb_y",
            )
            if bbb_cout["error"]:
                self.bbb_addlg(bbb_cout["log"])
                return

            #######################################################################

            bbb_y, y_inf = bdm_DtMn.bdm_ids(
                bdm_dsraw=bbb_y,
                bdm_cvar=self.bbb_outn,
            )
            del y_inf

            ty = pd.DataFrame(
                self.bbb_prepy.transform(bbb_y),
                columns=self.bbb_pcoly,
                index=bbb_y.index,
            )

        except Exception as ex:
            self.bbb_addlg(str(ex))
            return

        return ty


    def bbb_sstat(
        self,
        bbb_savef: str = "",
        bbb_ftype: str = "excel",
        bbb_form: bool = False,
        **kwargs,
    ):
        """
        Salva as tabelas geradas em bbb_savef.

        :param bbb_savef: Pasta para salvar as tabelas.
        :param bbb_ftype: Formato para salvar os arquivos ("excel" ou "csv").
        """

        try:

            # checar entrada
            #######################################################################
            self.bbb_regmt(bbb_methd="bbb_sstat", **kwargs)

            bbb_cout = bc_Check.bc_type(bbb_savef, [str], "bbb_savef")
            if bbb_cout["error"]:
                self.bbb_addlg(bbb_cout["log"])
                return

            bbb_cout = bc_Check.bc_inset(
                bc_var=bbb_ftype,
                bc_dval=["excel", "csv"],
                bc_vname="bbb_ftype",
                bc_subs="excel",
            )
            if bbb_cout["error"]:
                bbb_ftype = bbb_cout["subs"]
                self.bbb_addlg(bbb_cout["log"])

            bbb_cout = bc_Check.bc_type(
                bc_var=bbb_form,
                bc_dtype=[bool],
                bc_vname="bbb_form",
                bc_subs=False,
            )
            if bbb_cout["error"]:
                self.bbb_addlg(bbb_cout["log"])
                bbb_form = bbb_cout["subs"]

            bbb_cout = bc_Check.bc_isfit(self)
            if bbb_cout["error"]:
                self.bbb_addlg(bbb_cout["log"])
                return
            #######################################################################

            if bbb_savef != "":
                if bbb_savef[-1] != "/":
                    bbb_savef += "/"

                if not os.path.exists(bbb_savef):
                    os.makedirs(bbb_savef)

            if bbb_form:
                bbb_sdf, bbb_smry = bdm_DtMn.bdm_ftab(self.bbb_sdf, self.bbb_smry)
            else:
                bbb_sdf, bbb_smry = self.bbb_sdf, self.bbb_smry

            bbb_mtrct = self.bbb_mtrct

            bbb_fform = "%.4f"
            # salvar tabelas

            try:
                if bbb_ftype == "excel":

                    with pd.ExcelWriter(bbb_savef + "/stats.xlsx") as writer:
                        bbb_mtrct.to_excel(
                            writer,
                            sheet_name="Métricas",
                            float_format=bbb_fform,
                        )

                        bbb_smry.to_excel(
                            writer,
                            sheet_name="Estatísticas Gerais",
                            float_format=bbb_fform,
                        )
                        bbb_sdf.to_excel(
                            writer,
                            sheet_name="Medições",
                            float_format=bbb_fform,
                        )

                        if self.bbb_compt is not None:
                            self.bbb_compt.to_excel(
                                writer,
                                sheet_name="Modelos",
                                float_format=bbb_fform,
                            )
                        if self.bbb_gsr is not None:
                            self.bbb_gsr.to_excel(
                                writer,
                                sheet_name="Grid Search",
                                float_format=bbb_fform,
                            )

                else:

                    bbb_mtrct.to_csv(
                        bbb_savef + "metrics.csv",
                        float_format=bbb_fform,
                    )
                    bbb_sdf.to_csv(bbb_savef + "stats.csv")
                    bbb_smry.to_csv(bbb_savef + "stats_summary.csv")
                    if self.bbb_gsr is not None:
                        self.bbb_gsr.to_csv(bbb_savef + "grid_search_results.csv")
                    if self.bbb_compt is not None:
                        self.bbb_compt.to_csv(bbb_savef + "models_comparison.csv")

                    self.bbb_addlg('Tabelas salvas em "' + bbb_savef + '".')

            except FileNotFoundError as bbb_err:
                self.bbb_elog(FileNotFoundError, bbb_err)
                self.bbb_addlg('Erro ao salvar tabelas em "' + bbb_savef + '".')
                return

            self.bbb_addlg('Tabelas salvas em "' + bbb_savef + '".')

        except Exception as ex:
            self.bbb_addlg(str(ex))
            return


    def bbb_pred(
        self,
        bbb_x: pd.DataFrame = None,
        bbb_fator: bool = False,
        bbb_noneg: bool = True,
        **kwargs,
    ) -> Optional[pd.DataFrame]:
        """
        Recebe um DataFrame com os inputs e retorna os outputs. Caso haja erro
        não recuperável, retornará None.

        :param bbb_x: DataFrame contendo os inputs necessários para realizar a
        predição, no formato (n_amostras, n_inputs).

        :param bbb_fator: Caso seja igual a True e o valor nominal respectivo
        estiver disponível, retornará a saída como fator de carga.

        :param bbb_noneg: Caso seja igual a True valores negativos das
        predições serão automaticamente convertidos para 0.

        :return: DataFrame contendo as predições (y).
        """

        try:

            self.bbb_addlg("Chamada para predição recebida.")

            # checar entrada
            #######################################################################
            self.bbb_regmt(bbb_methd="bbb_pred", **kwargs)

            bbb_cout = bc_Check.bc_type(
                bc_var=bbb_fator,
                bc_dtype=[bool],
                bc_vname="bbb_fator",
                bc_subs=True,
            )
            if bbb_cout["error"]:
                bbb_fator = bbb_cout["subs"]
                self.bbb_addlg(bbb_cout["log"])

            # checar dataframe
            bbb_cout = bc_Check.bc_ds(
                bc_model=self,
                bc_vars=self.bbb_inn,
                bc_dataf=bbb_x,
                bc_clen=False,
                bc_vname="bbb_x",
            )
            if bbb_cout["error"]:
                self.bbb_addlg(bbb_cout["log"])
                return

            bbb_cout = bc_Check.bc_isfit(self)
            if bbb_cout["error"]:
                self.bbb_addlg(bbb_cout["log"])
                return
            #######################################################################

            bbb_x, x_inf = bdm_DtMn.bdm_ids(
                bdm_dsraw=bbb_x,
                bdm_cvar=self.bbb_inn,
            )
            del x_inf

            bbb_normy = self.bbb_model.predict(bbb_x)
            bbb_normy = bbb_normy.reshape((len(bbb_normy), len(self.bbb_pcoly)))

            if self.bbb_inv:
                bbb_y = self.bbb_prepy.inverse_transform(bbb_normy)
            else:
                bbb_y = bbb_normy

            bbb_y = pd.DataFrame(
                data=bbb_y,
                columns=self.bbb_pcoly,
                index=bbb_x.index,
            )

            if bbb_fator and self.bbb_inv:
                for (i, (j, w)) in enumerate(bbb_y.iteritems()):
                    if self.bbb_onom[i] is not None:
                        bbb_y[j] = w / self.bbb_onom[i]

            if bbb_noneg:
                for (i, (j, w)) in enumerate(bbb_y.iteritems()):
                    bbb_y[j] = bbb_y[j].apply(lambda x: x if x >= 0 else 0)

            self.bbb_addlg("Predição executada com êxito.")

        except Exception as ex:
            self.bbb_addlg(str(ex))
            return

        return bbb_y



    def bbb_stats(self, bbb_form: bool = False, **kwargs):
        """
        Retorna as estatísticas do modelo.

        Retorna as estatísticas do modelo em um dicionário.

        :param bbb_form: Caso o parâmetro bbb_form seja igual a False, serão
        retornados os DataFrames sem formatação (ou seja, em formato numérico),
        mais apropriados para criação de gráficos.

        :return: Dicionário contendo os seguintes elementos:
            'bbb_sdf': DataFrame contendo a comparação das saídas do modelo com
            as Ground Truths, para a partição de validação do dataset passado.
            'bbb_smry': DataFrame contendo as estatísticas descritivas de
            bbb_sdf: erros máximo e mínimo, quartis, IQR etc.
            'bbb_mtrct': DataFrame contendo as métricas calculadas para o modelo.
            'bbb_gsr': DataFrame contendo resultados da Grid Search (retornará
            None caso o modelo não tenha sido treinado por Grid Search).
            'bbb_compt': DataFrame contendo comparando aos outros modelos
            (caso bmm_auto tenha sido utilizado).
        """

        try:

            # checar entrada
            #######################################################################
            self.bbb_regmt(bbb_methd="bbb_stats", **kwargs)

            bbb_cout = bc_Check.bc_type(
                bc_var=bbb_form,
                bc_dtype=[bool],
                bc_vname="bbb_form",
                bc_subs=False,
            )
            if bbb_cout["error"]:
                bbb_form = bbb_cout["subs"]
                self.bbb_addlg(bbb_cout["log"])
                return

            bbb_cout = bc_Check.bc_isfit(self)
            if bbb_cout["error"]:
                self.bbb_addlg(bbb_cout["log"])
                return
            #######################################################################

            if bbb_form:
                bbb_sdf, bbb_smry = bdm_DtMn.bdm_ftab(self.bbb_sdf, self.bbb_smry)
            else:
                bbb_sdf, bbb_smry = self.bbb_sdf, self.bbb_smry

            bbb_s = {
                "bbb_sdf": bbb_sdf,
                "bbb_smry": bbb_smry,
                "bbb_mtrct": self.bbb_mtrct,
            }

            if self.bbb_gsr is not None:
                bbb_s["bbb_gsr"] = self.bbb_gsr
            else:
                bbb_s["bbb_gsr"] = None

            if self.bbb_compt is not None:
                bbb_s["bbb_compt"] = self.bbb_compt
            else:
                bbb_s["bbb_compt"] = None

        except Exception as ex:
            self.bbb_addlg(str(ex))
            return

        return bbb_s

    def bbb_testm(self, bbb_form: bool = False, **kwargs):
        """
        Retorna as estatísticas comparando com a partição de testes.

        AVISO: O mal uso deste método pode acarretar no comprometimento da
        capacidade de reportar problemas de overfitting.

        :param bbb_form: Caso o parâmetro bbb_form seja igual a False, serão
        retornados os DataFrames sem formatação (ou seja, em formato numérico),
        mais apropriados para criação de gráficos.

        :return: Dicionário contendo os seguintes elementos:
            'bbb_tsdf': DataFrame contendo a comparação das saídas do modelo com
            as Ground Truths, para a partição de validação do dataset passado.
            'bbb_tsmry': DataFrame contendo as estatísticas descritivas de
            bbb_sdf: erros máximo e mínimo, quartis, IQR etc.
            'bbb_tr2': Métrica R^2.
        """

        try:
            bbb_mtrcs = {}
            bbb_out = bp_Perfm.bp_apred(bp_bbox=self, bp_df="tst")

            if bbb_out is None:
                return None

            for (i, j) in enumerate(["bbb_tsdf", "bbb_tsmry", "bbb_tr2"]):
                bbb_mtrcs[j] = bbb_out[i]

            if bbb_form:
                bbb_mtrcs["bbb_tsdf"], bbb_mtrcs["bbb_tsmry"] = bdm_DtMn.bdm_ftab(
                    bbb_mtrcs["bbb_tsdf"], bbb_mtrcs["bbb_tsmry"]
                )

        except Exception as ex:
            self.bbb_addlg(str(ex))
            return

        return bbb_mtrcs

    def bbb_addlg(self, bbb_s: str = "", **kwargs):
        """Adiciona a string no log interno (uso interno)."""

        if bbb_s != "":
            # self.__bbb_log += self.bbb_regmt(bbb_methd="bbb_addlg")
            self.__bbb_log += bl_Log.bl_addl(bl_msg=bbb_s, bl_obj=self) + "\n"

    def bbb_regmt(self, bbb_methd: str = "", **kwargs):
        """Registra o uso de métodos (uso interno)."""

        self.__bbb_log += (
            bl_Log.bl_regmt(bl_methd=bbb_methd, bl_obj=self, **kwargs) + "\n"
        )

    def bbb_elog(self, bbb_etype, bbb_err, **kwargs):
        """Registra erros levantados no log (uso interno)."""

        self.__bbb_log += bl_Log.bl_elog(bbb_etype, bbb_err, self) + "\n"
