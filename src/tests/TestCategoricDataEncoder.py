import unittest
import pandas as pd
from metadata import DatasetMetadataLoader, FeatureType
from engine import PreprocessingEngine
from missingdata import ImputeStrategy

from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
from categoricdata import CategoricDataEncoder


class TestPreprocessingEngine(unittest.TestCase):
    def test_encodeCategoricColumns_columnsEncoded(self):
        metadata = DatasetMetadataLoader("metadata.ini")
        dataset = pd.read_csv('Data.csv')

        processedDataset = self.prepareDataset(dataset, metadata)
        categoricColumns = [column for column in processedDataset.columns
                            if metadata.getFeatureType(column) == FeatureType.CATEGORIC]

        for categoricColumn in categoricColumns:
            self.assertTrue(is_string_dtype(processedDataset[categoricColumn]))

        testee = CategoricDataEncoder(processedDataset, metadata)
        encodedDataset = testee.encodeCategoricColumns()

        for categoricColumn in categoricColumns:
            self.assertTrue(is_numeric_dtype(encodedDataset[categoricColumn]))

    def prepareDataset(self, dataset, metadata):
        return PreprocessingEngine(dataset, metadata) \
            .imputeNumericDataUsing(ImputeStrategy.MEAN) \
            .filterMissingCategoricData() \
            .getProcessedDataframe()
