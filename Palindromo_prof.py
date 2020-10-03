def palindromo(s):
    tam=len(s)
    i=0
    while(i < tam//2):
        if s[i]!= s[tam-1-i]:
            return False
        i=i+1
    return True

x=palindromo('12321')
print(x)
y=palindromo('aloalo')
print(y)
