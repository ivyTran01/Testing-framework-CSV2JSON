NUMBER_OF_TESTS = 18

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
        lineNumber = 0
        identical = True
        print(f"Performing test {index} ---------------------------")
        with open(expectedPath, 'r') as expected, open(actualPath, 'r') as actual:
            while True:
                expectedResult = expected.readline()
                actualResult = actual.readline()
                lineNumber += 1

                if not expectedResult and not actualResult:
                    if identical:
                        print(f"Test {index}: pass")
                    else:
                        print(f"Test {index}: fail")
                    break

                if not expectedResult or not actualResult:
                    print(f"Line {lineNumber}:")
                    print(f"Expect output: {expectedResult.strip()}")
                    print(f"Actual output: {actualResult.strip()}")
                    print(f"Test {index}: fail\n")
                    break

                if expectedResult != actualResult:
                    identical = False
                    print(f"Line {lineNumber}:")
                    print(f"Expect output: {expectedResult.strip()}")
                    print(f"Actual output: {actualResult.strip()}")



if __name__ == "__main__":
    main()