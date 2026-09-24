import pandas as pd


def pandas_dataframe_tutorial():
    print("=== PANDAS DATAFRAME COMPREHENSIVE TUTORIAL ===\n")

    # ---------------------------------------------------------
    # 1. CREATING A DATAFRAME
    # ---------------------------------------------------------
    # The most common way to build a DataFrame manually is from a Dictionary of Lists.
    # Dictionary keys become column headers; list elements become row values.
    raw_data = {
        "Student": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
        "Course": ["Precalculus", "Sociology", "Precalculus", "Sociology", "Precalculus"],
        "Score": [92, 85, 88, 95, 79],
        "Study_Hours": [6.5, 4.0, 5.5, 8.0, 3.5],
    }

    df = pd.DataFrame(raw_data)
    print("1. Initial DataFrame Created:")
    print(df)
    print("-" * 50)

    # ---------------------------------------------------------
    # 2. INSPECTING DATAFRAME METADATA
    # ---------------------------------------------------------
    print("\n2. Data Structure & Metadata:")
    print(f"Shape (Rows, Columns): {df.shape}")
    print(f"Column Names:          {list(df.columns)}")
    print(f"Data Types:\n{df.dtypes}")
    print("-" * 50)

    # ---------------------------------------------------------
    # 3. SELECTING & FILTERING DATA
    # ---------------------------------------------------------
    print("\n3. Selecting Single Column ('Score'):")
    print(df["Score"])

    print("\n4. Filtering Rows (Students studying > 5 hours):")
    high_study = df[df["Study_Hours"] > 5.0]
    print(high_study)

    print("\n5. Multiple Filters (Sociology students with Score >= 85):")
    soc_high = df[(df["Course"] == "Sociology") & (df["Score"] >= 85)]
    print(soc_high)
    print("-" * 50)

    # ---------------------------------------------------------
    # 4. ADDING & MODIFYING COLUMNS
    # ---------------------------------------------------------
    print("\n6. Adding Calculated Column ('Passed'):")
    df["Passed"] = df["Score"] >= 80

    print("\n7. Adding Column with Mathematical Operations:")
    # Calculate score efficiency: score points earned per study hour
    df["Points_Per_Hour"] = (df["Score"] / df["Study_Hours"]).round(2)
    print(df)
    print("-" * 50)

    # ---------------------------------------------------------
    # 5. AGGREGATION & GROUPING (groupby)
    # ---------------------------------------------------------
    print("\n8. Grouping by 'Course' and Calculating Mean Metrics:")
    grouped_df = df.groupby("Course")[["Score", "Study_Hours"]].mean().round(2)
    print(grouped_df)
    print("-" * 50)


if __name__ == "__main__":
    pandas_dataframe_tutorial()