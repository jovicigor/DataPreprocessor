import unittest

from datapreprocessor.metadata import DatasetMetadataLoader
from datapreprocessor.metadata import FeatureType


class TestDatasetMetadataLoader(unittest.TestCase):
    def test_loadCategoricType_returnsCategoric(self):
        metadata = DatasetMetadataLoader("metadata.ini")

        featureType = metadata.getFeatureType("Country")

        self.assertEqual(featureType, FeatureType.CATEGORIC)

    def test_loadNumericType_returnsNumeric(self):
        metadata = DatasetMetadataLoader("metadata.ini")

        featureType = metadata.getFeatureType("Age")

        self.assertEqual(featureType, FeatureType.NUMERIC)
