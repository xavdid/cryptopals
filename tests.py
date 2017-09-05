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
        start = '1c0111001f010100061a024b53535009181c'.decode('hex')
        xor = '686974207468652062756c6c277320657965'.decode('hex')
        end = '746865206b696420646f6e277420706c6179'.decode('hex')
        self.assertEqual(f.fixed_xor(start, xor), end)

    def test__1_3(self):
        start = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
        self.assertIn('bacon', f.decode_cipher(start).message)

    def test__1_4(self):
        ciphertexts = f.get_strings_from_web('https://cryptopals.com/static/challenge-data/4.txt')
        self.assertIn('jumping', f.decode_multi_xor(ciphertexts).message)

    def test__1_5(self):
        plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
        key = 'ICE'
        result = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
        self.assertEqual(f.encrypt_multi_xor(plaintext, key).encode('hex'), result)

if __name__ == '__main__':
    unittest.main()
