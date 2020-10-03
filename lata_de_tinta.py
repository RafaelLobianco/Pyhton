def area_retangulo(h,r):
   c = 2*3.1415*r
   retangulo = h*c
   return retangulo
def area_circulo(r):
   area = (3.1415)*r
   return area
def calcula_cilindro(h,r):
   area = 2*area_circulo(r)+area_retangulo(h,r)
   return area
def calcula(h,r):
   metragem = calcula_cilindro(h,r)
   litro = metragem/3
   lata = litro/5
   preco = lata*20
   print("O valor a pagar eh: "+str(preco)+" e serao usadas: "+str(lata))
   return
x=float(input("digite a altura da figura: "))
y=float(input("digite o raio da figura: "))
calcula(x,y)
