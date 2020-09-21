from unittest import TestCase

decoding_map = {str(x + 1): chr(x + ord('A')) for x in range(26)}


def decode(encoded_str):
    if len(encoded_str) == 1:
        possible_words = [decoding_map[encoded_str]]

    return possible_words


class MyTest(TestCase):
    def test(self):
        self.assertCountEqual(['K', 'AA'], decode("11"))

MyTest().test()