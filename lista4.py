#Exercício 1

def faixa_idade(atual,nasc):
    """Identifica se uma pessoa é classificada como bebê, criança, adolescente, adulta ou idosa;
        int, int -> str"""
    idade = atual - nasc
    bebe = 'Bebê' * (idade >= 0 and idade <= 3)
    crianca = 'Criança' * (idade >= 4 and idade <= 10)
    adolescente = 'Adolescente' * (idade >= 11 and idade <= 18)
    adulta = 'Adulta' * (idade >= 19 and idade <= 60)
    idosa = 'Idosa' * (idade >= 61)
    return bebe + crianca + adolescente + adulta + idosa

#Exercício 2

def situacao_aluno(p1,p2,tr,qf):
    """Calcula se um aluno será aprovado, reprovado, reprovado por faltas ou fará prova final a partir
        das notas de duas provas, de um trabalho e da quantidade de faltas;
        float, float, float, int -> str"""
    media_notas = (3*p1 + 5*p2 + 2*tr)/10
    aprovado = 'Aprovado' * (media_notas >= 7 and qf <= 15)
    reprovado_nota = 'Reprovado por nota' * (media_notas < 3 and qf <= 15)
    reprovado_falta = 'Reprovado por falta' * (qf > 15)
    prova_final = 'Prova Final' * (media_notas >= 3 and media_notas < 7 and qf <= 15)
    return aprovado + reprovado_nota + reprovado_falta + prova_final

#Exercício 3

def quadrante(x,y):
    """A partir de dois pontos, identifica em qual quadrante ou em qual eixo esse ponto se encontra;
    float, float -> str"""
    origem = 'Na origem' * (x == 0 and y == 0)
    eixox = 'No eixo x' * (x == 0 and y != 0)
    eixoy = 'No eixo y ' * (x != 0 and y == 0)
    pq = 'Primeiro quadrante' * (x > 0 and y > 0)
    sq = 'Segundo quadrante' * (x < 0 and y > 0)
    tq = 'Terceiro quadrante' * (x < 0 and y < 0)
    qq = 'Quarto quadrante' * (x > 0 and y < 0)
    return origem + eixox + eixoy + pq + sq + tq + qq

#Exercício 4

#a) (((10>5 or 3<7) and (True or False and not(False)) or not(8 / 2 == 4) and ('Python' != 'python' or True)))
# (((True or True) and (True or False and True)) or not(True) and (True or True)))
# (True and (True or False) or False and True)
# (True and True or False and True)
# True or False and True
# True or False
# True

#b) ((not((12 - 6 == 6) and (True or False and not(True)) or not(15 % 4 > 1) and (False or True)))
# ((not(True and (True or False and False) or not(True) and (True)))
# ((not(True and (True or False) or False and True))
# ((not(True and True or False and True))
# not(True or False and True)
# not(True or False)
# not(True)
# False

#c) ((not(5 * 2 < 12) or (True and False and not(False)) and not(7 / 2 == 3.5) or ('OpenAI' == 'openai' and True)))
# ((not(True) or (False and True) and not(True) or (False and True))
# False or False and False or False
# False or False or False
# False or False
# False

#Exercício 5 no pdf em anexo (feito no caderno)

