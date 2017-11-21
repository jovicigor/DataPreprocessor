import unittest

import pandas as pd
from pandas.api.types import is_numeric_dtype
from pandas.api.types import is_string_dtype

from datapreprocessor.categoricdata import CategoricDataEncoder
from datapreprocessor.engine import PreprocessingEngine
from datapreprocessor.metadata import DatasetMetadataLoader, FeatureType
from datapreprocessor.missingdata import ImputeStrategy


class TestPreprocessingEngine(unittest.TestCase):
    def test_encodeCategoricColumns_columnsEncoded(self):
        metadata = DatasetMetadataLoader("metadata.ini")
        dataset = pd.read_csv('Data.csv')

        processedDataset = self.prepareDataset(dataset, metadata)
        categoricColumns = [column for column in processedDataset.columns
                            if metadata.getFeatureType(column) == FeatureType.CATEGORIC]

        for categoricColumn in categoricColumns:
            self.assertTrue(is_string_dtype(processedDataset[categoricColumn]))

        testee = CategoricDataEncoder(metadata, processedDataset)
        encodedDataset = testee.encodeCategoricColumns()

        for categoricColumn in categoricColumns:
            self.assertTrue(is_numeric_dtype(encodedDataset[categoricColumn]))
        print(encodedDataset)

    def test_encodeCategoricColumnsAndTransformOne_encodedTransformedAndDeleted(self):
        metadata = DatasetMetadataLoader("metadata.ini")
        dataset = pd.read_csv('Data.csv')

        processedDataset = self.prepareDataset(dataset, metadata)

        testee = CategoricDataEncoder(metadata, processedDataset)
        encodedDataset = testee.encodeCategoricColumns(columnsToTransform=["Country"])

        self.assertFalse("Country" in encodedDataset.columns)
        self.assertTrue("Spain" in encodedDataset.columns)
        self.assertTrue("Germany" in encodedDataset.columns)
        self.assertTrue("France" in encodedDataset.columns)

    def prepareDataset(self, dataset, metadata):
        return PreprocessingEngine(dataset, metadata) \
            .imputeNumericDataUsing(ImputeStrategy.MEAN) \
            .filterMissingCategoricData() \
            .getProcessedDataframe()
