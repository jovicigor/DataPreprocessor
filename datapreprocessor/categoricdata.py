from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

from datapreprocessor.metadata import FeatureType


class CategoricDataEncoder:
    def __init__(self, metadata, dataframe):
        self.dataset = dataframe.copy()
        self.categoricColumns = [columnName for columnName in dataframe.columns
                                 if metadata.getFeatureType(columnName) == FeatureType.CATEGORIC]

    def encodeCategoricColumns(self, columnsToTransform=[]):
        labelencoder = LabelEncoder()
        for column in self.categoricColumns:
            self.dataset[column] = labelencoder.fit_transform(self.dataset[column])
            if column in columnsToTransform:
                self.transformColumn(column, labelencoder.classes_)
        return self.dataset

    def transformColumn(self, column, newColumns):
        onehotencoder = OneHotEncoder(categorical_features=[0])

        for index, newColumnName in enumerate(newColumns):
            valuesToTransform = [[value] for value in self.dataset[column]]
            self.dataset[newColumnName] = onehotencoder.fit_transform(valuesToTransform).toarray()[:, index:index + 1]

        self.dataset.drop(column, axis=1, inplace=True)
        return self.dataset
