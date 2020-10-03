def retorna_cedulas(valor):
   if (valor//100!=0):
      retorno= (valor/100)
      print("Serao necessarias: "+str(retorno)+" cedulas de 100 reais.")
   elif(valor//50!=0):
      retorno1= (valor/50)
      print("Serao necessarias: "+str(retorno1)+" cedulas de 50 reais.")
   elif(valor//20!=0):
      retorno2= (valor/20)
      print("Serao necessarias: "+str(retorno2)+" cedulas de 20 reais.")
   elif(valor//10!=0):
      retorno3= (valor/10)
      print("Serao necessarias: "+str(retorno3)+" cedulas de 10 reais.")
   elif(valor//5!=0):
      retorno4= (valor/5)
      print("Serao necessarias: "+str(retorno4)+" cedulas de 5 reais.")
   elif(valor//2!=0):
      retorno5= (valor/2)
      print("Serao necessarias: "+str(retorno5)+" cedulas de 2 reais.")
   else:
      retorno6= (valor/1)
      print("Serao necessarias: "+str(retorno6)+" cedulas de 1 real.")
x=int(input("Digite o valor em reais: "))
retorna_cedulas(x)

