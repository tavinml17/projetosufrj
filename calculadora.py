print("Possíveis operações:")
print("soma")
print("subtração")
print("multiplicação")
print("divisão")
print("radiciação")
print("Escreva da forma apresentada")
    
operacao = input("Digite a operação: ")
if operacao == 'soma':
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    resultado_soma = valor1 + valor2
    print("Resultado: ", valor1, "+", valor2, "=", resultado_soma)
if operacao == 'subtração':
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    resultado_subtracao = valor1 - valor2
    print("Resultado: ", valor1, "-", valor2, "=", resultado_subtracao)
if operacao == 'multiplicação':
    valor1 = int(input("Digite o primeiro fator: "))
    valor2 = int(input("Digite o segundo fator: "))
    resultado_multiplicacao = valor1 * valor2
    print("Resultado: ", valor1, "x", valor2, "=", resultado_multiplicacao)
if operacao == 'divisão':
    valor1 = int(input("Digite o dividendo: "))
    valor2 = int(input("Digite o divisor: "))
    resultado_divisao = valor1 / valor2
    print("Resultado: ", valor1, "÷ ", valor2, "=", resultado_divisao)
if operacao == 'exponenciação':
    valor1 = int(input("Digite a base: "))
    valor2 = int(input("Digite o expoente: "))
    resultado_exponenciacao = valor1 ** valor2
    print("Resultado: ", valor1, "^", valor2, "=", resultado_exponenciacao)
if operacao == 'radiciação':
    valor1 = int(input("Digite o radicando: "))
    valor2 = int(input("Digite o índice: "))
    indice = 1 / valor2
    resultado_radiciacao = valor1 ** indice
    print("Resultado: ", valor1, "^", "(", indice, ") =", resultado_radiciacao)
