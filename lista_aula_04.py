import math

#Exercício 1

def validar_votar(idade):
    """A partir da idade informada, retorna se é possível votar (para idades maiores ou
    iguais a 18 anos) ou não (para idades menores que 18 anos);
    int -> str"""
    resultado = idade >= 18
    return f"A pessoa é elegível para votar? {resultado}"

#Exercício 2

def bissexto(ano):
    """Calcula se um ano é considerado bissexto a partir do ano informado;
    int -> str"""
    calc_bissexto = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
    return f"O ano é bissexto? {calc_bissexto}"

#Exercício 3

def ponto_circulo(x,y,raio):
    """Verifica se um determinado ponto está dentro de um círculo de contro na origem a partir do
    raio;
    float, float, float -> bool"""
    dentro = math.sqrt(x**2 + y**2)
    resultado = dentro < raio
    return resultado

#Exercício 4

def validar_capacidade(pessoas,carros):
    """Verifica se a quantidade de carros com capacidade de 5 lugares suporta o número de pessoas
    dado;
    int, int -> bool"""
    nlugares = carros * 5
    capacidade = (nlugares >= pessoas) and pessoas != 0
    return capacidade

#Exercício 5

# a) 1 * True = 1, tipo int
# b) 0 * True = 0, tipo int
# c) 1 * False = 0, tipo int
# d) 4.3 * True = 4.3, tipo float
# e) 5.6 * False = 0, tipo float
# f) 'aluno' * True = 'aluno', tipo str
# g) 'aluno' * False = '', tipo str
# h) 'aluno' * 0 = '', tipo str
# i) 'aluno' * 1 = 'aluno', tipo str
# j) 'Universidade' * True + 'Estácio' * True = 'UniversidadeEstácio', tipo str
# k) 'Universidade' * True + 'Estácio' * False = 'Universidade', tipo str
# l) 'Universidade' * False + 'Estácio' * True = 'Estácio', tipo str
# m) 'Universidade' * False + 'Estácio' * False = '', tipo str

#Exercício 6

def faixa_temp(C):
    """Recebe um valor de temperatura em graus Celsius e retorna uma descrição embasada em
    uma faixa de temperatura;
    float -> str"""
    return ('Muito frio' * (C < 10)) + ('Frio' * (C >= 10 and C<= 17)) + ('Agradável' * (C >= 18 \
    and C <= 25)) + ('Quente' * (C >= 26 and C <= 35)) + ('Muito quente' * (C > 35))

#Exercício 7

# a) True, já que "a" é do tipo string.
# b) True, já que "b" é do tipo float.
# c) False, já que "c" não é do tipo int, e sim do tipo float.
# d) True, já que "d" é do tipo bool.
# e) True, já que "e" é do tipo float (string convertida para float).


