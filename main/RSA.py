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


    for i in range(len(stri)):
        start = i
        end = (i + 1)

        temp=stri[start:end]

        tempo=[]
        for j in range(len(temp)):
            tempo.append(ord(temp[j]))
        men_arr.append(tempo)
    return  men_arr



def getE(lim):
    #return random.randint(1, lim)
    return 7


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


def sign(strin):
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

    re=''
    for i in range(len(y)):
        re=re+str(y[i])+'&'
    return re

# def ver(y,m):
#     x = []
#     test=y.rstrip('&').split('&')
#     for i in range(len(test)):
#         mens = powermod(int(test[i]), e, n)
#         x.append(mens)
#     fx=''
#     for i in range(len(x)):
#         fx=fx+str(x[i])+'&'
#     fn=fx.rstrip('&').split('&')
#
#     fx=''
#     for j in range(len(fn)):
#         fx=fx+chr(int(fn[j]))
#     if(fx == m):
#         return fx
#     else:
#         return 'Firma no valida'


def ver(y):
    x = []
    test=y.rstrip('&').split('&')
    for i in range(len(test)):
        mens = powermod(int(test[i]), e, n)
        x.append(mens)
    # fx = '' 
    # for i in range(len(x)):
    #     fx=fx+str(x[i])+'&'
    # fn=fx.rstrip('&').split('&')
    # fx=''
    # for j in range(len(fn)):
    #     fx=fx+chr(int(fn[j]))
    # return fx
    try:
        fn = getFn(x)
        return getMessage(fn)
    except:
        return 0
def getFn(x):
    fx = ''
    for i in range(len(x)):
        fx=fx+str(x[i])+'&'
    return fx.rstrip('&').split('&')

def getMessage(fn):
    fx=''
    for j in range(len(fn)):
        fx=fx+chr(int(fn[j]))
    return fx
def prE():
    return e
def prD():
    return d



#m='6882326879666683'
m='Hello'
#m='AZaz'
mens_array=[]

st=str(m)


crip_array=sign(st)

#messa_array=ver('9883992373/5548158300/3903790183/10476177647/7025471146/168550448/3903790183/452861407/',270618377,n,m)
messa_array=ver(crip_array)
#
# print(prE())
# print(prD())


