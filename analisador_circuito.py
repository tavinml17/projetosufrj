V = float(input('Digite o valor da tensão: '))
R1 = float(input('Digite o valor da resistência do resistor 1: '))
R2 = float(input('Digite o valor da resistência do resistor 2: '))
R3 = float(input('Digite o valor da resistência do resistor 3: '))

def calcular_corrente(V,R1,R2,R3):
    """Calcula a corrente do circuito;
    float, float, float, float -> str"""
    req = R1 + R2 + R3
    i = V/req
    return f'Corrente do circuito: {i:.2f} A'
def calcular_tensoes(V,R1,R2,R3):
    """Calcula as tensões em cada resistor do circuito;
    float, float, float, float -> str"""
    req = R1 + R2 + R3
    i = V/req
    V1 = R1*i
    V2 = R2*i
    V3 = R3*i
    return f'Tensão em R1: {V1:.2f} V / Tensão em R2: {V2:.2f} V / Tensão em R3: {V3:.2f} V'
def calcular_potencias(V,R1,R2,R3):
    """Calcula as potências dissipadas em cada resistor do circuito;
    float, float, float, float -> str"""
    req = R1 + R2 + R3
    i = V/req
    P1 = R1*(i**2)
    P2 = R2*(i**2)
    P3 = R3*(i**2)
    return f'Potência dissipada em R1: {P1:.2f} W / Potência dissipada em R2: {P2:.2f} W / Potência dissipada em R3: {P3:.2f} W'
if R1 < 0 or R2 < 0 or R3 < 0:
    print('Valor(es) de resistência(s) inválido(s) [negativo(s)]')
elif V == 0:
    print('Valor de tensão inválido [zero]')
else:
    print(calcular_corrente(V,R1,R2,R3))
    print(calcular_tensoes(V,R1,R2,R3))
    print(calcular_potencias(V,R1,R2,R3))


