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
Adicionado o método bdm_ftab.

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
    Padronização dos nomes de variáveis e argumentos dos métodos de
bdm_DtMn. Ajustes nas docstrings refletindo as alterações.

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
    Adicionados métodos para salvar modelos. Adicionado método para carregar
modelos. Adicionado comentário explicando a não padronização dos imports de
bml_dtmn.

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
    Removido o parâmetro bdm_normt da classe bdm_DtMn. Métodos de bdm_DtMn
convertidos para métodos estáticos. Classe bdm_DtMn separada nas classes
bp_Perfm e bdm_DtMn (para tomada de métricas do modelo e manipulações gerais de
dados). Instanciamento da classe bdm_DtMn em bbb_BBox removido.

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
    Atualização na descrição da classe bdm_DtMn. Métodos para salvamento e
carregamento de modelos movidos para a classe bmm_MM.

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
    Adicionado código em bml_dtmn para ignorar aviso caso um DataFrame tenha
shape (n_samples, 1) ao inves de (n_samples,). Alterado o formato padrão dos
dados (treinamento, predição etc) de NumPy para DataFrame, conforme
padronização do projeto. Parâmetro bbb_normt removido. Passagem de Métodos
bdm_nds, bdm_dnorm e bdm_norm removidos. Adicionados atributos bbb_pcolx e
bbb_pcoly, que guardam listas contendo os nomes das colunas para apresentação
do pré-processamento. Atualização ao método bdm_ids adicionando flexibilidade
para permitir testes independentes do módulo de KDD ou respeitar as divisões de
escopo estabelecidas conforme necessidade (será atualizado futuramente).
Adicionado "else" statement caso select_columns for igual a False em bdm_ids.
Variáveis chn_variables (diversos) e add_time (bdm_ids) removidas (não mais
necessárias). Método bdm_gettr adicionado, que gera os preprocessadores.
Adicionadas estratégias de préprocessamento de variáveis: conversão de
intervalos, normalização, binning, discretização kbins e binarização.
Alterações nos métodos envolvendo atividades de préprocessamento
refletindo alterações no fluxo de dados: leitura inicial do dataframe passado,
preprocessamento, predição/treinamento. Atualização no método de
particionamento do DataFrame para treinamento, validação e teste: métodos
bdm_dfpar, bdm_dfsim, bdm_dfgrn, bdm_gdiv adicionados, possibilitando a divisão
das partições de forma granular (cada partição cobrirá o mesmo horizonte de
tempo que o DataFrame original). Opções de pré-processamento de variáveis
temporais adicionadas: days_since_start e months_since_start. Ajustes gerais na
documentação do módulo.

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
    Type hints parcialmente adicionadas. Métodos bdm_mlsk e bdm_tdict
adicionados. Progresso parcial no tratamento de erros. Método bmm_fdflt movido
para bml_dtmn. Documentação atualizada.
"""

from math import isclose
import warnings
import datetime as dt
import inspect
from typing import Union, Any, Optional, Iterable, Callable


import pandas as pd
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import (
    MinMaxScaler,
    LabelBinarizer,
    StandardScaler,
    Binarizer,
    KBinsDiscretizer,
)
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.exceptions import (
    DataConversionWarning,
    ConvergenceWarning,
    FitFailedWarning,
)
# from onedal.datatypes.validation import DataConversionWarning as OnDcWarning

"""
Define a classe bdm_DtMn, que objetiva oferecer utilitários que auxiliam na 
manipulação dados (para utilização interna).

Métodos
----------

 bdm_dfgrn: Particiona o DataFrame de forma granular
 bdm_dfpar: Particiona um DataFrame
 bdm_dfsim: Particiona o DataFrame de forma simples
 bdm_gdiv: Retorna o menor divisor de um número
 bdm_ftab: Formata um objeto DataFrame e sua descrição para apresentação
 bdm_gettr: Gera transformadores conforme opções
 bdm_ids: Leitura inicial da base de dados
 bdm_splxy: Separa um dataframe em x e y apropriados
 bdm_fdflt: Extrai valores default do método passado.

