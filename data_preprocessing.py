import pandas as pd
from sqlalchemy import create_engine

def preprocess_marketing(marketing_csv):
    df_marketing = pd.read_csv(marketing_csv, sep="\t")
    df_marketing.columns = df_marketing.columns.str.strip()
    print("Marketing dataset columns:", df_marketing.columns.tolist())
    
    df_marketing['Dt_Customer'] = pd.to_datetime(df_marketing['Dt_Customer'], format='%d-%m-%Y', errors='coerce')
    
    if 'ID' in df_marketing.columns:
        df_marketing.drop(columns=['ID'], inplace=True)
    
    df_marketing.reset_index(drop=True, inplace=True)
    df_marketing['CustomerID'] = df_marketing.index + 1
    
    return df_marketing

def preprocess_creditcard(credit_csv):
    df_credit = pd.read_csv(credit_csv)
    df_credit['Amount'] = df_credit['Amount'].astype(float)
    df_credit.reset_index(drop=True, inplace=True)
    df_credit['CustomerID'] = df_credit.index + 1
    
    return df_credit

def combine_datasets(df_marketing, df_credit, join_key='CustomerID'):
    print("Combining datasets on key:", join_key)
    df_combined = pd.merge(df_marketing, df_credit, on=join_key, how='inner', suffixes=('_marketing', '_credit'))
    return df_combined

def load_to_sqlite(df, db_url, table_name='stg_users'):
    engine = create_engine(db_url)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Data successfully loaded into SQLite table '{table_name}'.")

if __name__ == '__main__':
    marketing_csv = 'marketing_campaign.csv'
    credit_csv = 'creditcard.csv'
    
    db_url = 'sqlite:///etl_pipeline.db'
    
    print("Preprocessing marketing campaign data...")
    df_marketing = preprocess_marketing(marketing_csv)
    
    print("\nPreprocessing credit card data...")
    df_credit = preprocess_creditcard(credit_csv)
    
    df_combined = combine_datasets(df_marketing, df_credit, join_key='CustomerID')
    print("\nCombined dataset preview:")
    print(df_combined.head())
    
    load_to_sqlite(df_combined, db_url, table_name='stg_users')