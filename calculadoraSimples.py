# 1- Calculadora Simples (Iniciante)
# Implemente uma calculadora simples que possa realizar operações básicas, como adição, subtração, multiplicação e divisão. Isso ajudará você a entender os conceitos fundamentais da linguagem Python.

numeroEscolhido = -1

while numeroEscolhido != 5:
    print("----------- Menu -----------\n")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair\n")

    numeroEscolhido = int(input("Digite o número da opção desejada: "))
    if numeroEscolhido != 5:
        if numeroEscolhido > 0 and numeroEscolhido < 5:
            primeiroNumero = int(input("Digite o primeiro número da operação: "))
            segundoNumero = int(input("Digite o segundo número da operação: "))
            if numeroEscolhido == 1:
                adicao = primeiroNumero + segundoNumero
                print(f"Resultado: {primeiroNumero} + {segundoNumero} = {adicao}")
            elif numeroEscolhido == 2:
                subtracao = primeiroNumero - segundoNumero
                print(f"Resultado: {primeiroNumero} - {segundoNumero} = {subtracao}")
            elif numeroEscolhido == 3:
                multiplicacao = primeiroNumero * segundoNumero
                print(f"Resultado: {primeiroNumero} * {segundoNumero} = {multiplicacao}")
            elif numeroEscolhido == 4:
                if segundoNumero == 0:
                    print("Não é possível realizar esta operação. Tente Novamente!")
                else:
                    divisao = primeiroNumero / segundoNumero
                    print(f"Resultado: {primeiroNumero} / {segundoNumero} = {divisao}")
        else:
            print("Número Incorreto. Tente Novamente!")
    else:
        print("Calculadora Encerrada!")


