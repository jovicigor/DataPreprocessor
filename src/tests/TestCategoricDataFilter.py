import unittest
import pandas as pd
from missingdata import CategoricDataFilter
from metadata import DatasetMetadataLoader


class TestCategoricDataFilter(unittest.TestCase):
    def test_impute_newDataframeContainsNoNullValuesInCategoricColumns(self):
        metadata = DatasetMetadataLoader("metadata.ini")
        dataset = pd.read_csv('Data.csv')

        testee = CategoricDataFilter(metadata, dataset)
        filteredDataset = testee.removeSamplesWithMissingData()

        containNull = [filteredDataset[column].isnull().any() for column in testee.categoricColumns]

        for columnContainsNull in containNull:
            self.assertFalse(columnContainsNull)
