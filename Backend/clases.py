'''
Clientes Classic 
    Tiene solamente una tarjeta de débito que se crea junto con el cliente.
    Solo tiene una caja ahorro en pesos creada cuando se dio de alta el cliente. Como no tiene cuenta en dólares, no puede comprar y vender dólares.
    Solo se le permite retirar hasta un máximo de $10.000 diarios por cajero.
    No tienen acceso a tarjetas de crédito ni chequeras
    La comisión por transferencias hechas es de 1%. 
    No puede recibir transferencias mayores a $150.000 sin previo aviso.
 
Clientes Gold 
    Tiene una tarjeta de débito que se crea con el cliente.
    Tiene una cuenta corriente con un descubierto de $10.000. Hay que tener 
    presente que como tiene cuenta corriente el saldo en la cuenta podría ser 
    negativo y hasta -$10.000 si tiene cupo diario para la operación que se 
    quiera realizar.
    Tiene una caja de ahorro en dólares, por lo que puede comprar dólares.
    Puede tener solo una tarjeta de crédito.
    Las extracciones de efectivo tienen un máximo de $20.000 por día.
    Pueden tener una chequera.
    La comisión por transferencias hechas es de 0,5%.
    No puede recibir transferencias mayores a $500.000 sin previo aviso.

Clientes Black 
    Los clientes Black tienen una caja de ahorro en pesos, cuenta corriente en pesos, y una caja de ahorro en dólares.
    Pueden tener un descubierto en su cuenta corriente de hasta $10.000.
    Pueden tener hasta 5 tarjetas de crédito.
    Pueden extraer hasta $100.000 por día
    Pueden tener hasta dos chequeras.
    No se aplican comisiones a las transferencias.
    Pueden recibir transferencias por cualquier monto sin previa autorización

JSON ENTRADA:
{
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
        "fecha": "10/10/2022 16:00:55",
        "numero": 1,
        "saldoEnCuenta": 100000,
        "totalTarjetasDeCreditoActualmente" : 5,
        "totalChequerasActualmente" : 2
    },
    {
        "estado": "RECHAZADA",
        "tipo": "ALTA_CHEQUERA",
        "cuentaNumero": 190,
        "cupoDiarioRestante": 3000,
        "monto": 9000,
        "fecha": "10/10/2022 16:00:55",
        "numero": 1,
        "saldoEnCuenta": 100000,
        "totalTarjetasDeCreditoActualmente" : 5,
        "totalChequerasActualmente" : 2
    }
    ]
}

RETIRO_EFECTIVO_CAJERO_AUTOMATICO: 
    Tener presente que si tiene cuenta corriente puede figurar el valor de saldo en cuenta como negativo hasta el importe del cupo establecido

ALTA_TARJETA_CREDITO: 
    Se solicito una nueva tarjeta de crédito
    
ALTA_CHEQUERA: 
    Se solicito una nueva chequera

COMPRAR_DOLAR: 
    Se solicito realizar la transacción para comprar dólares, pero solo lo pueden hacer los clientes que tengan cuenta en dólares.

TRANSFERENCIA_ENVIADA: 
    Solo se puede en pesos y lo que tenga en caja de ahorro y cuenta corriente debe poder pagar la comisión que se cobra.

TRANSFERENCIA_RECIBIDA: 
    Sólo en pesos y tener presente que va a estar rechaza si no estuvo autorizada.



SALIDA:
    LA MEJOR FORMA DE ABORDAR ESTE PROBLEMA ES GENERAR UNA APLICACIÓN QUE RECIBA COMO INPUT LA INFORMACIÓN DEL TPS, LA PROCESE Y EMITA UN REPORTE QUE SEA CAPAZ DE MOSTRAR LA RAZÓN DE PORQUE ESTAS TRANSACCIONES FUERON RECHAZADAS PARA PONERLA A DISPOSICIÓN DEL EQUIPO DE ATENCIÓN AL CLIENTE. SI SON ACEPTADAS SIMPLEMENTE SE AGREGA AL REPORTE LA TRANSACCIÓN QUE SE HIZO SIN DETALLE PARTICULAR, DE ESTA FORMA QUEDARA COMPLETO EL INFORME.
    EN EL REPORTE SE DEBE INCLUIR EL NOMBRE DE CLIENTE, NÚMERO, DNI, DIRECCIÓN Y PARA CADA TRANSACCIÓN LA FECHA , EL TIPO DE OPERACIÓN, EL ESTADO, EL MONTO Y RAZÓN POR LA CUAL SE RECHAZÓ (VACÍO EN CASO DE SER ACEPTADA).
'''


# Función que compruebe el formato del archivo JSON

# Uso de clases para procesar los datos


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


