import pandas as pd
import csv

TEST_FILE_PATH_PREFIX = "TestData/TestFiles/test"
TEST_FILE_PATH_SUFFIX = ".csv"
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


def generateTest(specs):
    # file size
    # file header
    #
    # value_empty_string
    # value_null
    #
    # value_contains_special_character
    # value_contains_quotes
    #
    # value_leading_whitespace
    # value_trailing_whitespace
    #
    # value_quoted (should be handled auto when "value contains special char")
    # value_contains_escape_double_quotes (should be handled auto when "value contains quotes")
    #
    #
    # file delimiter //set with csv writer
    # file_space_after_delimiter //set with csv writer

    global data
    if specs['file_size'] == 1:
        if specs['file_header']:
            data = [DATA_TEMPLATE[0]]
        else:
            data = [DATA_TEMPLATE[1]]
    elif specs['file_size'] == 2:
        if specs['file_header']:
            data = DATA_TEMPLATE[:]
        else:
            data = DATA_TEMPLATE[1:]

    print(data)
    return data


def main():
    testFrames = getTestFramesDF()

    for index, row in testFrames.iterrows():
        testData = generateTest(row)
        testPath = getTestFilePath(index)
        with open(testPath, mode="w", newline="") as file:
            csv_writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
            for record in testData:
                csv_writer.writerow(record)


if __name__ == "__main__":
    main()
