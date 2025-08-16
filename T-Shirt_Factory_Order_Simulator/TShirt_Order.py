

class MenuTShirt:
    def __init__(self):
        self.value = 0
        self.TshirModels = {"MCS":1.80,"MLS":2.10,"MCE":2.95,"MLE":3.20}
        self .transport = {"transportadora": 100.00,"sedex":200.00, "retirar":0.00}

    @staticmethod
    def countdescont(quantidade):
        if quantidade < 20:
            return 0.0
        elif quantidade == 200:
            return 0.5
        elif quantidade <= 2000:
            return 0.7
        elif  quantidade <= 20000:
             return 0.12
        else:
            print("não aceitamos esse pedido")
            return None





    def menu(self):
        print("Bem vindo à Fábrica de Camisetas do João Marcelo")

        print("Entre com o modelo desejado")
        print("MCS - Manga Curta Simples")
        print("MLS - Manga Longa Simples")
        print("MCE - Manga Curta Com Estampa")
        print("MLE - Manga Longa Com Estampa")

        while True:
            try:
                chose_model = input("Entre com o modelo desejado: ").strip().upper()
                if chose_model not in ["MCS","MLS","MCE","MLE"]:
                    print("modelo invlido tente novamnete")
                    continue
                order = int(input("Entre com a quantidade: "))
                descont = self.countdescont(order)
                if descont is None:
                    break
                unit_price = self.TshirModels[chose_model]
                total_price = unit_price * order
                total_descont = total_price *   descont
                total_price_descont =  total_price - total_descont
                print(f"voce escolheu a camiseta do modelo{chose_model}")
                print(f"---------------------")
                option = input("Entre com o transporte:(sedex,transportadora ou retirar): ").strip().lower()
                if option not in ["transportadora","retirar","sedex"]:
                    self.transport += option
                    print("transporte invlido tente novamente")
                    continue
                else :
                    price_whit_transport = self.transport[option]

                    print(f"total de R$ {total_price_descont + price_whit_transport:.2f} , modelo {chose_model}  com desconto de R$ {total_descont:.2f} e transporte {option}:{price_whit_transport}")
                    break

            except ValueError:
                print("Erro,tente novamente")
                break
