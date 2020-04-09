from transcribe_n import int2uc
from string import ascii_uppercase as a

def a2i(txt):
    """
    Transform an alphabetic character string into an integer ("A" => 0, "B" => 1, ...)
    """
    return ''.join([str(a.index(x)) if x in a else x for x in txt])

def a2c(txt):
    """
    Transform an alphabetic character string into a Unicode enclosed alphanumeric
    form of the corresponding indexed number from the a2i function, after transcribing
    via the int2uc function defined in the transcribe_n module, which in turn uses the
    num2words package's function num2words()
    """
    return ''.join([int2uc.get(a.index(x)) if x in a else x for x in txt])
