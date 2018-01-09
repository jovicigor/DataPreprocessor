import unittest

import pandas as pd
from datapreprocessor.shift import ColumnShifter


class TestColumnShifter(unittest.TestCase):
    def test_shiftColumnToRight_columnShifted(self):
        dataset = pd.read_csv('Data.csv')
        column_to_shift = "Country"

        testee = ColumnShifter(dataset)
        shifted_dataset = testee.shiftRight(column_to_shift)

        self.assertEqual(column_to_shift, shifted_dataset.columns.values[-1])
