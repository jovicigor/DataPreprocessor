import unittest
from metadata import DatasetMetadataLoader
from metadata import FeatureType


class TestDatasetMetadataLoader(unittest.TestCase):
    def test_loadCategoricType_returnsCategoric(self):
        metadata = DatasetMetadataLoader("metadata.ini")

        feature_type = metadata.get_feature_type("Country")

        self.assertEqual(feature_type, FeatureType.CATEGORIC)

    def test_loadNumericType_returnsNumeric(self):
        metadata = DatasetMetadataLoader("metadata.ini")

        feature_type = metadata.get_feature_type("Age")

        self.assertEqual(feature_type, FeatureType.NUMERIC)
