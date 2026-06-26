import pandas as pd
import numpy as np

class WaterDataPreprocessor:

    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self):

        print("Loading dataset...")

        df = pd.read_csv(self.filepath)

        return df

    def clean_column_names(self, df):

        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        return df

    def remove_duplicates(self, df):

        before = len(df)

        df = df.drop_duplicates()

        after = len(df)

        print(f"Removed {before-after} duplicate rows")

        return df

    def handle_missing_values(self, df):

        numeric_cols = df.select_dtypes(
            include=np.number
        ).columns

        for col in numeric_cols:

            df[col] = df[col].fillna(
                df[col].median()
            )

        categorical_cols = df.select_dtypes(
            exclude=np.number
        ).columns

        for col in categorical_cols:

            df[col] = df[col].fillna(
                "Unknown"
            )

        return df

    def remove_outliers(self, df):

        numeric_cols = [
            "ph",
            "tds",
            "turbidity",
            "do"
        ]

        for col in numeric_cols:

            if col not in df.columns:
                continue

            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)

            iqr = q3 - q1

            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr

            df = df[
                (df[col] >= lower) &
                (df[col] <= upper)
            ]

        return df

    def create_risk_labels(self, df):

        risk = []

        for _, row in df.iterrows():

            tds = row["tds"]
            turbidity = row["turbidity"]
            ph = row["ph"]

            if (
                tds > 700 or
                turbidity > 8 or
                ph < 6 or
                ph > 8.5
            ):

                risk.append("High Risk")

            elif (
                tds > 400 or
                turbidity > 4
            ):

                risk.append("Moderate Risk")

            else:

                risk.append("Safe")

        df["risk"] = risk

        return df

    def feature_engineering(self, df):

        df["water_quality_index"] = (
            (14 - abs(df["ph"] - 7))
            + (1000 - df["tds"]) / 100
            + (10 - df["turbidity"])
        )

        df["tds_category"] = pd.cut(
            df["tds"],
            bins=[0,300,600,1000,5000],
            labels=[
                "Low",
                "Medium",
                "High",
                "Critical"
            ]
        )

        return df

    def preprocess(self):

        df = self.load_data()

        df = self.clean_column_names(df)

        df = self.remove_duplicates(df)

        df = self.handle_missing_values(df)

        df = self.remove_outliers(df)

        df = self.create_risk_labels(df)

        df = self.feature_engineering(df)

        return df


if __name__ == "__main__":

    processor = WaterDataPreprocessor(
        "../data/raw/cpcb_water_quality.csv"
    )

    processed_df = processor.preprocess()

    processed_df.to_csv(
        "../data/processed/cleaned_water_data.csv",
        index=False
    )

    print("Preprocessing Completed")

    print(processed_df.head())
