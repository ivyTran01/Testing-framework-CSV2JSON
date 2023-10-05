import subprocess
import pandas as pd
import copy

TEST_FILE_PATH_PREFIX = "TestData/TestFiles/test"
TEST_FILE_PATH_SUFFIX = ".csv"

OUTPUT_RAW_PATH_PREFIX = "TestData/ActualOutputRaw/test"
OUTPUT_RAW_PATH_SUFFIX = ".json"

OUTPUT_FINAL_PATH_PREFIX = "TestData/ActualOutputFinal/test"
OUTPUT_FINAL_PATH_SUFFIX = ".json"

COMMAND_TEMPLATE = [
    "csvtojson",
    "test_input",
    ">",
    "test_output16",
    "--checkType=true",
    "--delimiter=auto",
    "--nullObject=true"
]


def getTestFramesDF():
    testFramesPath = "docs/testFrames.csv"
    testFramesDF = pd.read_csv(testFramesPath)
    return testFramesDF


def getTestFilePath(index):
    return TEST_FILE_PATH_PREFIX + str(index) + TEST_FILE_PATH_SUFFIX


def getOutputRawPath(index):
    return OUTPUT_RAW_PATH_PREFIX + str(index) + OUTPUT_RAW_PATH_SUFFIX


def getOutputFinalPath(index):
    return OUTPUT_FINAL_PATH_PREFIX + str(index) + OUTPUT_FINAL_PATH_SUFFIX


def generateOutputRaw():
    testFrames = getTestFramesDF()
    for index, row in testFrames.iterrows():
        command = copy.deepcopy(COMMAND_TEMPLATE)
        command[1] = getTestFilePath(index)
        command[3] = getOutputRawPath(index)

        if not row['file_header']:
            command.append("--noheader=true")

        subprocess.run(command, shell=True)


def finalizeOutput():
    testFrames = getTestFramesDF()
    for index, _ in testFrames.iterrows():
        df = pd.read_json(getOutputRawPath(index))
        df.to_json(getOutputFinalPath(index), orient='records')


def main():
    generateOutputRaw()
    finalizeOutput()


if __name__ == "__main__":
    main()
