from string import ascii_uppercase as a


def matrix_to_alpha(m_num, blank="_"):
    """
    Edit a numerical matrix, `m_num`, turning it into an alphabetic one.

    Transcribe the range 0-25 into the letters A-Z, with any values over 25
    transcribed as the value of `blank` (default: underscore).
    """
    m_alpha = [[a[e] if e in range(len(a)) else "_" for e in row] for row in m_num]
    return m_alpha
