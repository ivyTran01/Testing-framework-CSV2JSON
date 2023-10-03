import pandas

utf16_path = "TestData/ActualOutput_utf16/test.json"
utf8_path = "TestData/ActualOutput_utf8/test.json"
expected_path = "TestData/ExpectedOutput/test.json"

def remove_linebreaks():
    df = pandas.read_json(utf16_path, encoding='utf-16')
    print(df)
    df.to_json(utf8_path, orient='records')


def compareOutput():
    with open(utf8_path, 'r') as file1, open(expected_path, 'r') as file2:
        line_number = 0  # Initialize a line number counter
        while True:
            line1 = file1.readline()
            line2 = file2.readline()
            line_number += 1

            # Check for the end of files
            if not line1 and not line2:
                print("Both files are identical.")
                break

            # Compare lines
            if line1 != line2:
                print(f"Difference at line {line_number}:")
                print(f"File 1: {line1.strip()}")
                print(f"File 2: {line2.strip()}\n")

def main():
    remove_linebreaks()
    compareOutput()



if __name__ == "__main__":
    main()