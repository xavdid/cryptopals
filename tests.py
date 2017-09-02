import unittest
import functions as f


class TestStringMethods(unittest.TestCase):

    def test__1_1(self):
        start = (
            '49276d206b696c6c696e6720796f7572206272616'
            '96e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        )
        end = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
        self.assertEqual(f.hex_to_b64(start), end)

    def test__1_2(self):
        start = '1c0111001f010100061a024b53535009181c'
        xor = '686974207468652062756c6c277320657965'
        end = '746865206b696420646f6e277420706c6179'
        self.assertEqual(f.fixed_xor(start, xor), end)


if __name__ == '__main__':
    unittest.main()
