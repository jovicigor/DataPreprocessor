# Data Preprocessing Engine

A simple library that wraps common data processing tasks into an easy to use preprocessing engine. 
The library currently supports transformation of csv files loaded into Pandas dataframe. 

## Getting Started

In order to get started simply fetch the package using the following pip command: 
```
pip install git+https://github.com/jovicigor/DataPreprocessor@v0.2
```
### Prerequisites
DataPreprocessor is built on top of existing Python libraries and therefore requires them in order to work properly. 

Here's the list of dependencies: 
- numpy==1.13.3
- pandas==0.20.3
- python-dateutil==2.6.1
- pytz==2017.2
- scikit-learn==0.19.0
- scipy==0.19.1
- six==1.11.0
- sklearn==0.0

### Usage

Here you can find examples of using DataPreprocessor for processing a dummy dataset.  

| Country | Age | Salary | Purchased | 
|---------|-----|--------|-----------| 
| France  | 44  | 72000  | No        | 
| Spain   | 27  | 48000  | Yes       | 
|         | 30  | 54000  | No        | 
| Spain   | 38  | 61000  | No        | 
| Germany | 40  |        | Yes       | 
| France  | 35  | 58000  | Yes       | 
| Spain   |     | 52000  | No        | 
| France  | 48  | 79000  | Yes       | 
| Germany | 50  | 83000  | No        | 
| France  | 37  | 67000  | Yes       | 

First step is defining the metadata for the dataset columns. The metadata for the given dataset would be as following: 
```
[FEATURE_TYPES]
Country = CATEGORIC
Age = NUMERIC
Salary = NUMERIC
Purchased = CATEGORIC
```

#### Handling missing data
One of the most common preprocessing tasks in machine learning is handling the missing data. DataProcessor handles missing **numeric** data by allowing you to exchange missing values with either MEAN or MEDIAN value of numeric columns. 

```
import pandas as pd

from datapreprocessor.engine import PreprocessingEngine
from datapreprocessor.metadata import DatasetMetadataLoader
from datapreprocessor.missingdata import ImputeStrategy

# Load metadata
metadata = DatasetMetadataLoader("metadata.ini")
# Load the dataset
dataset = pd.read_csv('Data.csv')

# Process the dataset 
processedDataframe = PreprocessingEngine(dataset, metadata) \
    .imputeNumericDataUsing(ImputeStrategy.MEAN) \
    .getProcessedDataframe()
```
Executing the above code would result in a new dataframe that has the missing values for age and salary filled with their means as shown on next table. 

| Country | Age               | Salary            | Purchased | 
|---------|-------------------|-------------------|-----------| 
| France  | 44.0              | 72000.0           | No        | 
| Spain   | 27.0              | 48000.0           | Yes       | 
|         | 30.0              | 54000.0           | No        | 
| Spain   | 38.0              | 61000.0           | No        | 
| Germany | 40.0              | 63777.77777777778 | Yes       | 
| France  | 35.0              | 58000.0           | Yes       | 
| Spain   | 38.77777777777778 | 52000.0           | No        | 
| France  | 48.0              | 79000.0           | Yes       | 
| Germany | 50.0              | 83000.0           | No        | 
| France  | 37.0              | 67000.0           | Yes       | 

* Handling missing categoric data such as Country is supported only by eliminating the rows with missing data using method

```
filteredDataframe = PreprocessingEngine(processedDataframe, metadata) \
          .filterMissingCategoricData()
          .getProcessedDataframe()
```

#### Encoding categoric columns

As shown in the following code, setting columnsToTransform to "Country" would eliminate that column and replace it with three columns: Germany, France and Spain. 

```
encodedDataframe = PreprocessingEngine(processedDataframe, metadata) \
            .encodeCategoricData(columnsToTransform="Country") \
            .getProcessedDataframe()
```
The dataframe after encoding looks like shown in the next table.  

