from Client import Client

class Bank :
    def __init__(self):
        self.clients = []
    
    def get_id(self):
        return len(self.clients)+1

    def add_client(self,fname,lname,deposit):
        client = Client(self.get_id(),fname,lname,deposit)
        self.clients.append(client)

    def del_client(self,id):
        self.clients.pop(id)
        for i in range(id,len(self.clients)):
            self.clients[i].set_id(i)
          
    
    def get_assets(self):
        assets = 0
        for client in self.clients:
            assets+=client.get_balance()

        return assets

    def get_clients(self,sort_by=None):
        if sort_by==None:
            return self.clients
        elif sort_by=="name":
            return sorted(self.clients,key=lambda x:x.get_lname())
        elif sort_by=="balance":
            return sorted(self.clients,key=lambda x:x.get_balance(),reverse=True) 
        elif sort_by=="id":
            return sorted(self.clients,key=lambda x:x.get_id())


        
    
