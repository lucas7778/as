from PyQt5.QtCore import pyqtSignal, QObject

class filterSelect1(QObject):
    itemChanged=pyqtSignal()
    def __init__(self,coord=None,eixoX=None,eixoY=None):
        super().__init__()
        self.coord=coord
        self.eixoX=eixoX
        self.eixoY=eixoY
    def setCoord(self, listCoord,xname,yname):
        self.coord=listCoord
        self.eixoX = xname
        self.eixoY = yname
        self.itemChanged.emit()

    def getCoord(self):
        return self.coord

    def getNames(self):
        return [self.eixoX,self.eixoY]

    def reset(self):
        self.coord = None
        self.eixoX = None
        self.eixoY = None