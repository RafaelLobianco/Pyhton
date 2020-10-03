Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import math
>>> help(math)
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module is always available.  It provides access to the
    mathematical functions defined by the C standard.

FUNCTIONS
    acos(...)
        acos(x)
        
        Return the arc cosine (measured in radians) of x.
    
    acosh(...)
        acosh(x)
        
        Return the inverse hyperbolic cosine of x.
    
    asin(...)
        asin(x)
        
        Return the arc sine (measured in radians) of x.
    
    asinh(...)
        asinh(x)
        
        Return the inverse hyperbolic sine of x.
    
    atan(...)
        atan(x)
        
        Return the arc tangent (measured in radians) of x.
    
    atan2(...)
        atan2(y, x)
        
        Return the arc tangent (measured in radians) of y/x.
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(...)
        atanh(x)
        
        Return the inverse hyperbolic tangent of x.
    
    ceil(...)
        ceil(x)
        
        Return the ceiling of x as an Integral.
        This is the smallest integer >= x.
    
    copysign(...)
        copysign(x, y)
        
        Return a float with the magnitude (absolute value) of x but the sign 
        of y. On platforms that support signed zeros, copysign(1.0, -0.0) 
        returns -1.0.
    
    cos(...)
        cos(x)
        
        Return the cosine of x (measured in radians).
    
    cosh(...)
        cosh(x)
        
        Return the hyperbolic cosine of x.
    
    degrees(...)
        degrees(x)
        
        Convert angle x from radians to degrees.
    
    erf(...)
        erf(x)
        
        Error function at x.
    
    erfc(...)
        erfc(x)
        
        Complementary error function at x.
    
    exp(...)
        exp(x)
        
        Return e raised to the power of x.
    
    expm1(...)
        expm1(x)
        
        Return exp(x)-1.
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(...)
        fabs(x)
        
        Return the absolute value of the float x.
    
    factorial(...)
        factorial(x) -> Integral
        
        Find x!. Raise a ValueError if x is negative or non-integral.
    
    floor(...)
        floor(x)
        
        Return the floor of x as an Integral.
        This is the largest integer <= x.
    
    fmod(...)
        fmod(x, y)
        
        Return fmod(x, y), according to platform C.  x % y may differ.
    
    frexp(...)
        frexp(x)
        
        Return the mantissa and exponent of x, as pair (m, e).
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(...)
        fsum(iterable)
        
        Return an accurate floating point sum of values in the iterable.
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(...)
        gamma(x)
        
        Gamma function at x.
    
    gcd(...)
        gcd(x, y) -> int
        greatest common divisor of x and y
    
    hypot(...)
        hypot(x, y)
        
        Return the Euclidean distance, sqrt(x*x + y*y).
    
    isclose(...)
        isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0) -> bool
        
        Determine whether two floating point numbers are close in value.
        
           rel_tol
               maximum difference for being considered "close", relative to the
               magnitude of the input values
            abs_tol
               maximum difference for being considered "close", regardless of the
               magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.
    
    isfinite(...)
        isfinite(x) -> bool
        
        Return True if x is neither an infinity nor a NaN, and False otherwise.
    
    isinf(...)
        isinf(x) -> bool
        
        Return True if x is a positive or negative infinity, and False otherwise.
    
    isnan(...)
        isnan(x) -> bool
        
        Return True if x is a NaN (not a number), and False otherwise.
    
    ldexp(...)
        ldexp(x, i)
        
        Return x * (2**i).
    
    lgamma(...)
        lgamma(x)
        
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x[, base])
        
        Return the logarithm of x to the given base.
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(...)
        log10(x)
        
        Return the base 10 logarithm of x.
    
    log1p(...)
        log1p(x)
        
        Return the natural logarithm of 1+x (base e).
        The result is computed in a way which is accurate for x near zero.
    
    log2(...)
        log2(x)
        
        Return the base 2 logarithm of x.
    
    modf(...)
        modf(x)
        
        Return the fractional and integer parts of x.  Both results carry the sign
        of x and are floats.
    
    pow(...)
        pow(x, y)
        
        Return x**y (x to the power of y).
    
    radians(...)
        radians(x)
        
        Convert angle x from degrees to radians.
    
    sin(...)
        sin(x)
        
        Return the sine of x (measured in radians).
    
    sinh(...)
        sinh(x)
        
        Return the hyperbolic sine of x.
    
    sqrt(...)
        sqrt(x)
        
        Return the square root of x.
    
    tan(...)
        tan(x)
        
        Return the tangent of x (measured in radians).
    
    tanh(...)
        tanh(x)
        
        Return the hyperbolic tangent of x.
    
    trunc(...)
        trunc(x:Real) -> Integral
        
        Truncates x to the nearest Integral toward 0. Uses the __trunc__ magic method.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793

