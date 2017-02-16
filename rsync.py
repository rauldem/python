#!/usr/bin/python
'''
# Script Name        : rsync.py
# Author             : Raul de Mingo
# Created            : 10th February 2017
# Last Modified      :
# Version            : 1.0
# Modifications      :

# Description        : Directories Synchronization
'''

import os
import shlex, subprocess
import time

#fecha    = datetime.date.today()        # Get Today's date
fecha = time.strftime('%Y%m%d%H%M%S')   #in the format YYYYMMDDHHMMSS
  
def configurapath(ruta):
    tamano = len(ruta)
    if ruta[tamano - 1] != "/":
        ruta = ruta + "/"
    return ruta

def chequearuta(ruta):
    if not os.path.exists(ruta):         # if not os.path.isdir(ruta)
        print("La ruta indicada " + ruta + " no existe")
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

comando1 = 'rsync --av --delete ' + origen +' ' + destino + ' >> /tmp/rysnc.' + fecha + '.log'
comando2 = shlex.split(comando1)
print("Ejecutando comando " + comando2)
subprocess.call(comando2)
