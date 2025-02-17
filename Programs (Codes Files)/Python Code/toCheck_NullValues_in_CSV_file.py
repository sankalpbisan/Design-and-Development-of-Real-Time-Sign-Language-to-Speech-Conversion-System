import pandas as pd
import os

def check_null_values_in_csvs(directory):
    """Checks for null values in all CSV files within a directory and prints detailed results."""

    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            filepath = os.path.join(directory, filename)

            try:
                df = pd.read_csv(filepath)
            except pd.errors.ParserError as e:
                print(f"Error parsing {filename}: {e}")
                continue

            null_counts = df.isnull().sum()  # Count null values in each column
            total_nulls = null_counts.sum()  # Calculate total nulls in the DataFrame

            if total_nulls > 0:
                print(f"{filename} has {total_nulls} null values:")
                print(null_counts)  # Print detailed null counts for each column
            else:
                print(f"{filename} has no null values.")

# Example usage:
directory = "C:\\Users\Com-6\\AppData\\Local\\Programs\\Python\\Python311\\Training_Dataset"  # Replace with the actual directory path
check_null_values_in_csvs(directory)
