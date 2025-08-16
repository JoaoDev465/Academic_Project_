from User_Model import User_Model
class Data:
    def __init__(self):
        self.User_Model = {}

    def adduser(self,user:User_Model):
        self.User_Model[user.id] = {
            "nome": user.nome,
            "cpf": user.cpf,
            "email": user.email,
            "função": user.funcao

        }
    def removeuser(self):
        id= int(input("insira a Id do user"))
        if  id in self.User_Model:
            del self.User_Model[id]
            print(f"Usuario removido com sucesso Id:{id}")
        else:
            print("não há registro")

