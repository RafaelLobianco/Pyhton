#Aula dia 01/06
#Arquivo

def lista_aprovados(arquivo):
   arq=open("dados.txt","r")
   for linha in arq:
      p1=linha.find(' ')   #espaço depois do nome
      nome=linha[:p1]
      p2=linha.find(' ',p1+1)  #espaço entre notas
      p3=linha.find(' ',p2+1)
      n1=float(linha[p1+1:p2])
      n2=float(linha[p2+1:p3])
      n3=float(linha[p3+1:])
      if (n1+n2+n3/3 >= 5.0):
         print(nome)    
   arq.close()
   return


