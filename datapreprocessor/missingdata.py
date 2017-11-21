import pandas as pd
from sklearn.preprocessing import Imputer

from datapreprocessor.metadata import FeatureType


class ImputeStrategy:
    MEAN = "mean"
    MEDIAN = "median"
    MOST_FREQUENT = "most_frequent"


class NumericDataImputer:
    def __init__(self, metadata, dataframe):
        self.dataframe = dataframe.copy()
        self.numericColumns = self.extractNumericColumns(dataframe, metadata)

    def extractNumericColumns(self, dataframe, metadata):
        return [columnName for columnName in dataframe.columns
                if metadata.getFeatureType(columnName) == FeatureType.NUMERIC]

    def impute(self, strategy=ImputeStrategy.MEAN):
        imputer = Imputer(missing_values='NaN', strategy=strategy, axis=0)

        for column in self.numericColumns:
            columnIndex = self.dataframe.columns.tolist().index(column)
            columnValues = self.dataframe.iloc[:, columnIndex:columnIndex + 1].values
            self.dataframe[column] = imputer.fit_transform(columnValues)

        return self.dataframe


class CategoricDataFilter:
    def __init__(self, metadata, dataframe):
        self.dataframe = dataframe.copy()
        self.categoricColumns = self.extractCategoricColumns(dataframe, metadata)

    def extractCategoricColumns(self, dataframe, metadata):
        return [columnName for columnName in dataframe.columns
                if metadata.getFeatureType(columnName) == FeatureType.CATEGORIC]

    def removeSamplesWithMissingData(self):
        for column in self.categoricColumns:
            self.dataframe = self.dataframe[pd.notnull(self.dataframe[column])]

        return self.dataframe
