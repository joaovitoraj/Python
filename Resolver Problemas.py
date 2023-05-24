n = int(input('Digite o número de problemas: '))
problemasResolvidos = 0

for i in range(n):
    print("Problema", (i+1))
    petya=int(input("Digite o valor de Petya: "))
    vasya=int(input("Digite o valor de vasya: "))
    tonya=int(input("Digite o valor de tonya: "))   
    soma = petya + vasya + tonya
    if soma >= 2:
        problemasResolvidos += 1
print ("Eles resolvem ", problemasResolvidos, 'problema(s)')
