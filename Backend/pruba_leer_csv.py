#!/usr/bin/env python3

import csv
import datetime


def csvToDic(fileName):
    dic = {}
    i = 0
    # open the CSV file
    with open(fileName, 'r')as file:
        
        # read the CSV file
        csvfile = csv.reader(file)
        row1 = next(csvfile)
        # transform csv to dic
        for name in row1:
            dic[name] = []

        for row in csvfile:
            for column in row:
                dic[row1[i]].append(column)
                i += 1
            i = 0
    return dic

def finderLittleThings(dicName, keyName, param):
    finalDic = {}
    i = 0
    for key in dicName:
        finalDic[key] = []
    
    for elem in dicName[keyName]:
    
        if elem == param:
        
            for key in dicName:
                finalDic[key].append(dicName[key][i])

        i += 1        
    print(finalDic)

          

#fileName = str(input('Ingrese el nombre de la archivo bobo: '))
fileName = 'file.csv'
#dni = str(input('ingrese dni: '))
dict_chesques = csvToDic(fileName)
#finderLittleThings(dict_chesques, "DNI", "23665789")


readable = datetime.datetime.fromtimestamp(1617591371).isoformat()
print(readable)

'''{
    'NroCheque': ['0001', '0005', '0005', '0010', '0002'],
    'CodigoBanco': ['1', '2', '55', '1', '55'],
    'CodigoScurusal': ['12', '11', '22', '12', '44'], 
    'NumeroCuentaOrigen': ['23123132', '2342342', '23423432432', '23123132', '2432432423'], 
    'NumeroCuentaDestino': ['12312312', '33344343', '34343434', '12312312', '343434343'], 
    'Valor': ['10000', '60000', '89000', '5000', '5559,76'], 
    'FechaOrigen': ['1617591371', '1617591371', '1617591371', '1617591371', '1620183371'], 
    'FechaPago': ['1620183371', '1620183371', '1620183371', '1617591371', '1620183371'], 
    'DNI': ['11580999', '40998788', '23665789', '1617591371', '23665789'], 
    'Tipo': ['EMITIDO', 'EMITIDO', 'EMITIDO', 'EMITIDO', 'EMITIDO'], 
    'Estado': ['APROBADO', 'APROBADO', 'APROBADO', 'RECHAZADO', 'PENDIENTE']
}'''