FILE
    (built-in)


>>> M = 100000*(1+(0.105*145))
>>> print (M)
1622500.0000000002
>>> #==========================================================================================
>>> M2 = 10000*(1+0.025)**12
>>> print(M2)
13448.88824246297
>>> #==========================================================================================
>>> x=(1902.36)/(1+0.02)**12
>>> print(x)
1499.9978774995195
>>> #==========================================================================================
>>> M = 100000*(1+(0.105*0.0403))
>>> print(M)
100423.15
>>> #==========================================================================================
>>> B(t) = 2**(144/12)
SyntaxError: can't assign to function call
>>> B = 2**(144/12)
>>> print(B)
4096.0
>>> 8*(2**10)
8192
>>> #==========================================================================================
>>> 2048 = k*(2**(-0.5*0))
SyntaxError: can't assign to literal
>>> k=2048/(2**((-0.5)*0))
>>> print(k)
2048.0
>>> #==========================================================================================
>>> acaros = (0.0001)*54
>>> print(acaros)
0.0054
>>> acaros = (10000)*54
>>> print(acaros)
540000
>>> #==========================================================================================
>>> total = 15+26+14+29
>>> print(total)
84
>>> cabecas = total
>>> print(cabecas)
84
>>> patas = (15*4)+(26*4)+(14*2)
>>> print(patas)
192
>>> #==========================================================================================
>>> 1540=x+625+447
SyntaxError: can't assign to literal
>>> parcelas = 1540-(625)-(447)
>>> print(parcelas)
468
>>> mult = (625)*(447)*(468)
>>> print(mult)
130747500
>>> #==========================================================================================
>>> 2540=1143*(x/100)
SyntaxError: can't assign to literal
>>> x=(2540/1143)*100
>>> print(x)
222.22222222222223
>>> 2540/1143
2.2222222222222223
>>> x=(1143/2540)*100
>>> print(x)
45.0
>>> #==========================================================================================
>>> dist = (600*100)/37.5
>>> print(dist)
1600.0
>>> #==========================================================================================
>>> 99**(1/3)
4.626065009182741
>>> #==========================================================================================
>>> pi= 3.1415
>>> area = ((pi)*(18/(2*pi))**2)
>>> print(area)
25.783861212796435
>>> #==========================================================================================
>>> math.sqrt(39)
6.244997998398398
>>> lado = math.sqrt(39)
>>> perimetro = 4*(lado)
>>> print (perimetro)
24.979991993593593
>>> #==========================================================================================
>>> pi=3.1415
>>> volume_esf=(4/3)*pi*((3)**3)
>>> print(volume_esf)
113.094
>>> volume_esf=(4*pi*(3**3))/3
>>> print(volume_esf)
113.09400000000001
>>> #==========================================================================================
>>> lado = 3/4
>>> print(lado)
0.75
>>> area = (lado)**2
>>> print(area)
0.5625
>>> #==========================================================================================
>>> area = (6*(5.196))/2
>>> print(area)
15.588
>>> perimetro = 6*3
>>> print(perimetro)
18
>>> #==========================================================================================
>>> area_trap = ((3+2)*10)/2
>>> print(area_trap)
25.0
>>> #==========================================================================================
>>> temp = ((392-32)/9)*5
>>> print(temp)
200.0
>>> #==========================================================================================
>>> temp= 273.15+34
>>> print(temp)
307.15
>>> #==========================================================================================
>>> comp = (3*(10**8))/(4.6*(10**14))
>>> print(comp)
6.521739130434783e-07
>>> #==========================================================================================
>>> peso_parado = 95*10
>>> print(peso_parado)
950
>>> peso_movimento= (95*0.5)+(95*10)
>>> print(peso_movimento)
997.5
>>> diferenca = (peso_parado/peso_movimento))*100
SyntaxError: invalid syntax
>>> diferenca = (peso_parado/peso_movimento)*100
>>> print(diferenca)
95.23809523809523
>>> 950/997.5
0.9523809523809523
>>> 100-diferenca
4.761904761904773
>>> #==========================================================================================
>>> media1 = (10+12+15+17)/4
>>> print(media1)
13.5
>>> media2 = (10+12+15+17+16)/5
>>> print(media2)
14.0
>>> #a media de idade sobe ao acrescentar uma pessoa de 16 anos ao grupo
>>> #==========================================================================================
>>> media_voto=(218+198+166+177+206)/5 #passando o tempo para minutos
>>> print(media_voto)
193.0
>>> #==========================================================================================
>>> total_votos = (100*196)/28
>>> print(total_votos)
700.0
>>> votos_vencedor = (26*700)/100
>>> print(votos_vencedor)
182.0
>>> indice_nulo = 100-(26+24+22)
>>> print(indice_nulo)
28
>>> #==========================================================================================
>>> imposto = (30*20)/100
>>> print(imposto)
6.0
>>> imposto_final= 30-imposto
>>> print(imposto_final)
24.0
>>> lucro = 10*0.5
>>> print(lucro)
5.0
>>> custo = (60*10)/100
>>> print(custo)
6.0
>>> custo_final = 60+custo
>>> print(custo_final)
66.0
>>> novo_valor = imposto_final + lucro + custo_final
>>> print(novo_valor)
95.0
>>> #==========================================================================================
>>> volume = 1.2*5*8
>>> print(volume)
48.0
>>> preenchimento = (48*1)/2
>>> print(preenchimento)
24.0
>>> #==========================================================================================
>>> disconto = (4200*10)/100
>>> print(disconto)
420.0
>>> preco_a_vista = (4200-420)+120
>>> print(preco_a_vista)
3900
>>> diferenca = 4200-(preco_a_vista)
>>> print(diferenca)
300
>>> #diferenca de 300 reais entre pagar a vista (10% de desconto) e a prazo
>>> #==========================================================================================
>>> arroz_inicial = 2.20*8
>>> feijao_inicial = 1.60*5
>>> custo_inicial = arroz_inicial = feijao_inicial
>>> print(custo_inicial)
8.0
>>> custo_inicial = arroz_inicial + feijao_inicial
>>> print(custo_inicial)
16.0
>>> custo = ((2.20)*8) +((1.60)*5)
>>> print(custo)
25.6
>>> aumento_arroz = (2.20*10)/100
>>> print (aumento_arroz)
0.22
>>> preco_2_arroz = 2.20+0.22
>>> print(preco_2_arroz)
2.4200000000000004
>>> reducao_feijao= (1.60*5)/100
>>> print(reducao_feijao)
0.08
>>> preco_2_feijao= 1.60 - 0.08
>>> print(preco_2_feijao)
1.52
>>> novo_custo = ((2.42)*8)+((1.52)*5)
>>> print(novo_custo)
26.96
>>> diferenca = (25.60*100)/26.96
>>> print(diferenca)
94.95548961424332
>>> aumento_percentual = 100-diferenca
>>> print(aumento_percentual)
5.044510385756681
>>> #houve um aumento percentual de 5.044510385756681% no gasto mensal da pessoa
