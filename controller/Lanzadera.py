from controller.Spacecraft import Spacecraft


class Lanzadera(Spacecraft):
    """
    Clase Spacecraft: Es la super clase utilizada, es decir la clase padre del proyecto
    que a su vez es una clase abstracta 
    """
    

    """
    Constructor heredado de la clase Spacecraft
    """
    def __init__(self, nombre, pais, tipo, combustible, velocidad, empuje, peso, altura, fecha, transporta):
        super().__init__(nombre, pais, tipo, combustible, velocidad, empuje, peso, altura, fecha)

        self.__transporta = transporta

    """Metodos encapsulados"""

    @property
    def transporta(self):
        return self.__transporta

    @transporta.setter
    def transporta(self,transporta):
        self.__transporta = transporta


    """Metodos de comportamientos"""

    def soltar(self, soltar):
        self.__soltar = soltar
        if self.__soltar == 0:
            return f'>>> No a soltado nave transportada <<<'
        elif self.__soltar ==1:
            return f'>>> Nave transportada soltada con exito <<<'

    #sobre escritura de metodos abstractos de la clase Spacecraft

    def despegar(self, despegar):
        self.__despegar = despegar
        if self.__despegar == 0:
            return f'Nave: {self.nombre} >>> No a despegado <<<'
        elif self.__despegar == 1:
            return f'Nave: {self.nombre} >>> Despegando <<<'

    def acelerar(self):
        self.__acelerar = self
        if self.__acelerar == 1:
            return f'Nave: {self.nombre} >>> Acelerando <<<'
        elif self.__acelerar  == 0:
            return f'Nave: {self.nombre} >>>> Mantener velocidad actual <<<<'

    def frenar(self):
        return super().frenar()

    # Sobre-escritura del metodo detalleNave de la clase padre Spacecraft
    def detalleNave(self):
        return (f'{super().detalleNave()}\n Transporta: {self.__transporta}')