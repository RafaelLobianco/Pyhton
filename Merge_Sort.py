#Aula de Recursão USP Parte 2

#Ordenação por Intercalação - MergeSort


def merge_sort(lista):
    if len(lista) <= 1:  #base da recursão
        return lista
    meio= len(lista)//2
    lado_esquerdo=merge_sort(lista[:meio])
    lado_direito=merge_sort(lista[meio:])
    return merge(lado_esquerdo,lado_direito)

def merge(lado_esquerdo,lado_direito):
    if not lado_esquerdo: #no lado esquerdo tiver uma lista vazia  #base da recursão
        return lado_direito
    if not lado_direito:
        return lado_esquerdo
    if lado_esquerdo[0]< lado_direito[0]:  #se o lado_esquerdo é menor, ele cria uma nova lista com ele sendo o primeiro elemento.
        return [lado_esquerdo[0]]+ merge(lado_esquerdo[1:],lado_direito)
    return [lado_direito[0]]+merge(lado_esquerdo,lado_direito[1:])

lista=[6,5,3,1,8,7,2,4]
x=merge_sort(lista)
print(x)
