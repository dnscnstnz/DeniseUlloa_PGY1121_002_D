import os
from re import A
import numpy as np

def llenadodeMatriz(departamentos,otra):
    x=1
    for a in range(10):
        for b in range(4):
            departamentos[a,b]=x
            otra[a,b]=x
            x+=1
           

def ValidarOp():
    op2=0
    while(True):
        try:
            op2=int(input("Ingrese una opción del menú"))
            if (op2>0 and op2<6):
                break
            else:
                print("Debe ingresar un número entre 1 y 5")
        except ValueError:
            print("Debe ingresar un número entero")
    return op2

def mostrarDptosDisponibles(departamentos):
    os.system("cls")
    for a in range(10):
        print("\n")
        for b in range(4):
            if b==0 or b==3:
                print("\t", departamentos[a,b], end="")
            else:
                print("\t", departamentos[a,b], end="")
    print("\n\n")

def ValidarTipoDpto():
    tipodpto=0
    while(True):
        try:
            print("Los precios en los departamentos, son los siguientes: ")
            print("Tipo A,3.800 UF ")
            print("Tipo B,3.000 UF ")
            print("Tipo C,2.800 UF ")
            print("Tipo D,3.500 UF ")
            tipodpto=int(input("Elija su departamento: "))
            if (tipodpto>=1 and tipodpto<=40):
                break
            else:
                print("Debe ingresar un número válido")
        except ValueError:
            print("Debe ingresar un número o un número entero")
    return tipodpto


def ValidaDptoDisp(departamentos,tipodpto):
    for a in range(10):
        for b in range(4):
            if(tipodpto==departamentos[a,b]):
                return True
    return False


def comprarDpto(departamentos,tipodpto,otra,ruts):
    if(tipodpto==1 or tipodpto==5 or tipodpto==9 or tipodpto==13 or tipodpto==17 or tipodpto==21 or tipodpto==25 or tipodpto==29 or tipodpto==33 or tipodpto==37):
        pago=3800
    if(tipodpto==2 or tipodpto==6 or tipodpto==10 or tipodpto==14 or tipodpto==18 or tipodpto==22 or tipodpto==26 or tipodpto==30 or tipodpto==34 or tipodpto==38):
        pago=3000   
    if(tipodpto==3 or tipodpto==7 or tipodpto==11 or tipodpto==15 or tipodpto==19 or tipodpto==23 or tipodpto==27 or tipodpto==31 or tipodpto==35 or tipodpto==39):
        pago=2800
    if(tipodpto==4 or tipodpto==8 or tipodpto==12 or tipodpto==16 or tipodpto==20 or tipodpto==24 or tipodpto==28 or tipodpto==32 or tipodpto==36 or tipodpto==40):
        pago=3500
    for a in range(10):
        for b in range(4):
            if(tipodpto==departamentos[a,b]):
                while(True):
                    while(True):
                        try:
                            rut=int(input("Ingrese su rut, sin dígito verificador, debe tener mínimo 7 dígitos "))
                            if(rut<999999):
                                print("Error, debe tener 7 dígitos mínimo")
                            else:
                                break
                        except ValueError:
                            print("Debe ser número entero")
                    if(len(ruts)>0): 
                        sw=0
                        for y in range(len(ruts)):
                            if(rut==ruts[y]):
                                sw=1
                        if(sw==1):
                            print("El rut ya existe y no se puede agregar el pasajero")
                        else:
                            ruts.append(rut)
                            break
                    else:
                        ruts.append(rut)
                        break
                departamentos[a,b]="X"
            
                otra[a,b]=pago
    return pago

def Listado(ruts):
    ruts.sort()
    print("Listado de pasajeros del avión ordenados de menor a mayor ")
    print("\t",ruts)

def Totales(departamentos):
    suma=0
    for a in range(10):
        for b in range(4):
            if(departamentos[a,b]!=0 and departamentos[a,b]>40):
                suma+=departamentos[a,b]
    return suma