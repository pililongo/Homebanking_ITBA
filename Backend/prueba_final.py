#!/usr/bin/env python3

from pruba_leer_csv import *

clearConsole()
print("\n       *******************         ")
file_name = str(input("Ingrese el nombre del archivo: "))
clearConsole()

while True:
    print("\n       *******************         ")
    dni = str(input("Ingrese el DNI del usuario: "))

    if dni.isnumeric() and (len(dni) == 7 or len(dni) == 8):
        clearConsole()
        break
    else:
        clearConsole()
        print("\n       *******************         ")
        print('ta mal, ingresa de nuevo')

print("\n       *******************         ")
elec = int(input("Tipos de cheque: \n1. Emitido\n2. Depositado\nSelecione el tipo de cheque: "))
if elec == 1:
    check_type = "EMITIDO"
else:
    check_type = "DEPOSITADO"

clearConsole()

print("\n       *******************         ")
check_state_input = True if str(input("Desea selecionar un estado de cheque? S/N ")).upper() == "S" else False
clearConsole()
if check_state_input:
    elec = int(input("Estados de cheque: \n1. Pendiente\n2. Aprobado\n3. Rechazado\nSelecione un estado de cheque: "))
    if elec == 1:
        check_state = 'PENDIENTE'
    elif elec == 2:
        check_state = 'APROBADO'
    elif elec == 3: 
        check_state = 'RECHAZADO'
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

dicc = csvToDicc(file_name)
dni_filter = diccFilter(dicc, 'DNI', dni)
check_type_filter = diccFilter(dni_filter, 'Tipo', check_type)
check_state_filter = diccFilter(check_type_filter, 'Estado', check_state)

if check_type == "EMITIDO":
    date_filter = time(check_state_filter, 'FechaOrigen', check_date)
elif check_type == "DEPOSITADO":
    date_filter =time(check_state_filter, 'FechaPago', check_date)

clearConsole()
print("\n       *******************         ")
print("            Resultados               ")
print("\n       *******************         ")
if output_type == 1:
    for item in date_filter:
        print(item, ' = ', date_filter[item])

elif output_type == 2:
    name = getCsvName(date_filter, 'DNI')
    trimedDic = trimDic(date_filter, ['NroCheque', 'CodigoBanco', 'CodigoScurusal', 'DNI', 'Tipo', 'Estado'])
    diccToCsv(trimedDic, name)

