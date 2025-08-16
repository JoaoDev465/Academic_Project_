from Cadaster_simulator.User_Model import User_Model
from Data import Data
from Admin_users import GetUsers
class Register:
    def __init__(self):
        self.data_Admin = Data()
        self.getusers = GetUsers(data_admin=self.data_Admin)

    def optionstogetuser(self,option):
        if option == '1':
            self.getusers.getall()
        elif option == '2':
            self.getusers.getusersforid()
        elif option == '3':
            self.getusers.getusersforfunction()
        elif option == '4':
            print("encerrando")
            return None
        else:
            print("opcao invalida")
            return None



    def Options_Cadaster(self,option):
        if  option == '1':
            user = User_Model()
            user.user()
            self.data_Admin.adduser(user)
            print("usuario cadastrado com sucesso")
        elif option == '2':
          self.menu_get_users()
        elif option == '3':
            self.data_Admin.removeuser()
        elif option == '4':
            print("encerrando")
            return None
        else:
            print('Opção invalida')
            return None



    def register_user(self):
        print("Bem vindo a Empresa do João Marcelo")
        print("------------------------------------")
        print("           MENU PRINCIPAL           ")
        print("------------------------------------")
        print("Escolha a opção desejada:")
        print("1 - Cadastrar Funcionários")
        print("2 - Consultar Funcionário(s)")
        print("3 - Remover Funcionário")
        print("4 - Sair")
        while True:
            try:
                option = input("insira a opção").strip()
                self.Options_Cadaster(option)
                if option == '4':
                    break
                else:
                    continue
            except ValueError:
                print("")
                break
    def menu_get_users(self):
        while True:
            try:
                print("\n-------- MENU CONSULTAR FUNCIONÁRIO ------------------")
                print("Escolha a opção desejada:")
                print("1 - Consultar Todos os Funcionários")
                print("2 - Consultar Funcionário por id")
                print("3 - Consultar Funcionário(s) por setor")
                print("4 - Retornar")
                option = input("digite uma opçao:").strip()
                self.optionstogetuser(option)
                if option == '4':
                    break
            except ValueError:
                print("Error")



if __name__ == '__main__':
    register = Register()
    register.register_user()