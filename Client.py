class Client:
    
    
    def __init__(self,id,fname,lname,balance):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.balance = balance

    #function returns full name of costumer
    
    def get_balance(self):
        return self.balance
    
    def get_lname(self):
        return self.lname
    
    def get_fname(self):
        return self.fname
        
    def get_id(self):
        return self.id