#!/usr/bin/python
'''
# Script Name        : users-name-check.py
# Author             : Raul de Mingo
# Created            : 9th February 2017
# Last Modified      :
# Version            : 1.0
# Modifications      :

# Description        : Check rules for create new users
#                       user name > 6 characters and < 12
#                       Alphanumeric
'''

condicion = 0

while condicion == 0:

    # User name request
    print("Por favor indicanos el nombre de usuario que quieres crear")
    nombre = input("Nombre usuario: ")

    # Between 6 and 12 characters
    if len(nombre) < 6:
        print("Debe especificar un tamano mayor de seis caracteres")
        condicion = 0
    elif len(nombre) > 12:
        print("Debe especificar un tamano menor de doce caracteres")
        condicion = 0
    # Name must be alphanumeric
    elif nombre.isalnum() == False:
        print("El nombre de usuario debe ser alfanumerico")
        condicion = 0
    else:
        print("El nombre de usuario " + nombre + " cumple todas las normativas")
        condicion = 1
