# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 13:25:03 2022

@author: Sámano Juárez Juana Jesús 
"""
#FUNCIONES 

#......................................................................................
def factorial(numero):
     f = 1
    #numero = int(input("Escribe un Numero: "))
     if numero != 0:
        for i in range(1, numero + 1):
           f = f * i
     return f
     return Menu1()
            
def euler(limite):
    e = 0
    for n in range(limite):
        e = e + 1/factorial(n)
    return e
    return Menu1()
      
    
def Mat():
    print("El resulatado es:", euler(int(input("Escribe un valor para el limite: ")))) 
    return Menu1()
#........................................................................................    



def Figuras():
     

    print("\n\t**********Eliga  figuira********")
    opcfig = int (input("\t1.-Cuadrado \n\t2.-Triangulo \n\t3.-Circulo \n\t4.-Regresar a menu principal "))
    
     
    if opcfig==1:
         print("\t-------Has elegido el cuadrado----------")
         lado= int(input("\tIngresa lado de cuadrado:"))
         areac = lado*lado
         print("\tEl area es \t",areac)
      
    elif opcfig==2:
          print("\t-------Has elegido el Triangulo----------")
          print("\tArea de triangulo:")
          base= int(input("\tIngresa la base del triangulo:"))
          altura= int(input("\tIngresa la aultura:"))
          areat= int(base) * int (altura) / 2.0
          print("\tEl area es:" + str(areat))
          
           
    elif opcfig==3:
          print("\tArea de circulo")
          PI = 3.14
          radio = float(input("\tIngresa el radio:"))
          areac = PI * radio * radio
          print("\tEl area es:", areac)
          
      
    elif opcfig==4:
          return Menu1()
    
    else:
      print("\tOpcion no disponible")  
    return Figuras()
     
     

def Zodiacal():
    print("\n\t------Ingrese datos para saber sus signo zodiacal----") 
    dia = int(input ("\tIngresa el valor de dia: "))
    mes = int (input("\tIngresa el valor de mes: "))
    
    if (dia>=21 and mes==3) or (dia<=20 and mes==4):
         print ("\tAries")
    if (dia>=24 and mes==9) or (dia<=23 and mes==10):
        print ("\tLibra")
    if (dia>=21 and mes==4) or (dia<=21 and mes==5):
        print ("\tTauro")
    if (dia>=24 and mes==10) or (dia<=22 and mes==11):
        print ("\tEscorpio")
    if (dia>=22 and mes==5) or (dia<=21 and mes==6):
        print ("\tG\u00E9minis")
    if (dia>=23 and mes==11) or (dia<=21 and mes==12):
        print ("\tSagitario")
    if (dia>=21 and mes==6) or (dia<=23 and mes==7):
        print ("\tC\u00E1ncer")
    if (dia>=22 and mes==12) or (dia<=20 and mes==1):
        print ("\tCapricornio")
    if (dia>=24 and mes==7) or (dia<=23 and mes==8):
        print ("\tLeo")
    if (dia>=21 and mes==1) or (dia<=19 and mes==2):
        print ("\tAcuario")
    if (dia>=24 and mes==8) or (dia<=23 and mes==9):
        print ("\tVirgo")
    if (dia>=20 and mes==2) or (dia<=20 and mes==3):
        print ("\tPiscis")
    else:
        print("t/Opcion invalida") 
    return Menu1()
       
def Cerrar():
    quit()
    
    
    
def Menu1():
    print("\n------------------------MENU PRINCIPAL-----------------------\n")
    print("1.-Areas \n2.-Signo Zodiacal \n3.-Proceso Matematico \n9.-Salir ")
    opc = int(input("Ingrese opcion que desea realizar: "))
    while opc !=9:
        if opc ==1:
           Figuras()
            
            
        elif opc == 2:
             Zodiacal()
            
            
        elif opc == 3:
             Mat()
        
        elif opc == 9:
            print("adios")
         
        else:
            print("Dato invalo")
            return Menu1()
    
Menu1()