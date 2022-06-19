from controller.Tripulada import Tripulada
from controller.Lanzadera import Lanzadera
from controller.Robotica import Robotica


"""Funciones para crear naves"""

#Funcion para crear nave lanzadera
def crearNaveL(tipo):
    tipo = tipo
    if tipo == 1:
        print(f'Tipo de nave a transportar\n 1 - sonda\n 2 - nave tripulda\n 3 - nave robotica')
        lanzadera = Lanzadera('','','','','',0,0,0,0,'')
        lanzadera.transporta = int(input('>> '))
        lanzadera.nombre = str(input('Nombre de la nave\n>> '))
        lanzadera.pais = str(input('Pais donde crearon la nave\n>> '))
        lanzadera.tipo = 'Lanzadera'
        lanzadera.combustible = str(input('Combustible que utiliza la nave\n>> '))
        lanzadera.velocidad = float(input('Velocidad maxima de la nave en km/h\n>> '))
        lanzadera.empuje = float(input('Empuje maximo que tiene la nave en toneladas\n>> '))
        lanzadera.peso = float(input('Peso que tiene la nave en toneladas\n>> '))
        lanzadera.altura = float(input('Altura que tiene la nave en metros\n>> '))
        lanzadera.fecha = str(input('Fecha de creacion la nave\n>> '))
                
        # condiciones para mostrar el tipo de nave a transportar
        if lanzadera.transporta == 1:
            lanzadera.transporta = 'Sonda'
            print('-'.center(40,'-'))
            print(lanzadera.detalleNave())
        elif lanzadera.transporta == 2:
            lanzadera.transporta = 'Nave tripulada'
            print('-'.center(40,'-'))
            print(lanzadera.detalleNave())
        elif lanzadera.transporta == 3:
            lanzadera.transporta = 'Nave robotica'
            print('-'.center(40,'-'))
            print(lanzadera.detalleNave())
            print('-'.center(40,'-'))
    else:
        pass

#Funcion para crear nave Tripulada
def crearNaveT(tipo):  
    tipo = tipo          
    if tipo == 2:
        tripulada = Tripulada('','','','',0,0,0,0,'','',0)
        tripulada.nombre = str(input('Nombre de la nave\n>> '))
        tripulada.pais = str(input('Pais donde crearon la nave\n>> '))
        tripulada.tipo = 'Tripulada'
        tripulada.pasajeros = int(input('Numero de pasajeros\n>>'))
        tripulada.combustible = str(input('Combustible que utiliza la nave\n>> '))
        tripulada.velocidad = float(input('Velocidad maxima de la nave en km/h\n>> '))
        tripulada.empuje = float(input('Empuje maximo que tiene la nave en toneladas\n>> '))
        tripulada.peso = float(input('Peso que tiene la nave en toneladas\n>> '))
        tripulada.altura = float(input('Altura que tiene la nave en metros\n>> '))
        tripulada.fecha = str(input('Fecha de creacion la nave\n>> '))
        print(f'Tipo de funcion de la nave\n 1 - Mision lunar\n 2 - Mantenimiento\n 3 - Estudio comportamiento humano')
        tripulada.funcion = int(input('>> '))
        print('-'.center(40,'-'))
        print(tripulada.detalleNave())
        print('-'.center(40,'-'))
    else:
        pass

#Funcion para crear nave robotica
def crearNaveR(tipo):
    tipo = tipo
    if tipo == 3:
        print(f'Planeta que estudia la nave\n 1 - Marte\n 2 - Jupiter\n 3 - Otro')
        robotica = Robotica('','','','',0,0,0,0,'',0)
        robotica.estudia = int(input('>> '))
        robotica.nombre = str(input('Nombre de la nave\n>> '))
        robotica.pais = str(input('Pais donde crearon la nave\n>> '))
        robotica.tipo = 'Robotica'
        robotica.combustible = str(input('Combustible que utiliza la nave\n>> '))
        robotica.velocidad = float(input('Velocidad maxima de la nave en km/h\n>> '))
        robotica.empuje = float(input('Empuje maximo que tiene la nave en toneladas\n>> '))
        robotica.peso = float(input('Peso que tiene la nave en toneladas\n>> '))
        robotica.altura = float(input('Altura que tiene la nave en metros\n>> '))
        robotica.fecha = str(input('Fecha de creacion la nave\n>> '))
                
        # condiciones para mostrar el planeta que estudia la nave robotica
        if robotica.estudia == 1:
            robotica.estudia = 'Marte'
            print('-'.center(40,'-'))
            print(robotica.detalleNave())
        elif robotica.estudia == 2:
            robotica.estudia = 'Jupiter'
            print('-'.center(40,'-'))
            print(robotica.detalleNave())
        elif robotica.estudia == 3:
            print(f'Ingrese planeta\n')
            robotica.estudia = str(input('>> '))
            print('-'.center(40,'-'))
            print(robotica.detalleNave())
            print('-'.center(40,'-'))