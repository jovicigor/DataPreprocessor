from datapreprocessor.categoricdata import CategoricDataEncoder
from datapreprocessor.missingdata import CategoricDataFilter
from datapreprocessor.missingdata import NumericDataImputer
from datapreprocessor.scaling import Scaler
from datapreprocessor.shift import ColumnShifter


class PreprocessingEngine:
    def __init__(self, dataframe, metadata):
        self.dataset = dataframe
        self.metadata = metadata

    def imputeNumericDataUsing(self, strategy):
        imputer = NumericDataImputer(self.metadata, self.dataset)
        self.dataset = imputer.impute(strategy)
        return self

    def filterMissingCategoricData(self):
        categoricDataFilter = CategoricDataFilter(self.metadata, self.dataset)
        self.dataset = categoricDataFilter.removeSamplesWithMissingData()
        return self

    def encodeCategoricData(self, columnsToTransform):
        categoricDataEncoder = CategoricDataEncoder(self.metadata, self.dataset)
        self.dataset = categoricDataEncoder.encodeCategoricColumns(columnsToTransform)
        return self

    def scaleDataset(self, sklearScaler):
        scaler = Scaler(sklearScaler)
        self.dataset = scaler.scaleDataset(self.dataset)
        return self

    def shiftRight(self, columnToShift):
        shifter = ColumnShifter(self.dataset)

        self.dataset = shifter.shiftRight(columnToShift)

        return self

    def getProcessedDataframe(self):
        return self.dataset
