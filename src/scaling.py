class Scaler:
    def __init__(self, scaler):
        self.scaler = scaler

    def scaleDataset(self, dataset):
        datasetCopy = dataset.copy()
        datasetCopy.loc[:, :] = self.scaler.fit_transform(datasetCopy.loc[:, :])

        return datasetCopy
