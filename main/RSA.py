import math
import random


print('################################# RSA')

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
########################################################################################################################
########################################################################################################################
########################################################################################################################
# m=6882326879666683
# print('m=',end=' ')
# print(m)
# p=1009
# print('p=',end=' ')
# print(p)
# q=1013
# print('q=',end=' ')
# print(q)
#
# mens_array=[]
#
# stri=str(m)
# for i in range(math.ceil(len(stri)/3)):
#     start=i*3
#     end=(i+1)*3
#     mens_array.append(int(stri[start:end]))
#
# print('Mensaje array=',end=' ')
# print(m)
# n=p*q
# print('n=',end=' ')
# print(n)
#
# phi=(p-1)*(q-1)
# print('phi=',end=' ')
# print(phi)
#
#
#
# d=-1;
# while(d < 0):
#     e = random.randint(1, phi)
#     while(gcd(e,phi) != 1):
#         e = random.randint(1, phi)
#
#
#
#     #print(gcd(e,phi))
#
#     EA = EEA(phi,e)
#
#     d = EA[2]
#
# print('e =')
# print(e)
# print('EEA =',end=' ')
# print(EA)
# print('d =',end=' ')
# print(d)
#
# print('Encript')
# crip_array=[]
# for i in range(len(mens_array)):
#    cr = powermod(mens_array[i],e,n)
#    crip_array.append(cr)
# print(crip_array)
#
# print('Decript')
# messa_array=[]
# for i in range(len(crip_array)):
#    me = powermod(crip_array[i],d,n)
#    messa_array.append(me)
# print(messa_array)

########################################################################################################################
########################################################################################################################
########################################################################################################################


m=6882326879666683
print('m=',end=' ')
print(m)
p=104723
print('p=',end=' ')
print(p)
q=104729
print('q=',end=' ')
print(q)

mens_array=[]

stri=str(m)
for i in range(math.ceil(len(stri)/3)):
    start=i*3
    end=(i+1)*3
    mens_array.append(int(stri[start:end]))

print('Mensaje array=',end=' ')
print(m)
n=p*q
print('n=',end=' ')
print(n)

phi=(p-1)*(q-1)
print('phi=',end=' ')
print(phi)



d=-1;
while(d < 0):
    e = random.randint(1, phi)
    while(gcd(e,phi) != 1):
        e = random.randint(1, phi)



    #print(gcd(e,phi))

    EA = EEA(phi,e)

    d = EA[2]

print('e =')
print(e)
print('EEA =',end=' ')
print(EA)
print('d =',end=' ')
print(d)

print('Sign')
crip_array=sign(mens_array,d,n)
print(crip_array)

print('Verification')
messa_array=ver(crip_array,e,n,m)
print(messa_array)


