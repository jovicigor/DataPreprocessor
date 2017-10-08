import configparser
import sys


class DatasetMetadataLoader:
    feature_types_section = "FEATURE_TYPES"

    def __init__(self, metadata_path):
        config_parser = configparser.ConfigParser()
        config_parser.read(metadata_path)
        self.config = config_parser

    def get_feature_type(self, feature: str) -> str:
        try:
            return self.config[DatasetMetadataLoader.feature_types_section][feature]
        except KeyError:
            print("{0} is not found in metadata configuration, with cause.".format(feature))
            sys.exit(0)


class FeatureType:
    CATEGORIC = "CATEGORIC"
    NUMERIC = "NUMERIC"
