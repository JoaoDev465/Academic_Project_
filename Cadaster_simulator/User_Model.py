class User_Model:
    def __init__(self):
        self.id = 0
        self.nome = ""
        self.cpf = ""
        self.email = ""
        self.funcao = ""
        self.idade = 0

    def user (self):
        self.id =int(input("Id"))
        self.nome = input("Nome: ")
        self.cpf = input("CPF: ")
        self.email = input("Email: ")
        self.funcao = input("função: ")
        self.idade = input("Idade: ")
