from tabnanny import check

print("\n       *******************         ")
file_name = str(input("Ingrese el nombre del archivo: "))

print("\n       *******************         ")
id = str(input("Ingrese el DNI del usuario: "))

print("\n       *******************         ")
check_type = int(input("Tipos de cheque: \n1. Emitido\n2. Depositado\nSelecione el tipo de cheque: "))

print("\n       *******************         ")
check_state_input = True if str(input("Desea selecionar un estado de cheque? S/N ")) == "S" else False
if check_state_input:
    check_state = int(input("Estados de cheque: \n1. Pendiente\n2. Aprobado\n3. Rechazado\nSelecione un estado de cheque: "))

print("\n       *******************         ")
check_date_input = True if str(input("Desea selecionar un rango de fecha? S/N ")) == "S" else False
if check_date_input:
    check_date = str(input("Selecione un rango de fecha: dd-mm-aaaa:dd-mm-aaaa "))

print("\n       *******************         ")
output_type = int(input("Tipos de salida: \n1. Pantalla\n2. CSV\nSelecione un tipo de salida: "))

print("\n       *******************         ")
print("VALORES REGISTRADOS")
print("Nombre de archivo: " + str(file_name))
print("DNI: " + str(id))
print("Tipo de cheque: " + str(check_type))
print("Estado de cheque: " + str(check_state if check_state_input else check_state_input))
print("Rango de fecha: " + str(check_date if check_date_input else check_date_input))
print("Salida: " + str(output_type))
