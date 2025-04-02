# SQL Query Optimization & ETL Pipeline Design (Hands-On Project)
## Overview
This project demonstrates a robust ETL pipeline designed to process user and financial data, optimize SQL queries, and generate interactive dashboards for automated reporting. It integrates multiple stages—including data extraction, transformation, quality checks, SQL query optimization, dashboarding, and orchestration—using modern data engineering tools.

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
