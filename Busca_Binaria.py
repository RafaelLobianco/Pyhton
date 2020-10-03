#Aula de Recursão USP Parte 2

#Busca Binária
#Por exemplo, vamos supor que eu queira encontrar a palavra Arcabouço no dicionário. Fazendo uma busca
#sequencial, eu demoraria muito pra achar. Pra isso, vamos usar a busca binária. Vamos abrir a metade do dicionário
# e vejo a palavra da página. Palavra Forma; a palavra forma é maior ou menor que arcabouço? Se é maior,
# então a palavra arcabouço está no lado esquerdo do dicionário. Agora repito recursivamente esse passo. Divido na metade
# a palavra deu Carpintaria. Repito recursivamente. Aporrinhado. Aporrinhado é menor, ai divido pela metade e
#repito recursivamente até achar.



#lista = lista de elementos; #elemento = elemento que eu vou buscar
#min e max = mínimo e máximo são os começos e fins da lista naquele momento. inicialmente,
#começo com a lista completa (min=0 e max = ultimo); a medida que eu executo o algoritmo
#recursivo, vou sempre dividindo pela metade. min vai subindo e máx vai descendo.
#ou vou encontrar o elemento, ou max vai passar do min e o elemento não tem.
    
def busca_binaria(lista,elemento,min, max):  #min e max são opcionais    if max==None:  #se max não tem nada, max é a lista completa.
        max=len(lista)-1 #posição do max é -1
    if max < min: #max ficou menor que o min
        return False
    else:  #caso contrario, calculo o novo meio
        meio = min + (max-min)//2  #ou (max+min)//2
    if lista[meio] > elemento: # elemento do meio é maior que o procurado. vamos procurar da esquerda ate um elemento menor que o meio.
        return busca_binaria(lista, elemento,min, meio-1)
    elif lista[meio] < elemento: #elemento do meio é menor que o procurado. procura de meio+1 ate o max)
        return busca_binaria(lista,elemento,meio+1,max)
    else:  #o elemento do meio é o elemento procurado
        return meio

a=[10,20,30,40,50,60]
elemento=10
ele=50
min=0
max=None

x=busca_binaria(a,elemento,min,max)
print("O elemento procurado está na posição", x)
y=busca_binaria(a,ele,min,max)
print("O elemento procurado esta na posição",y)

