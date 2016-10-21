#fizbuzz
for i in range(1,100):
    if ((i) % 15)==0:
        print("FizzBuzz")
    elif ((i) % 3)==0:
        print("Fizz")
    elif ((i) % 5)==0:
        print("Buzz")

    else:
        print(i)

#fibonach
a=0
b=1
n=1


def fib(a,b,n):
    c=a+b

    if(n==100-2):
        print(c)
    if(n!=100-2):

        fib(b,c,n+1)


fib(a,b,1)

#linspace
import numpy

print (numpy.linspace(2,3,5,1,1))


def linsp(startA,stopA,num, boolSh,retstep):
    z=numpy.array([])
    startA=float(startA)
    stopA=float(stopA)
    boolSh=bool(boolSh)
    retstep=bool(retstep)
    #print num
    num=num-boolSh
    #print num
    for i in range(num+boolSh):
        p=startA+(stopA-startA)/num*i
        z=numpy.append(z,p)
        #print p

    if(retstep==True):
        z=(z,(stopA-startA)/num)
    return z

print linsp(2,3,5,1,1)

#plot

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-5., 5., 0.1)
plt.subplot(121)
plt.plot(t, t, 'r--', t, t**2/5, 'bs', t, t**3/5**2, 'g^')

plt.xlabel('X hor')
plt.ylabel('Y ver')

plt.text(1.2, 2.0, r'$y=x$')
plt.text(2.7, 2.5, r'$y=x^2$')
plt.text(3.5, 1.0, r'$y=x^3$')

plt.grid(True)

plt.subplot(122)
plt.plot(t, -t, 'r--')

plt.xlabel('X hor')
plt.ylabel('Y ver')

plt.text(1.2, 2.0, r'$y=-x$')


plt.grid(True)
plt.savefig('plt.png')
plt.show()
