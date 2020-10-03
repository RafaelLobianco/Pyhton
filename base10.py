def base10(n):
   if(n==0):
      return 1
   if(int(n[0])//2==0):
      return n[0]
   else:
      return n[0]+base10(n[1:])
x = input("digite o numero a ser convertido: ")
y = base10(x)
print(y)
