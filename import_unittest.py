import unittest
from units import convert

class TestUnits(unittest.TestCase):
    def test_three_units(self):
        ratios = {
            ("gleep", "glorp"): 3, # 3 gleeps = 1 glorp
            ("shneep", "glorp"): 60, # 60 shneeps = 1 glorp
        }

        # 2 gleeps = 40 shneeps
        self.assertEqual(convert(ratios, "gleep", "shneep", 2), 40)

    def test_impossible(self):
        ratios = {
            ("gleep", "glorp"): 3, # 3 gleeps = 1 glorp
            ("glarg", "toriver"): 70, # 70 glargs = 1 toriver
        }

        # It's impossible to convert gleeps to torivers
        self.assertIsNone(convert(ratios, "gleep", "toriver", 1))

    def test_trivial(self):
        ratios = {
            ("gleep", "glorp"): 3, # 3 gleeps = 1 glorp
        }

        # 6 gleeps = 2 glorps
        self.assertEqual(convert(ratios, "gleep", "glorp", 6), 2)

    def test_trivial_backwards(self):
        ratios = {
            ("gleep", "glorp"): 3, # 3 gleeps = 1 glorp
        }

        # 2 glorps = 6 gleeps
        self.assertEqual(convert(ratios, "glorp", "gleep", 2), 6)

if __name__ == '__main__':
    unittest.main()
