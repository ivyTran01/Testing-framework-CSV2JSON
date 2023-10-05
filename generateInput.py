import pandas as pd
def main():
    csv_path = "TestData/TestFiles/test0.csv"
    json_path = "TestData/ExpectedOutput/test0.json"

    df = pd.read_csv(csv_path)
    df.to_json(json_path, orient='records')


if __name__ == "__main__":
    main()