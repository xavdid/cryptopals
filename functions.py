import urllib2
import numpy
from collections import namedtuple
Result = namedtuple('Result', 'message score')
import string
from functools import reduce

SINGLE_BITS = map(chr, range(256))
# from https://en.wikipedia.org/wiki/Letter_frequency
LETTER_FREQUENCIES = numpy.array([.08167, .01492, .02782, .04253, .02702, .02228, .02015, .06094, .06966, .00153, .00772, .04025, .02406, .06749, .07507, .01929, .00095, .05987, .06327, .09056, .02758, .00978, .02360, .00150, .01974, .0007])

words = set(line.strip() for line in open('/usr/share/dict/words'))

# challenge 1.1
def hex_to_b64(s):
    return s.decode("hex").encode("base64").strip()  # has a trailing newline


# challenge 1.2
def fixed_xor(a, b):
    return hex(int(a, 16) ^ int(b, 16))[2:-1]  # has extra characters

def score_english(s):
    s = s.lower()  # compare everything case insensitive
    test_values = numpy.array(relative_frequency(s))
    score = numpy.linalg.norm(LETTER_FREQUENCIES - test_values)
    num_non_english = map(lambda x: x not in string.printable, s).count(True)
    return score * numpy.exp(num_non_english / float(len(s)))

def relative_frequency(s):
    message_length = float(len(s))
    result = []
    for letter in string.letters[:26]:
        result.append(s.count(letter) / message_length)

    return result


# https://stackoverflow.com/a/40949538/1825390
def string2bits(s):
    return [bin(ord(x))[2:].zfill(8) for x in s]


def bits2string(b):
    return ''.join([chr(int(x, 2)) for x in b]).strip()


def xor_bytestr(a, b):
    return bin(int(a, 2) ^ int(b, 2))[2:]

# challenge 1.3
def decode_cipher(s):
    """
    returns tuple of (message, score)
    """
    message_bits = string2bits(s.strip().decode('hex'))
    res = []

    for bit in SINGLE_BITS:
        xor = string2bits(bit)[0]
        message = bits2string([xor_bytestr(b, xor) for b in message_bits])
        res.append(Result(message, score_english(message)))

    best_match = sorted(res, key=lambda x: x.score)[0]
    return best_match

# challenge 1.4
def get_strings_from_web(url):
    res = []
    for line in urllib2.urlopen(url):
        res.append(line)

    return res

def decode_multi_xor(ciphertexts):
    res = []
    for s in ciphertexts:
        res.append(decode_cipher(s))

    return sorted(res, key=lambda x: x.score)[0]

if __name__ == 'main':
    pass
