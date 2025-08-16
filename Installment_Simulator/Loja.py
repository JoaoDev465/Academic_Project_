
from time import sleep


class Loja:
    def __init__(self):
        self.value = 0

    def venda(self):
        while True:
            print("Bem vindo a Flex Computer")
            sleep(1)
            print("-------------------------")
            sleep(1)
            value = int(input("entre com o valor:"))
            self.value = value
            print("-------------------------")

            try:
                order = float(input("entre com a quantidade de parcelas:"))
                if order <= 4:
                    print(f"o valor da compra com {order} parcelas será {self.value:.2f} ")
                    break
                elif order >=4 and order < 6:
                    result =((self.value * 4) / 100) + self.value
                    print(f"o valor da compra com {order} parcelas será de {result:.2f} ")
                    break
                elif order >=6 and order < 9:
                    result =((self.value * 8) / 100) + self.value
                    print(f"o valor da compra com {order} parcelas será de {result:.2f} ")
                    break
                elif order >=9 and order < 13:
                    result =((self.value * 16) / 100) + self.value
                    print(f"o valor da compra com {order} parcelas será de {result:.2f} ")
                    break
                elif order >= 13:
                    result =((self.value * 32) / 100) + self.value
                    print(f"o valor da compra com {order} parcelas será de {result:.2f} ")
                    break
                else:
                    print("numero de parcelas invalido, tente novamente")
                    continue

            except ValueError:
                print("o input aceitada apenas numero, sem especaços ou caracteres")
