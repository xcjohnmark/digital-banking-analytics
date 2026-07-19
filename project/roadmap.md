# Product Data Analyst: Digital Banking Project Roadmap

This roadmap outlines the end-to-end development of the **Digital Banking Product Analytics** portfolio project. It serves as your guide to transforming raw generated data into a corporate-ready analytics showcase.

---

## 🗺️ Phase 1: Environment & Data Preparation (Completed)

Focus on setting up the workspace, virtual environments, and generating the core datasets.

*   ### Task 1.1: Project Directory & Environment Setup ✅
    *   [x] **Todo 1**: Create project folder structure (`data/`, `sql/`, `notebooks/`, `dashboards/`, `docs/`, `images/`).
    *   [x] **Todo 2**: Define libraries in [requirements.txt](file:///C:/Users/ADMIN/Documents/portfolio/product-data-analyst/digital-banking/requirements.txt).
    *   [x] **Todo 3**: Initialize the virtual environment (`venv`) and install dependencies using a PyPI mirror.
*   ### Task 1.2: Synthetic Data Generation ✅
    *   [x] **Todo 1**: Design and write the script logic to simulate user behaviors and onboarding funnels.
    *   [x] **Todo 2**: Run [generate_data.py](file:///C:/Users/ADMIN/Documents/portfolio/product-data-analyst/digital-banking/data/generate_data.py) and output 5 CSV datasets (`users.csv`, `accounts.csv`, `transactions.csv`, `events.csv`, `sessions.csv`).
*   ### Task 1.3: Git & GitHub Version Control Setup
    *   [ ] **Todo 1**: Initialize a Git repository in the project folder (`git init`).
    *   [ ] **Todo 2**: Create a `.gitignore` file to ignore the `venv/` folder and database credentials.
    *   [ ] **Todo 3**: Create a blank repository on GitHub and link it to this local folder.

---

## 🗄️ Phase 2: Database Setup & Data Loading (Next Step)

Set up a local PostgreSQL database, model the relational schema, and import the generated CSVs.

*   ### Task 2.1: PostgreSQL Installation & Database Creation ✅
    *   [x] **Todo 1**: Install PostgreSQL (if not already installed) and open pgAdmin or connection client.
    *   [x] **Todo 2**: Create a new database named `digital_banking_analytics`.
*   ### Task 2.2: Define Relational Schema (DDL) ✅
    *   [x] **Todo 1**: Design table schemas enforcing primary and foreign key constraints to model relational integrity.
    *   [x] **Todo 2**: Create an SQL script `sql/create_tables.sql` containing `CREATE TABLE` scripts for the 5 entities.
*   ### Task 2.3: Data Import (DML) ✅
    *   [x] **Todo 1**: Write a Python automation script `data/db_setup.py` to handle database connections and load CSV files.
    *   [x] **Todo 2**: Run imports, verify successful table row creation, and close database connections cleanly.

---

## 📊 Phase 3: SQL Exploratory Data Analysis & Product Metrics (Next Step)

Write clean, structured SQL queries (using CTEs, joins, and window functions) to answer product questions.

*   ### Task 3.1: Funnel & Activation Analysis ✅
    *   [x] **Todo 1**: Write an SQL query to calculate overall conversion rates from `App Opened` to `Account Created`.
    *   [x] **Todo 2**: Calculate drop-off rates at each stage: `Sign Up Started` $\rightarrow$ `Email Verified` $\rightarrow$ `BVN Verified` $\rightarrow$ `KYC Completed` $\rightarrow$ `Account Created` to pinpoint onboarding friction.
*   ### Task 3.2: User Engagement Metrics ✅
    *   [x] **Todo 1**: Write queries to calculate Daily Active Users (DAU), Weekly Active Users (WAU), and Monthly Active Users (MAU).
    *   [x] **Todo 2**: Calculate the **App Stickiness Ratio** ($DAU / MAU$) to evaluate user habit-formation.
*   ### Task 3.3: Transaction Performance & Financial Health ✅
    *   [x] **Todo 1**: Calculate average transaction size and transaction volume split by payment type (Transfer, Card, Airtime, etc.).
    *   [x] **Todo 2**: Identify transaction success rates and calculate the total fee revenue collected by the platform.
*   ### Task 3.4: Cohort Retention Analysis ✅
    *   [x] **Todo 1**: Write a query to perform monthly cohort analysis (grouping users by signup month and checking how many return to log in or transact in Month 1, Month 2, Month 3).

---

## 🐍 Phase 4: Python Analytics & Visual Cohorts (Next Step)

Dive deeper using Python/Jupyter Notebooks to run statistics, identify outliers, and plot retention heatmaps.

*   ### Task 4.1: Jupyter Notebook Connection ✅
    *   [x] **Todo 1**: Create a notebook `notebooks/product_analytics.ipynb`.
    *   [x] **Todo 2**: Connect to PostgreSQL using `psycopg2` or `sqlalchemy` and fetch query results into pandas DataFrames.
*   ### Task 4.2: Cohort Heatmap Visualization ✅
    *   [x] **Todo 1**: Use Pandas to format your cohort query results into a retention matrix.
    *   [x] **Todo 2**: Generate a professional, styled cohort retention heatmap using `seaborn` and `matplotlib`.
*   ### Task 4.3: Outlier & Behavioral Deep Dive ✅
    *   [x] **Todo 1**: Analyze distributions of transaction amounts to flag outliers (e.g. potential fraud or high-value power users).
    *   [x] **Todo 2**: Calculate correlation between onboarding time (time elapsed between `Sign Up Started` and `Account Created`) and subsequent transaction activity.

---

## 📊 Phase 5: Power BI Interactive Dashboard (Next Phase)

Connect Power BI to your Postgres database and build a dynamic dashboard explaining product performance.

*   ### Task 5.1: Data Modeling in Power BI ✅
    *   [x] **Todo 1**: Import tables into Power BI Desktop, define relationships (1-to-many from Users to Transactions, Events, etc.).
    *   [ ] **Todo 2**: Create a Date Dimension table and write DAX measures for key metrics (DAU, MAU, Total Fees, Conversion Rates).
*   ### Task 5.2: Creating Report Pages
    *   [ ] **Todo 1**: Build the **Executive Overview** showing high-level KPIs, growth trends, and revenue.
    *   [ ] **Todo 2**: Build the **Onboarding Funnel** visual showing drop-offs, average activation time, and friction stages.
    *   [ ] **Todo 3**: Build the **User Engagement & Transactions** page showcasing WAU/MAU trends and payment success rates.
*   ### Task 5.3: Formatting & UI Polish
    *   [ ] **Todo 1**: Apply a cohesive, modern visual theme (dark mode or sleek corporate branding) with clear headings, typography, and tooltips.

---

## 📝 Phase 6: Documentation & Portfolio Presentation

Package your code, database scripts, and findings into a stellar, employer-ready GitHub repository.

*   ### Task 6.1: Writing the Project README
    *   [ ] **Todo 1**: Explain the business problem, your role, and the tech stack.
    *   [ ] **Todo 2**: Detail your findings (e.g., *"We found a 25% drop-off at the BVN verification stage due to..."*).
    *   [ ] **Todo 3**: Present clear product recommendations based on data (e.g., *"Improve error handling on BVN verification; introduce SMS fallbacks"*).
    *   [ ] **Todo 4**: Add screenshots of your Power BI dashboard pages.
*   ### Task 6.2: Push to GitHub & Present
    *   [ ] **Todo 1**: Create a `.gitignore` file to exclude your `venv/` folder from git.
    *   [ ] **Todo 2**: Commit all code, SQL scripts, notebooks, and push to GitHub.
