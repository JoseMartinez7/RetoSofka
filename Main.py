from controller.FuncionesUtiles import *

import Main

class Main():

    def main():
        # ciclo while: Se repite infinitamente hasta que el usuario desee salir
        while True:
            print(f'quiere crear nave espacial: \n1 - Si\n0 - No')
            print('-'.center(40,'-'))
            crear = int(input('\n>> '))
            print('-'.center(40,'-'))
            
            """
            Condiciones
            """
            #Codicion validar si desea seguir creando naves
            if crear == 1:    
                """
                Condiciones para seleccionar el tipo de nave a crear
                """
                # Menu para seleccionar el tipo de nave a crear
                print(f' Menu Naves '.center(20,'*'),f'\n1 - Lanzadera\n2 - Tripuladas\n3 - Roboticas\n')
                tipo = int(input('Ingrese opcion\n>> '))
                print('Creando Nave Espacial'.center(40,'-'))

                # Condiciones para validar el tipo de nave a crear

                #creando nave
                if tipo == 1 or tipo == 2 or tipo == 3:
                    crear = crearNave(tipo) 

                else:
                    print('error') 
            elif crear == 0:  
                print(f'Exit')
                break
            else:
                print('Ingreso un valor erroneo')     
        print('-'.center(40,'-'))


if __name__ == '__main__':
     Main.main()