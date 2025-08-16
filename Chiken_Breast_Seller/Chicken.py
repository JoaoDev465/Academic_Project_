class Chiken:
    def __init__(self):
        self.bife = {"P":16, "M":18,"G":22}
        self.frango = {"P":15, "M":17,"G":21}
        self. value = 0

    def menu(self):
        print("------ Bem-vindo à Loja de Marmitas do joão Marcelo ----------")
        print("-----------------------------Cardápio---------------------------")
        print("|  Tamanho  | Bife Acebolado(BA) | Filé de Frango(FF) |")
        print("|-----------|---------------------|---------------------|")
        print("|     P     |       R$ 16.00      |       R$ 15.00      |")
        print("|     M     |       R$ 18.00      |       R$ 17.00      |")
        print("|     G     |       R$ 22.00      |       R$ 21.00      |")
        print("----------------------------------------------------------------")

        while True:
            try:
                orderofmeat = input("Escolha uma opçaõ de carne").strip().lower()
                if orderofmeat not in ["bife","frango"]:
                    print("carne inválifa,tente novamente")
                    continue

                orderofsize = input("agora escolha o tamnho P,M,G").strip().upper()
                if orderofsize not in  ["P", "M", "G"]:
                    print("tamanho inválido, tente novamente")
                    continue

                if orderofmeat == "frango":
                    price = self.frango[orderofsize]
                else:
                    price = self.bife[orderofsize]

                self.value += price
                print(f"o seu pedido foi {orderofmeat.upper()} de tamanho {orderofsize.upper()} e preço {price}")
                chose = input("deseja mais alguma coisa (S,N)").strip().upper()
                if chose != "S":
                    print("agradecemos a compra")
                    print(f"valor total RS {self.value}")
                    break

            except  ValueError:
                print("Erro")
                continue

