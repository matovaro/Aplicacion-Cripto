import math
import random
import codecs

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)


def EEA(a,b):


    if b==0:
        z=[a,1,0]
        return z
    else:
        qu = math.floor(a / b)
        zp=EEA(b,a%b)
        z=[zp[0],zp[2],zp[1]- (qu*zp[2])]
        return z

def bitLen(int_type):
    length = 0
    while (int_type):
        int_type >>= 1
        length += 1
    return(length)

def powermod(a,b,n):
    binary=bin(b).lstrip('0b')
    z=1
    for i in range(bitLen(b)):
        b=binary[i:i+1]

        if(b == '1'):
            z = ((z**2)*a)% n
        elif(b == '0'):
            z = (z**2)%n

    return z

def breakArray(stri):
    men_arr=[]

    for i in range(math.ceil(len(stri) / 3)):
        start = i * 3
        end = (i + 1) * 3

        temp=stri[start:end]

        tempo=[]
        for j in range(len(temp)):
            tempo.append(ord(temp[j]))
        men_arr.append(tempo)
    return  men_arr

def sign(strin,d,n):
    y = []
    x = breakArray(strin)
    for i in range(len(x)):
        g=x[i]
        tm=''
        for j in range(len(g)):
            tm=tm+str(g[j])

        te=int(tm)
        cr = powermod(te, d, n)
        y.append(cr)
    arrt=[]
    arrt.append(x)
    arrt.append(y)
    return arrt

def ver(y,e,n,m):
    x = []
    for i in range(len(y[1])):
        mens = powermod(y[1][i], e, n)
        x.append(mens)

    fc=[]
    for i in range(len(y[0])):
        veri=''
        for j in range(len(y[0][i])):
            veri=veri+str(y[0][i][j])
        fc.append(int(veri))

    ty=y[0]
    fx=''
    if(fc==x):
        for i in range(len(ty)):
            for j in range(len(ty[i])):
                fx=fx+chr(ty[i][j])
    if(fx == m):
        return fx
    else:
        return 'Firma no valida'

def getE(lim):
    return random.randint(1, lim)


p=104723
q=104729


n=p*q

phi=(p-1)*(q-1)



d=-1;
while(d < 0):
    e = getE(phi)
    while(gcd(e,phi) != 1):
        e = getE(phi)





    EA = EEA(phi,e)

    d = EA[2]


def prE():
    return e
def prD():
    return d



#m='6882326879666683'
m='Hello my friendjhjhjhj'
#m='AZaz'
print('m=',end=' ')
print(m)
mens_array=[]

st=str(m)


print('Sign')
crip_array=sign(st,d,n)
print(crip_array[1])

print('Verification')
messa_array=ver(crip_array,e,n,m)
print(messa_array)


print(prE())
print(prD())


