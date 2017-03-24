#!/usr/bin/python
'''
# Script Name        : rsync.py
# Author             : Raul de Mingo
# Created            : 10th February 2017
# Last Modified      :
# Version            : 1.0
# Modifications      :

# Description        : Directory Synchronization
'''

import os
import shlex, subprocess
import time

fecha = time.strftime('%Y%m%d%H%M%S')   #in the format YYYYMMDDHHMMSS

def configurapath(ruta):
    tamano = len(ruta)
    if ruta[tamano - 1] != "/":
        ruta = ruta + "/"
    return ruta

def chequearuta(ruta):
    if not os.path.exists(ruta):
        print("La ruta indicada no existe:    " + ruta)
        #os.mkdir(ruta)
        return "False"
    else:
        return "True"

print("Sincronizacion de directorios en Linux mediante RSYNC")
origen = input("Indica el path de origen:  /path/directorio/ ")
# Chequeamos que el path finalice con "/"
origen = configurapath(origen)
# Chequear que el path existe.
if chequearuta(origen) == "False":
    exit(1)        # break

destino = input("Indica el path de destino:  /path/directorio/ ")
destino = configurapath(destino)
if chequearuta(destino) == "False":
    exit(1)        # break

comando1 = 'rsync -aq --delete ' + origen +' ' + destino + ' --log-file=/tmp/rsync.' + fecha + '.log'
mensaje = "Ejecutando comando:     (" + str(comando1) + ")"
comando2 = shlex.split(comando1)
print(mensaje)
subprocess.call(comando2)