| Age               | Salary            | Purchased | France | Germany | Spain | 
|-------------------|-------------------|-----------|--------|---------|-------| 
| 44.0              | 72000.0           | 0         | 1.0    | 0.0     | 0.0   | 
| 27.0              | 48000.0           | 1         | 0.0    | 0.0     | 1.0   | 
| 38.0              | 61000.0           | 0         | 0.0    | 0.0     | 1.0   | 
| 40.0              | 63777.77777777778 | 1         | 0.0    | 1.0     | 0.0   | 
| 35.0              | 58000.0           | 1         | 1.0    | 0.0     | 0.0   | 
| 38.77777777777778 | 52000.0           | 0         | 0.0    | 0.0     | 1.0   | 
| 48.0              | 79000.0           | 1         | 1.0    | 0.0     | 0.0   | 
| 50.0              | 83000.0           | 0         | 0.0    | 1.0     | 0.0   | 
| 37.0              | 67000.0           | 1         | 1.0    | 0.0     | 0.0   | 

#### Scaling the data

Scaling the dataframe can be performed using scaleDataset() method which accepts any sklearn scaler. In the following example, min-max scaling was used as strategy. 

```
from sklearn.preprocessing import MinMaxScaler

 scaledDataframe = PreprocessingEngine(encodedDataframe, metadata) \
            .scaleDataset(MinMaxScaler()) \
            .getProcessedDataframe()
```


| Age                 | Salary              | Purchased | France | Germany | Spain | 
|---------------------|---------------------|-----------|--------|---------|-------| 
| 0.7391304347826089  | 0.6857142857142855  | 0.0       | 1.0    | 0.0     | 0.0   | 
| 0.0                 | 0.0                 | 1.0       | 0.0    | 0.0     | 1.0   | 
| 0.4782608695652175  | 0.37142857142857144 | 0.0       | 0.0    | 0.0     | 1.0   | 
| 0.5652173913043479  | 0.45079365079365075 | 1.0       | 0.0    | 1.0     | 0.0   | 
| 0.34782608695652173 | 0.2857142857142856  | 1.0       | 1.0    | 0.0     | 0.0   | 
| 0.5120772946859904  | 0.11428571428571432 | 0.0       | 0.0    | 0.0     | 1.0   | 
| 0.9130434782608696  | 0.8857142857142857  | 1.0       | 1.0    | 0.0     | 0.0   | 
| 1.0                 | 1.0                 | 0.0       | 0.0    | 1.0     | 0.0   | 
| 0.43478260869565233 | 0.5428571428571427  | 1.0       | 1.0    | 0.0     | 0.0   | 

#### Moving columns

There are times when we want to move some columns to the rightmost column of the dataset. This can be done using shiftRight() method in PreprocessingEngine. 


| Age                 | Salary              | Purchased | France | Germany | Spain | 
|---------------------|---------------------|-----------|--------|---------|-------| 
| 0.7391304347826089  | 0.6857142857142855  | 0.0       | 1.0    | 0.0     | 0.0   | 
| 0.0                 | 0.0                 | 1.0       | 0.0    | 0.0     | 1.0   | 

For example in the dataframe above we could move the Purchased column to right by executing the following code. 

```

shiftedDataframe = PreprocessingEngine(encodedDataframe, metadata) \
            .shiftRight("Purchased") \
            .getProcessedDataframe()
```

The shiftedDataFrame would look like shown in the next table. 


| Age                 | Salary              | France | Germany | Spain | Purchased | 
|---------------------|---------------------|--------|---------|-------|-----------|
| 0.7391304347826089  | 0.6857142857142855  | 1.0    | 0.0     | 0.0   | 0.0       |
| 0.0                 | 0.0                 | 0.0    | 0.0     | 1.0   | 1.0       |

#### Transforming the dataset in one go

The transformation operations can be executed in one go just by calling them one after the other. 

```
processedDataframe = PreprocessingEngine(dataset, metadata) \
            .imputeNumericDataUsing(ImputeStrategy.MEAN) \
            .filterMissingCategoricData() \
            .encodeCategoricData(columnsToTransform="Country") \
            .scaleDataset(MinMaxScaler()) \
            .getProcessedDataframe()
```

## Running the tests

In order to run the tests clone this repository and execute following commands: 
```
pip install -r requirements.txt
cd tests
python RunAllUnitTests.py
```

## Authors

* **Igor Jovic** - [jovicigor](https://github.com/jovicigor)
