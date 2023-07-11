import os
import numpy as np
import funcionesprueba as fp
departamentos=np.empty([10,4],type(int))
otra=np.empty([10,4],type(int))
ruts=[]
fp.llenadodeMatriz(departamentos,otra)
op=0
tipodpto=0

while(op!=5):
    os.system("cls")
    print("*****  CASA FELIZ *****")
    print("***********************")
    print("1. Comprar departamento")
    print("2. Mostrar departamentos disponibles")
    print("3. Ver listado de compradores")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
    op=fp.ValidarOp()
    if(op==1):
        fp.mostrarDptosDisponibles(departamentos)
        tipodpto=fp.ValidarTipoDpto()
        disp=fp.ValidaDptoDisp(departamentos,tipodpto)
        if (disp): 
                print("El departamento está disponible")
                pago=fp.comprarDpto(departamentos,tipodpto,otra,ruts)
                print("\t Usted deberá cancelar un total de: $", pago, " UF")
                os.system("pause")
    if(op==2):
        fp.mostrarDptosDisponibles(departamentos)
        os.system("pause")
    if(op==3):
        fp.Listado(ruts)
        os.system("pause")
    if(op==4):
        suma=0
        suma=fp.Totales(otra)
        if(suma==0):
            print("\t No se han vendido pasajes aún")
        else:
            print("\t El total vendido hasta ahora es de: $", suma, " UF")
        os.system("pause")
    if(op==5):
        os.system("cls")
        print("Gracias por utilizar mi sistema, Denise Ulloa Cebrián - 11/7/2023")
    



