"""
Título do Projeto: Sistema inteligente para levantamento dos fatores de uso de
cargas elétricas nos FPSOs correlacionados às demandas de produção
Número de registro do Projeto: 5900.0117579.21.9

Back-end: X
Módulo: Machine Learning
Caso de uso:

Versão 0.5:
Adição da classe bmm_MM
Caso de uso:
Data de Início: 02/03/2022
Data de Entrega para Revisão: 01/02/2022
Data de Release: --/--/----
Nome do Responsável: Vitor Hugo Ferreira
Contato: vhferreira@id.uff.br
Desenvolvedor: Daniel Cunha de Araujo Júnior
Contato: dc_junior@id.uff.br
Caso de teste:
Responsável pelo Teste:
Bloco geral de observações importantes:
    Definida a classe bp_MM, cuja funções principais são oferecer
funcionalidades para atender os casos de uso e gerenciar a criação,
carregamento, serialização e comparação de modelos.

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
    Adicionado o módulo bml_mman e a classe bmm_MM. Métodos para salvamento e
carregamento de modelos movidos para a classe bmm_MM. Adicionado o método
bmm_MM.bmm_amdls, que retorna os nomes dos modelos disponíveis. Adicionado o
método bmm_MM.bmm_getm, que retorna um modelo construido conforme requisitado.

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
    Método bp_eval adicionado a bp_Perfm. Método bmm_comp adicionado a bmm_MM.
Método bmm_compt adicionado a bmm_MM. Classe bmm_Dflt adicionada (devolve
valores padrões para os métodos a serem utilizados pelo Front-End). Ajustes
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
    Método argumento bmm_obj do método bmm_gdict convertido para argumento
opcional. Método bmm_getm alterado para opcionalmente já preparar o modelo para
treinamento. Variável bbb_log que contém o log interno de utilização do modelo
adicionada. Método bbb_addl, que adiciona informações ao log, adicionado.
Atualização parcial nos métodos do módulo bml_check de forma a possibilitar o
tratamento de exceções. Type hints parcialmente adicionadas. Adicionado
argumento bmm_name ao método bmm_auto. Progresso parcial no tratamento de
erros. Método bmm_fdflt movido para bml_dtmn. Variável bbb_compt, que segura
os resultados de bmm_auto, adicionada à classe BBox. Progresso parcial na
adição de type hints. Documentação atualizada.
"""
import numpy as np
import pandas as pd
import pickle
import inspect
from typing import Union, Optional, Any, Iterable, Callable


from machine_learning import bml_bbox
from machine_learning.bml_check import bc_Check
from machine_learning import bml_model
from machine_learning import bml_perfm
from machine_learning import bml_dtmn
from machine_learning import bml_log


"""
Define a classe bp_MM, cuja funções principais são oferecer funcionalidades 
para atender os casos de uso e gerenciar a criação, carregamento, serialização 
e comparação de modelos. Define também a classe bmm_Dflt, que objetiva passar
valores default para o Front-End.

Métodos
----------

 Classe bmm_MM:
 
 bmm_amdls: Retorna uma tupla contendo os nomes dos modelos disponíveis.
 bmm_auto: Aplica a funcionalidade de Grid Search a diversos modelos.
 bmm_comp: A partir de uma lista de modelos, retorna o melhor.
 bmm_compt: A partir de uma lista de modelos, retorna uma tabela comparativa.  
 bmm_getm: Retorna o modelo especificado a partir da tag passada.
 bmm_load: Carrega um modelo.
 bmm_save: Salva um modelo.
 
 Classe bmm_Dflt:
 __bmm_gobja: Retorna valores default pré-processados (uso interno).
 bmm_gdict: Retorna um dicionário com os valores default.
 
"""


