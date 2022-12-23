import pandas as pd
from pandas import DataFrame as dataFrame
class Eqp_Proc:

    def __init__(self, nome:str, potNominal:float, fP:float, potProc:float, df:dataFrame, varDep:str, varProc:list,
                 fc:float, fi:float, outpredict:float):
        self.nome = nome
        self.potNominal = potNominal
        self.fP = fP
        self.varDep = varDep
        self.varProc = varProc
        self.potProc = potProc
        # essa abordagem pode gerar um grande consumo de memória
        self.df = df

        self.fc = fc
        self.fi = fi
        self.outpredict = outpredict

        self.modelo_nome = None
        self.modelo = None
        self.estProc = None

        self.novo=True

class Subsistema:
    """
    Classe para representar os subsistemas da plataforma. Um subsistemas é definido a partir da união
    de equipamentos previamente criados.
    """

    def __init__(self, nome, eqpsSelected, pot_nom, pot_proc, output, fc, fi, modelo, nome_modelo, df2, varProcs, regime):
        self.nome = nome
        self.eqpsSelected = eqpsSelected
        self.pot_nom = pot_nom
        self.pot_proc = pot_proc
        self.output = output
        self.fc = fc
        self.fi = fi
        self.modelo = modelo
        self.nome_modelo = nome_modelo
        self.df2 = df2
        self.varProcs=varProcs
        self.regime=regime

    def calcEstmativa(self,variaveis:list):
        if self.modelo != None:
            self.estProc= self.modelo.getEstimativa(variaveis)
        return self.estProc

    
class Eqp_Rede:
    def __init__(self, nome:str, **parametros):
        self.nome=nome
        self.parametros=parametros

class Plataforma:
    def __init__(self,eqpProc:list, eqpRede=None, subsistemas=None,  circuito=None):
        self.eqpProc=eqpProc
        self.eqpRede=eqpRede
        self.subsistemas=subsistemas
        self.circuito=circuito


