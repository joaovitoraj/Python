'''
Supermercado
Maria está participando de um programa de intercâmbio no reino da
Nlogônia. Ela está gostando muito da experiência, e decidiu fazer um
churrasco para suas novas amigas da escola. Como não tem muito

dinheiro, Maria vai fazer uma pesquisa para comprar carne no super-
mercado mais barato que encontrar.

No entanto ela está um pouco confusa para saber qual supermercado
tem o menor preço. O dinheiro na Nlogônia é o Bit, abreviado por B$,

mas não é esse o problema. O problema é que o costume na Nlogô-
nia é informar o preço de uma maneira diferente do que Maria está

acostumada. Os preços são anunciados como “X Bits por Y gramas do
produto”.
Por exemplo o preço de um dado produto é anunciado como sendo B$
24,00 por 250 gramas em um supermercado, B$ 16,00 por 100 gramas

em outro supermercado, B$ 19,00 por 120 gramas em outro supermer-
cado, e assim por diante.

Você pode ajudar Maria? Dados os preços anunciados pelos super-
mercados no bairro em que Maria mora, determine o menor valor que

Maria deve gastar para comprar 1 kilograma (1000 gramas) de carne.
Entrada:

A primeira linha contém um número inteiro N, o número de superme-
rcados próximos à casa de Maria. Em seguida, você deve capturar o

preço da carne P (float) em um supermercado e, em seguida, número
inteiro G, indicando que G gramas de carne custam P Bits para cada
supermercado.
Saída:
Seu programa deve produzir uma única linha, com apenas um número
real, o menor preço para comprar 1 kilograma de carne.

Restrições
• 1 ≤ N ≤ 100
• 0 < P ≤ 1000.00, representado com dois dígitos após o ponto decimal.
• 1 ≤ G ≤ 1000
'''

N=int(input("Digite o número de mercados: "))
lista=[]
for i in range(N):
    print("Mercado", i+1)
    P=float(input("Digite o preço: "))
    G=int(input("Digite a grarmatura: "))
    bit=P/G*1000
    lista.append(bit)
lista.sort()
print(lista[0])
