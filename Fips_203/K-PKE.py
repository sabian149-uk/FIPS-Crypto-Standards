import General, XOF, numpy


n = 256
q=3329
k = 4
eta = 2 #eta1 and eta2 are the same value sete in the apporved parameter set
d1 = 11 #d^u is what is defined on the parameter set but easier to type as d1
d2 = 5 #d^v is what is defined on the parameter set but easier to type as d2

def KeyGen():
    N = 0 #TODO Finish



def Encrypt(key, message, random):

    #TODO Define variable for matrixes and such.
    N = 0
    temp = []
    t = []
    A = [] [] #Need to set correct matrix size.
    #Runs ByteDecode k time on seperated key segments.
    for x in range(k): 
        temp.append(key[(384*x) : (384*(x+1))])
    for x in range(k):
        t.append(General.ByteDecode(temp[x]))

    p = key[(384*k) : (384*k) + 32]
    for i in range(k): # re-generate matrix 𝐀
        for j in range(k):
            A[i][j] = General.SampleNTT(p| i.to_bytes | j.to_bytes )

    for i in range(k): #generate 𝐲 
        y[i] = General.SamplePolyCBD(XOF.PRF(random, N, 1), 2)
        N += 1 

    for i in range(k): #gemerate e1
        e1[i] = General.SamplePolyCBD(XOF.PRF(r,N,2) 2)
        N += 1

    e2 = General.SamplePolyCBD(XOF.PRF(r,N,2), 2)
    y2 = General.NTT(y)
    u = General.NTTi((numpy.multiply(t,y2))+e)
    u2 = XOF.Decompress(General.ByteDecode(message, 1))
    v = General.NTTi((numpy.multiply(t,y)) + e2 + u2)
    c1 = General.ByteEncode() #TODO Finish

    