class Client:
    def __init__(self, dictJSON, dictRestrictions):
        self.number = dictJSON["numero"]
        self.name = dictJSON["nombre"]
        self.lastname = dictJSON["apellido"]
        self.dni = dictJSON["DNI"]
        self.adress = Adress(dictJSON)
        self.transactions = []
        self.reason = []
        for i in range(len(dictJSON["transacciones"])):
            self.transactions.append(Transaction(dictJSON,dictRestrictions,i))
          
    def dataToHTML(self):
        HTML = '<!DOCTYPE html>\n<html>\n<head>\n\t<meta charset="utf-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1">\n\t<title>Informe</title>\n</head>\n<body>'
        HTML += '\n\t<div class="container">\n\t\t<h1 class="fullname">{} {}</h1>\n\t\t<h4 class="number">{}</h4>\n\t\t<h4 class="direction">{}</h4>'.format(self.name,self.lastname,self.number,self.adress.__str__())
        for i in range(len(self.transactions)):
            REASON = ''
            if self.transactions[i].state == "RECHAZADA":
                if self.transactions[i].type == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
                    REASON = self.transactions[i].validateMaxWhithdrawls()
                elif self.transactions[i].type == "ALTA_TARJETA_CREDITO":
                    REASON = self.transactions[i].validateCreditCardsMax()
                elif self.transactions[i].type == "ALTA_CHEQUERA":
                    REASON = self.transactions[i].validateCheckbooks()
                elif self.transactions[i].type == "COMPRAR_DOLAR":
                    REASON = self.transactions[i].validateAccountUSD()
                elif self.transactions[i].type == "TRANSFERENCIA_ENVIADA":
                    REASON = self.transactions[i].validateTransferSend()
                elif self.transactions[i].type == "TRANSFERENCIA_RECIBIDA":
                    REASON = self.transactions[i].validateTransferReceived()
            HTML += '\n\t\t<div class="transaction">\n\t\t\t<h4 class="transaction-numbre">#{}</h4>\n\t\t\t<ul class="data">\n\t\t\t\t<li class="date">{}</li>\n\t\t\t\t<li class="operation">{}</li>\n\t\t\t\t<li class="state">{}</li>\n\t\t\t\t<li class="amount">{}</li>\n\t\t\t\t<li class="rejectionReason">{}</li>\n\t\t\t</ul>\n\t\t</div>'.format(self.transactions[i].number,self.transactions[i].date,self.transactions[i].type,self.transactions[i].state,self.transactions[i].amount,REASON)
        
        HTML += '\n\t</div>\n</body>\n</html>'
        return HTML
    

class Restrictions:
    def __init__(self, dictJSON, dictRestrictions):
        self.CreditCardsMax     = dictRestrictions[dictJSON["tipo"]]["CreditCardsMax"]
        self.AccountUSD         = dictRestrictions[dictJSON["tipo"]]["AccountUSD"]
        self.CheckingAccount    = dictRestrictions[dictJSON["tipo"]]["CheckingAccount"]
        self.MaxWhithdrawls     = dictRestrictions[dictJSON["tipo"]]["MaxWhithdrawls"]
        self.Checkbooks         = dictRestrictions[dictJSON["tipo"]]["Checkbooks"]
        self.TransferFee        = dictRestrictions[dictJSON["tipo"]]["TransferFee"]
        self.MaxTranferReceived = dictRestrictions[dictJSON["tipo"]]["MaxTranferReceived"]
 
class Adress:
    def __init__(self, dictJSON):
        self.street = dictJSON["calle"]
        self.number = dictJSON["numero"]
        self.city = dictJSON["ciudad"]
        self.province = dictJSON["provincia"]
        self.country = dictJSON["pais"]
    
    def __str__(self):
        return '{} {}, {}, {}, {}'.format(self.street,self.number,self.city,self.province,self.country)

class Transaction:
    def __init__(self,dictJSON,dictRestrictions,i):
        self.state = dictJSON["transacciones"][i]["estado"]
        self.type = dictJSON["transacciones"][i]["tipo"]
        self.accountNumber = dictJSON["transacciones"][i]["cuentaNumero"]
        self.dailyQuotaLeft = dictJSON["transacciones"][i]["cupoDiarioRestante"]
        self.amount = dictJSON["transacciones"][i]["monto"]
        self.date = dictJSON["transacciones"][i]["fecha"]
        self.number = dictJSON["transacciones"][i]["numero"]
        self.accountBalance = dictJSON["transacciones"][i]["saldoEnCuenta"]
        self.numberCreditCards = dictJSON["transacciones"][i]["totalTarjetasDeCreditoActualmente"]
        self.numberCheckbooks =dictJSON["transacciones"][i]["totalChequerasActualmente"]
        self.restrictions = Restrictions(dictJSON,dictRestrictions)

    def validateMaxWhithdrawls(self):
        if self.amount>self.dailyQuotaLeft:
            return 'Amigo ya retiraste demasiaaaado culiaaaaaaaaa'
        elif self.accountBalance - self.amount < -self.restrictions.CheckingAccount:
            return 'Amigo queres plata grati?'
        else:
            return False
    
    def validateCreditCardsMax(self):
        if self.numberCreditCards == self.restrictions.CreditCardsMax:
            return 'Flaco ya tenes una baaaanda de tarjetas'
        else:
            return False

    def validateCheckbooks(self):
        if self.numberCheckbooks == self.restrictions.Checkbooks:
            return 'Flaco ya tenes una baaaanda de chequeras'
        else:
            return False

    def validateAccountUSD(self):
        if self.restrictions.AccountUSD:
            return False
        else:
            return 'Pobre no pode comprar USD pui pui'

    def validateTransferSend(self):
        if self.accountBalance - self.amount - self.amount*self.restrictions.TransferFee < -self.restrictions.CheckingAccount:
            return 'Flaco no podes mandar plata que no tenes'
        else:
            return False
        
    def validateTransferReceived(self):
        if self.restrictions.MaxTranferReceived:
            if self.amount > self.restrictions.MaxTranferReceived:
                return 'Flaco no te pueden mandar tanta plata ¿Vendes droga?'
            else:
                return False
        else:
            return False


cliente_1= Client(A,ACCOUNTS_RESTRICTIONS)
print(cliente_1.dataToHTML())

