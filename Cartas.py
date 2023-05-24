carta1=int(input())
carta2=int(input())
carta3=int(input())
carta4=int(input())
carta5=int(input())
lista=[carta1,carta2,carta3,carta4,carta5]
if lista[0]<lista[1] and lista[1]<lista[2] and lista[2]<lista[3] and lista[3]<lista[4]:
    print("C")
elif lista[0]>lista[1] and lista[1]>lista[2] and lista[2]>lista[3] and lista[3]>lista[4]:
    print("D")
else:
    print("N")
