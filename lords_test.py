import lords_support
import unittest


def mock_request(tag_information):
    tags = tag_information

    def get(tag, default_value):
        if tag in tags:
            return tags[tag]
        return default_value


class Lords(unittest.TestCase):
    def test(self):
        """test"""
        expected_total = {lords_support.LEVEL1: 10,
                          lords_support.LEVEL2: 10,
                          lords_support.LEVEL3: 10,
                          lords_support.LEVEL4: 10}
        expected_percents = {lords_support.LEVEL1: [0.1, 0.2, 0.3, 0.4],
                             lords_support.LEVEL2: [0.4, 0.3, 0.2, 0.1],
                             lords_support.LEVEL3: [0.1, 0.2, 0.3, 0.4],
                             lords_support.LEVEL4: [0.4, 0.3, 0.2, 0.1]}
        troops = {lords_support.LEVEL1: lords_support.Troops(1, 2, 3, 4),
                  lords_support.LEVEL2: lords_support.Troops(4, 3, 2, 1),
                  lords_support.LEVEL3: lords_support.Troops(1, 2, 3, 4),
                  lords_support.LEVEL4: lords_support.Troops(4, 3, 2, 1)}

        totals, percents = lords_support.calculate_percents(troops)
        self.assertEqual(expected_total, totals)
        self.assertEqual(expected_percents, percents)
