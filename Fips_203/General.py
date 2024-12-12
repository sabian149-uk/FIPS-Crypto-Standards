from bitarray import bitarray
import XOF
import hashlib


#All global parameters define in the ML-KEM parameter set. Went with MNL-KEM-1024 but can be easily altered.

n = 256
q=3329
k = 4
eta = 2 #eta1 and eta2 are the same value sete in the apporved parameter set
d1 = 11 #d^u is what is defined on the parameter set but easier to type as d1
d2 = 5 #d^v is what is defined on the parameter set but easier to type as d2


primitiveRoot = 3 # primitive of root of "q". Shouldnt need to be changed but if q is changed it will need to be changed. Made global as used by mutliple functions.


def BitsToBytes(input): #Converts array of bits to array of bytes. 
    length = len(input)
    bytesArray = []
    if length % 8 == 0:
        for x in range(0, length, 8):
            tempArray = input[x:x+8]  # gets 8 integers and stores in temp.
            tempString = ""
            for y in range(0,8):
                tempString += str(tempArray[y])
            bytesArray.append(int(tempString, 2))  # Appends byte to array as integer. Easier to read and easily convertible to byte. 


    else:
        print("Function BitsToBytes failed. Inputted Array was not of length.")

    return bytes(bytesArray)

def BytesToBits(input): #Converts array of bytes to bits and stores them individually.
    length = len(input)
    bytesArray = []
    for x in range(length):
        temp = format(input[x], '08b')
        for y in range(0,8):
            bytesArray.append(int(temp[y]))
        
    return bytesArray


def ByteEncode(input): #TODO Need to add d
    byteArray = []
    if(len(input) == 256):
        for temp in input:
            for y in range(12):
                byteArray.append(temp % 2) # Gets the first bit in the input
                temp >>= 1 #Shifts bit by 1
        
        byteArray = BitsToBytes(byteArray)    

    else:
        print("Function ByteEncode failed. Inputted Array was not of length.")

    return byteArray


def ByteDecode(input): #TODO Need to add d variable.
    bitsArray = BytesToBits(input)
    byteArray = []
    if (len(bitsArray) == 256):
        for x in range(0, len(bitsArray), 12):
            temp = 0
            for y in range(12):
                if(y+ x < len(bitsArray)):     
                    temp = (bitsArray[y+x]*(2**y)) + temp #Gets 12 bits following x and coverts to integer
            
            temp = temp % q
            byteArray.append(temp)

    else:
        print("Function ByteDecode failed. Inputted Array was not of length.")
    return byteArray

def SampleNTT(input):
    ctx = XOF.Init()
    XOF.Absorb(ctx, input)
    output = []
    j = 0
    while j != 256:
        C = XOF.Squeeze(ctx, 3)
        d1 = C[0] + 256 * (C[1] % 16)
        d2 = (C[1]//16) + 16*C[2]
        if d1 < q:
            output.append(d1)
            j += 1
        if d2 < q and j < 256:
            output.append(d2)
            j += 1


    return output    

def SamplePolyCBD(input, length):
    bits = BytesToBits(input)
    output = []
    print(bits)
    for x in range(256):
        temp1 = 0
        temp2 = 0
        for y in range(eta-1):
            temp1 += bits[2 * x * length + y]
            print(temp1)
        for y in range(eta-1):
            temp2 += bits[2 * x * length + length + y]
            print(temp2)

        output.append((temp1-temp2) % q)
        print("new line")
    return output


def BitReverse(input, bitLength): #Needed for the NTT function
    reversedInput = 0
    for x in range(bitLength):
        reversedInput = (reversedInput << 1) | (input & 1)
        input >>= 1
    return reversedInput



def NTT(input):
    primitiveRoot = 3 # primitive of root of "q". Shouldnt need to be changed but if q is changed it will need to be changed.
    inputCopy = input[:]
    i = 1
    length = 128
    while (length >= 2):
        start = 0
        while(start < 256):
            reversedBit = bitReverse(i,7)
            zeta = pow(primitiveRoot, reversedBit, q) # Is basically just doing prime^bit mod q but in a more efficient way. # TODO IMPLEMENT EVERYWHERE WITH MOD 
            i += 1
            j = start
            while(j < start + length):
                t = (zeta*input[j+length]) % q
                inputCopy[j+length] = (inputCopy[j] - t) % q 
                inputCopy[j] = (inputCopy[j] + t) % q
                j += 1
            start += (2*length)
        length = length//2

    return inputCopy

def NTTi(input):

    inputCopy = input[:]
    i = 127
    length = 2
    while (length <= 128):
        start = 0
        while(start < 256):
            reversedBit = bitReverse(i,7)
            zeta = pow(primitiveRoot, reversedBit, q) # Is basically just doing prime^bit mod q but in a more efficient way. # TODO IMPLEMENT EVERYWHERE WITH MOD 
            i += 1
            j = start
            while(j < start + length):
                t = inputCopy[j]
                inputCopy[j]= t + inputCopy[f+length]
                inputCopy[j+length] = zeta* (inputCopy[j+length]-t)
                j += 1
            start += (2*length)
        length = 2*length
    inputCopy = pow
    return inputCopy

def BaseCaseMultiply(a0,a1,b0,b1,gamma):
    c0 = (a0*b0+a1*b1*gamma) % q
    c1 = (a0*b1+a1*b0) % q
    return(c0,c1)



def MultiplyNTTs(f,g):
    h = [0] * 256
    for i in range(128):
        (h[2*i], h[2*i+1]) = BaseCaseMultiply(f[2*i],f[2*i+1],g[2*i],g[2*i+1], pow(primitiveRoot, bitReverse(i,7)+1))
    return(h)



        
