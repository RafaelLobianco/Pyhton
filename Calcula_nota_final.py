def indice_presenca(aulas):
   if (aulas >= (0.95*80)):
      ind=3
      return  ind
   elif(aulas >= (0.90*80)):
      ind = 2
      return ind
   elif(aulas >= (0.80*80)):
      ind=1
      return ind
   else:
      ind=0
      return ind
def acrescimo(aulas):
   x=indice_presenca(aulas)
   percent = x*0.03
   return percent
def calcula_nota(aulas,nota_inicial):
   y=indice_presenca(aulas)
   z=acrescimo(aulas)
   nota_final = (nota_inicial)+(z*10)
   if(nota_final>10):
      nota_final=10
   print("Sua nota final eh: "+str(nota_final)+" seu acrescimo foi: "+str(z)+" e seu indice foi: "+str(y))
   return
x=int(input("digite o numero de aulas presentes do aluno: "))
y=float(input("digite a nota inicial do aluno: "))
calcula_nota(x,y)
