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