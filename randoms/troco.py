def gerar_troco(custo, pago):
    troco = pago - custo
    if troco > 0:
        coins_1 = troco // 1
        coins_05 = (troco % 1) // 0.5
        coins_025 = ((troco % 1) % 0.5) // 0.25
        coins_010 = (((troco % 1) % 0.5) % 0.25) // 0.10
        coins_005 = ((((troco % 1) % 0.5) % 0.25) % 0.10) // 0.05

        moedas = [coins_1, coins_05, coins_025, coins_010, coins_005]
        label = ["1 real", "50 centavos", "25 centavos", "10 centavos", "5 centavos"]
        moedas_n = []

        for i in range(len(moedas)):
            if moedas[i] > 0:
                moedas_n.append(f"{label[i]} : {moedas[i]}")

        print(f"1 real: {coins_1}, 50 centavos: {coins_05}, 25 centavos: {coins_025}, 10 centavos: {coins_010}, 5 centavos: {coins_005}")

        print("Outra forma:")
        for item in moedas_n:
            print(item)


    elif troco == 0:
        print("Não há troco")
    else:
        print("Não há dinheiro o suficiente")



gerar_troco(45.65,589.95)