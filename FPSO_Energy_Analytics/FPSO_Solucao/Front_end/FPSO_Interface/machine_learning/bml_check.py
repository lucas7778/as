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
Adicionado o método bc_class.

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
    Padronização dos nomes de variáveis e argumentos em bc_Check. Ajustes nas
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
    Ajustes na string retornada em bc_outn. Métodos de bc_Check convertidos
para métodos estáticos.

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
    Adicionado método bc_isfit em bc_Check para checar se o modelo pode ser
usado para atividades que requerem treinamento. Adicionado parâmetro bbb_isfit
que contém informações a respeito do status de treinamento do modelo. Parâmetro
bbb_isdp adicionado a classe bbb_BBox: informa se o modelo está pronto para ser
treinado. Ajustes gerais na documentação do módulo.

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
    Atualização parcial nos métodos do módulo bml_check de forma a possibilitar
o tratamento de exceções. Type hints parcialmente adicionadas. Progresso
parcial no tratamento de erros. Progresso parcial no tratamento de erros.
Método bc_schek adicionado. Métodos bc_range, bc_svar, bc_pintn adicionados.
Método bc_array atualizado. Rotinas de controle de entrada de hiperparâmetros
atualizada. Error catching geral adicionado em bbb_fit, bbb_pdata, bbb_trnsx,
bbb_trnsy, bbb_pred, bbb_sstat. Progresso parcial no controle de entrada
(rotinas para checagem do dataset e partições atualizadas). Progresso parcial
na adição de type hints. Adição do controle de entrada do método bbb_pdata
concluido. Documentação atualizada.
"""

from math import isclose
from typing import Optional, Any, Union
import pandas as pd
import numpy as np

from machine_learning.bml_log import bl_Log

"""
Define a classe bc_Check, que objetiva oferecer utilitários que auxiliam na 
detecção de erros de utilização dos métodos e funções do pacote (para 
utilização interna).

Métodos
----------
    bc_array: Checa se o array fornecido é pertinente
    bc_bound: Checa se a variável (numérica) respeita a condição desejada.
    bc_c: Checa se o valor de C é pertinente. 
    bc_class: Checa se a classe da variável passada é pertinente.
    bc_ds: Checa se o dataset passado é pertinente.
    bc_dscol: Checa se o dataframe contém as colunas passadas.
    bc_dslen: Checa se o tamanho do dataframe é pertinente.
    bc_dsspl: Checa se a tupla fornecida para divisão de datasets é pertinente.
    bc_dsvar: Checa se o dataset apresenta colunas constantes.
    bc_epsil: Checa se o valor de epsilon é pertinente.
    bc_isbc: Checa se o modelo foi instanciado corretamente.
    bc_isdp: Checa se o modelo já teve seu dataset preparado. 
    bc_isfit: Checa se o modelo já foi treinado.
    bc_inset: Checa se o valor da variável pertence ao conjunto esperado.
    bc_naint: Checa se a variável pode representar um número inteiro positivo.
    bc_pintn: Checa uma variável é um número inteiro positivo ou None.
    bc_outn: Checa se o número de outputs é compatível com o modelo.
    bc_pfrac: Checa se a variável está contida no intervalo (0,1].
    bc_range: Checa se um range é pertinente.
    bc_schek: Retorna referências às rotinas de controle de entrada.
    bc_svar: Checa se as opções de pré-processamento especial são pertinentes.
    bc_type: Checa se o tipo da variável passada é pertinente.
