import unittest
from crypt import Crypto


KEY = 'тест'


class TestMain(unittest.TestCase):
    _crypto: Crypto = Crypto(KEY)

    def test_generate_token(self):
        token = self._crypto.generate_token()
        self.assertIsNotNone(token)

    def test_convert_text(self):
        convert_text = self._crypto._convert_text('абв')
        self.assertEqual(convert_text, 321345368)

    def test_shuffle_text(self):
        digit_text = self._crypto.shuffle_text(398376376314, 321345368, 213)
        self.assertEqual(digit_text, 152414153436154854)

    def test_convert_key(self):
        convert_key = self._crypto.convert_key(2413)
        self.assertEqual(convert_key, 398376376314)

    # def test_convert_of_notation(self):
    #     shuffle_string = self._crypto.convert_to_notation(152414153436154854, 4)
    #     self.assertTupleEqual(shuffle_string, ('21233203130120311313323113102', '44'))

    def test_crypto(self):
        crypto_text = self._crypto.crypt('21233203130120311313323113102')
        print(crypto_text)
        self.assertEqual('21233203130120311313323113102', 'вбвггвагбгабвагббгбггвгббгбав')

if __name__ == '__main__':
    unittest.main()