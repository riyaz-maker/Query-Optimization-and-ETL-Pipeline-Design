import sqlalchemy
from sqlalchemy import create_engine, text

def transform_data(db_url):
    engine = create_engine(db_url)
    transformation_query = """
    CREATE TABLE IF NOT EXISTS users_transformed AS
    SELECT 
        CustomerID,
        Year_Birth,
        (strftime('%Y', 'now') - Year_Birth) AS Age,
        Education,
        Marital_Status,
        Income,
        Dt_Customer,
        (julianday('now') - julianday(Dt_Customer)) AS Customer_Tenure,
        Recency,
        MntWines,
        MntFruits,
        MntMeatProducts,
        MntFishProducts,
        MntSweetProducts,
        MntGoldProds,
        NumDealsPurchases,
        NumWebPurchases,
        NumCatalogPurchases,
        NumStorePurchases,
        NumWebVisitsMonth,
        AcceptedCmp3,
        AcceptedCmp4,
        AcceptedCmp5,
        AcceptedCmp1,
        AcceptedCmp2,
        Complain,
        Z_CostContact,
        Z_Revenue,
        Response,
        Amount,
        Time,
        V1, V2, V3, V4, V5, V6, V7, V8, V9, V10,
        V11, V12, V13, V14, V15, V16, V17, V18, V19, V20,
        V21, V22, V23, V24, V25, V26, V27, V28,
        Class
    FROM stg_users;
    """
    
    with engine.connect() as conn:
        conn.execute(text(transformation_query))
        print("Data transformation complete. Table 'users_transformed' created.")

if __name__ == '__main__':
    db_url = 'sqlite:///etl_pipeline.db'
    transform_data(db_url)