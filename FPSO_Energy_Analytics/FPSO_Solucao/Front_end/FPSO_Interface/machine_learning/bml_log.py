"""
Versão 0.x:

Caso de uso:
Data de Início: 30/06/2022
Data de Entrega para Revisão: /2022
Data de Release: --/--/----
Nome do Responsável: Vitor Hugo Ferreira
Contato: vhferreira@id.uff.br
Desenvolvedor: Daniel Cunha de Araujo Júnior
Contato: dc_junior@id.uff.br
Caso de teste:
Responsável pelo Teste: Iahn Igel
Bloco geral de observações importantes:

"""

import os
from math import isclose
from datetime import datetime
from typing import Union, Optional

"""
Define a classe bl_Log, responsável pela criação e manutenção de logs.

Métodos
----------
 bl_addl: Adiciona uma mensagem ao log.
 bl_clog: Limpa o log de uso.
 bl_regmt: Registra uma chamada de método.
 bl_lkw: Registra argumentos inesperados passados aos métodos.
"""


class bl_Log:
    """
    Classe responsável pela criação e manutenção de logs.

    Métodos públicos:
        bl_addl, bl_clog, bl_regmt, bl_lkw

    """

    bl_lpath = "log.txt"
    bl_print = True

    @staticmethod
    def bl_addl(bl_msg: str = "", bl_obj: object = None) -> str:
        """
        Adiciona uma string (bl_msg) ao log, registrando opcionalmente também
        uma referência ao objeto bl_obj (uso interno).
        """

        if bl_obj is None:
            bl_slist = [str(datetime.now()), bl_msg]
        else:
            bl_slist = [str(datetime.now()), str(bl_obj), bl_msg]

        bl_div = " --- "

        bl_str = "".join([i + bl_div for i in bl_slist])
        bl_str = bl_str[: -len(bl_div)]

        with open(bl_Log.bl_lpath, "a") as f:
            f.write(bl_str + "\n")

        if bl_Log.bl_print:
            print(bl_str)

        return bl_str

    @staticmethod
    def bl_clog():
        """Limpa o log de uso."""

        with open(bl_Log.bl_lpath, "w") as f:
            f.write("")

    @staticmethod
    def bl_regmt(bl_methd: str = "", bl_obj: object = None, **kwargs) -> str:
        """
        Registra uma chamada no método bl_methd, e opcionalmente uma
        referência ao objeto bl_obj (uso interno).
        """

        bl_list = ["Chamada no método ", bl_methd, "."]

        if kwargs != {}:
            bl_list.append(bl_Log.bl_lkw(**kwargs))

        bl_str = bl_Log.bl_addl("".join(bl_list), bl_obj=bl_obj)

        return bl_str

    @staticmethod
    def bl_lkw(**kwargs) -> str:
        """
        Adiciona comentários a respeito de variáveis não esperadas
        nos logs (uso interno).
        """

        bl_str = " Argumentos não reconhecidas na chamada: "

        for bl_arg in kwargs:
            bl_str += bl_arg + ", "

        bl_str = bl_str[:-2]
        bl_str += "."

        return bl_str

    @staticmethod
    def bl_elog(bl_etype, bl_err, bl_obj=None) -> str:
        """Adiciona no log erros encontrados."""

        bl_str = bl_Log.bl_addl(
            bl_msg="".join([bl_etype.__qualname__, ": ", str(bl_err)]),
            bl_obj=bl_obj,
        )

        return bl_str
