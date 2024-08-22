import math
# Suma
def sumacplx(c1,c2):
    parteR=c1[0]+c2[0]
    parteI=c1[1]+c2[1]
    return(parteR,parteI)
# Resta
def restacplx(a1,a2):
    parteR=a1[0]-a2[0]
    parteI=a1[1]-a2[1]
    return(parteR,parteI)
# Multiplicación
def multicplx(b1,b2):
    parteR=((b1[0]*b2[0])-(b1[1]*b2[1]))
    parteI=(b1[0]*b2[1])+(b2[0]*b1[1])
    return(parteR,parteI)
# División
def divcplx(e1,e2):
    parteR= round(((e1[0]*e2[0])+(e1[1]*e2[1]))/((e2[0]**2)+(e2[1]**2)))
    parteI= round(((e2[0]*e1[1])-(e1[0]*e2[1]))/((e2[0]**2)+(e2[1]**2)))
    return(parteR,parteI)
#Módulo
def modulocplx(m1,m2):
    parteR= round((m1**2)+(m2**2)**(1/2))
    return(parteR)
#Conjugado
def conjugadocplx(j1,j2):
    parteR= j1
    parteI= -j2
    return(parteR,parteI)
#Conversión polar a cartesiano
def conversptoccplx(t1,t2):
    parteR= round(t1*math.cos(math.radians(t2)))
    parteI= round(t1*math.sin(math.radians(t2)))
    return(parteR,parteI)
#Conversión cartesiano a polar
def conversctopcplx(u1,u2):
    parteR= ((u1**2)+(u2**2))**(1/2)
    x= math.degrees(math.atan(u2/u1))
    if u1>0 and u2>0:
        parteI=x
    elif u1<0 and u2<0:
        parteI=x+180
    elif u1>0 and u2<0:
        parteI=360-x
    elif u1<0 and u2>0:
        parteI=180-x
    return(parteR,parteI)
#Fase de un número
def fasecplx(f1,f2):
    x= math.degrees(math.atan(f2/f1))
    if f1>0 and f2>0:
        angulo=x
    elif f1<0 and f2<0:
        angulo=x+180
    elif f1>0 and f2<0:
        angulo=360-x
    elif f1<0 and f2>0:
        angulo=180-x
    return(round(angulo))
if __name__ == '__main__':
    print(sumacplx((3,4),(-4,6.7)))
    print(restacplx((3,2),(-5,6.4)))
    print(multicplx((4,5),(-5,5.8)))
    print(divcplx((3,8,2),(-7,5.5)))
    print(modulocplx((3),(-6.7)))
    print(conjugadocplx((3),(-7.2)))
    print(conversptoccplx((2),(-75)))
    print(conversctopcplx((3*((3)**(1/2))),(3)))
    print(fasecplx((3),(-5.2)))