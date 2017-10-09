import unittest

import pandas as pd

from metadata import DatasetMetadataLoader
from missingdata import NumericDataImputer


class TestNumericDataImputerLoader(unittest.TestCase):
    def test_impute_newDataframeContainsNoNullValuesInNumericColumns(self):
        metadata = DatasetMetadataLoader("metadata.ini")
        dataset = pd.read_csv('Data.csv')

        testee = NumericDataImputer(metadata, dataset)
        imputedDataset = testee.impute("mean")

        containNull = [imputedDataset[column].isnull().any() for column in testee.numericColumns]

        for columnContainsNull in containNull:
            self.assertFalse(columnContainsNull)
