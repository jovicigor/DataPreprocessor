import configparser
import sys


class DatasetMetadataLoader:
    FEATURE_TYPES_SECTION = "FEATURE_TYPES"

    def __init__(self, metadata_path):
        configParser = configparser.ConfigParser()
        configParser.read(metadata_path)
        self.config = configParser

    def getFeatureType(self, feature: str) -> str:
        try:
            return self.config[DatasetMetadataLoader.FEATURE_TYPES_SECTION][feature]
        except KeyError:
            print("{0} is not found in metadata configuration, with cause.".format(feature))
            sys.exit(0)


class FeatureType:
    CATEGORIC = "CATEGORIC"
    NUMERIC = "NUMERIC"
