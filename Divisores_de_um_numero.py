'''Escreva um programa para ler números inteiros positivos do teclado e
imprimir na tela a soma de seus divisores (exceto ele mesmo). Utilize
a função soma_divisores para obter a soma.
Função: SomaDivisores Descrição: Calcula a soma dos divisores do
número informado (exceto ele mesmo). Entrada: Um número inteiro
positivo. Saída: A soma dos divisores do número, exceto ele mesmo.
Obs: O seu programa não deverá aceitar números negativos nem zero,
imprimindo a mensagem “Número inválido” nestes casos.'''


n = int(input(""))
lista=[]

if n < 0:
    print("número invalido")
else:
    for i in range(1,n-1):
        if n%i == 0:
            lista.append(i)

    def soma_divisores():
        soma = sum(lista)
        return soma

print(soma_divisores())
