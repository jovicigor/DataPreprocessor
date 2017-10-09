import unittest
import pandas as pd
from metadata import DatasetMetadataLoader
from engine import PreprocessingEngine
from missingdata import ImputeStrategy


class TestPreprocessingEngine(unittest.TestCase):
    def test_preprocessMissingData_createdDataframeContansNoNullValues(self):
        metadata = DatasetMetadataLoader("metadata.ini")
        dataset = pd.read_csv('Data.csv')

        processedDataframe = PreprocessingEngine(dataset, metadata) \
            .imputeNumericDataUsing(ImputeStrategy.MEAN) \
            .filterMissingCategoricData() \
            .getProcessedDataframe()

        containNull = [processedDataframe[column].isnull().any() for column in dataset.columns]

        for columnContainsNull in containNull:
            self.assertFalse(columnContainsNull)
