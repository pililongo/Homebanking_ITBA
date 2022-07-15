class Client:
    def __init__(self, dictJSON, dictRestrictions):
        self.number = dictJSON["numero"]
        self.name = dictJSON["nombre"]
        self.lastname = dictJSON["apellido"]
        self.dni = dictJSON["dni"]
        self.adress = Adress(dictJSON)
        self.transactions = []
        for i in range(len(dictJSON["transacciones"])):
            self.transactions.append(Transaction(dictJSON,dictRestrictions,i))

    def dataToHTML(self):
        HTML = '<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1">\n\t<link rel="stylesheet" href="style.css">\n\t<title>Informe</title>\n</head>\n<body>'
        HTML += '\n\t<div class="container">\n\t\t<h1 class="fullname">{} {}</h1>\n\t\t<h4 class="dni">{}</h4>\n\t\t<h4 class="number">{}</h4>\n\t\t<h4 class="direction">{}</h4>'.format(self.name,self.lastname,self.dni,self.number,self.adress.__str__())
        for i in range(len(self.transactions)):
            REASON = ''
            if self.transactions[i].state == "RECHAZADA":
                if self.transactions[i].type == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
                    REASON = self.transactions[i].validateMaxWhithdrawls()
                elif self.transactions[i].type == "ALTA_TARJETA_CREDITO":
                    REASON = self.transactions[i].validateCreditCardsMax()
                elif self.transactions[i].type == "ALTA_CHEQUERA":
                    REASON = self.transactions[i].validateCheckbooks()
                elif self.transactions[i].type == "COMPRA_DOLAR":
                    REASON = self.transactions[i].validateAccountUSD()
                elif self.transactions[i].type == "TRANSFERENCIA_ENVIADA":
                    REASON = self.transactions[i].validateTransferSend()
                elif self.transactions[i].type == "TRANSFERENCIA_RECIBIDA":
                    REASON = self.transactions[i].validateTransferReceived()
            HTML += '\n\t\t<div class="transaction {}">\n\t\t\t<h4 class="transaction-number">#{}</h4>\n\t\t\t<ul class="data">\n\t\t\t\t<li class="date">{}</li>\n\t\t\t\t<li class="operation">{}</li>\n\t\t\t\t<li class="amount">{}</li>\n\t\t\t\t<li class="state">{}</li>\n\t\t\t\t<li class="rejectionReason">{}</li>\n\t\t\t</ul>\n\t\t</div>'.format(self.transactions[i].state.lower(),self.transactions[i].number,self.transactions[i].date,self.transactions[i].type,self.transactions[i].amount,self.transactions[i].state,REASON)

        HTML += '\n\t</div>\n</body>\n</html>'
        return HTML

class Adress:
    def __init__(self, dictJSON):
        self.street = dictJSON["direccion"]["calle"]
        self.number = dictJSON["direccion"]["numero"]
        self.city = dictJSON["direccion"]["ciudad"]
        self.province = dictJSON["direccion"]["provincia"]
        self.country = dictJSON["direccion"]["pais"]

    def __str__(self):
        return '{} {}, {}, {}, {}'.format(self.street,self.number,self.city,self.province,self.country)

class Restrictions:
    def __init__(self, dictJSON, dictRestrictions):
        self.CreditCardsMax     = dictRestrictions[dictJSON["tipo"]]["CreditCardsMax"]
        self.AccountUSD         = dictRestrictions[dictJSON["tipo"]]["AccountUSD"]
        self.CheckingAccount    = dictRestrictions[dictJSON["tipo"]]["CheckingAccount"]
        self.MaxWhithdrawls     = dictRestrictions[dictJSON["tipo"]]["MaxWhithdrawls"]
        self.Checkbooks         = dictRestrictions[dictJSON["tipo"]]["Checkbooks"]
        self.TransferFee        = dictRestrictions[dictJSON["tipo"]]["TransferFee"]
        self.MaxTranferReceived = dictRestrictions[dictJSON["tipo"]]["MaxTranferReceived"]

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
            return 'Rechazado por cupo diario de extracción'
        elif self.accountBalance - self.amount < -self.restrictions.CheckingAccount:
            return 'Rechazado por falta de dinero'
        else:
            return 'Rechazado por error en el sistema Legacy'

    def validateCreditCardsMax(self):
        if self.numberCreditCards == self.restrictions.CreditCardsMax:
            return 'Rechazado por máximo de tarjetas de crédito alcanzado'
        else:
            return 'Rechazado por error en el sistema Legacy'

    def validateCheckbooks(self):
        if self.numberCheckbooks == self.restrictions.Checkbooks:
            return 'Rechazado por máximo de chequeras alcanzado'
        else:
            return 'Rechazado por error en el sistema Legacy'

    def validateAccountUSD(self):
        if self.restrictions.AccountUSD:
            if self.accountBalance - self.amount < -self.restrictions.CheckingAccount:
                return 'Rechazado por falta de fondos'
            return 'Rechazado por error en el sistema Legacy'
        else:
            return 'Rechazado por falta de caja de ahorro en dólares'

    def validateTransferSend(self):
        if self.accountBalance - self.amount - self.amount*self.restrictions.TransferFee < -self.restrictions.CheckingAccount:
            return 'Rechazado por falta de fondos'
        else:
            return 'Rechazado por error en el sistema Legacy'

    def validateTransferReceived(self):
        if self.restrictions.MaxTranferReceived:
            if self.amount > self.restrictions.MaxTranferReceived:
                return 'Rechazado por máximo de transferencia recibida sin previo aviso'
            else:
                return 'Rechazado por error en el sistema Legacy'
        else:
            return 'Rechazado por error en el sistema Legacy'