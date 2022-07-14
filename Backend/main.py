from classes import *

ACCOUNTS_RESTRICTIONS = {
    "CLASSIC":{
        "CreditCardsMax": 0,
        "AccountUSD": False,
        "CheckingAccount": 0,
        "MaxWhithdrawls": 10000,
        "Checkbooks": 0,
        "TransferFee": 0.01,
        "MaxTranferReceived": 150000 
    },
    "GOLD":{
        "CreditCardsMax": 1,
        "AccountUSD": True,
        "CheckingAccount": 10000,
        "MaxWhithdrawls": 20000,
        "Checkbooks": 1,
        "TransferFee": 0.005,
        "MaxTranferReceived": 500000 
    },
    "BLACK":{
        "CreditCardsMax": 5,
        "AccountUSD": True,
        "CheckingAccount": 10000,
        "MaxWhithdrawls": 100000,
        "Checkbooks": 2,
        "TransferFee": 0,
        "MaxTranferReceived": False
    }
}

A= {
    "numero": 100001,
    "nombre": "Nicolas",
    "apellido": "Gastón",
    "DNI": "29494777",
    "calle": "9 de Julio",
    "numero": "1231",
    "ciudad": "Córdoba",
    "provincia": "Córdoba",
    "pais": "Argentina",
    "tipo": "BLACK",
    "transacciones": [
    {
        "estado": "ACEPTADA",
        "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
        "cuentaNumero": 190,
        "cupoDiarioRestante": 9000,
        "monto": 1000,
        "fecha": "10/10/2022 16: 00: 55",
        "numero": 1,
        "saldoEnCuenta": 100000,
        "totalTarjetasDeCreditoActualmente" : 5,
        "totalChequerasActualmente" : 2
    },
    {
        "estado": "RECHAZADA",
        "tipo": "ALTA_CHEQUERA",
        "cuentaNumero": 190,
        "cupoDiarioRestante": 9000,
        "monto": 10000,
        "fecha": "10/10/2022 16:40:55",
        "numero": 1,
        "saldoEnCuenta": 100000,
        "totalTarjetasDeCreditoActualmente" : 5,
        "totalChequerasActualmente" : 2
    }
    ]
}

cliente_1= Client(A,ACCOUNTS_RESTRICTIONS)
print(cliente_1.dataToHTML())