import hashlib

def Init():
    return hashlib.shake_128()


def Absorb(ctx, data):
    ctx.update(data)

def Squeeze(ctx, byteLength):
    output_data = ctx.digest(byteLength)
    return ctx, output_data

def PRF(s,b,length):
 
    input_data = s + bytes([b])
    init = Init()
    init.update(input_data)
    output = init.digest(64 * length)

    return(output)

def Compress(z, d, q):
    output = (((x**d)//q) * z) % 2^d
    return output

def Decompress(z, d, q):
    q = 12
    output = ((q//(2**d))*z) 
    return output

import math # Temp AI code to make it work

# Compress function
def compress_d(x, d, q=3329):
    """
    Compresses an integer x in Z_q into Z_(2^d).

    Parameters:
    x (int): The input value in Z_q (0 <= x < q).
    d (int): The target bit length (d < 12).
    q (int): The modulus (default is 3329).

    Returns:
    int: The compressed value in Z_(2^d).
    """
    if not (0 <= x < q):
        raise ValueError("x must be in the range [0, q).")
    if not (0 < d < 12):
        raise ValueError("d must be in the range (0, 12).")
    return math.floor((2**d / q) * x) % (2**d)

# Decompress function
def decompress_d(y, d, q=3329):
    """
    Decompresses an integer y in Z_(2^d) back to Z_q.

    Parameters:
    y (int): The input value in Z_(2^d) (0 <= y < 2^d).
    d (int): The original bit length (d < 12).
    q (int): The modulus (default is 3329).

    Returns:
    int: The decompressed value in Z_q.
    """
    if not (0 <= y < 2**d):
        raise ValueError("y must be in the range [0, 2^d).")
    if not (0 < d < 12):
        raise ValueError("d must be in the range (0, 12).")
    return math.floor((q / 2**d) * y)

