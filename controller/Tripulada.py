from controller.Spacecraft import Spacecraft

class Tripulada(Spacecraft):

    def __init__(self, nombre, pais, tipo, combustible, velocidad, empuje, peso, altura, fecha, pasajeros, funcion):
        super().__init__(nombre, pais, tipo, combustible, velocidad, empuje, peso, altura, fecha)

        self.__pasajeros = pasajeros
        self.__funcion = funcion

    """
    Metodos
    """

    # metodos encapsulados del atributo utilidad
    @property
    def pasajeros(self):
        return self.__pasajeros

    @pasajeros.setter
    def pasajeros(self, pasajeros):
        self.__pasajeros = pasajeros


    @property
    def funcion(self):
        if self.__funcion == 1:
            self.__funcion = 'Mision lunar'
            return  f'Funcion: {self.__funcion}'
        elif self.__funcion == 2:
            self.__funcion = 'Estudiar comportamiento humano'
            return f'Funcion: {self.__funcion}'
        elif self.__funcion == 3:
            self.__funcion = 'Mantenimiento'

    @funcion.setter
    def funcion(self, funcion):
        self.__funcion = funcion


    """metodos de comportamientos"""

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
            return f'Nave: {self.__nombre} >>> No a despegado <<<'
        elif self.__despegar == 1:
            return f'Nave: {self.__nombre} >>> Despegando <<<'

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


    # Sobre-escritura del metodo detalleNave de la clase padre Spacecraft
    def detalleNave(self):
        return f'{super().detalleNave()}\n Numero de pasajeros: {self.__pasajeros}'
