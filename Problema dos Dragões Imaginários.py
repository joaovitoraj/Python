'''
Problema dos Dragões Imaginários
“Um dragão. Dois dragões. Três dragões” - a princesa estava
contando. Ela tinha dificuldade em pegar no sono e se cansou de
contar carneiros quando tinha nove anos.
No entanto, apenas contar dragões também era entediante, então
ela se divertia o máximo que podia. Nesta noite, ela imaginou que
todos os dragões estavam ali para roubá-la, e ela lutava contra
eles. A cada k-ésimo dragão, ela dava uma pancada no rosto com
uma frigideira.
A cada l-ésimo dragão, ela prendia o rabo na porta da varanda. A
cada m-ésimo dragão, ela pisoteava as patas do dragão.
Finalmente, ela ameaçou chamar a mãe de cada n-ésimo dragão,
e ele recuava em pânico.
Quantos dragões imaginários sofreram danos morais ou físicos
nesta noite, se a princesa contou um total de d dragões?
Entrada:
Os dados de entrada contêm números inteiros k, l, m, n e d, cada
número em uma linha separada (1 ≤ k, l, m, n ≤ 10, 1 ≤ d ≤ 105).
Saída:
Informe o número de dragões moralmente ou fisicamente abatidos.
'''

k = int(input("k-ésimo: "))
l = int(input("l-ésimo: "))
m = int(input("m-ésimo: "))
n = int(input("n-ésimo: "))
d = int(input("Número de Dragões: "))
i = 0

# total de dragões que sofreram dano
Tdrag = 0

while i < d:
    i += 1
    if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
        Tdrag += 1
print(Tdrag)
