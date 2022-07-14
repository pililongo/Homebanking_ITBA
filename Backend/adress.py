class Adress:
    def __init__(self, dictJSON):
        self.street = dictJSON["calle"]
        self.number = dictJSON["numero"]
        self.city = dictJSON["ciudad"]
        self.province = dictJSON["provincia"]
        self.country = dictJSON["pais"]
    
    def __str__(self):
        return '{} {}, {}, {}, {}'.format(self.street,self.number,self.city,self.province,self.country)