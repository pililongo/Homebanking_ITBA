from funciones import *

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
        print('Por favor, ingresa de nuevo \nEl dni debe tener entre 7 y 8 caracteres')

print("\n       *******************         ")
while True:
    choose = int(input("Tipos de cheque: \n1. Emitido\n2. Depositado\nSeleccione el tipo de cheque: "))
    if choose == 1:
        check_type = "EMITIDO"
        break
    elif choose == 2:
        check_type = "DEPOSITADO"
        break
    else:
        clearConsole()
        print("\n       *******************         ")
        print('Elija la opcion correspondiente')
        print("\n       *******************         ")

clearConsole()
print("\n       *******************         ")
check_state_input = True if str(input("¿Desea selecionar un estado de cheque? S/N ")).upper() == "S" else False
clearConsole()
while True:
    if check_state_input:
        choose = int(input("Estados de cheque: \n1. Pendiente\n2. Aprobado\n3. Rechazado\nSeleccione un estado de cheque: "))
        if choose == 1:
            check_state = 'PENDIENTE'
            clearConsole()
            break
        elif choose == 2:
            check_state = 'APROBADO'
            clearConsole()
            break
        elif choose == 3: 
            check_state = 'RECHAZADO'
            clearConsole()
            break
        else:
            clearConsole()
            print("\n       *******************         ")
            print('Elija la opcion correspondiente')
            print("\n       *******************         ")

    else:
        check_state = ''

print("\n       *******************         ")
check_date_input = True if str(input("¿Desea seleccionar un rango de fecha? S/N ")).upper() == "S" else False
clearConsole()
if check_date_input:
    print("\n       *******************         ")
    check_date = str(input("Seleccione un rango de fecha\n       *******************         \ndd-mm-aaaa:dd-mm-aaaa: "))
    clearConsole()
else:
    check_date = ''


print("\n       *******************         ")
while True:
    output_type = int(input("Tipos de salida: \n1. Pantalla\n2. CSV\nSeleccione un tipo de salida: "))
    if output_type >= 1 and output_type <= 2:
        break
        clearConsole()
    else:
        clearConsole()
        print("\n       *******************         ")
        print('Elija la opcion correspondiente')
        print("\n       *******************         ")

dicc = csvToDicc(file_name)
dni_filter = diccFilter(dicc, 'DNI', dni)
check_type_filter = diccFilter(dni_filter, 'Tipo', check_type)
diccExist = check_type_filter #variable actualizada con los dicc filtrados existentes.

if check_state:
    check_state_filter = diccFilter(check_type_filter, 'Estado', check_state)
    diccExist = check_state_filter


if check_type == "EMITIDO":
    if check_date:
        date_filter = time(diccExist, 'FechaOrigen', check_date)
        diccExist = date_filter
    error = error(dni_filter, 'NroCheque', 'NumeroCuentaOrigen')
elif check_type == "DEPOSITADO":
    if check_date:
        date_filter = time(diccExist, 'FechaPago', check_date)
        diccExist = date_filter
    error = error(dni_filter, 'NroCheque', 'NumeroCuentaDestino')

clearConsole()
if error:
    print('Error: cheque duplicado en la cuenta\nNo es posible visualizar datos.')
else:
        print("\n       *******************         ")
        print("            Resultados               ")
        print("\n       *******************         ")
        if output_type == 1:
            for item in diccExist:
                print(item, ' = ', diccExist[item])

        elif output_type == 2:
            name = getCsvName(diccExist, 'DNI')
            trimedDic = trimDic(diccExist, ['NroCheque', 'CodigoBanco', 'CodigoScurusal', 'DNI', 'Tipo', 'Estado'])
            diccToCsv(trimedDic, name)
