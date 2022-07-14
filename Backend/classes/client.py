from adress import Adress
from transaction import Transaction
from restrictions import Restrictions
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
        HTML = '<!DOCTYPE html>\n<html>\n<head>\n\t<meta charset="utf-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1">\n\t<link rel="stylesheet" href="style.css">\n\t<title>Informe</title>\n</head>\n<body>'
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
            HTML += '\n\t\t<div class="transaction">\n\t\t\t<h4 class="transaction-nombre">#{}</h4>\n\t\t\t<ul class="data">\n\t\t\t\t<li class="date">{}</li>\n\t\t\t\t<li class="operation">{}</li>\n\t\t\t\t<li class="state">{}</li>\n\t\t\t\t<li class="amount">{}</li>\n\t\t\t\t<li class="rejectionReason">{}</li>\n\t\t\t</ul>\n\t\t</div>'.format(self.transactions[i].number,self.transactions[i].date,self.transactions[i].type,self.transactions[i].state,self.transactions[i].amount,REASON)
        
        HTML += '\n\t</div>\n</body>\n</html>'
        return HTML