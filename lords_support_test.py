import logging
import lords_support
import sys
import unittest


class Lords(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(stream=sys.stderr)
        logging.getLogger(
            "Lords.test_precentstroop_type").setLevel(logging.DEBUG)

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
        log = logging.getLogger('Lords.test_precentstroop_type')
        troops = {lords_support.LEVEL1: lords_support.Troops(1, 2, 3, 4),
                  lords_support.LEVEL2: lords_support.Troops(1, 2, 3, 4),
                  lords_support.LEVEL3: lords_support.Troops(1, 2, 3, 4),
                  lords_support.LEVEL4: lords_support.Troops(1, 2, 3, 4)}
        self.assertEqual(len(troops), 4)
        self.assertEqual((troops[lords_support.LEVEL1]).seige, 4)
        for key, data in troops.iteritems():
            log.info('%s: %s' % (key, data))
        totals, percents = lords_support.calculate_type_percents(troops)
        self.assertEqual(percents, {lords_support.TYPE_INF: 20,
                                    lords_support.TYPE_CAV: 10,
                                    lords_support.TYPE_RNG: 30,
                                    lords_support.TYPE_SEG: 40})
        self.assertEqual(totals, {lords_support.TYPE_INF: 8,
                                  lords_support.TYPE_CAV:4,
                                  lords_support.TYPE_RNG: 12,
                                  lords_support.TYPE_SEG: 16})


if __name__ == '__main__':
    unittest.main()
