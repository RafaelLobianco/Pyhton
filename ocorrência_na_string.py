def exibe(s,c):
   if(s[0]==c):
      return True
   else:
      exibe(s[1:],c)
      return False
x = exibe("sol","t")
print(x)
y = exibe("sol","o")
print(y)
      
