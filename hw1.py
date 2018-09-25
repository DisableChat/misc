# Cs 4040 hw1

import math

# algorithm 1
def functionA(x):
      return 3*math.pow(x,2) + (2*x) + 42

# algorithm 2
def functionB(x):
      return 343*x*math.log2(x)

def functionC(x):
    return 243*x*(math.pow(math.log2(x), 2))

def get_value1(x):
    return(x)

def main():

    # Bad variable names sincec its quick program
    a1  =   0
    b1  =   0
    c1  =   0
    x   =   2
    y   =   2
    k   =   2
    k1  =   2

    functionC_vs_A = 0
    functionC_vs_B = 0

    while(functionA(x) <= functionB(x)):
        #print('function A: {}, function B: {}'.format(functionA(x), functionB(x)))
        #print("Value: {}".format(x))
        a1 = functionA(x)
        b1 = functionB(x)
        x += 1

    while(y <= 1163):
        functionC(y)
        #print('function C: {}'.format(functionC(y)))
        c1 = functionC(y)
        y += 1

    while(functionC(k) >= functionA(k)):
        #print('function A: {}, function C: {}'.format(functionA(k),functionC(k)))
        #print(k)
        functionC_vs_A = k
        k += 1

    while(functionC(k1) <= functionB(k1)):
        #print('function B: {}, function C: {}'.format(functionB(k1),functionC(k1)))
        #print(k1)
        functionC_vs_B = k1
        k1 += .001

    print('function a and b @ 1163: ' + str(a1) + ' '+ str(b1))
    print('@ 1164: ' + str(functionA(1164)) + ' ' + str(functionB(1164)))

    print('first value: {}'.format(get_value1(x - 1)))

    # function C is greater than A untill the following value
    print('c vs a: ' + str(functionC_vs_A))

    # function c is less than b untill the following value
    print('c vs b: ' + str(functionC_vs_B))

    #print(functionA(16000))
    #print(functionB(1163))
    print(functionB(2.65))
    print(functionC(2.65))

main()

#first value: 1162.757999979393 (using .001 accuracy)
#c vs a: 15745
#c vs b: 2.6599999999999273
