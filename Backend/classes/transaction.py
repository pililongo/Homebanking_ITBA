from restrictions import Restrictions

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