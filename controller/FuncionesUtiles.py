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


    #llamando a las funciones que contiene los metodos
    metodoDespegar(tipo)
    metodoSoltar(tipo)
    

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

    #llamando a las funciones que contiene los metodos
    metodoDespegar(tipo)
    metodoAcelerar(tipo)
    metodoFrenar(tipo)
    metodoOrbitar(tipo)

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
    else:
        pass

    #llamando a las funciones que contiene los metodos
    metodoDespegar(tipo)
    metodoAcelerar(tipo)
    metodoFrenar(tipo)
    metodoOrbitar(tipo)

"""Funciones para instanciar los metodos de comportamientos de las clases hijas""" 

#funcion para metodo despegar          
def metodoDespegar(tipo):
    if tipo == 1 or tipo == 2 or tipo == 3: 
        print('-'.center(40,'-'))
        print(f'Despegar Nave\n 1 - Si\n 0 - No')
        despegar = int(input('\n>> '))
        if despegar == 1 or despegar == 0:
            if tipo == 1:
                lanzadera = Lanzadera('','','','',0,0,0,0,'','')
                # llamando al metodo despegar de la nave lanzadera
                print('-'.center(40,'-'))
                print(lanzadera.despegar(despegar))
                print('-'.center(40,'-'))
            elif tipo == 2:
                # llamando al metodo despegar de la nave tripulada
                tripulada = Tripulada('','','','',0,0,0,0,'',0,'')
                print('-'.center(40,'-'))
                print(tripulada.despegar(despegar))
                print('-'.center(40,'-'))
            elif tipo == 3:
                # llamando al metodo despegar de la nave robotica
                robotica = Robotica('','','','',0,0,0,0,'','')
                print('-'.center(40,'-'))
                print(robotica.despegar(despegar))
                print('-'.center(40,'-'))
        else:
            print('Ingreso un valor erroneo')
    else:
        print('Ingreso un valor erroneo')

#Funcion para el metodo acelerar
def metodoAcelerar(tipo):
    if tipo == 2 or tipo == 3: 
        print('-'.center(40,'-'))
        print(f'Acelerar Nave\n 1 - Si\n 0 - No')
        acelerar = int(input('\n>> '))
        if acelerar == 1 or acelerar == 0:
            if tipo == 2:
                # llamando al metodo despegar de la nave tripulada
                tripulada = Tripulada('','','','',0,0,0,0,'',0,'')
                print('-'.center(40,'-'))
                print(tripulada.acelerar(acelerar))
                print('-'.center(40,'-'))
            elif tipo == 3:
                # llamando al metodo despegar de la nave robotica
                robotica = Robotica('','','','',0,0,0,0,'','')
                print('-'.center(40,'-'))
                print(robotica.acelerar(acelerar))
                print('-'.center(40,'-'))
        else:
            print('Ingreso un valor erroneo')
    else:
        print('Ingreso un valor erroneo')

# funcion para el metodo frenar
def metodoFrenar(tipo):
    if tipo == 2 or tipo == 3: 
        print('-'.center(40,'-'))
        print(f'Frenar Nave\n 1 - Si\n 0 - No')
        frenar = int(input('\n>> '))
        if frenar == 1 or frenar == 0:
            if tipo == 2:
                # llamando al metodo despegar de la nave tripulada
                tripulada = Tripulada('','','','',0,0,0,0,'',0,'')
                print('-'.center(40,'-'))
                print(tripulada.frenar(frenar))
                print('-'.center(40,'-'))
            elif tipo == 3:
                # llamando al metodo despegar de la nave robotica
                robotica = Robotica('','','','',0,0,0,0,'','')
                print('-'.center(40,'-'))
                print(robotica.frenar(frenar))
                print('-'.center(40,'-'))
        else:
            print('Ingreso un valor erroneo')
    else:
        print('Ingreso un valor erroneo')

# funcion para el metodo orbitar
def metodoOrbitar(tipo):
    if tipo == 2 or tipo == 3: 
        print('-'.center(40,'-'))
        print(f'Orbitar Nave\n 1 - Si\n 0 - No')
        orbitar = int(input('\n>> '))
        if orbitar == 1 or orbitar == 0:
            if tipo == 2:
                # llamando al metodo despegar de la nave tripulada
                tripulada = Tripulada('','','','',0,0,0,0,'',0,'')
                print('-'.center(40,'-'))
                print(tripulada.orbitar(orbitar))
                print('-'.center(40,'-'))
            elif tipo == 3:
                # llamando al metodo despegar de la nave robotica
                robotica = Robotica('','','','',0,0,0,0,'','')
                print('-'.center(40,'-'))
                print(robotica.orbitar(orbitar))
                print('-'.center(40,'-'))
        else:
            print('Ingreso un valor erroneo')
    else:
        print('Ingreso un valor erroneo')

# funcion para el metodo soltar
def metodoSoltar(tipo):
    if tipo == 1: 
        print('-'.center(40,'-'))
        print(f'soltar Nave\n 1 - Si\n 0 - No')
        soltar = int(input('\n>> '))
        if soltar == 1:
            # llamando al metodo despegar de la nave tripulada
            lanzadera = Lanzadera('','','','','',0,0,0,0,'')
            print('-'.center(40,'-'))
            print(lanzadera.soltar(soltar))
            print('-'.center(40,'-'))
        elif soltar == 0:
            # llamando al metodo despegar de la nave robotica
            lanzadera = Lanzadera('','','','','',0,0,0,0,'')
            print('-'.center(40,'-'))
            print(lanzadera.soltar(soltar))
            print('-'.center(40,'-'))
        else:
            print('Ingreso un valor erroneo')
    else:
        print('Ingreso un valor erroneo')