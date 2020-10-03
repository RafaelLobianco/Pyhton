def inverte(palavra):
   if(len(palavra)==1):
      return palavra
   else:
      return inverte(palavra[1:])+palavra[0]
x = input("Digite a palavra a ser invertida: ")
y = inverte(x)
print(y)
