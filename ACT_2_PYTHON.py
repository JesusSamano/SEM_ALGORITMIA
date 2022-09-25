# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 21:04:02 2022

@author: ThinkPad T440
"""

def S(a,b):
    return a+b
    
def R(a,b):
    return a-b

while True:
    print("1.- Suma")
    print("2.- Resta")
    opc= input("Ingrese menu")
    n1 = float(input())
    n2 = float(input()) 
    if opc=="1":
        print("La suma es ", S(n1,n2))
    elif opc=="2":
        print("La resta es ", S(n1,n2))
    else:
        print("opcion invalida")