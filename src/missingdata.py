from sklearn.preprocessing import Imputer
from metadata import FeatureType


class ImputeStrategy:
    MEAN = "mean"
    MEDIAN = "median"
    MOST_FREQUENT = "most_frequent"


class NumericDataImputer:
    def __init__(self, metadata, dataframe):
        self.metadata = metadata
        self.dataframe = dataframe.copy()
        self.numericColumns = [columnName for columnName in dataframe.columns
                               if metadata.get_feature_type(columnName) == FeatureType.NUMERIC]

    def impute(self, strategy=ImputeStrategy.MEAN):
        imputer = Imputer(missing_values='NaN', strategy=strategy, axis=0)

        for column in self.numericColumns:
            columnIndex = self.dataframe.columns.tolist().index(column)
            columnValues = self.dataframe.iloc[:, columnIndex:columnIndex + 1].values
            self.dataframe[column] = imputer.fit_transform(columnValues)

        return self.dataframe
