from num2words import num2words as n2w
from unicodedata import lookup as UC


def get_int2uc_dict(max_n=50):
    i2uc = dict()
    for n in range(max_n + 1):
        i2uc[n] = transcribe(n)
    return i2uc


def transcribe(n):
    if n < 10:
        u = UC("CIRCLED DIGIT " + n2w(n).upper())
    else:
        u = UC("CIRCLED NUMBER " + n2w(n).upper().replace("-", " "))
    return u


int2uc = get_int2uc_dict()
