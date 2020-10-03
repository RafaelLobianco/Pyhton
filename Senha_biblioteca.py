def soma_dig(n):
   a = n//10
   b = n%10
   soma = a+b
   return soma
def senha_aluno(d,m,a):
   p1  = soma_dig(d)
   p2  = soma_dig(m)
   p3 = soma_dig(a)
   soma = str(p1)+str(p2)+str(p3)
   return soma
d = int(input("informe o dia de nascimento: "))
m = int(input("informe o mes de nascimento: "))
a = int(input("informe os dois digitos finais do ano de nascimento: "))
x = senha_aluno(d,m,a)
print("A senha do aluno eh: " + str(x))
