circuito = []
correntes = []
potencias = []
aparelhos = []

#Recebe o valor da tensão (em volts) do circuito
while True:
    serie_paralelo = input("Digite o tipo de circuito (série/paralelo): ").lower()
    if serie_paralelo in ["série", "paralelo"]:
        break  # Se a entrada for válida, sai do loop
    else:
        print("Por favor, digite 'série' ou 'paralelo'.")
tensao = float(input("Digite o valor da tensão do circuito (em volts): "))

while True:
    #Pergunta se o usuário quer cadastrar um novo aparelho
    cadastro = input("Quer cadastrar um novo aparelho no circuito? (sim/não): ")
    if cadastro.lower() == "não":
        break

    try:
        #Recebe as informações dos aparelhos
        nome = input("Digite o nome do aparelho: ")
        qtd_aparelho = int(input("Digite o número de aparelhos iguais: "))
        potencia = float(input("Digite a potência do aparelho (em watts): "))

        #Trata as entradas de valores de potência inválidos (menores ou iguais a zero)
        if potencia <= 0:
            print("Valor de potência inválido!")
            continue

    #Trata as entradas de valores inválidos
    except ValueError:
        print("Digite um número válido!")
        continue

    #Calcula a corrente total para um certo tipo de aparelho
    corrente = (potencia * qtd_aparelho) / tensao
    
    #Atualiza a lista de correntes, potências e quantidade de aparelhos
    correntes.append(corrente)
    potencias.append(potencia * qtd_aparelho)
    aparelhos.append(qtd_aparelho)

#Calcula a soma das potências, das correntes e da quantidade de aparelhos do circuito
soma_potencias = sum(potencias)
soma_correntes = sum(correntes)
soma_aparelhos = sum(aparelhos)

#Calcula a corrente total do circuito caso ele seja em série
corrente_serie = soma_potencias / tensao

#Calcula a amperagem adequada do disjuntor necessitado para o circuito
disjuntor_paralelo = soma_correntes * 1.25
disjuntor_serie = corrente_serie * 1.25

#Faz o resumo geral dos resultados obtidos
if serie_paralelo == "serie":
    print("\nResumo Geral: ")
    print("------------------------------------------------------------------------")
    print(f"Número de aparelhos do circuito: {soma_aparelhos}")
    print(f"Tensão do circuito: {tensao} V")
    print(f"Corrente total do circuito em série: {corrente_serie:.2f} A")
    print(f"Potência total do circuito em série: {soma_potencias:.2f} W")
    print(f"Disjuntor adequado para o circuito: {disjuntor_serie:.2f} A")
    print("------------------------------------------------------------------------\n")
else:
    print("\nResumo Geral: ")
    print("------------------------------------------------------------------------")
    print(f"Número de aparelhos do circuito: {soma_aparelhos}")
    print(f"Tensão do circuito: {tensao} V")
    print(f"Corrente total do circuito em paralelo: {soma_correntes:.2f} A")
    print(f"Potência total do circuito em paralelo: {soma_potencias:.2f} W")
    print(f"Disjuntor adequado para o circuito: {disjuntor_paralelo:.2f} A")
    print("------------------------------------------------------------------------\n")