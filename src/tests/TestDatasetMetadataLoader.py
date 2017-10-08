import unittest
from metadata import DatasetMetadataLoader
from metadata import FeatureType


class TestDatasetMetadataLoader(unittest.TestCase):
    def test_loadCategoricType_returnsCategoric(self):
        metadata = DatasetMetadataLoader("metadata.ini")

        featureType = metadata.getFeatureType("Country")

        self.assertEqual(featureType, FeatureType.CATEGORIC)

    def test_loadNumericType_returnsNumeric(self):
        metadata = DatasetMetadataLoader("metadata.ini")

        featureType = metadata.getFeatureType("Age")

        self.assertEqual(featureType, FeatureType.NUMERIC)
