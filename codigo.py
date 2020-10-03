def calcula_percent(v,p):
   N = v*(p/100)
   return N
def calcula_valor(cod1,cod2):
   Pi = cod1*15+cod2
   t = calcula_percent(Pi,cod2)
   total = Pi - t
   return total   
cod1 = int(input("Digite a primeira parte do cod: "))
cod2 =int(input("DIgite a segunda parte do cod: "))
x = calcula_valor(cod1,cod2)
print("O valor a pagar eh: " +str(x)+" reais")
