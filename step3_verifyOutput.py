NUMBER_OF_TESTS = 17

EXPECTED_FILE_PATH_PREFIX = "TestData/ExpectedOutput/test"
EXPECTED_FILE_PATH_SUFFIX = ".json"

OUTPUT_FINAL_PATH_PREFIX = "TestData/ActualOutputFinal/test"
OUTPUT_FINAL_PATH_SUFFIX = ".json"

def getExpectedFilePath(index):
    return EXPECTED_FILE_PATH_PREFIX + str(index) + EXPECTED_FILE_PATH_SUFFIX
def getOutputFinalPath(index):
    return OUTPUT_FINAL_PATH_PREFIX + str(index) + OUTPUT_FINAL_PATH_SUFFIX

def main():
    for index in range(NUMBER_OF_TESTS):
        expectedPath = getExpectedFilePath(index)
        actualPath = getOutputFinalPath(index)
        with open(expectedPath, 'r') as expected, open(actualPath, 'r') as actual:
            expectedResult = expected.readline()
            actualResult = actual.readline()

            if expectedResult != actualResult:
                print(f"Test {index}: fail")
                print(f"Expect output: {expectedResult}")
                print(f"Actual output: {actualResult}\n")
            else:
                print(f"Test {index}: pass\n")



if __name__ == "__main__":
    main()