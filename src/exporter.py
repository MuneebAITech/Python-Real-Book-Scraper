import pandas as pd


def save_to_csv(data):

    df = pd.DataFrame(data)

    df.to_csv(
        "data/books.csv",
        index=False
    )

    print("\nCSV File Saved Successfully!")


def save_to_excel(data):

    df = pd.DataFrame(data)

    df.to_excel(
        "data/books.xlsx",
        index=False
    )

    print("Excel File Saved Successfully!")