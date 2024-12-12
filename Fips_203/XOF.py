import hashlib

def Init():
    return hashlib.shake_128()


def Absorb(ctx, data):
    ctx.update(data)

def Squeeze(ctx, byteLength):
    return ctx.digest(byteLength)

def PRF(s,b,length):
    input_data = s + bytes([b])
    init = Init()
    init.update(input_data)
    output = shake.digest(64 * length)

    return(output)

def Compress(z, d, q):
    output = (((x**d)//q) * z) % 2^d
    return output

def Decompress(z, d, q):
    q = 12
    output = ((q//(2**d))*z) 
    return output
