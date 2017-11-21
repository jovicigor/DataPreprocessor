import unittest

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

from datapreprocessor.engine import PreprocessingEngine
from datapreprocessor.metadata import DatasetMetadataLoader
from datapreprocessor.missingdata import ImputeStrategy


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

        encodedDataframe = PreprocessingEngine(processedDataframe, metadata) \
            .encodeCategoricData(columnsToTransform="Country") \
            .getProcessedDataframe()

        self.assertFalse("Country" in encodedDataframe.columns)
        self.assertTrue("Spain" in encodedDataframe.columns)
        self.assertTrue("Germany" in encodedDataframe.columns)
        self.assertTrue("France" in encodedDataframe.columns)

        scaledDataframe = PreprocessingEngine(encodedDataframe, metadata) \
            .scaleDataset(MinMaxScaler()) \
            .getProcessedDataframe()

        # TODO: add list of columns to be scaled
        # allcolumns are scaled
        for column in scaledDataframe.columns:
            columnIsScaled = (scaledDataframe[column] <= 1).all()
            self.assertTrue(columnIsScaled)

        print(scaledDataframe)
        print(scaledDataframe[["Age", "Salary"]])
