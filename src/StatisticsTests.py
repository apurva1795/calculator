import unittest
from Statistics import Statistics

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def tearDown(self):
        if self.statistics is not None:
            self.statistics = None

    def test_instantiate_statistics(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_Mean(self):
        list = [5, 78, 3]
        result = 28.666666666666668
        self.assertEqual(self.statistics.Mean(list), result)

    def test_PopVariance(self):
        list = [21, 13, 19, 13,19,13]
        result = 11.5555555556
        self.assertEqual(self.statistics.PopVariance(list), result)

    def test_StandardDeviation(self):
        list = [21, 13, 19, 13,19,13]
        result = 4.8989794855664
        self.assertEqual(self.statistics.StandardDeviation(list), result)




