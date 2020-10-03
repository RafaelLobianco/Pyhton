def potencia(n,x):
   if(x==1):
      return n
   else:
      return (n)*potencia(n,x-1)
x=int(input("Numero: "))
y=int(input("potencia: "))
z = potencia(x,y)
print(z)
