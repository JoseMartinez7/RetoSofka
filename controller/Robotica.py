from controller.Spacecraft import Spacecraft


class Robotica(Spacecraft):
    """
    Clase Spacecraft: Es la super clase utilizada, es decir la clase padre del proyecto
    que a su vez es una clase abstracta 
    """
    

    """
    Constructor heredado de la clase Spacecraft
    """
    def __init__(self, nombre, pais, tipo, combustible, velocidad, empuje, peso, altura, fecha, estudia):
        super().__init__(nombre, pais, tipo, combustible, velocidad, empuje, peso, altura, fecha)

        self.__estudia = estudia


    # # metodos encapsulados del atributo estuia: 
    @property
    def estudia(self):
        return self.__estudia

    @estudia.setter
    def estudia(self,estudia):
        self.__estudia = estudia



    """metodos de comportamientos """
    def orbitar(self, orbitar):
        self.__orbitar = orbitar
        if self.__orbitar == 0:
            return f'Nave: {self.__nombre} >>> no esta en orbita <<<'
        elif self.__orbitar == 1:
            return f'Nave: {self.__nombre} >>> en orbita <<<'
       

    #sobre escritura de metodos abstractos de la clase Spacecraft

    def despegar(self, despegar):
        self.__despegar = despegar
        if self.__despegar == 0:
            return f'Nave: {self.nombre} >>> No a despegado <<<'
        elif self.__despegar == 1:
            return f'Nave: {self.nombre} >>> Despegando <<<'

    def acelerar(self,acelerar):
        self.__acelerar = acelerar
        if self.__acelerar == 1:
            return f'Nave: {self.__nombre} >>> acelerando <<<'
        elif self.__acelerar  == 0:
            return f'Nave: {self.__acelerar} >>> desacelerando <<<'

    def frenar(self, frenar):
        self.__frenar = frenar
        if self.__frenar == 1:
            return f'Nave: {self.__nombre} >>> Frenando <<<'
        elif self.__frenar  == 0:
            return f'Comportamiento: {self.__nombre} >>> Mantener velocidad <<<'
        


    #Sobre-escritura del metodo detalleNave de la clase padre Spacecraft
    def detalleNave(self):
        return f'{super().detalleNave()}\n Estudia planeta: {self.__estudia}'