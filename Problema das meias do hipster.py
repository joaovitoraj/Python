'''
Problema das Meias do Hipster
Um dia, Vasya, o Hipster, decidiu contar quantas meias ele tinha.
De scobriu que tinha a meias vermelhas e b meias azuis.
De acordo com a última moda, os hipsters devem usar meias de
cores diferentes: uma vermelha no pé esquerdo e uma azul no pé
direito.
Todos os dias, Vasya coloca meias novas pela manhã e as joga
fora antes de ir para a cama, pois não quer lavá-las.
Vasya se pergunta qual é o número máximo de dias em que ele
pode se vestir de forma elegante e usar meias diferentes e, depois
disso, por quantos dias ele pode usar as mesmas meias até que
ele fique sem meias ou não consiga formar um único par com as
meias que possui.
Você pode ajudá-lo?
Entrada
A entrada deve sere dois números inteiros positivos a e b (1 ≤ a, b
≤ 100) — o número de meias vermelhas e azuis que Vasya possui.
Saída
Imprima dois números inteiros separados por espaço — o número
máx imo de dias em que Vasya pode usar meias diferentes e o
número de dias em que ele pode usar as mesmas meias até ficar
sem meias ou não conseguir formar um único par com as meias
que possui.
Lembre-se de que, no final do dia, Vasya joga fora as meias que
usou no dia.'''

a = int(input("Vermelhas: "))
b = int(input("Azuis: "))
if a > b:
    print(a, a-b)
else:
    print(b, b-a)