class ColumnShifter:

    def __init__(self, dataframe):
        self.dataset = dataframe.copy()

    def shiftRight(self, column_to_shift):
        dataset_columns = list(self.dataset.columns.values)

        dataset_columns.pop(dataset_columns.index(column_to_shift))

        return self.dataset[dataset_columns + [column_to_shift]]
