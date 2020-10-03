l=[-30,4,3,10]

def somando(lista):
    soma=0
    for el in lista:
        soma=soma+el
    return soma

def maior(lista):
    maior = -1000
    for el in lista:
        if el> maior:
            maior=el
    return maior
            
def menor(lista):
    menor=9999
    for el in lista:
        if el<menor:
            menor=el
    return menor

def exibe(lista):
    i=0
    n=len(lista)
    while i<n:
        print("O elemento de índice "+str(i)+" tem valor de "+str(lista[i]))
        i=i+1
        
#print(w) ---> ele vai colocar none, pois ele irá printar uma função que já faz print.
#logo,vai printar none

def verifica(lista,valor):
    i=0
    n=len(lista)
    while i<n:
        if lista[i]==valor:
            return i
        i+=1
    return False

def recebe(lista):
    x=somando(lista)
    print("A soma dos elementos da lista é: "+str(x))
    y=maior(lista)
    print("O maior valor da lista é: "+str(y))
    z=menor(lista)
    print("O menor valor da lista é: "+str(z))
    w=exibe(lista)
    print(' ')
    a=verifica(l,-30)  #0
    print(a)
    b=verifica(l,4)    #1
    print(b)
    c=verifica(l,3.1)  #false
    print(c)
    d=verifica(l,3)    #2
    print(d)
    e=verifica(l,10) #3
    print(e)
    f=verifica(l,20)  #false
    print(f)

recebe(l)
        
