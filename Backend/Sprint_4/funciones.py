import csv
import os
from datetime import datetime
from optparse import Values


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def csvToDicc(fileName):
    ''' 
    Convierte un archivo .csv en un dicc. Utiliza la primera fila   
    del archivo .csv para establecer las keywords del dicc.

    Argumento: 
        fileName: nombre del arcivo .csv.
    Salida: 
        dicc: dicc.
    ''' 
    # constant
    dicc = {}
    i = 0
    # open the CSV file
    with open(fileName, 'r') as file:
        # read the CSV file
        csvfile = csv.reader(file)
        row1 = next(csvfile)
        # sets the keywords
        for name in row1:
            dicc[name] = []
        # fill the empty dicc with the content of the .csv file
        for row in csvfile:
            for column in row:
                dicc[row1[i]].append(column)
                i += 1
            i = 0
    # outputs dicc
    return dicc

def diccFilter(dicName, keyName, param):
    '''
    Filtra un dicc mediante una keyword y un parametro dado.

    Argumentos:
        dicName: dicc a filtrar.
        keyName: keyword donde se filtra.
        param: parametro utilizado para filtrar.
    Salida:
        filteredDic: dicc filtrado.
    '''
    # constant
    filteredDic = {}
    i = 0
    # sets the keywords
    for key in dicName:
        filteredDic[key] = []
    # fills the dicc with the filtered elements
    for elem in dicName[keyName]:
        if elem == param:
            for key in dicName:
                filteredDic[key].append(dicName[key][i])
        i += 1 
    # outputs dicc
    return filteredDic

def isoToTimestamp(value : str) -> int:
    '''
    Transforma en timestamp el formato dia-mes-año.
    '''
    dt = datetime.strptime(value, "%d-%m-%Y")
    return int(dt.timestamp())


def time(dicc,keyName,rangeDate):
    '''
    Crea un diccionario filtrado con un rango de fechas determinado.

    Argumentos:
        dicc: dicc a filtrar.
        keyName: keyword donde se filtra.
        rangeDate: rango de fecha utilizado.
    Salida:
        filteredDic: dicc filtrado.
    '''
    filteredDic = {}
    i = 0
    [dateIncial, dateFinal] = rangeDate.split(":")
    dateTsInicial = isoToTimestamp(dateIncial)
    dateTsFinal = isoToTimestamp(dateFinal)

    for key in dicc:
        filteredDic[key] = []

    for elem in dicc[keyName]:
        if int(elem)>=dateTsInicial and int(elem)<=dateTsFinal:
            for key in dicc:
                filteredDic[key].append(dicc[key][i])
        i += 1 

    return filteredDic
            
def error(dicc, keyName1, keyName2):
    '''
    Muestra un error en caso de que encuentre más de un elemento 
    en uno de los parámetros dados, indicando que este se repite.

    Argumentos:
        dicc: dicc a recorrer.
        keyName1: keyword a comparar.
        keyName2: keyword a comparar.
    Salida:
        retorna un booleano. 
    '''
    for elem1 in dicc[keyName1]:
        aux = diccFilter(dicc, keyName1, elem1)
        if len(aux[keyName1]) != 1:
            for elem2 in aux[keyName2]:
                aux_2 = diccFilter(aux,keyName2,elem2)
                if len(aux_2[keyName2]) != 1:
                    return True

def trimDic(dicc, lst=[]):
    '''
    Devuelve un diccionario sin los valores que forman parte de la lista.

    Argumentos:
        dicc: dicc a recorrer.
        lst: lista de valores a eliminar. 
    Salida:
        retorna un diccionario.
    '''
    for item in lst:
        dicc.pop(item)
    return dicc

def getCsvName(dicc, value):
    '''
    Utiliza un valor y el timestamp actual como nombre del csv de salida.

    Argumentos:
        dicc: dicc a recorrer.
        value: valor utilizado como parte del nombre.
    Salida:
        retorna el nombre del archivo.
    '''
    name = str(dicc[value][0]) 
    date = str(int(datetime.now().timestamp()))
    return name + '_' + date + '.csv'

def diccToCsv(dicc, name):
    '''
    Convierte un dicc en un archivo .csv. Utiliza las keywords del dicc para establacer la primera fila   
    del archivo .csv.

    Argumento: 
        dicc: dicc a transformar.
        name: nombre del arcivo .csv.
    Salida: 
        archivo .csv.
    '''
    with open(name, 'w', newline='') as csvfile:
        fieldnames = dicc.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        keys=[]
        csvDicc = {}
        for key in dicc:
            keys.append(key)
        writer.writeheader()
        for i in range(len(dicc[keys[0]])):
            for j in range(len(dicc)):
                csvDicc.update({keys[j] : dicc[keys[j]][i]})
            writer.writerow(csvDicc)
    print(name)
