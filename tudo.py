# a mudança
m=int(input("Ângulo: "))

#manha
if m < 90 or m == 360:
    print("Bom dia!")
#tarde
elif m < 180:
    print("Boa tarde!")
#noite
elif m < 270:
    print("Boa noite!")
#madrugada
else:
    print("Boa madrugada")
    '''
    6h - inicio manha - 0°
    12h - inicio tarde - 90°
    18h - inicio noite - 180°
    24h - inicio da madrugada - 270°



    madrugada entre 00h e nascer do sol
    15° = 1h 
    '''
    
    k=int(input("Digite k: "))
l=int(input("Digite l: "))
m=int(input("Digite m: "))
n=int(input("Digite n: "))
d=int(input("Digite d: "))

''' 
k pancada no rosto
l prender o rabo
m pisotear a pata
n chamar a mãe
d total de dragoes
'''


d1=d%k
d2=d%l
d3=d%m
d4=d%n

print(d1,d2,d3,d4)



#area e perimetro

from math import pi
r=int(input("raio do circulo: "))

def area_circulo(r):
    area = pi*r**2
    return area

def comp_circunferencia(r):
    comprimento = 2*pi*r
    return comprimento


print(area_circulo(r), comp_circunferencia(r))

n = int(input('n: '))
min_esforco = 9999999
min__trilha = 0
for i in range(1, n + 1):
    m = int(input('M: '))
    h = []
    for _ in range(m):
        h.append(int(input()))
    print(h)
    esforco_ida = 0
    esforco_volta = 0
    a = h[0]
    for k in range(1, m):
        b = h[k]
        if a <= b:
            esforco_ida += b - a
        else:
            esforco_volta += a - b
        a = b
    esforco = min(esforco_ida, esforco_volta)
    if min_esforco > esforco:
        min_esforco = esforco
        min_trilha = i
print(min_trilha)  






aeroportos = int(input())
voos = int(input())
lista_voos = []
for i in range(voos):
    aerox = int(input())
    aeroy = int(input())
    if aerox and aeroy == 0:
        break

    
    