class bmm_MM:
    """
    Classe bmm_MM, cuja funções principais são oferecer funcionalidades para
    atender os casos de uso e gerenciar a criação, carregamento, serialização
    e comparação de modelos.

    Métodos públicos:

    """

    @staticmethod
    def bmm_save(
        bmm_model: bml_bbox.bbb_BBox, bmm_path: str, **kwargs
    ) -> None:
        """Salva o modelo no caminho especificado"""

        # checar entrada
        #######################################################################
        bml_log.bl_Log.bl_regmt(bl_methd="bmm_save", bl_obj=None, **kwargs)

        bmm_o = bc_Check.bc_class(bmm_model, [bml_bbox.bbb_BBox], "bmm_model")
        if bmm_o["error"]:
            return

        bmm_cout = bc_Check.bc_slpth(bmm_path, "bmm_path")
        if bmm_cout["error"]:
            return
        #######################################################################

        try:
            with open(bmm_path, "wb") as bbb_file:
                pickle.dump(
                    bmm_model, bbb_file, protocol=pickle.HIGHEST_PROTOCOL
                )

        except FileNotFoundError as bmm_err:
            bml_log.bl_Log.bl_elog(FileNotFoundError, bmm_err, bmm_model)

        bmm_model.bbb_addlg(
            bl_msg="".join(['Modelo salvo em "', bmm_path, '".']),
            bl_obj=bml_model,
        )

    @staticmethod
    def bmm_load(bmm_path: bml_bbox.bbb_BBox, **kwargs) -> bml_bbox.bbb_BBox:
        """Carrega o modelo no caminho especificado."""

        # checar entrada
        #######################################################################
        bml_log.bl_Log.bl_regmt(bl_methd="bmm_load", bl_obj=None, **kwargs)

        bmm_cout = bc_Check.bc_slpth(bmm_path, "bmm_path")
        if bmm_cout["error"]:
            return
        #######################################################################

        try:
            with open(bmm_path, "rb") as bdm_file:
                bmm_model = pickle.load(bdm_file)

        except FileNotFoundError as bmm_err:
            bml_log.bl_Log.bl_elog(FileNotFoundError, bmm_err)

        bmm_model.bbb_addlg('Modelo carregado de "' + bmm_path + '".')
        return bmm_model

    @staticmethod
    def bmm_amdls(**kwargs) -> tuple:
        """Retorna uma tupla contendo os nomes dos modelos disponíveis."""

        bml_log.bl_Log.bl_regmt(bl_methd="bmm_amdls", bl_obj=None, **kwargs)

        bmm_mdls = (
            "Multilayer Perceptron",
            "Multivariate Regression",
            "Support-Vector Machine",
            "Gradient Boosting Regression",
            "Random Forest Regression",
            "Ridge Regression",
            "Decision Tree Regression",
        )

        return bmm_mdls

    @staticmethod
    def bmm_getm(
        bmm_tag: str = "Multivariate Regression",
        bmm_name: str = None,
        bmm_inn: tuple = None,
        bmm_outn: tuple = None,
        bmm_build: bool = False,
        bmm_pdata: dict = None,
        bmm_fit: dict = None,
        **kwargs,
    ) -> bml_bbox.bbb_BBox:
        """
        Retorna o modelo especificado a partir da tag passada. Caso bmm_build
        seja igual a True e as variáveis bmm_pdata e bmm_fit não sejam
        passadas, acusará erro.

        :param bmm_tag: Tag referente ao modelo desejado.
        :param bmm_name: Nome do modelo a ser criado.
        :param bmm_inn: Tupla contendo o nome das variáveis de entrada.
        :param bmm_outn: Tupla contendo o nome da variável de saída.
        :param bmm_build: True se o modelo já deve ser preparado para uso.
        :param bmm_pdata: Dicionário contendo as entradas do método bbb_pdata.
        :param bmm_fit: Dicionário contendo as entradas do método bm_fit.

        :return: Modelo.
        """

        bmm_mdls = {
            "Multilayer Perceptron": bml_model.bm_MLP,
            "Multivariate Regression": bml_model.bm_MVR,
            "Support-Vector Machine": bml_model.bm_SVM,
            "Gradient Boosting Regression": bml_model.bm_GBR,
            "Random Forest Regression": bml_model.bm_RFR,
            "Ridge Regression": bml_model.bm_RDG,
            "Decision Tree Regression": bml_model.bm_DTR,
        }

        # checar entrada
        #######################################################################
        bml_log.bl_Log.bl_regmt(bl_methd="bm_getm", bl_obj=None, **kwargs)

        bmm_o = bc_Check.bc_inset(
            bc_var=bmm_tag,
            bc_dval=list(bmm_mdls),
            bc_vname="bmm_tag",
            bc_subs="Multivariate Regression",
        )
        #######################################################################
        if bmm_o["error"]:
            bmm_tag = bmm_o["subs"]

        bmm_m = bmm_mdls[bmm_tag](
            bm_name=bmm_name,
            bm_inn=bmm_inn,
            bm_outn=bmm_outn,
        )

        if bmm_o["error"]:
            bmm_m.bbb_addlg(bmm_o["log"])

        if bmm_build:
            bmm_m.bbb_pdata(**bmm_pdata)
            bmm_m.bm_fit(**bmm_fit)

        return bmm_m

    @staticmethod
    def bmm_comp(
        bmm_list: Iterable, bmm_metrc: str = "mae", **kwargs
    ) -> bml_bbox.bbb_BBox:
        """
        A partir de uma lista de modelos passada, retorna o melhor segundo a
        métrica escolhida.

        :param bmm_list: Lista contendo os modelos a serem comparados.
        :param bmm_metrc: Métrica escolhida.

        :return: Modelo escolhido.
        """

        bml_log.bl_Log.bl_regmt(bl_methd="bmm_comp", bl_obj=None, **kwargs)

        if bmm_metrc == "r2":
            bmm_order = max
        else:
            bmm_order = min

        bmm_best = bmm_order(
            bmm_list,
            key=lambda x: bml_perfm.bp_Perfm.bp_eval(
                bp_model=x,
                bp_metrc=bmm_metrc,
                bp_log=False,
            ),
        )
        bml_log.bl_Log.bl_regmt("bp_eval")

        return bmm_best

    @staticmethod
    def bmm_compt(
        bmm_list: Iterable, bmm_nstyle: str = "name", **kwargs
    ) -> pd.DataFrame:
        """
        Retorna um DataFrame apresentado métricas para cada modelo da lista
        passada.

        :param bmm_list: Lista contendo os modelos a serem comparados.
        :param bmm_nstyle: Tipo de nomenclatura utilizada na construção da
        tabela.

        :return: DataFrame.
        """

        bml_log.bl_Log.bl_regmt(bl_methd="bmm_compt", bl_obj=None, **kwargs)

        if bmm_nstyle == "type":
            bmm_names = [i.bbb_mtype for i in bmm_list]
        else:
            bmm_names = [i.bbb_name for i in bmm_list]
            if len(bmm_names) != len(set(bmm_names)):
                bmm_names = ["model_" + str(i) for i in range(len(bmm_list))]

        bmm_df = []
        bmm_allm = ["r2", "mae", "mdae", "maep", "mdaep"]
        for (i, m) in enumerate(bmm_list):

            bmm_gmtcs = lambda x: bml_perfm.bp_Perfm.bp_eval(
                bp_model=m,
                bp_metrc=x,
                bp_log=False,
            )
            bmm_df.append([*map(bmm_gmtcs, bmm_allm)])

        bmm_allm = [bmm_i.upper().replace("P", " %") for bmm_i in bmm_allm]

        bmm_df = pd.DataFrame(data=bmm_df, columns=bmm_allm, index=bmm_names)

        return bmm_df

    @staticmethod
    def bmm_auto(
        bmm_inn: tuple = None,
        bmm_outn: tuple = None,
        bmm_avail: Union[tuple, str] = (
            "Multilayer Perceptron",
            "Support-Vector Machine",
            "Random Forest Regression",
            "Ridge Regression",
            "Gradient Boosting Regression",
        ),
        bmm_dsraw: pd.DataFrame = None,
        bmm_setup: dict = None,
        bmm_grids: dict = None,
        bmm_metrc: str = "mae",
        bmm_name: str = "",
        **kwargs,
    ) -> tuple:
        """
        Aplica a funcionalidade de Grid Search a diversos modelos e retorna o
        melhor.

        :param bmm_inn: Tupla contendo os inputs.
        :param bmm_outn: Tupla contendo o output.
        :param bmm_avail: Tupla contendo tags dos modelos a serem testados.
        Caso seja igual a "all", todos os modelos disponíveis serão testados.
        :param bmm_dsraw: DataFrame referente a base de dados.
        :param bmm_setup: Dicionário contendo o setup de pré-processamento.
        :param bmm_metrc: Métrica utilizada para comparar os modelos.
        :param bmm_grids: Dicionário relacionando cada tipo de modelo
        declarado em bmm_avail com a respectiva lista de dicionários de
        parâmetros para busca em grid.
        :param bmm_name: Nome do modelo (equipamento) a ser criado.

        :return: Tupla contendo o modelo selecionado e a tabela de
        comparação.
        """

        bml_log.bl_Log.bl_regmt(bl_methd="bmm_auto", bl_obj=None, **kwargs)

        if bmm_avail == "all":
            bmm_avail = bmm_MM.bmm_amdls()

        if bmm_grids is None:
            bmm_grids = {}
            for bmm_mname in bmm_avail:
                bmm_grids[bmm_mname] = None
        else:
            for bmm_mname in bmm_avail:
                if bmm_mname not in bmm_grids:
                    bmm_grids[bmm_mname] = None

        bmm_mdls = []

        if bmm_name != "":
            bmm_name += " "

        for bmm_mname in bmm_avail:

            bmm_model = bmm_MM.bmm_getm(
                bmm_tag=bmm_mname,
                bmm_name=bmm_name,
                bmm_inn=bmm_inn,
                bmm_outn=bmm_outn,
            )

            bml_log.bl_Log.bl_addl(f"Criando modelo {bmm_mname}", bmm_model)

            bmm_model.bbb_pdata(
                bbb_dsraw=bmm_dsraw,
                bbb_setup=bmm_setup,
            )

            # if bmm_model.bbb_trnds is not None:
            #     print(
            #         "train:",
            #         len(bmm_model.bbb_trnds),
            #         "val:",
            #         len(bmm_model.bbb_valds),
            #         "test:",
            #         len(bmm_model.bbb_tstds),
            #     )

            bmm_model.bm_fitgs(
                bm_grid=bmm_grids[bmm_mname],
                bm_score=bmm_metrc,
            )

            if bmm_model.bbb_isfit:
                bmm_mdls.append(bmm_model)

                bml_log.bl_Log.bl_addl(
                    bl_msg="".join(
                        [
                            "Modelo ",
                            bmm_mname,
                            " treinado:\n",
                            bmm_model.bbb_info(),
                        ]
                    ),
                    bl_obj=bmm_model,
                )

        if bmm_mdls == []:
            return None, None

        bmm_best = bmm_MM.bmm_comp(
            bmm_list=bmm_mdls,
            bmm_metrc=bmm_metrc,
        )

        bmm_df = bmm_MM.bmm_compt(
            bmm_list=bmm_mdls,
            bmm_nstyle="type",
        )

        bmm_best.bbb_compt = bmm_df.copy()

        bml_log.bl_Log.bl_addl(
            bl_msg="".join(["Resultados de bmm_auto:\n", str(bmm_df)]),
        )

        bml_log.bl_Log.bl_addl(
            bl_msg="".join(
                ["Melhor modelo encontrado: \n", bmm_best.bbb_info()]
            ),
            bl_obj=bmm_best,
        )

        return bmm_best, bmm_df


