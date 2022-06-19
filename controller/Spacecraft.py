from abc import ABC, abstractmethod

class Spacecraft(ABC):
    """
    Clase Spacecraft: Es la super clase utilizada, es decir la clase padre del proyecto
    que a su vez es una clase abstracta """
    
    #construcctor con parametros 

    def __init__(self, nombre,pais,tipo,combustible,velocidad,empuje,peso,altura,fecha):
        self.__nombre = nombre
        self.__pais = pais
        self.__tipo = tipo
        self.__combustible = combustible
        self.__velocidad = velocidad
        self.__empuje = empuje
        self.__peso = peso
        self.__altura = altura
        self.__fecha = fecha
        
    """Metodos"""

    # Metodos setter & getter encapsulados

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def pais(self):
        return self.__pais

    @pais.setter
    def pais(self, pais):
        self.__pais = pais

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self,tipo):
        self.__tipo = tipo

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo
        
    @property
    def combustible(self):
        return self.__combustible

    @combustible.setter
    def combustible(self, combustible):
        self.__combustible = combustible
        
    @property 
    def velocidad(self):
        return self.__velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self.__velocidad = velocidad

    @property
    def empuje(self):
        return self.__empuje

    @empuje.setter
    def empuje(self, empuje):
        self.__empuje = empuje

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso
        
    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, altura):
        self.__altura = altura
    
    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    
    
    # metodo detalleNave: Devuelve el valor de los atributos de la clase Spacecraft

    def detalleNave(self):
        return (f'Detalles de la nave:' 
        f'\n---------------------------------------'
        f'\n Nombre: {self.__nombre}\n Pais: {self.__pais}'
        f'\n Tipo: {self.__tipo}'
        f'\n Combustible: {self.__combustible}\n Velocidad: {self.__velocidad}'
        f'\n Empuje: {self.__empuje}\n Peso: {self.__peso}'
        f'\n Altura: {self.__altura}\n Fecha: {self.__fecha}')
        #return f'\nDetalles de la nave:\n Nombre: {self.__nombre} \n Pais: {self.__pais}\n Velocidad: {self.__velocidad}'


    """Metodos de comportamiento"""

    
    # Metodos abstractos de comportamiento
    
    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frenar(self):
        pass

    @abstractmethod
    def despegar(self):
        pass
