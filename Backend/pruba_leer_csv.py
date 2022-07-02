#!/usr/bin/env python3

import csv
from datetime import datetime
from optparse import Values
import os
import numpy as np

# path = os.getcwd()


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
            

def diccToCsv(dicc):
    with open('testSalida.csv', 'w', newline='') as csvfile:
        fieldnames = dicc.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        keys=[]
        csvDicc = {}
        for key in dicc:
            keys.append(key)
        writer.writeheader()
        for i in range(len(dicc[keys[0]])):
            csvDicc.clear()
            for j in range(len(dicc)):
                csvDicc.update({keys[j] : dicc[keys[j]][i]})
            writer.writerow(csvDicc)
        

fileName = 'file2.csv'
dict_chesques = csvToDicc(fileName)
diccToCsv(dict_chesques)

# diccTime = time(dict_chesques,"FechaPago","01-01-2019:01-02-2019")



# readable = datetime.fromtimestamp(855543600)
# print(readable)
# print(datetime(2002, 3, 1))
# t = ['1547596800', '1547683200', '1548374400', '1547769600', '1546646400', '1548979200', '1547942400', '1546387200']
# for elem in t:
# print(datetime.fromtimestamp(int(elem)))
# with open('names.csv', 'w', newline='') as csvfile:
#     dicNames = []
#     dicValues = []
#     csvDic = []
#     i = 0
#     j = 0
#     k = 0
#     # fieldnames = dct.keys()
#     # dctValues = dct.values()
    # # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # writer.writeheader()
    # for arr in dctValues:
        # for val in arr:
                # print(val)
   
   
    # for names in dct:
    #     dicNames.append(names)
    # # print(dicNames)

    # for values in dctValues:
    #     dicValues.append(values)
    # # print(dicValues)

    # writer = csv.DictWriter(csvfile, fieldnames=dicNames)
    # writer.writeheader()

    # while k < len(dicValues[0]):

    #     for val in dicValues:
    #         if len(csvDic) == 0 or i == 0:
    #             csvDic.append({dicNames[i] : val[j]})
    #         if len(csvDic) != 0:
    #             csvDic[j][dicNames[i]] = val[j]
    #         i += 1
    #         if i == 3:
    #             j += 1
    #             i = 0
    #             k += 1
    # print(csvDic)




