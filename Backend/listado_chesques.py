#!/usr/bin/env python3

import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

clearConsole()
print("\n       *******************         ")
file_name = str(input("Ingrese el nombre del archivo: "))
clearConsole()

while True:
    print("\n       *******************         ")
    id = str(input("Ingrese el DNI del usuario: "))

    if id.isnumeric() and (len(id) == 7 or len(id) == 8):
        clearConsole()
        break
    else:
        clearConsole()
        print("\n       *******************         ")
        print('ta mal, ingresa de nuevo')

print("\n       *******************         ")
check_type = int(input("Tipos de cheque: \n1. Emitido\n2. Depositado\nSelecione el tipo de cheque: "))
clearConsole()

print("\n       *******************         ")
check_state_input = True if str(input("Desea selecionar un estado de cheque? S/N ")).upper() == "S" else False
clearConsole()
if check_state_input:
    check_state = int(input("Estados de cheque: \n1. Pendiente\n2. Aprobado\n3. Rechazado\nSelecione un estado de cheque: "))
    clearConsole()

print("\n       *******************         ")
check_date_input = True if str(input("Desea selecionar un rango de fecha? S/N ")).upper() == "S" else False
clearConsole()
if check_date_input:
    check_date = str(input("Selecione un rango de fecha: dd-mm-aaaa:dd-mm-aaaa "))
    clearConsole()


print("\n       *******************         ")
output_type = int(input("Tipos de salida: \n1. Pantalla\n2. CSV\nSelecione un tipo de salida: "))
clearConsole()


print("\n       *******************         ")
print("VALORES REGISTRADOS")
print("Nombre de archivo: " + str(file_name))
print("DNI: " + str(id))
print("Tipo de cheque: " + str("Emitido" if check_type == 1 else 'Depositado'))
print("Estado de cheque: " + str(check_state if check_state_input else check_state_input))
print("Rango de fecha: " + str(check_date if check_date_input else check_date_input))
print("Salida: " + str(output_type))