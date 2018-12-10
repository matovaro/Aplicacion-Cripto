import math
import random

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


def sign(x,d,n):
    y = []
    for i in range(len(x)):
        cr = powermod(x[i], d, n)
        y.append(cr)
    return y

def ver(y,e,n,m):
    x = []
    for i in range(len(y)):
        mens = powermod(y[i], e, n)
        x.append(mens)
    fx=''
    for i in range(len(x)):
        fx=fx + str(x[i])

    fx=int(fx,10);
    if(fx == m):
        return True
    else:
        return False

def getE(lim):
    return random.randint(1, lim)

def breakArray(stri):
    men_arr=[]
    for i in range(math.ceil(len(stri) / 3)):
        start = i * 3
        end = (i + 1) * 3
        men_arr.append(int(stri[start:end]))
    return  men_arr
p=104723
q=104729


n=p*q

phi=(p-1)*(q-1)



d=-1;
while(d < 0):
    e = getE(phi)
    while(gcd(e,phi) != 1):
        e = getE(phi)



    #print(gcd(e,phi))

    EA = EEA(phi,e)

    d = EA[2]


def prE():
    return e
def prD():
    return d



m=6882326879666683
print('m=',end=' ')
print(m)
mens_array=[]

st=str(m)

mens_array = breakArray(st);
print('Mensaje array=',end=' ')
print(mens_array)

print('Sign')
crip_array=sign(mens_array,d,n)
print(crip_array)

print('Verification')
messa_array=ver(crip_array,e,n,m)
print(messa_array)


print(prE())
print(prD())


