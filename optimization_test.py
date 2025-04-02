import pandas as pd
from sqlalchemy import create_engine, text

def create_indexes(db_url):
    engine = create_engine(db_url)
    with engine.connect() as conn:
        conn.execute(text("CREATE INDEX IF NOT EXISTS idx_age ON users_transformed(Age);"))
        conn.execute(text("CREATE INDEX IF NOT EXISTS idx_income ON users_transformed(Income);"))
        conn.execute(text("CREATE INDEX IF NOT EXISTS idx_education ON users_transformed(Education);"))
        print("Indexes created on Age, Income, and Education.")

def run_optimized_query(db_url):
    engine = create_engine(db_url)
    
    sample_query = """
    SELECT Education, AVG(Income) AS Avg_Income, COUNT(*) AS Num_Customers
    FROM users_transformed
    GROUP BY Education;
    """
    
    explain_query = f"EXPLAIN QUERY PLAN {sample_query}"
    
    with engine.connect() as conn:
        print("=== Query Plan ===")
        result = conn.execute(text(explain_query))
        for row in result:
            print(row)
        
        df_results = pd.read_sql(sample_query, engine)
        print("\n=== Query Results ===")
        print(df_results)

if __name__ == '__main__':
    db_url = 'sqlite:///etl_pipeline.db'
    create_indexes(db_url)
    run_optimized_query(db_url)