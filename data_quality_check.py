import pandas as pd
from sqlalchemy import create_engine

def check_data_quality(db_url):
    engine = create_engine(db_url)
    df = pd.read_sql("SELECT * FROM users_transformed", engine)
    
    print("Data Quality Report\n")
    missing_values = df.isnull().sum()
    print("Missing Values in Each Column:")
    print(missing_values, "\n")
    
    if 'Age' in df.columns:
        age_min = df['Age'].min()
        age_max = df['Age'].max()
        age_mean = df['Age'].mean()
        print(f"Age: min={age_min}, max={age_max}, average={age_mean:.2f}")
    else:
        print("Column 'Age' not found in the data.")
    
    duplicate_count = df.duplicated().sum()
    print(f"\nNumber of duplicate rows: {duplicate_count}")
    
    if 'Customer_Tenure' in df.columns:
        negative_tenure = (df['Customer_Tenure'] < 0).sum()
        print(f"Number of records with negative Customer_Tenure: {negative_tenure}")
    else:
        print("Column 'Customer_Tenure' not found in the data.")
    
    print("\nSummary Statistics:")
    print(df.describe())

if __name__ == '__main__':
    db_url = 'sqlite:///etl_pipeline.db'
    check_data_quality(db_url)