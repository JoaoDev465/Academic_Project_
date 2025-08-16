from Data import Data
class GetUsers:
    def __init__(self,data_admin):
        self.get = data_admin
        self.Chose = ""

    def getall(self):
        for user_id,dados in self.get.User_Model.items():
            print(user_id,dados)

    def getusersforfunction(self):
        function = input("digite a funçao do usuario").strip().lower()
        encontrados = False
        for user_id,dados in self.get.User_Model.items():
            if dados.get('função','').lower() == function:
                print(user_id,dados)
                encontrados = True
            if not encontrados:
                print("nenhuma funçao de usuario encontrada")


    def getusersforid(self):
        while True:
            try:
                user_id = int(input("digite o Id:").strip())
            except ValueError:
                print("apenas numeros,tente novamente")
                continue
            if user_id  in self.get.User_Model:
                dados = self.get.User_Model[user_id]
                self.printuser(user_id,dados)
            else:
                print("usuario não encontrado")
                break

    def printuser(self,user_id,dados):
        print(f"id:{user_id}")
        print(f"cpf:{dados.get('cpf')}")
        print(f"email:{dados.get('email')}")
        print(f"funcao:{dados.get('funcao')}")
