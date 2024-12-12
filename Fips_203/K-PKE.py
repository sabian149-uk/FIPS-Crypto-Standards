import General, XOF

n = 256
q=3329
k = 4
eta = 2 #eta1 and eta2 are the same value sete in the apporved parameter set
d1 = 11 #d^u is what is defined on the parameter set but easier to type as d1
d2 = 5 #d^v is what is defined on the parameter set but easier to type as d2

def KeyGen():
    print("TODO") # TODO


def Encrypt(key, message, random):
    N = 0
    temp = []
    t = []
    A = []
    #Runs ByteDecode k time on seperated key segments.
    for x in range(k): 
        temp.append(key[(384*x) : (384*(x+1))])
    for x in range(k):
        t.append(General.ByteDecode(temp[x]))

    p = key[(384*k) : (384*k) + 32]
    for x in range(k):
        for y in range(k):
            a



    