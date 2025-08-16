


class Loja:
    def __init__(self):
        self.value = 0

    def venda(self):
        while True:
            print("Bem vindo ao Sistema de vendas do João Marcelo")
            print("-------------------------")
            value = int(input("entre com o valor:"))
            self.value = value
            print("-------------------------")

            try:
                order = float(input("entre com a quantidade de parcelas:"))
                if order <= 4:
                    print(f"o valor da compra com nenhuma parcela será {value} ")
                    break
                elif order < 6:
                    result =((self.value * 4) / 100) + self.value
                    installments_quant = result / order
                    print(f"prestação total de {installments_quant} ")
                    print(f"o valor da compra com {order} parcelas será de {result:.2f} ")
                    break
                elif order  < 9:
                    result =((self.value * 8) / 100) + self.value
                    installments_quant = result / order
                    print(f"prestação total de {installments_quant} ")
                    print(f"o valor da compra com {order} parcelas será de {result:.2f} ")
                    break
                elif order  < 13:
                    result =((self.value * 16) / 100) + self.value
                    installments_quant = result / order
                    print(f"prestação total de {installments_quant} ")
                    print(f"o valor da compra com {order} parcelas será de {result:.2f} ")
                    break
                elif order >= 13:
                    result =((self.value * 32) / 100) + self.value
                    installments_quant = result / order
                    print(f"prestação total de {installments_quant} ")
                    print(f"o valor da compra com {order} parcelas será de {result:2f} ")
                    break
                else:
                    print("numero de parcelas invalido, tente novamente")
                    continue

            except ValueError:
                print("o input aceitada apenas numero, sem especaços ou caracteres")

if __name__ == "__main__":
    banana = Loja()
    banana.venda()