class bmm_Dflt:
    """
    Classe que objetiva retornar valores Default.

    Métodos Privados:
       __bmm_gobja

    Métodos Públicos:
        bmm_gdict, bmm_gopt
    """

    @staticmethod
    def __bmm_gobja(bmm_obj: object) -> dict:
        """Retorna o valores default pré-processados dos métodos do objeto.
        (uso interno)"""

        if isinstance(bmm_obj, bml_bbox.bbb_BBox):
            bmm_sarg = {
                bmm_obj.bbb_pdata: {
                    "bbb_setup": {
                        "scale": "minmax",
                        "range": (-1, 1),
                        "special_preprocessing": {},
                        "dataset_split": (0.6, 0.2, 0.2),
                        "dataset_split_type": "granular",
                        "ds_gran_interval": (2, 100),
                        "out_nominal": tuple(
                            [None for i in range(len(bmm_obj.bbb_outn))]
                        ),
                        "nokdd": True,
                    }
                },
            }

            if isinstance(bmm_obj, bml_model.bm_MLP):
                if bmm_obj.bbb_pcolx is None:
                    bmm_n = len(bmm_obj.bbb_inn)
                else:
                    bmm_n = len(bmm_obj.bbb_pcolx)

                bmm_sarg[bmm_obj.bm_fit] = {
                    "bm_hlyr": 2 * bmm_n + 1,
                }
                bmm_sarg[bmm_obj.bm_fitgs] = {
                    "bm_grid": {
                        "hidden_layer_sizes": [2 * bmm_n + 1, 10, 50],
                        "activation": ["relu", "tanh"],
                        "learning_rate_init": [0.01, 0.001],
                        "max_iter": [2000],
                        "batch_size": [200],
                        "tol": [1e-4, 1e-5],
                        "n_iter_no_change": [100],
                        "epsilon": [1e-7],
                    }
                }
            elif isinstance(bmm_obj, bml_model.bm_SVM):
                bmm_sarg[bmm_obj.bm_fitgs] = {
                    "bm_grid": [
                        {
                            "kernel": [
                                "linear",
                                "rbf",
                                "poly",
                            ],
                            "C": [5, 3, 1],
                            "epsilon": [0.1, 0.5, 1],
                        }
                    ],
                }

            elif isinstance(bmm_obj, bml_model.bm_MVR):
                pass
            elif isinstance(bmm_obj, bml_model.bm_GBR):
                bmm_sarg[bmm_obj.bm_fitgs] = {
                    "bm_grid": [
                        {
                            "n_estimators": [10, 50],
                            "learning_rate": [0.1, 0.2],
                            "criterion": [
                                "squared_error",
                                "friedman_mse",
                            ],
                        },
                    ],
                }

            elif isinstance(bmm_obj, bml_model.bm_RFR):
                bmm_sarg[bmm_obj.bm_fitgs] = {
                    "bm_grid": [
                        {
                            "n_estimators": [10, 50],
                            "max_depth": [1, 3, 5],
                            "criterion": [
                                "absolute_error",
                                "squared_error",
                            ],
                        },
                    ],
                }

            elif isinstance(bmm_obj, bml_model.bm_RDG):
                bmm_sarg[bmm_obj.bm_fitgs] = {
                    "bm_grid": [{"alpha": [0.0, 0.1, 0.25, 0.5, 1]}],
                }

            elif isinstance(bmm_obj, bml_model.bm_DTR):
                bmm_sarg[bmm_obj.bm_fitgs] = {
                    "bm_grid": [
                        {
                            "max_depth": [1, 3, 5],
                            "criterion": [
                                "absolute_error",
                                "squared_error",
                                "friedman_mse",
                            ],
                        },
                    ],
                }

        return bmm_sarg

    @staticmethod
    def bmm_gdict(
        bmm_f: Callable,
        bmm_obj: Optional[object] = None,
        **kwargs,
    ) -> dict:
        """
        Retorna um dicionário com os valores default do método.

        :param bmm_f: Método
        :param bmm_obj: Objeto sobre o qual se chama o método.


        :return: Dicionário com os parâmetros default do método.
        """

        bml_log.bl_Log.bl_regmt(bl_methd="bmm_gdict", bl_obj=None, **kwargs)

        # tomar o dicionário com os valores default
        bmm_dict = bml_dtmn.bdm_DtMn.bdm_fdflt(bmm_f)

        # tomar os valores default especiais
        if bmm_obj is not None:
            bmm_sarg = bmm_Dflt.__bmm_gobja(bmm_obj)

            if bmm_f in bmm_sarg:
                for bmm_arg in bmm_sarg[bmm_f]:
                    bmm_dict[bmm_arg] = bmm_sarg[bmm_f][bmm_arg]

        return bmm_dict

    @staticmethod
    def bmm_gopt(bmm_f: Callable, **kwargs) -> Union[dict, None]:
        """
        Retorna um dicionário que contém uma lista dos valores disponíveis para
        cada argumento categórico de bmm_f.

        :param bmm_f: Método

        :return: Dicionário
        """

        bml_log.bl_Log.bl_regmt(bl_methd="bmm_gopt", bl_obj=None, **kwargs)

        try:
            bmm_func = bmm_f.__func__
            bmm_clss = bmm_f.__self__.__class__

        except:
            return None

        bmm_ssets = {
            "fitgs": [
                bml_model.bm_MLP.bm_fitgs,
                bml_model.bm_SVM.bm_fitgs,
                bml_model.bm_MVR.bm_fitgs,
                bml_model.bm_GBR.bm_fitgs,
                bml_model.bm_RFR.bm_fitgs,
                bml_model.bm_RDG.bm_fitgs,
                bml_model.bm_DTR.bm_fitgs,
            ],
        }

        if bmm_func in bmm_ssets["fitgs"]:
            bmm_func = "fitgs"

        bmm_metrc = ["r2", "mae", "mdae"]
        bmm_setup = {
            "scale": ["standard", "minmax", "none"],
            "special_preprocessing": {
                "Nome da variável para processamento especial": {
                    "transformer": [
                        "kbins",
                        "bin",
                        "binning",
                    ],
                },
            },
            "dataset_split_type": ["granular", "simple"],
        }

        bmm_dict = {
            bml_model.bm_MLP.bm_fit: {
                "bm_actvn": ["identity", "logistic", "tanh", "relu"],
            },
            bml_model.bm_SVM.bm_fit: {
                "bm_krnel": ["linear", "poly", "rbf", "sigmoid"],
            },
            bml_model.bm_MVR.bm_fit: {},
            bml_model.bm_GBR.bm_fit: {
                "bm_crite": ["friedman_mse", "squared_error"],
            },
            bml_model.bm_RFR.bm_fit: {
                "bm_crite": ["squared_error", "absolute_error", "poisson"],
            },
            bml_model.bm_RDG.bm_fit: {},
            bml_model.bm_DTR.bm_fit: {
                "bm_crite": [
                    "squared_error",
                    "friedman_mse",
                    "absolute_error",
                    "poisson",
                ],
            },
            "fitgs": {
                "bm_score": bmm_metrc,
            },
            bml_bbox.bbb_BBox.bbb_pdata: {"bbb_setup": bmm_setup},
            bml_bbox.bbb_BBox.bbb_sstat: {
                "bbb_ftype": ["excel", "csv"],
            },
            bmm_MM.bmm_getm: {
                "bmm_tag": [
                    "Multilayer Perceptron",
                    "Multivariate Regression",
                    "Support-Vector Machine",
                    "Gradient Boosting Regression",
                    "Random Forest Regression",
                    "Ridge Regression",
                    "Decision Tree Regression",
                ],
                "bmm_pdata": [],
            },
            bmm_MM.bmm_comp: {
                "bmm_metrc": bmm_metrc,
            },
            bmm_MM.bmm_compt: {
                "bmm_nstyle": ["name", "type"],
            },
            bmm_MM.bmm_auto: {
                "bmm_avail": [
                    "all",
                    "Multilayer Perceptron",
                    "Multivariate Regression",
                    "Support-Vector Machine",
                    "Gradient Boosting Regression",
                    "Random Forest Regression",
                    "Ridge Regression",
                    "Decision Tree Regression",
                ],
                "bmm_metrc": bmm_metrc,
                "bmm_setup": bmm_setup,
            },
            bml_perfm.bp_Perfm.bp_eval: {
                "bp_metrc": bmm_metrc,
            },
            bml_perfm.bp_Perfm.bp_apred: {
                "bp_df": [
                    "trn",
                    "val",
                    "tst",
                    "(instância de um pd.DataFrame)",
                ],
            },
        }

        return bmm_dict[bmm_func]