"""


class bc_Check:
    """
    Classe de utilitários que auxiliam na detecção de erros de utilização
    (controle de entrada) do pacote (para utilização interna).

    Métodos públicos:
        bc_array, bc_bound, bc_c, bc_class, bc_ds, bc_dscol, bc_dslen,
        bc_dsspl, bc_dsvar, bc_epsil, bc_isbc, bc_isdp, bc_isfit, bc_inset,
        bc_naint, bc_pintn, bc_outn, bc_pfrac, bc_range, bc_schek, bc_svar,
        bc_type.
    """

    @staticmethod
    def __bc_gcout(
        bc_raise: bool,
        bc_subs: Any,
        bc_log: str,
        bc_etype=ValueError,
    ) -> dict:
        """Retorna o dicionario de saída (uso interno)."""

        try:
            if bc_raise:
                raise bc_etype(bc_log)

        except bc_etype as bc_err:
            bl_Log.bl_elog(bc_etype, bc_err)

        if bc_subs is not None:
            if not isinstance(bc_subs, pd.DataFrame):
                bc_log += " Revertendo para " + str(bc_subs) + "."
        else:
            bc_log += " Abortando operação."

        bc_cout = {
            "error": bc_raise,
            "log": bc_log,
            "subs": bc_subs,
        }

        return bc_cout

    @staticmethod
    def bc_bound(
        bc_var: Any,
        bc_sym: str,
        bc_bound: Union[int, float],
        bc_vname: str,
        bc_subs: Optional[Any] = None,
    ) -> dict:
        """
        Checa se a variável (numérica) respeita a condição desejada. Se
        respeitar, retorna a própria variável. Se não respeitar e o parâmetro
        bc_subs tenha sido passado, retorna bc_subs. Se não respeitar e o
        parâmetro bc_subs não tenha sido passado, acusa ValueError.

        :param bc_var: float, int
            Variável a comparar.
        :param bc_sym: str
            Tipo de comparação (deve ser igual a "==", "!=", ">=", ">" etc).
        :param bc_bound: float, int
            Lado direito da comparação. O valor sobre o qual a variável deve
            ser maior, menor, igual etc.
        :param bc_vname: str
            Nome da variável.

        :return: Dicionário contendo resultado da checagem.

        """

        bc_raise: bool = False

        if bc_sym == ">=":
            if bc_var < bc_bound:
                bc_raise = True

        elif bc_sym == "<=":
            if bc_var > bc_bound:
                bc_raise = True

        elif bc_sym == "==":
            if bc_var != bc_bound:
                bc_raise = True

        elif bc_sym == "!=":
            if bc_var == bc_bound:
                bc_raise = True

        elif bc_sym == ">":
            if bc_var <= bc_bound:
                bc_raise = True

        elif bc_sym == "<":
            if bc_var >= bc_bound:
                bc_raise = True

        bc_str = (
            "Condição não respeitada: "
            + bc_vname
            + " "
            + bc_sym
            + " "
            + str(bc_bound)
            + "."
        )

        bc_cout = bc_Check.__bc_gcout(
            bc_raise=bc_raise,
            bc_subs=bc_subs,
            bc_log=bc_str,
            bc_etype=ValueError,
        )

        return bc_cout

    @staticmethod
    def bc_type(
        bc_var: Any,
        bc_dtype: list,
        bc_vname: str,
        bc_subs: Optional[Any] = None,
    ) -> dict:
        """
        Checa se o tipo da variável passada é pertinente. Se não for, acusa
        TypeError.

        :param bc_var: Variável as ser checada.
        :param bc_dtype: Tipos (type(var)) aceitos. Deve ser uma lista.
        :param bc_vname: Nome da varíavel. Deve uma string contendo o nome
        declarado no código.
        """

        bc_raise = False
        if type(bc_var) not in bc_dtype:
            bc_raise = True

        bc_str = "O tipo de " + bc_vname + " deve pertencer ao conjunto {"
        for bc_i in bc_dtype:
            bc_str += str(bc_i) + ", "
        bc_str = bc_str[:-2] + "}."

        bc_cout = bc_Check.__bc_gcout(
            bc_raise=bc_raise,
            bc_subs=bc_subs,
            bc_log=bc_str,
            bc_etype=TypeError,
        )

        return bc_cout

    @staticmethod
    def bc_inset(
        bc_var: Any,
        bc_dval: list,
        bc_vname: str,
        bc_subs: Optional[Any] = None,
    ) -> dict:
        """
        Checa se o valor da variável está contida no array desired_values. Se
        não estiver, acusa ValueError.

        :param bc_var: Variável as ser checada.
        :param bc_dval: Valores aceitos. Deve ser uma lista.
        :param bc_vname: Nome da variável. Deve uma string contendo o nome
        declarado no código.
        :param bc_subs: Valor a substituto, caso o checado não seja pertinente.

        """

        bc_raise = False
        bc_log = ""
        if bc_var not in bc_dval:
            bc_raise = True
            bc_log += bc_vname + " deve ser igual a: " + str(set(bc_dval))

        bc_cout = bc_Check.__bc_gcout(
            bc_raise=bc_raise,
            bc_subs=bc_subs,
            bc_log=bc_log,
            bc_etype=ValueError,
        )
        return bc_cout

    @staticmethod
    def bc_array(
        bc_var: Any,
        bc_atype: list,
        bc_dtype: list,
        bc_vname: str,
        bc_dlen: int = None,
        bc_subs: Optional[Any] = None,
    ) -> dict:
        """
        Checa se o array fornecido é pertinente, primeiramente o array em si e
        posteriormente item a item. Opcionalmente checa se o tamanho do array é
        pertinente, ao se passar o parâmetro 'desired_len'. Se qualquer dos
        casos não forem satisfeitos, acusará o tipo de erro pertinente.

        :param bc_var: Variável as ser checada.
        :param bc_atype: Tipos (type(var)) aceitos para o array. Deve ser
        uma lista.
        :param bc_dtype: Tipos (type(var[i])) aceitos para os itens do
        array. Deve ser uma lista.
        :param bc_vname: Nome da variável. Deve uma string contendo o nome
        declarado no código.
        :param bc_dlen: Tamanho desejado do array.
        """

        # checar o tipo do array (tupla, lista etc)
        bc_cout = bc_Check.bc_type(
            bc_var=bc_var,
            bc_dtype=bc_atype,
            bc_vname=bc_vname,
            bc_subs=bc_subs,
        )
        if bc_cout["error"]:
            return bc_cout

        # checar o tamanho
        bc_raise = False
        bc_log = ""
        if bc_dlen is not None:
            if len(bc_var) != bc_dlen:
                bc_raise = True
                bc_log = (
                    "O array "
                    + bc_vname
                    + " deve ter dimensão ("
                    + str(bc_dlen)
                    + ",)"
                )
        bc_cout = bc_Check.__bc_gcout(
            bc_raise=bc_raise,
            bc_subs=bc_subs,
            bc_log=bc_log,
            bc_etype=ValueError,
        )
        if bc_cout["error"]:
            return bc_cout

        # checar itens
        bc_raise = False
        bc_log = ""
        for (i, j) in enumerate(bc_var):
            if type(j) not in bc_dtype:
                bc_raise = True
                bc_log += str(i) + ", "

        if bc_raise:
            bc_log = (
                "Os itens {"
                + bc_log[:-2]
                + "} do array não são do tipo esperado."
                + "Os itens de "
                + bc_vname
                + " devem ser do tipo "
                + str(set(bc_dtype))
            )

        bc_cout = bc_Check.__bc_gcout(
            bc_raise=bc_raise,
            bc_subs=bc_subs,
            bc_log=bc_log,
            bc_etype=TypeError,
        )

        return bc_cout

    @staticmethod
    def bc_outn(bbb_outn: list, bbb_mtype: str) -> dict:
        """
        Checa se o número de outputs é compatível com o modelo. Se não for,
        acusa ValueError.

        :param bbb_outn: Array com os outputs.
        :param bbb_mtype: String contendo o tipo do modelo.
        """

        bc_raise = False
        bc_log = ""
        if len(bbb_outn) != 1:
            bc_raise = True
            bc_log = (
                "O modelo "
                + bbb_mtype
                + " só é compatível com 1 output. "
                + "Foram encontrados "
                + str(len(bbb_outn))
                + " outputs. Considere montar um modelo para cada output."
            )

        bc_cout = bc_Check.__bc_gcout(
            bc_raise=bc_raise,
            bc_subs=(bbb_outn[0],),
            bc_log=bc_log,
            bc_etype=ValueError,
        )

        return bc_cout

    @staticmethod
    def bc_class(
        bc_var: Any,
        bc_dclss: list,
        bc_vname: str,
        bc_subs: Any = None,
    ) -> dict:
        """
        Checa se a classe da variável passada é pertinente. Se não for, acusa
        TypeError.

        :param bc_var: Variável as ser checada.
        :param bc_dclss: Classes aceitas. Deve ser uma lista.
        :param bc_vname: Nome da variável. Deve uma string contendo o nome
        declarado no código.

        :return: Dicionário contendo resultado da checagem.
        """

        bc_raise = True

        for i in bc_dclss:
            if isinstance(bc_var, i):
                bc_raise = False

        # if bc_raise:
        #     bc_str = bc_vname + " deve ser uma instancia da classe:\n"
        #     for (i, j) in enumerate(bc_dclss) -> dict:
        #         bc_str += "\t\t\t\t" + str(i + 1) + ".  " + str(j) + "\n"
        #
        #     raise ValueError(bc_str)

        bc_str = bc_vname + " deve ser uma instancia das classes do conjunto {"
        for bc_i in bc_dclss:
            bc_str += str(bc_i) + ", "
        bc_str = bc_str[:-2] + "}."

        bc_cout = bc_Check.__bc_gcout(
            bc_raise=bc_raise,
            bc_subs=bc_subs,
            bc_log=bc_str,
            bc_etype=TypeError,
        )

        return bc_cout

    @staticmethod
    def bc_isfit(bc_model: Any) -> dict:
        """
        Checha se o modelo está pronto para ser utilizado. Se não estiver,
        acusa ValueError.
        """

        bc_raise = False
        bc_log = ""
        if not bc_model.bbb_isfit:
            bc_raise = True
            bc_log = "O modelo não está pronto para ser utilizado."

        bc_cout = bc_Check.__bc_gcout(
            bc_raise=bc_raise,
            bc_subs=None,
            bc_log=bc_log,
            bc_etype=ValueError,
        )

        return bc_cout

    @staticmethod
    def bc_isdp(bc_model: Any) -> dict:
        """Checa se o modelo está pronto para ser treinado."""

        bc_raise = False
        bc_log = ""
        if not bc_model.bbb_isdp:
            bc_raise = True
            bc_log = "O modelo não está pronto para ser treinado."

        bc_cout = bc_Check.__bc_gcout(
            bc_raise=bc_raise,
            bc_subs=None,
            bc_log=bc_log,
            bc_etype=ValueError,
        )

        return bc_cout

    @staticmethod
    def bc_isbc(bc_model: Any) -> dict:
        """Checa se o modelo foi instanciado corretamente."""

        bc_raise = False
        bc_log = ""
        if not bc_model.bbb_isbc:
            bc_raise = True
            bc_log = "O modelo não foi instanciado corretamente."

        bc_cout = bc_Check.__bc_gcout(
            bc_raise=bc_raise,
            bc_subs=None,
            bc_log=bc_log,
            bc_etype=ValueError,
        )

        return bc_cout

    @staticmethod
    def bc_dscol(
        bc_ds: pd.DataFrame,
        bc_vars: tuple,
        bc_vname: str = "bbb_dsraw",
        bc_utvar: bool = False,
    ) -> dict:
        """Checa se o dataframe contém as colunas passadas."""

        bc_tvars = (
            "hour",
            "day",
            "month",
            "year",
            "day_of_week",
            "week_of_year",
            "days_since_start",
            "months_since_start",
        )

        if bc_utvar:
            bc_vars = bc_vars
        else:
            bc_vars = [bc_var for bc_var in bc_vars if bc_var not in bc_tvars]

        # checar se todas as variáveis necessárias estão presentes
        bc_log = ""
        bc_raise = False

        for bc_var in bc_vars:
            if bc_var not in bc_ds.columns:
                bc_raise = True
                bc_log += bc_var + ", "

        if bc_raise:
            bc_log = (
                "Variáveis faltantes no dataset passado em "
                + bc_vname
                + ": "
                + bc_log[:-2]
                + "."
            )

        bc_cout = bc_Check.__bc_gcout(
            bc_raise=bc_raise,
            bc_subs=None,
            bc_log=bc_log,
            bc_etype=ValueError,
        )
        return bc_cout

    @staticmethod
    def bc_dslen(
        bc_ds: pd.DataFrame,
        bc_dlen: tuple = (20, np.inf),
        bc_vname: str = "Dataset",
    ) -> dict:
        """Checa se a quantidade de pontos de dados do dataframe está contida
        no intervalo."""

        bc_cout = bc_Check.bc_bound(
            bc_var=len(bc_ds),
            bc_sym=">=",
            bc_bound=bc_dlen[0],
            bc_vname=bc_vname,
        )
        if bc_cout["error"]:
            return bc_cout

        if bc_dlen[1] == np.inf:
            bc_maxd = len(bc_ds)
        else:
            bc_maxd = bc_dlen[1]

        bc_cout = bc_Check.bc_bound(
            bc_var=len(bc_ds),
            bc_sym="<",
            bc_bound=bc_dlen[1],
            bc_vname="len(" + bc_vname + ")",
            bc_subs=bc_ds[-bc_maxd:],
        )

        # if bc_cout["error"]:
        #     bc_cout["log"] += (
        #         " Alterando para " + str(len(bc_cout["subs"])) + "."
        #     )

        return bc_cout

    @staticmethod
    def bc_dsvar(
        bc_ds: pd.DataFrame,
        bc_outn: tuple,
        bc_vname: str = "dataset",
    ) -> dict:
        """Checa se o dataset apresenta colunas constantes."""

        bc_raise = False
        bc_log = ""
        for (bc_name, bc_col) in bc_ds.iteritems():
            if bc_col.nunique() == 1:
                bc_log += bc_name + ", "
                if bc_name in bc_outn:
                    bc_raise = True

        if bc_log != "":
            bc_log = (
                "Variáveis constantes encontradas em "
                + bc_vname
                + ": "
                + bc_log[:-2]
                + "."
            )

        if bc_raise:
            bc_log += " Abortando operação."

        bc_cout = {
            "error": bc_raise,
            "log": bc_log,
            "subs": None,
        }

        return bc_cout

    @staticmethod
    def bc_ds(
        bc_model: Any,
        bc_dataf: pd.DataFrame,
        bc_vars: tuple,
        bc_vname: str = "bbb_dsraw",
        bc_utvar: bool = False,
        bc_clen: bool = True,
        bc_dlen: tuple = (20, np.inf),
    ) -> dict:
        """
        Checa se o dataset passado é pertinente.
        """

        bc_cout = bc_Check.bc_class(
            bc_var=bc_dataf,
            bc_vname=bc_vname,
            bc_dclss=[pd.DataFrame],
        )
        if bc_cout["error"]:
            return bc_cout

        bc_cout = bc_Check.bc_dscol(
            bc_ds=bc_dataf,
            bc_vars=bc_vars,
            bc_vname=bc_vname,
            bc_utvar=bc_utvar,
        )
        if bc_cout["error"]:
            return bc_cout

        if bc_clen:
            bc_ols = ["Multivariate Regression", "Ridge Regression"]
            if bc_model.bbb_mtype in bc_ols:
                bbb_mind = min(bc_dlen[0], len(bc_model.bbb_inn))
            else:
                bbb_mind = bc_dlen[0]

            bbb_maxd = bc_dlen[1]
        else:
            bbb_mind = 1
            bbb_maxd = np.inf

        bc_cout = bc_Check.bc_dslen(
            bc_ds=bc_dataf,
            bc_dlen=(bbb_mind, bbb_maxd),
            bc_vname=bc_vname,
        )

        return bc_cout

    @staticmethod
    def bc_naint(
        bc_var: Any,
        bc_subs: Optional[int] = None,
        bc_vname: str = "numero",
    ) -> dict:
        """Checa se a variável pode representar um número inteiro positivo."""

        bc_cout = bc_Check.bc_class(
            bc_var=bc_var,
            bc_dclss=[int],
            bc_vname=bc_vname,
            bc_subs=bc_subs,
        )
        if bc_cout["error"]:
            return bc_cout
        else:
            bc_cout = bc_Check.bc_bound(
                bc_var=bc_var,
                bc_sym=">",
                bc_bound=0,
                bc_vname=bc_vname,
                bc_subs=bc_subs,
            )

        return bc_cout

    @staticmethod
    def bc_pintn(
        bc_var: Any,
        bc_subs: Optional[int] = None,
        bc_vname: str = "numero",
    ) -> dict:
        """
        Checa uma variável que pode representar um número inteiro positivo
        ou None.
        """

        bc_cout = bc_Check.bc_class(
            bc_var=bc_var,
            bc_dclss=[int, None.__class__],
            bc_vname=bc_vname,
            bc_subs=bc_subs,
        )
        if bc_cout["error"] or isinstance(bc_var, None.__class__):
            return bc_cout
        else:
            bc_cout = bc_Check.bc_bound(
                bc_var=bc_var,
                bc_sym=">",
                bc_bound=0,
                bc_vname=bc_vname,
                bc_subs=bc_subs,
            )

        return bc_cout

    @staticmethod
    def bc_pfrac(
        bc_var: Any,
        bc_subs: Any = None,
        bc_vname: str = "frac",
        bc_izero: bool = False,
    ) -> dict:
        """Checa se a variável pode representar um valor pertencente ao
        intervalo (0,1], ou opcionalmente, [0,1]."""

        bc_cout = bc_Check.bc_class(
            bc_var=bc_var,
            bc_dclss=[float, int],
            bc_vname=bc_vname,
            bc_subs=bc_subs,
        )
        if bc_cout["error"]:
            return bc_cout

        if bc_izero:
            bc_sym = ">="
        else:
            bc_sym = ">"

        bc_cout = bc_Check.bc_bound(
            bc_var=bc_var,
            bc_sym=bc_sym,
            bc_bound=0,
            bc_vname=bc_vname,
            bc_subs=bc_subs,
        )
        if bc_cout["error"]:
            return bc_cout

        bc_cout = bc_Check.bc_bound(
            bc_var=bc_var,
            bc_sym="<=",
            bc_bound=1,
            bc_vname=bc_vname,
            bc_subs=bc_subs,
        )

        return bc_cout

    @staticmethod
    def bc_epsil(
        bc_var: Union[int, float],
        bc_subs: Optional[float] = None,
        bc_vname: str = "epsilon",
    ) -> dict:
        """Checa se o valor de epsilon é pertinente."""

        bc_cout = bc_Check.bc_class(
            bc_var=bc_var,
            bc_dclss=[int, float],
            bc_vname=bc_vname,
            bc_subs=bc_subs,
        )
        if bc_cout["error"]:
            return bc_cout
        else:
            bc_cout = bc_Check.bc_bound(
                bc_var=bc_var,
                bc_sym=">",
                bc_bound=0,
                bc_vname=bc_vname,
                bc_subs=bc_subs,
            )

        return bc_cout

    @staticmethod
    def bc_c(
        bc_var: Any,
        bc_subs: Optional[float] = None,
        bc_vname: str = "C",
    ) -> dict:
        """Checa se o valor de C é pertinente."""

        bc_cout = bc_Check.bc_class(
            bc_var=bc_var,
            bc_dclss=[int, float],
            bc_vname=bc_vname,
            bc_subs=bc_subs,
        )
        if bc_cout["error"]:
            return bc_cout
        else:
            bc_cout = bc_Check.bc_bound(
                bc_var=bc_var,
                bc_sym=">=",
                bc_bound=0,
                bc_vname=bc_vname,
                bc_subs=bc_subs,
            )

        return bc_cout

    @staticmethod
    def bc_svar(
        bc_var: Any,
        bc_cvars: tuple,
        bc_vname: str = 'bbb_setup["special_preprocessing"]',
    ) -> dict:
        """
        Checa se as variáveis escolhidas para pré-processamento
        especial são pertinentes.
        """

        bc_cout = bc_Check.bc_type(
            bc_var=bc_var,
            bc_dtype=[dict],
            bc_subs={},
            bc_vname=bc_vname,
        )
        if bc_cout["error"]:
            return bc_cout

        bc_raise = False
        bc_log = ""
        bc_subs = {**bc_var}
        for bc_svar in bc_var:
            if bc_svar not in bc_cvars:
                bc_raise = True
                bc_subs.pop(bc_svar)
                bc_log += str(bc_svar) + ", "

        if bc_log != "":
            bc_log = (
                "Variáveis especificadas em "
                + bc_vname
                + " não fazem parte do modelo: "
                + bc_log[:-2]
                + "."
            )

        if bc_var != bc_subs:
            bc_var = {**bc_subs}

        bc_log2 = ""
        for bc_svar in bc_var:
            bc_rem = False
            if "transformer" not in bc_var[bc_svar]:
                bc_rem = True
            elif bc_var[bc_svar]["transformer"] not in [
                "kbins",
                "bin",
                "binning",
                "none",
            ]:
                bc_rem = True

            else:
                if bc_var[bc_svar]["transformer"] == "kbins":
                    if "n_bins" not in bc_var[bc_svar]:
                        bc_rem = True
                    else:
                        bc_o = bc_Check.bc_naint(bc_var[bc_svar]["n_bins"])
                        if bc_o["error"]:
                            bc_rem = True

                    if "strategy" not in bc_var[bc_svar]:
                        bc_rem = True
                    else:
                        bc_o = bc_Check.bc_inset(
                            bc_var=bc_var[bc_svar]["strategy"],
                            bc_dval=["uniform", "quantile", "kmeans"],
                            bc_vname="strategy",
                        )
                        if bc_o["error"]:
                            bc_rem = True

                elif bc_var[bc_svar]["transformer"] == "bin":
                    if "threshold" not in bc_var[bc_svar]:
                        bc_subs[bc_svar]["threshold"] = 0
                    else:
                        bc_o = bc_Check.bc_type(
                            bc_var=bc_var[bc_svar]["threshold"],
                            bc_dtype=[int, float],
                            bc_vname="threshold",
                        )
                        if bc_o["error"]:
                            bc_subs[bc_svar]["threshold"] = 0

                # bc_var[bc_svar]["transformer"] == "binning":

            if bc_rem:
                bc_raise = True
                bc_subs.pop(bc_svar)
                bc_log2 += bc_svar + ", "

        if bc_log2 != "":
            bc_log2 = (
                "Opções de pré-processamento inapropriadas em: {"
                + bc_log2[:-2]
                + "}."
            )

        if bc_log != "":
            bc_log2 = " " + bc_log2

        bc_log = bc_log + bc_log2

        bc_cout = bc_Check.__bc_gcout(bc_raise, bc_subs, bc_log, ValueError)
        return bc_cout

    @staticmethod
    def bc_dsspl(
        bc_var: tuple,
        bc_subs: tuple = (0.6, 0.2, 0.2),
        bc_vname: str = 'bbb_setup["dataset_split"]',
    ) -> dict:
        """Checa se a tupla fornecida para divisão de datasets é pertinente."""

        bc_cout = bc_Check.bc_array(
            bc_var=bc_var,
            bc_atype=[tuple],
            bc_dtype=[float],
            bc_vname=bc_vname,
            bc_subs=bc_subs,
            bc_dlen=3,
        )
        if bc_cout["error"]:
            return bc_cout

        for (bc_i, bc_j) in enumerate(bc_var):
            if bc_i == 2:
                bc_izero = True
            else:
                bc_izero = False

            bc_cout = bc_Check.bc_pfrac(
                bc_var=bc_var[bc_i],
                bc_subs=bc_subs,
                bc_vname=bc_vname + "[" + str(bc_i) + "]",
                bc_izero=bc_izero,
            )
            if bc_cout["error"]:
                break

        if bc_cout["error"]:
            return bc_cout

        if not isclose(sum(bc_var), 1, abs_tol=1e-5):
            bc_log = (
                "A somatório das porcentagens definidas em "
                + bc_vname
                + " deve ser igual a 1."
            )
            bc_cout = bc_Check.__bc_gcout(
                bc_raise=True,
                bc_subs=bc_subs,
                bc_log=bc_log,
            )

        return bc_cout

    @staticmethod
    def bc_range(
        bc_var: tuple,
        bc_subs: Optional[tuple] = None,
        bc_vname: str = 'bbb_setup["range"]',
        bc_rngtp: list = [int, float],
    ) -> dict:
        """Checa se um range é pertinente."""

        bc_cout = bc_Check.bc_array(
            bc_var=bc_var,
            bc_atype=[tuple],
            bc_dtype=bc_rngtp,
            bc_subs=bc_subs,
            bc_vname=bc_vname,
            bc_dlen=2,
        )
        if bc_cout["error"]:
            return bc_cout

        bc_cout = bc_Check.bc_bound(
            bc_var=bc_var[1],
            bc_sym=">",
            bc_bound=bc_var[0],
            bc_vname=bc_vname + "[1]",
            bc_subs=bc_subs,
        )

        return bc_cout

    @staticmethod
    def bc_slpth(bc_var: str, bc_vname: str = "bmm_path") -> dict:
        """Checa se um caminho para salvar/carregar modelos é pertinente."""

        bc_cout = bc_Check.bc_type(bc_var, [str], "bmm_path")
        if bc_cout["error"]:
            return bc_cout

        bc_raise = False
        if len(bc_var) < 6:
            bc_raise = True

        elif bc_var[-5:] != ".bbox":
            bc_raise = True

        bc_cout = bc_Check.__bc_gcout(
            bc_raise=bc_raise,
            bc_subs=None,
            bc_log="Deve ser especificado um arquivo do tipo .bbox",
            bc_etype=ValueError,
        )

        return bc_cout

    @staticmethod
    def bc_schek(
        bc_mtype: str,
        bc_subs: dict,
    ) -> dict:
        """
        Retorna dicionário de funções que envelopa as rotinas de controle de
        entrada para cada variável.
        """

        if bc_mtype == "Multilayer Perceptron":
            bc_chk = {
                # MLP
                "bm_hlyr": lambda bc_var: bc_Check.bc_naint(
                    bc_var=bc_var,
                    bc_subs=bc_subs["bm_hlyr"],
                    bc_vname="bm_hlyr",
                ),
                "bm_actvn": lambda bc_var: bc_Check.bc_inset(
                    bc_var=bc_var,
                    bc_dval=["identity", "logistic", "tanh", "relu"],
                    bc_subs=bc_subs["bm_actvn"],
                    bc_vname="bm_actvn",
                ),
                "bm_lrate": lambda bc_var: bc_Check.bc_pfrac(
                    bc_var=bc_var,
                    bc_subs=bc_subs["bm_lrate"],
                    bc_vname="bm_lrate",
                ),
                "bm_maxit": lambda bc_var: bc_Check.bc_naint(
                    bc_var=bc_var,
                    bc_subs=bc_subs["bm_maxit"],
                    bc_vname="bm_maxit",
                ),
                "bm_tol": lambda bc_var: bc_Check.bc_pfrac(
                    bc_var=bc_var,
                    bc_subs=bc_subs["bm_tol"],
                    bc_vname="bm_tol",
                ),
                "bm_bsize": lambda bc_var: bc_Check.bc_naint(
                    bc_var=bc_var,
                    bc_subs=bc_subs["bm_bsize"],
                    bc_vname="bm_bsize",
                ),
                "bm_ninc": lambda bc_var: bc_Check.bc_naint(
                    bc_var=bc_var,
                    bc_subs=bc_subs["bm_ninc"],
                    bc_vname="bm_ninc",
                ),
            }

        elif bc_mtype == "Support-Vector Machine":
            bc_chk = {
                "bm_krnel": lambda bc_var: bc_Check.bc_inset(
                    bc_var=bc_var,
                    bc_dval=["linear", "rbf", "poly"],
                    bc_subs=bc_subs["bm_krnel"],
                    bc_vname="bm_krnel",
                ),
                "bm_c": lambda bc_var: bc_Check.bc_c(
                    bc_var=bc_var,
                    bc_subs=bc_subs["bm_c"],
                    bc_vname="bm_c",
                ),
                "bm_epsil": lambda bc_var: bc_Check.bc_epsil(
                    bc_var=bc_var,
                    bc_subs=bc_subs["bm_epsil"],
                    bc_vname="bm_epsil",
                ),
            }

        elif bc_mtype == "Gradient Boosting Regression":
            bc_chk = {
                "bm_nesti": lambda bc_var: bc_Check.bc_naint(
                    bc_var=bc_var,
                    bc_subs=bc_subs["bm_nesti"],
                    bc_vname="bm_nesti",
                ),
                "bm_lr": lambda bc_var: bc_Check.bc_pfrac(
                    bc_var=bc_var,
                    bc_subs=bc_subs["bm_lr"],
                    bc_vname="bm_lr",
                ),
                "bm_crite": lambda bc_var: bc_Check.bc_inset(
                    bc_var=bc_var,
                    bc_dval=[
                        "squared_error",
                        "friedman_mse",
                        "absolute_error",
                    ],
                    bc_vname="bm_crite",
                    bc_subs=bc_subs["bm_crite"],
                ),
                "bm_mdep": lambda bc_var: bc_Check.bc_pintn(
                    bc_var=bc_var,
                    bc_subs=bc_subs["bm_mdep"],
                    bc_vname="bm_mdep",
                ),
            }

        elif bc_mtype == "Multivariate Regression":
            bc_chk = {}

        elif bc_mtype == "Random Forest Regression":
            bc_chk = {
                "bm_nesti": lambda bc_var: bc_Check.bc_naint(
                    bc_var=bc_var,
                    bc_subs=bc_subs["bm_nesti"],
                    bc_vname="bm_nesti",
                ),
                "bm_mdep": lambda bc_var: bc_Check.bc_pintn(
                    bc_var=bc_var,
                    bc_subs=bc_subs["bm_mdep"],
                    bc_vname="bm_mdep",
                ),
                "bm_mleaf": lambda bc_var: bc_Check.bc_pintn(
                    bc_var=bc_var,
                    bc_subs=bc_subs["bm_mleaf"],
                    bc_vname="bm_mleaf",
                ),
                "bm_crite": lambda bc_var: bc_Check.bc_inset(
                    bc_var=bc_var,
                    bc_dval=[
                        "squared_error",
                        "friedman_mse",
                        "mse",
                        "absolute_error",
                    ],
                    bc_vname="bm_crite",
                    bc_subs=bc_subs["bm_crite"],
                ),
            }

        elif bc_mtype == "Ridge Regression":
            bc_chk = {
                "bm_alpha": lambda bc_var: bc_Check.bc_pfrac(
                    bc_var=bc_var,
                    bc_subs=bc_subs["bm_alpha"],
                    bc_vname="bm_alpha",
                )
            }

        elif bc_mtype == "Decision Tree Regression":
            bc_chk = {
                "bm_mdep": lambda bc_var: bc_Check.bc_pintn(
                    bc_var=bc_var,
                    bc_subs=bc_subs["bm_mdep"],
                    bc_vname="bm_mdep",
                ),
                "bm_mleaf": lambda bc_var: bc_Check.bc_pintn(
                    bc_var=bc_var,
                    bc_subs=bc_subs["bm_mleaf"],
                    bc_vname="bm_mleaf",
                ),
                "bm_crite": lambda bc_var: bc_Check.bc_inset(
                    bc_var=bc_var,
                    bc_dval=[
                        "squared_error",
                        "friedman_mse",
                        "mse",
                        "absolute_error",
                    ],
                    bc_vname="bm_crite",
                    bc_subs=bc_subs["bm_crite"],
                ),
            }

        else:
            bc_chk = {}

        return bc_chk
