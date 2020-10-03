def respostas (nome,idade,altura,peso):
    print("Seu peso eh: "+str(nome))
    print("Seu peso eh: "+str(idade))
    print("Sua altura eh: "+str(altura))
    print("Seu peso eh: "+str(peso))
    return

def calcula_IMC (peso,altura):
    IMC = peso/(altura)**2
    print("Seu IMC eh: "+str(IMC))
    return

nome = str(input("Informe o seu nome: "))
idade = float(input("Informe a sua idade: "))
altura = float(input("Informe a sua altura em metros: "))
peso = float(input("Informe o seu peso: "))
respostas(nome,idade,altura,peso)
calcula_IMC(peso,altura)
