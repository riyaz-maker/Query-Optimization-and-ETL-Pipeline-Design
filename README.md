# SQL Query Optimization & ETL Pipeline Design
## Overview
This project demonstrates a robust ETL pipeline designed to process user and financial data, optimize SQL queries, and generate interactive dashboards for automated reporting. It integrates multiple stages—including data extraction, transformation, quality checks, SQL query optimization, dashboarding, and orchestration—using data engineering tools.

# Features
## Data Extraction & Loading:
Load raw data from CSV files into a SQLite database staging table.

## Data Transformation:
Cleanse and enrich the data by computing additional fields (e.g., Age, Customer Tenure) and creating a transformed table.

## Data Quality Checks:
Automatically verify data integrity by checking for missing values, duplicates, and range validations.

## SQL Query Optimization:
Optimize SQL queries using indexing and query profiling for improved performance.

## Interactive Dashboard:
Build an interactive dashboard using Dash and Plotly for data visualization and automated reporting.

## Pipeline Orchestration:
Automate and schedule the entire ETL process using Apache Airflow.

# Technologies Used
Python 3.7+

Pandas for data manipulation

SQLAlchemy for database connectivity

SQLite for data storage (demo purposes)

Plotly & Dash for interactive dashboards

Apache Airflow for ETL pipeline orchestration

# Usage Instructions
Data Extraction & Loading:
Execute data_preprocessing.py to load raw CSV data into the SQLite staging table.

Data Transformation:
Execute data_transformation.py to clean and enrich the data.

Data Quality Checks:
Execute data_quality_check.py to perform automated quality validations.

Dashboard:
Run dashboard.py to launch the interactive dashboard for visualization.

# Future Enhancements
Data Integration:
Integrate additional data sources and transition from SQLite to a production-grade database (e.g., PostgreSQL).

Advanced Quality Checks:
Expand the data quality checks with more robust validations and error handling.

Scalability:
Enhance the pipeline to support incremental loads and optimize resource usage.

Enhanced Dashboard:
Add more interactive features, filters, and visualizations to the dashboard.

CI/CD Integration:
Implement CI/CD pipelines for continuous integration and deployment of the ETL process.

# Screenshots of Dashboard
<img width="1440" alt="Screenshot 2025-04-02 at 17 52 50" src="https://github.com/user-attachments/assets/070ddc75-5f9d-4067-a387-be261b0a063b" />
<img width="1440" alt="Screenshot 2025-04-02 at 17 53 00" src="https://github.com/user-attachments/assets/4f9417f2-fed5-43fb-9faf-c60b6164308c" />
<img width="1228" alt="Screenshot 2025-04-02 at 17 53 21" src="https://github.com/user-attachments/assets/b5b8d8a1-e6e7-4aba-91ff-db83c0b983a8" />


