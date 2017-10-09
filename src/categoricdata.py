from sklearn.preprocessing import LabelEncoder

from metadata import FeatureType


#
# dataset = pd.read_csv('Data.csv')
# metadata = DatasetMetadataLoader("metadata.ini")
#
# labelencoder = LabelEncoder()
#
# column = "Country"
#
# dataset[column] = labelencoder.fit_transform(dataset[column])
# newColumnNames = labelencoder.classes_
#
# onehotencoder = OneHotEncoder(categorical_features=[0])
# print(newColumnNames)
# for index, newColumnName in enumerate(newColumnNames):
#     valuesToTransform = [[value] for value in dataset[column]]
#     dataset[newColumnName] = onehotencoder.fit_transform(valuesToTransform).toarray()[:, index:index + 1]
#
# print(dataset)


class CategoricDataEncoder:
    def __init__(self, dataframe, metadata):
        self.dataset = dataframe.copy()
        self.categoricColumns = [columnName for columnName in dataframe.columns
                                 if metadata.getFeatureType(columnName) == FeatureType.CATEGORIC]

    def encodeCategoricColumns(self):
        labelencoder = LabelEncoder()
        for column in self.categoricColumns:
            self.dataset[column] = labelencoder.fit_transform(self.dataset[column])
        return self.dataset
