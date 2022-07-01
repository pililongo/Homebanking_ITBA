#!/usr/bin/env python3

import csv
from datetime import datetime
import os

# path = os.getcwd()


def csvToDic(fileName):
    ''' 
    Convierte un archivo .csv en un diccionario. Utiliza la primera fila   
    del archivo .csv para establecer las keywords del diccionario.

    Argumento: 
        fileName: nombre del arcivo .csv.
    Salida: 
        dicc: diccionario.
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
    Filtra un diccionario mediante una keyword y un parametro dado.

    Argumentos:
        dicName: diccionario a filtrar.
        keyName: keyword donde se filtra.
        param: parametro utilizado para filtrar.
    Salida:
        filteredDic: diccionario filtrado.
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
    dt = datetime.strptime(value, "%d-%m-%Y")
    return int(dt.timestamp())


def time(dicc,keyName,rangeDate):
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
            
# def error(dicc, keyName):

#     for elem in dicc[keyName]:
#         aux = diccFilter(dicc, keyName, elem)
#         if len(aux[keyName]) != 1:
            

# def diccToCsv(dicc):
    

# #fileName = str(input('Ingrese el nombre de la archivo: '))
# fileName = 'file2.csv'
# #dni = str(input('ingrese dni: '))
# dict_chesques = csvToDic(fileName)
# # print(dict_chesques)
# diccTime = time(dict_chesques,"FechaPago","01-01-2019:01-02-2019")
# print(len(diccTime["DNI"]))

#print(diccFilter(dict_chesques, "DNI", "236625789"))


# readable = datetime.fromtimestamp(855543600)
# print(readable)
# print(datetime(2002, 3, 1))
# t = ['1547596800', '1547683200', '1548374400', '1547769600', '1546646400', '1548979200', '1547942400', '1546387200']
# for elem in t:
#     print(datetime.fromtimestamp(int(elem)))

dct = {'Name': ['Lucia','Nano','Pili','John'], 'Age': ['80','11','36','23'], 'Country': ['USA','MADAGASCAR','USA','USA']}
print(len(dct.values()))

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = dct.keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in dct:
        writer.writerow({'Name':"Lucia","Age":100})
  

# dct = { "Australia" : 456, "Germany" : 2678, "China" : 1890,"Japan":1667}
# with open('TEST.csv', 'w') as csvfile:
#     header_key = dct.keys()
#     new_val = csv.DictWriter(csvfile, fieldnames=header_key)

#     new_val.writeheader()
#     for elem in dct:
#         new_val.writerow({'Country': elem, 'Value': dct[elem]})