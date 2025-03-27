import unittest

from huffman import compress, decompress

class HuffmanTest(unittest.TestCase):
    def test_compress_happypath(self):
        self.assertEqual(compress('hello'), '110100101101100011011110')

    def test_decompress_happypath(self):
        self.assertEqual(decompress('110100101101100011011110'), 'hello')

    def test_encode_tree(self):
        pass

        
if __name__ == '__main__':
    unittest.main()