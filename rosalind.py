def revc(s):
    '''

    :param s:  the input sequence
    :return: the reverse complement
    '''

    s_c = ""
    pair = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    for letter in s[::-1]:
        s_c += pair[letter];

    return s_c;

def rna(t):
    '''

    :param u: input sequence
    :return: rna sequence
    '''

    u = ""
    for letter in t:
        if letter == 'T':
            u += 'U'
        else:
            u += letter
    return u

def dna(s):
    '''

    :param s: input sequence
    :return: output amount
    '''

    count = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for char in s:
        count[char] += 1

    return (s['A'], s['T'], s['G'], s['C'])