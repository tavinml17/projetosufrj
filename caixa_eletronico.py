quantidade = int(input('Insira a quantidade: '))
notas100 = quantidade // 100
resto = quantidade % 100
notas50 = resto // 50
resto = resto % 50
notas20 = resto // 20
resto = resto % 20
notas10 = resto // 10
resto = resto % 10
notas5 = resto // 5
print("Notas de 100:", notas100, ", Notas de 50:", notas50, ", Notas de 20:", notas20, ", Notas de 10:", notas10, "Notas de 5:", notas5)
