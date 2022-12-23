"""
PEP - Python Enhancement Proposals
    |> São propostas para melhorias para a linguagem Python aceitas mundialmente

    |> A ideia da PEP 8 é que possamos escrever código Python dentro das melhores práticas aprovadas pelo comitê
    mantendedor da linguagem Python. A seguir alguns exemplos - há muito mais consulte o documento.

        [1] - Utilize Camel Case para nomes de Classes
        [2] - Utilize letras minúsculas para nomes de funções e variáveis (use nomes sugestivos) separados por
        underline
        [3] - Utilize quatro espaços para identação -> Atenção são espaços e não TAB
        [4] - Linhas em branco -> A PEP 8 nos indica o número de linhas que devem ficar em branco entre uma ação e outra
        fique atento, se estiver usando o Pycharm ele sempre o avisara a respeito desse processo. Nota, será um aviso,
        não siginfica que terá problemas com a execução -> lembre-se estamos falando de melhores práticas.
        Separar funções e definições de classes com duas linhas em branco. Métodos dentro de uma classe devem ser
        separados com uma única linha em branco
        [5] - Imports -> devem ser sempre feitos em linhas separadas
            Imports devem ser colocados no Topo do arquivo, logo depois do cabeçalho ou de qualquer DocStrings e antes
            de constantes ou variáeis globais
        [6] - Espaços em expressões e instruções
        [7] - Termine sempre uma instrução com uma nova linha

    |> Atenção: estes foram apenas alguns exemplos, há muito mais no documento PEP8
"""
"""
# [1] Camel Case nos momes de Classes

class Calculadora:
    pass


class CalculadoraCientifica:
    pass


# [2] - Utilize letras minúsculas para nomes de funções e variáveis (use nomes sugestivos) separados por underline

def soma():
    pass


def soma_dois():
    pass


numero = 33
numero_par = 48


# [3] - Utilize quatro espaços para identação -> Atenção são espaços e não TAB

if 'b' in 'jaboticaba':  # Correto
    print(f"Encontramos b em jaboticaba")


if 'a' in 'abacate':  # Errado
print(f"Tem a em abacate")



[4] - Linhas em branco -> A PEP 8 nos indica o número de linhas que devem ficar em branco entre uma ação e outra
        fique atento, se estiver usando o Pycharm ele sempre o avisara a respeito desse processo. Nota, será um aviso,
        não siginfica que terá problemas com a execução -> lembre-se estamos falando de melhores práticas


class Classe:  # Erro
    pass
def melao():  # Erro
    pass


# [5] - Imports -> devem ser sempre feitos em linhas separadas

import sys, os # Errado

# import certo

import sys
import os

# Não há problemas em utilizar algo como:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote -> acima de 2 recomenda-se fazer como segue

from types import (
    StringType,
    ListType,
    SetType,
    MaisUmType,
    UltimoType
)


# [6] - Espaços em expressões e instruções
# Não faça

funcao( param[ 1 ], { dic: 1 } ):  # Não deixe os espaços em branco

# Faça assim

funcao(param[1], {dic: 1}):  # É isso

# Não faça

algo ( 1 )

# Faça

algo(1)

# Não faça

dict ['chave'] = list [indice]

# Faça

dict['chave'] = list[indice]

# Não faça

x                     = 4
var                   = 33
variavel_longa_demais = 100

# Faça

x = 4
var = 33
variavel_longa_demais = 100

# [7] - Termine sempre uma instrução com uma nova linha

print(f"Se essa for sua última instrução, deixe uma linha em branco após")
# Esta linha em branco deve estar ao final -> claro sem esses comentários

"""