"""

# ignorar aviso se o array tiver shape (n_samples, 1) ao invés de (n_samples,)
warnings.filterwarnings(action="ignore", category=DataConversionWarning)
# warnings.filterwarnings(action="ignore", category=OnDcWarning)
warnings.filterwarnings(action="ignore", category=FutureWarning)

# ignorar aviso que o modelo não está convergindo bem
warnings.filterwarnings(action="ignore", category=ConvergenceWarning)
warnings.filterwarnings(action="error", category=FitFailedWarning)


# pd.set_option("display.max_columns", None)
# pd.set_option("display.max_colwidth", None)
# pd.set_option("display.width", None)
pd.set_option("display.precision", 4)


class bdm_DtMn:
    """
    Classe que engloba funções utilitárias de manipulação dados.

    Métodos públicos:
         bdm_dfgrn, bdm_dfpar, bdm_dfsim, bdm_gdiv, bdm_ftab, bdm_gettr,
         bdm_ids, bdm_splxy
    """

    @staticmethod
    def bdm_gettr(
        bdm_vars: tuple,
        bdm_scale: str = "minmax",
        bdm_range: tuple = (-1, 1),
        bdm_sprep: dict = None,
        bdm_trnds: pd.DataFrame = None,
    ):
        """
        Gera transformadores conforme opções.

        :param bdm_vars: Nomes das variáveis.
        :param bdm_scale: Estratégia de conversão de escala/normalização.
        :param bdm_range: Intervalo da conversão de escala.
        :param bdm_sprep: Opções especiais de pré-processamento.
        :param bdm_trnds: Partição de treinamento do dataset.

        :return: Tupla contendo transformadores e nomes para colunas.
        """

        if bdm_scale == "standard":
            bbb_sc = StandardScaler()

        elif bdm_scale == "none":
            bbb_sc = SimpleImputer(strategy="constant", add_indicator=True)

        elif bdm_scale == "minmax":
            bbb_sc = MinMaxScaler(feature_range=(bdm_range[0], bdm_range[1]))

        else:
            bbb_sc = MinMaxScaler(feature_range=(-1, 1))

        # para binning
        bdm_baseb = {
            "hour": 24,
            "day": 31,
            "month": 12,
            "day_of_week": 7,
            "week_of_year": 54,
        }
        bdm_vbins = {}

        bbb_nx = []  # nomes das variáveis numéricas
        bbb_sx = []  # nomes das variáveis especiais
        bbb_sxpl = []  # pipelines das variáveis especiais

        # separar as variáveis em numéricas e especiais
        for bbb_var in bdm_vars:
            if bbb_var not in bdm_sprep:
                # se for uma variável comum (numérica), colocar em bbb_nx
                bbb_nx.append(bbb_var)
            else:
                # se não, colocar em bbb_sx
                bbb_sx.append(bbb_var)

                # tomar o preprocessamento escolhido
                if bdm_sprep[bbb_var]["transformer"] == "kbins":
                    bbb_tr = KBinsDiscretizer(
                        n_bins=bdm_sprep[bbb_var]["n_bins"],
                        # encode="onehot-dense",
                        encode="ordinal",
                        strategy=bdm_sprep[bbb_var]["strategy"],
                    )
                    bbb_prepr = Pipeline(steps=[("kbins", bbb_tr)])

                # elif bdm_sprep[bbb_var]["transformer"] == "disc":
                #     bbb_tr = KBinsDiscretizer(
                #         n_bins=bdm_sprep[bbb_var]["n_bins"],
                #         encode="ordinal",
                #         strategy=bdm_sprep[bbb_var]["strategy"],
                #     )
                #     bbb_prepr = Pipeline(steps=[("disc", bbb_tr)])

                elif bdm_sprep[bbb_var]["transformer"] == "bin":
                    bbb_tr = Binarizer(
                        threshold=bdm_sprep[bbb_var]["threshold"]
                    )
                    bbb_prepr = Pipeline(steps=[("bin", bbb_tr)])

                elif bdm_sprep[bbb_var]["transformer"] == "binning":
                    if bbb_var in bdm_baseb:
                        bdm_vbins[bbb_var] = bdm_baseb[bbb_var]
                    else:
                        bdm_vbins[bbb_var] = min(
                            1000, len(bdm_trnds[bbb_var].unique())
                        )

                    bbb_tr = KBinsDiscretizer(
                        n_bins=bdm_vbins[bbb_var],
                        encode="onehot-dense",
                        strategy="uniform",
                    )
                    bbb_prepr = Pipeline(steps=[("binning", bbb_tr)])

                elif bdm_sprep[bbb_var]["transformer"] == "none":
                    bbb_prepr = SimpleImputer(strategy="constant")

                # guardar
                bbb_sxpl.append((bbb_var, bbb_prepr, [bbb_var]))

        bbb_trnfs = []
        if bbb_nx != []:
            # transformador das variáveis numéricas
            bbb_nxtrs = Pipeline(steps=[("scaler", bbb_sc)])

            bbb_trnfs.append(("numeric", bbb_nxtrs, bbb_nx))
        if bbb_sx != []:
            # transformador(es) das variáveis especiais
            bbb_sxtrs = ColumnTransformer(transformers=bbb_sxpl)

            bbb_trnfs.append(("special", bbb_sxtrs, bbb_sx))

        bbb_prepx = ColumnTransformer(transformers=bbb_trnfs)

        # nomes para colunas para exibição do resultado do preprocessamento
        bbb_pcol = [*bbb_nx]
        for bbb_var in bbb_sx:
            if bdm_sprep[bbb_var]["transformer"] == "kbins":
                for bbb_i in range(bdm_sprep[bbb_var]["n_bins"]):
                    bbb_pcol.append(bbb_var + "_kbins_" + str(bbb_i))
            elif bdm_sprep[bbb_var]["transformer"] == "bin":
                bbb_pcol.append(bbb_var + "_bin")
            elif bdm_sprep[bbb_var]["transformer"] == "binning":
                for bbb_i in range(bdm_vbins[bbb_var]):
                    bbb_pcol.append(bbb_var + "_binning_" + str(bbb_i))
            elif bdm_sprep[bbb_var]["transformer"] == "disc":
                bbb_pcol.append(bbb_var + "_disc")

        return bbb_prepx, bbb_pcol

    @staticmethod
    def bdm_ids(
        bdm_dsraw: pd.DataFrame,
        bdm_cvar: tuple,
    ):
        """
        Formata informações temporais, seleciona colunas (variáveis de
        interesse). Se necessário, remove linhas com valores 'Bad',
        troca virgula por ponto e converte as variáveis para float64.

        :param bdm_dsraw: DataFrame.
        :param bdm_cvar: Colunas de interesse.

        :return: Tupla contendo o DataFrame e sua descrição.
        """

        bdm_ds = pd.DataFrame(index=bdm_dsraw.index)
        # bdm_ds.index = bdm_dsraw.index

        # time
        bdm_tvars = (
            "hour",
            "day",
            "month",
            "year",
            "day_of_week",
            "week_of_year",
            "days_since_start",
            "months_since_start",
        )

        bdm_ctime = []
        bdm_timev = False
        for i in bdm_tvars:
            if i in bdm_cvar:
                bdm_timev = True
                bdm_ctime.append(i)

        if "index" in bdm_dsraw:
            # as variáveis temporais serão tomadas de "index"
            bdm_findx = True
        else:
            # as variáveis temporais serão tomadas já prontas do dataset
            bdm_findx = False

        if bdm_timev:

            if bdm_findx:
                # bdm_ds["full_date"] = [
                #     pd.Timestamp(dt.datetime.strptime(d, "%d/%m/%Y %H:%M:%S"))
                #     for d in bdm_dsraw["index"]
                # ]

                bdm_ds["full_date"] = pd.to_datetime(
                    bdm_dsraw["index"],
                    format="%d/%m/%Y %H:%M:%S",
                )

                if "hour" in bdm_ctime:
                    bdm_ds["hour"] = [
                        pd.Timestamp(d).hour for d in bdm_ds["full_date"]
                    ]

                if "day" in bdm_ctime:
                    bdm_ds["day"] = [
                        pd.Timestamp(d).day for d in bdm_ds["full_date"]
                    ]

                if "month" in bdm_ctime:
                    bdm_ds["month"] = [
                        pd.Timestamp(d).month for d in bdm_ds["full_date"]
                    ]

                if "year" in bdm_ctime:
                    bdm_ds["year"] = [
                        pd.Timestamp(d).year for d in bdm_ds["full_date"]
                    ]

                if "day_of_week" in bdm_ctime:
                    bdm_ds["day_of_week"] = [
                        pd.Timestamp(d).dayofweek for d in bdm_ds["full_date"]
                    ]

                if "week_of_year" in bdm_ctime:
                    bdm_ds["week_of_year"] = [
                        pd.Timestamp(d).weekofyear for d in bdm_ds["full_date"]
                    ]

                if "days_since_start" in bdm_ctime:
                    bdm_start = bdm_ds["full_date"].iloc[0]
                    bdm_ds["days_since_start"] = [
                        (d - bdm_start).days for d in bdm_ds["full_date"]
                    ]

                if "months_since_start" in bdm_ctime:
                    bdm_start = bdm_ds["full_date"].iloc[0]
                    bdm_ds["months_since_start"] = [
                        int((d - bdm_start).days / 30)
                        for d in bdm_ds["full_date"]
                    ]

                bdm_ds = bdm_ds.drop(columns="full_date")

            else:
                for i in bdm_ctime:
                    bdm_ds[i] = bdm_dsraw.loc[:, [i]]

        # passar colunas de interesse para o dataset principal
        for i in bdm_cvar:
            if i not in bdm_ctime:
                bdm_ds[i] = bdm_dsraw.loc[:, [i]]

        # Tratamento das variáveis
        ## Trocar virgulas por pontos (Excel em portugues...)
        bdm_ds = bdm_ds.replace(",", ".", regex=True)
        ## Trocar 'Bad' por NaN
        bdm_ds = bdm_ds.replace("Bad", np.nan)
        ## Remover NaN do dataset
        bdm_ds = bdm_ds.loc[bdm_ds.notna().all(1)]
        ## passar os valores para numericos
        bdm_ds = bdm_ds.astype("float64")

        # normalizar e tirar as estatisticas destritivas basicas
        bdm_dsinf = bdm_ds.describe()

        # padronizar ordem das colunas
        bdm_ds = bdm_ds[list(bdm_cvar)]

        return bdm_ds.copy(), bdm_dsinf.copy()

    @staticmethod
    def bdm_splxy(bdm_data: pd.DataFrame, bdm_inn: tuple, bdm_outn: tuple):
        """
        Recebe um dataframe e os nomes dos inputs e output e
        os separa o dataframe em x e y apropriados.

        :param bdm_data: DataFrame.
        :param bdm_inn: Nomes dos Inputs.
        :param bdm_outn: Nome do Output.

        :return: Tupla (x,y)
        """

        bdm_x = bdm_data[list(bdm_inn)]
        bdm_y = bdm_data[list(bdm_outn)]

        return bdm_x, bdm_y

    @staticmethod
    def bdm_dfpar(
        bdm_df: pd.DataFrame,
        bdm_dsspl: tuple = (0.6, 0.2, 0.2),
        bdm_type: str = "simple",
        bdm_dint: tuple = (2, 100),
    ):
        """
        Particiona o DataFrame conforme o método requisitado.

        :param bdm_df: DataFrame.
        :param bdm_dsspl: Percentuais das partições.
        :param bdm_type: Estratégia de particionamento.
        :param bdm_dint: Intervalo de busca do melhor intervalo de divisão.

        :return: Tupla contendo os DataFrames das partições.
        """

        if bdm_type == "simple":
            bdm_dfs = bdm_DtMn.bdm_dfsim(
                bdm_df=bdm_df,
                bdm_dsspl=bdm_dsspl,
            )

        if bdm_type == "granular":
            bdm_dfs = bdm_DtMn.bdm_dfgrn(
                bdm_df=bdm_df,
                bdm_dsspl=bdm_dsspl,
                bdm_dint=bdm_dint,
            )

        return bdm_dfs

    @staticmethod
    def bdm_dfsim(bdm_df: pd.DataFrame, bdm_dsspl: tuple = (0.6, 0.2, 0.2)):
        """
        Particiona o DataFrame de forma simples.

        :param bdm_df: DataFrame.
        :param bdm_dsspl: Percentuais das partições.

        :return: Tupla contendo os DataFrames das partições.
        """

        bdm_trndf = bdm_df.iloc[0 : int(bdm_dsspl[0] * len(bdm_df))]
        bdm_valdf = bdm_df.iloc[
            int(bdm_dsspl[0] * len(bdm_df)) : int(
                (bdm_dsspl[0] + bdm_dsspl[1]) * len(bdm_df)
            )
        ]
        bdm_tstdf = bdm_df.iloc[
            int((bdm_dsspl[0] + bdm_dsspl[1]) * len(bdm_df)) :
        ]

        return bdm_trndf, bdm_valdf, bdm_tstdf

    @staticmethod
    def bdm_dfgrn(
        bdm_df: pd.DataFrame,
        bdm_dsspl: tuple = (0.6, 0.2, 0.2),
        bdm_dint: tuple = (2, 100),
    ):
        """
        Particiona o DataFrame de forma granular.

        :param bdm_df: DataFrame.
        :param bdm_dsspl: Percentuais das partições.
        :param bdm_dint: Intervalo de busca do melhor intervalo de divisão.

        :return: Tupla contendo os DataFrames das partições.
        """

        bdm_dflen = len(bdm_df)

        bdm_div = bdm_DtMn.bdm_gdiv(
            bdm_dflen=bdm_dflen,
            bdm_dsspl=bdm_dsspl,
            bdm_dint=bdm_dint,
        )

        bdm_intvl = [round(j * bdm_div) for j in bdm_dsspl]

        bdm_trndf = pd.DataFrame(columns=bdm_df.columns)
        bdm_valdf = pd.DataFrame(columns=bdm_df.columns)
        bdm_tstdf = pd.DataFrame(columns=bdm_df.columns)

        for (idx, row) in bdm_df.iterrows():
            if idx % bdm_div < bdm_intvl[0]:
                bdm_trndf.loc[idx] = row

            elif idx % bdm_div < bdm_intvl[0] + bdm_intvl[1]:
                bdm_valdf.loc[idx] = row

            else:
                bdm_tstdf.loc[idx] = row

        return bdm_trndf, bdm_valdf, bdm_tstdf

    @staticmethod
    def bdm_gdiv(
        bdm_dflen: int,
        bdm_dsspl: tuple,
        bdm_dint: tuple = (2, 100),
    ):
        """
        Retorna o menor divisor de um número cujas divisões pelas
        porcentagens passadas seja inteira dentro do intervalo.

        :param bdm_dflen: Número.
        :param bdm_dsspl: Percentuais.
        :param bdm_dint: Intervalo de busca do divisor.

        :return: Divisor.
        """

        bdm_done = False
        bdm_k = 0
        while not bdm_done:
            for bdm_div in range(bdm_dint[0], bdm_dint[1] + 1):
                if isclose(bdm_dflen % bdm_div, 0, abs_tol=1e-4):

                    bdm_done = all(
                        [
                            isclose((bdm_div * j) % 1, 0, abs_tol=1e-4)
                            for j in bdm_dsspl
                        ]
                    )

                    if bdm_done:
                        break

            if bdm_done:
                break
            bdm_dflen -= 1
            bdm_k += 1
            if bdm_k > 3:
                bdm_div = 100
                break

        return bdm_div

    @staticmethod
    def bdm_ftab(bdm_df: pd.DataFrame, bdm_info: pd.DataFrame):
        """
        Formata um objeto DataFrame e sua descrição (pd.DataFrame().describe())
        para apresentação, retornando ambos formatados.

        :param bdm_df: DataFrame.
        :param bdm_info: DataFrame equivalente a data.describe().

        :return: Tupla "(bdm_df, bdm_info)" contendo os DataFrames devidamente
        formatados.
        """

        bdm_dff = bdm_df.loc[:, :].astype("object")
        bdm_infof = bdm_info.loc[:, :].astype("object")

        bdm_infof.loc["count"] = bdm_infof.loc["count"].map("{:.0f}".format)

        for i in bdm_dff.iteritems():
            bdm_dff.loc[:, i[0]] = bdm_dff[i[0]].map("{:.4f}".format)
            bdm_infof.loc["mean":"IQR", i[0]] = bdm_infof.loc[
                "mean":"IQR", i[0]
            ].map("{:.4f}".format)
        bdm_dff = bdm_dff.astype("str")
        bdm_infof = bdm_infof.astype("str")

        return bdm_dff, bdm_infof

    @staticmethod
    def bdm_mlsk(bdm_tag: str, bdm_inv: bool = False) -> dict:
        """
        Retorna um dicionário que traduz a nomenclatura de hiperparâmetros
        do pacote para a nomenclatura do scikit-learn.
        """

        bdm_mlp = {
            "bm_hlyr": "hidden_layer_sizes",
            "bm_actvn": "activation",
            "bm_lrate": "learning_rate_init",
            "bm_maxit": "max_iter",
            "bm_tol": "tol",
            "bm_bsize": "batch_size",
            "bm_ninc": "n_iter_no_change",
        }

        bdm_mvr = {}

        bdm_svm = {
            "bm_krnel": "kernel",
            "bm_epsil": "epsilon",
            "bm_c": "C",
        }

        bdm_gbr = {
            "bm_bmdl": "init",
            "bm_nesti": "n_estimators",
            "bm_lr": "learning_rate",
            "bm_crite": "criterion",
            "bm_mdep": "max_depth",
        }

        bdm_rfr = {
            "bm_nesti": "n_estimators",
            "bm_mdep": "max_depth",
            "bm_mleaf": "max_leaf_nodes",
            "bm_crite": "criterion",
        }

        bdm_rdg = {"bm_alpha": "alpha"}

        bdm_dtr = {
            "bm_mdep": "max_depth",
            "bm_mleaf": "max_leaf_nodes",
            "bm_crite": "criterion",
        }

        bdm_dtags = {
            "Multilayer Perceptron": bdm_mlp,
            "Multivariate Regression": bdm_mvr,
            "Support-Vector Machine": bdm_svm,
            "Gradient Boosting Regression": bdm_gbr,
            "Random Forest Regression": bdm_rfr,
            "Ridge Regression": bdm_rdg,
            "Decision Tree Regression": bdm_dtr,
        }

        bdm_dict = bdm_dtags[bdm_tag]

        if bdm_inv:
            bdm_dict = {bdm_v: bdm_k for bdm_k, bdm_v in bdm_dict.items()}

        return bdm_dict

    @staticmethod
    def bdm_tdict(bdm_mtype: str, bdm_dict: dict, bdm_inv: bool = False):
        """Traduz um dicionário de parâmetros."""

        bdm_kdic = bdm_DtMn.bdm_mlsk(bdm_tag=bdm_mtype, bdm_inv=bdm_inv)

        bdm_tdict = {}
        for bdm_i in bdm_dict:
            if bdm_i in bdm_kdic:
                bdm_tdict[bdm_kdic[bdm_i]] = bdm_dict[bdm_i]

        return bdm_tdict

    @staticmethod
    def bdm_stdgr(bdm_model, bdm_gsr: pd.DataFrame):
        """Padroniza a tabela de resultados da Grid Search."""

        bdm_drop = [
            "mean_fit_time",
            "std_fit_time",
            "mean_score_time",
            "std_score_time",
            "params",
        ]
        bdm_gsr.drop(columns=bdm_drop, inplace=True)
        bdm_cols = [
            bdm_i.replace("param_m__", "") for bdm_i in bdm_gsr.columns
        ]
        bdm_tdic = bdm_DtMn.bdm_mlsk(bdm_model.bbb_mtype, bdm_inv=True)

        for (bdm_i, bdm_j) in enumerate(bdm_cols):
            if bdm_j in bdm_tdic:
                bdm_cols[bdm_i] = bdm_tdic[bdm_j]
            else:
                bdm_cols[bdm_i] = (
                    bdm_j.replace("split", "K-fold ")
                    .replace("_test_score", " Score")
                    .title()
                )

        bdm_gsr.columns = bdm_cols

        for (i, j) in bdm_gsr.iteritems():
            if "Score" in i:
                if j.min() < 0:
                    bdm_gsr[i] = bdm_gsr[i].abs()

        return bdm_gsr

    @staticmethod
    def bdm_fdflt(bmm_f: Callable) -> dict:
        """Retorna um dicionário com os valores default dos argumentos
        opcionais passados."""

        bmm_sign = inspect.signature(bmm_f)
        return {
            k: v.default
            for k, v in bmm_sign.parameters.items()
            if v.default is not inspect.Parameter.empty
        }
