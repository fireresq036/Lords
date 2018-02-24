import lords_support
import unittest


class Lords(unittest.TestCase):
    def test_totals(self):
        """test"""
        expected_total = {lords_support.LEVEL1: 10,
                          lords_support.LEVEL2: 10,
                          lords_support.LEVEL3: 10,
                          lords_support.LEVEL4: 10,
                          lords_support.LEVELALL: 40}
        troops = {lords_support.LEVEL1: lords_support.Troops(1, 2, 3, 4),
                  lords_support.LEVEL2: lords_support.Troops(4, 3, 2, 1),
                  lords_support.LEVEL3: lords_support.Troops(1, 2, 3, 4),
                  lords_support.LEVEL4: lords_support.Troops(4, 3, 2, 1)}

        totals = lords_support.calculate_totals(troops)
        self.assertEqual(expected_total, totals)

    def test_percent_total(self):
        """test"""
        expected_total = {lords_support.LEVEL1: 10,
                          lords_support.LEVEL2: 10,
                          lords_support.LEVEL3: 10,
                          lords_support.LEVEL4: 10,
                          lords_support.LEVELALL: 40}
        expected_percents = {lords_support.LEVEL1: [0.1, 0.2, 0.3, 0.4],
                             lords_support.LEVEL2: [0.4, 0.3, 0.2, 0.1],
                             lords_support.LEVEL3: [0.1, 0.2, 0.3, 0.4],
                             lords_support.LEVEL4: [0.4, 0.3, 0.2, 0.1]}
        troops = {lords_support.LEVEL1: lords_support.Troops(1, 2, 3, 4),
                  lords_support.LEVEL2: lords_support.Troops(4, 3, 2, 1),
                  lords_support.LEVEL3: lords_support.Troops(1, 2, 3, 4),
                  lords_support.LEVEL4: lords_support.Troops(4, 3, 2, 1)}

        percents = lords_support.calculate_percents(troops, expected_total)
        self.assertEqual(expected_percents, percents)

    def test_zero(self):
        """test"""
        expected_totals = {lords_support.LEVEL1: 0,
                           lords_support.LEVEL2: 0,
                           lords_support.LEVEL3: 0,
                           lords_support.LEVEL4: 0,
                           lords_support.LEVELALL: 0}
        expected_percents = {lords_support.LEVEL1: [0., 0., 0., 0.],
                             lords_support.LEVEL2: [0., 0., 0., 0.],
                             lords_support.LEVEL3: [0., 0., 0., 0.],
                             lords_support.LEVEL4: [0., 0., 0., 0.]}
        troops = {lords_support.LEVEL1: lords_support.Troops(0, 0, 0, 0),
                  lords_support.LEVEL2: lords_support.Troops(0, 0, 0, 0),
                  lords_support.LEVEL3: lords_support.Troops(0, 0, 0, 0),
                  lords_support.LEVEL4: lords_support.Troops(0, 0, 0, 0)}

        percents = lords_support.calculate_percents(troops, expected_totals)
        self.assertEqual(expected_percents, percents)

    def test_precentstroop_type(self):
        troops = {lords_support.LEVEL1: lords_support.Troops(1, 2, 3, 4),
                  lords_support.LEVEL2: lords_support.Troops(4, 3, 2, 1),
                  lords_support.LEVEL3: lords_support.Troops(1, 2, 3, 4),
                  lords_support.LEVEL4: lords_support.Troops(4, 3, 2, 1)}
        percents = lords_support.calculate_type_percents(troops)
        self.assertEqual(percents, "0")
