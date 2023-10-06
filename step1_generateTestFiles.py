import numpy as np
import pandas as pd
import csv
import copy

TEST_FILE_PATH_PREFIX = "TestData/TestFiles/test"
TEST_FILE_PATH_SUFFIX = ".csv"

EXPECTED_FILE_PATH_PREFIX = "TestData/ExpectedOutput/test"
EXPECTED_FILE_PATH_SUFFIX = ".json"

DATA_TEMPLATE = [
    ["name", "age", "ice_cream_lover"],
    ["Ivy", "22", "true"],
    ["Tanzil", "25", "false"],
    ["Danny", "21", "true"]
]


def getTestFramesDF():
    testFramesPath = "docs/testFrames.csv"
    testFramesDF = pd.read_csv(testFramesPath)
    return testFramesDF


def getTestFilePath(index):
    return TEST_FILE_PATH_PREFIX + str(index) + TEST_FILE_PATH_SUFFIX


def getExpectedFilePath(index):
    return EXPECTED_FILE_PATH_PREFIX + str(index) + EXPECTED_FILE_PATH_SUFFIX


def extractDelimiter(row):
    if row['file_delimiter'] == "comma":
        return ','
    elif row['file_delimiter'] == "semicolon":
        return ';'
    else:
        return '\t'


def generateTest(specs):
    global data
    headerFlag = specs['file_header']
    file_size = specs['file_size']
    file_delimiter = extractDelimiter(specs)
    # ---------------------------------------------
    if specs['value_data_type'] == "string":
        column = 0
    elif specs['value_data_type'] == "number":
        column = 1
    else:
        column = 2
    # ---------------------------------------------
    if specs['file_size'] == 1:
        if headerFlag:
            data = copy.deepcopy([DATA_TEMPLATE[0]])
        else:
            data = copy.deepcopy([DATA_TEMPLATE[1]])
    elif specs['file_size'] == 2:
        if headerFlag:
            data = copy.deepcopy(DATA_TEMPLATE[:])
        else:
            data = copy.deepcopy(DATA_TEMPLATE[1:])
    # -------------------------------------
    if specs['value_empty_string']:
        if specs['file_size'] == 1:
            data[0][column] = '""'
            return data, csv.QUOTE_NONE, file_delimiter
        else:
            data[1][column] = '""'
            return data, csv.QUOTE_NONE, file_delimiter

    if specs['value_null']:
        if specs['file_size'] == 1:
            data[0][column] = 'null'
            return data, csv.QUOTE_MINIMAL, file_delimiter
        else:
            data[1][column] = 'null'
            return data, csv.QUOTE_MINIMAL, file_delimiter
    # ----------------------------------------
    if specs['value_contains_special_character']:
        if file_size == 1:
            data[0][column] = data[0][column] + file_delimiter
        else:
            data[1][column] = data[1][column] + file_delimiter
    # ---------------------------------------
    if specs['value_contains_quotes']:
        if file_size == 1:
            data[0][column] = data[0][column] + " \"inside\" end"
        else:
            data[1][column] = data[1][column] + " \"inside\" end"
    # ---------------------------------------
    if specs['value_leading_whitespace']:
        if file_size == 1:
            data[0][column] = " " + data[0][column]
        else:
            data[1][column] = " " + data[1][column]
    # ---------------------------------------
    if specs['value_trailing_whitespace']:
        if file_size == 1:
            data[0][column] = data[0][column] + " "
        else:
            data[1][column] = data[1][column] + " "

    return data, csv.QUOTE_MINIMAL, file_delimiter


def writeAllTestFiles(testFrames):
    for index, row in testFrames.iterrows():
        testData, quotingOption, delimiterOption = generateTest(row)
        testPath = getTestFilePath(index)

        with open(testPath, mode="w", newline="") as file:
            if quotingOption == csv.QUOTE_MINIMAL:
                csv_writer = csv.writer(file, quoting=quotingOption, delimiter=delimiterOption)
            else:
                csv_writer = csv.writer(file, quoting=quotingOption, quotechar=' ', delimiter=delimiterOption)
            for record in testData:
                csv_writer.writerow(record)


type_dict = {0: np.str_, 1: np.int32, 2: np.bool_}

def writeAllExpectedOutput(testFrames):
    for index, row in testFrames.iterrows():
        delimiter = extractDelimiter(row)
        if not row['file_header']:
            df = pd.read_csv(getTestFilePath(index),
                             sep=delimiter,
                             header=None, names=['field1', 'field2', 'field3'],
                             skipinitialspace=True)
        else:
            df = pd.read_csv(getTestFilePath(index),
                             sep=delimiter,
                             skipinitialspace=True)

        df.to_json(getExpectedFilePath(index), orient='records')

def main():
    testFrames = getTestFramesDF()
    writeAllTestFiles(testFrames)
    writeAllExpectedOutput(testFrames)


if __name__ == "__main__":
    main()
