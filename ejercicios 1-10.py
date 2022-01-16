def hola_mundo():
    print("Hola mundo")
    return None

hola_mundo()

def hola_mundo2():
    a="Hola Mundo"
    print(a)
    return None

hola_mundo2()

def hola3(n):
    print("Hola "+n)
    return None

hola3("abu")

def operac1():
    print(((3+2)/2*5)**2)
    return None

operac1()

def horas_pago(n,c):
    pago=n*c
    print("Te toca recibir $ " +str(pago))
    return None

horas_pago(8,1000)

def suma(n):
    suma=n*(n+1)/2
    print(suma)
    return None

suma(4)

def imc(p,t):
    imc=round(p/(t**2),2)
    print("Tu IMC es "+str(imc))
    return None
 
imc(50,1.8)

def division(a,b):
    div=a/b
    coc=a//b
    res=a%b
    div=str(a)+ " entre " + str(b)+ " da como resultado "+str(coc) + " con un cociente de " + str(res)
    print(div)
    return None

division(50,3)

def interes_simple(c,i,t):
    n=1
    total=c
    while n<=t:
        interes=c*i*n
        total+=interes
        n+=1
    print("ganaste "+str(total))
    return None

interes_simple(500,0.03,5)

def peso(p,m):
    ppay=112*p
    pmu=75*m
    ptot=ppay+pmu
    print("El peso total es "+str(ptot)+" gramos")
    return None

peso(12,50)

