import math

#Exercício 1

def celsius_para_fahrenheit(C):
    """Converte a temperatura de graus Celsius para Fahrenheit;
    float -> float"""
    F = (9*C/5) + 32
    return F

#Exercício 2

def horario_despertador(ha,hd):
    """Calcula em qual horário um despertador deve tocar a partir da hora atual
    e de quantas horas após o instante atual o despertador vai tocar;
    int, int -> int"""
    horario = (ha + hd)% 24
    return horario

#Exercício 3

def torricelli(h):
    """Calcula, a partir da altura, a velocidade em que a bola de gude
    atinge o chão após uma queda livre;
    float -> float"""
    g = 9.81
    v = math.sqrt(2*g*h)
    return v

#Exercício 4

def sistema_linear_2d(a,b,c,d,y1,y2):
    """Calcula a solução de um sistema 2 por 2 (x1,x2) a partir dos valores de
    a,b,c,d,y1,y2;
    float, float, float, float, float,float -> str"""
    D = (a*d) - (b*c)
    Dx1 = (y1*d) - (y2*b)
    Dx2 = (y2*a) - (y1*c)
    x1 = Dx1 / D
    x2 = Dx2 / D
    return f"x1 = {x1}, x2 = {x2}"

#Exercício 5

def horario_chegada(h,m,d):
    """Calcula o horário de chegada de uma viagem a partir do horário atual,
    dado em horas e minutos e do tempo de duração da viagem, dado em minutos;
    int, int, int -> str"""
    hora_atual_minutos = h*60 + m
    horas_chegada = ((hora_atual_minutos + d) // 60) % 24
    minutos_chegada = (hora_atual_minutos +d) % 60
    return f"{horas_chegada}h{minutos_chegada}min"

#Exercíco 6

def corrente(Vf,R1,R2,R3):
    """Calcula a corrente elétrica que passa pela fonte de um circuito com
    fonte de tensão Vf, resistências R1, R2 e R3;
    float, float, float, float -> float"""
    Req = R1 + ((R2 * R3) / (R2 + R3))
    I = Vf / Req
    return I


