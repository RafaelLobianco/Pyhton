def intercala(n,t):
   if(len(n)==0):
      return ''
   if(len(n)==len(t)):
      return n[0]+t[0]+intercala(n[1:],t[1:])
   elif(len(n)<len(t)):
      return t[0]+intercala(n,t[1:])
   else:
      return n[0]+intercala(n[1:],t)
x = intercala("236","13458")
print(x)
   
