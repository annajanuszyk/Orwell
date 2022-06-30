import unittest
import string
import utilities as u


str_Chinese = "那是四月份的一天，天气晴朗而寒冷，时钟敲响了十三点。温斯顿·史密斯的下巴紧紧抵着胸膛，躲避寒风的侵袭。他快步穿过胜利大厦的玻璃门，但还是慢了一些，一股席卷着沙砾的旋风尾随着他刮了进来。"

str_Polish = "Był jasny, zimny dzień kwietniowy i zegary biły trzynastą. Winston Smith, z głową wtuloną w ramiona dla osłony przed tnącym wiatrem, wślizgnął się przez szklane drzwi do Bloku Zwycięstwa, ale nie dość szybko, by powstrzymać tuman ziarnistego pyłu, który wtargnął za nim do środka."

str_English = "It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him."


class TestWordCount(unittest.TestCase):
    def test_Polish(self):
        out = u.word_count(str_Polish)
        self.assertEqual(len(str_Polish.split(" "))-1,
                         len(out))
                        
    def test_English_1(self):
        out = u.word_count(str_English)
        self.assertEqual(len(str_English.split(" "))-6-2,
                         len(out))

    def test_English_2(self):
        out = u.word_count(str_English)
        self.assertEqual(out["the"], 3)

    def test_English_3(self):
        out = u.word_count(str_English)
        self.assertEqual(out["quickly"], 2)




if __name__ == '__main__':
    unittest.main()
