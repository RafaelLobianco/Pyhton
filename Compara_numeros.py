def compara_numeros(n,t):
   if(n[0]>t[0]):
      return False
   elif(n[0]<t[0]):
      return True
   elif(len(n)>1):
      return compara_numeros(n[1:],t[1:])
   else:
      return True
x = compara_numeros("1234","2456")
print(x)
y = compara_numeros("1234","1214")
print(y)
