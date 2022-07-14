class Restrictions:
    def __init__(self, dictJSON, dictRestrictions):
        self.CreditCardsMax     = dictRestrictions[dictJSON["tipo"]]["CreditCardsMax"]
        self.AccountUSD         = dictRestrictions[dictJSON["tipo"]]["AccountUSD"]
        self.CheckingAccount    = dictRestrictions[dictJSON["tipo"]]["CheckingAccount"]
        self.MaxWhithdrawls     = dictRestrictions[dictJSON["tipo"]]["MaxWhithdrawls"]
        self.Checkbooks         = dictRestrictions[dictJSON["tipo"]]["Checkbooks"]
        self.TransferFee        = dictRestrictions[dictJSON["tipo"]]["TransferFee"]
        self.MaxTranferReceived = dictRestrictions[dictJSON["tipo"]]["MaxTranferReceived"]