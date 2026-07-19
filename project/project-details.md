This is one of the strongest portfolio projects you can build if you're targeting companies like Mono, Paystack, Flutterwave, Moniepoint, Kuda, Grey, Nomba, or OnePipe. The goal is not to create a fancy dashboard—it's to replicate how a Product Data Analyst works inside a fintech.

---

# Project Overview

**Title**

Digital Banking Product Analytics

**Role Simulated**

Product Data Analyst at a fintech company

**Business Scenario**

You have joined a digital bank as the Product Data Analyst.

The product team has launched a new version of the mobile banking app. They want to understand:

* Are users successfully completing onboarding?
* Which features are most popular?
* Where are users dropping off?
* Are users returning after signing up?
* Which customers are becoming active users?
* Which features should the team improve?

Your job is to answer these questions using SQL, Python, and Power BI.

---

# Project Goal

Replicate the day-to-day work of a Product Data Analyst by:

* cleaning raw data
* querying a relational database
* calculating product metrics
* analyzing user behavior
* identifying product bottlenecks
* presenting insights through dashboards
* making data-driven recommendations

---

# What Data You Need

Real fintechs don't usually have one CSV called `bank_data.csv`.

Instead, they have many tables.

Your project should mimic that.

## Core Tables

### Users

```text
user_id
signup_date
country
device_type
os
referral_source
```

---

### Accounts

```text
account_id
user_id
account_type
account_created
kyc_level
status
```

---

### Transactions

```text
transaction_id
user_id
date
amount
merchant
type
status
fee
```

Types

* Transfer
* Airtime
* Bill payment
* Card payment
* Savings
* Deposit

---

### Product Events

This is the most important table.

```text
event_id
user_id
timestamp
event_name
```

Examples

```
App Opened

Sign Up Started

Email Verified

BVN Submitted

BVN Verified

KYC Completed

Account Created

Linked Card

Transfer Initiated

Transfer Successful

Transfer Failed

Bill Payment

Savings Created

Loan Viewed

Loan Applied

Card Ordered

Referral Sent
```

This table is what companies like Paystack, Kuda, and Moniepoint analyze every day.

---

### Sessions

```text
session_id
user_id
login_time
logout_time
device
```

---

### Support Tickets

Optional

```text
ticket_id

user_id

category

opened

resolved

rating
```

---

# Where to Get Data

## Option 1 (Recommended): Generate Your Own Synthetic Data

This is the closest to industry practice because it lets you design realistic event logs and relational tables.

Use Python with libraries like:

* Faker
* NumPy
* pandas

Generate datasets such as:

* 50,000 users
* 1 million events
* 300,000 transactions
* 150,000 sessions

Advantages:

* Complete control over the schema.
* No privacy concerns.
* Easy to add realistic edge cases (failed KYC, abandoned onboarding, duplicate logins, etc.).
* Demonstrates data engineering and simulation skills in addition to analysis.

---

## Option 2: Kaggle

Useful datasets include:

* Digital banking transactions
* Mobile banking datasets
* Customer transaction datasets
* Bank marketing datasets

These often need to be reshaped into multiple relational tables to resemble production systems.

---

## Option 3: Public Open Banking Data

Some financial institutions and regulators publish anonymized transaction data. This can provide realistic transaction patterns, though you'll still need to create supporting tables like events and sessions.

---

## Option 4: Build a Hybrid Dataset (Best Portfolio Choice)

This is what I recommend.

Use:

* synthetic Users
* synthetic Events
* synthetic Sessions

combined with

* real transaction data from Kaggle

This gives you realistic financial activity while preserving the flexibility to model product behavior.

---

# Tools

Database

* PostgreSQL

Programming

* Python
* pandas

SQL

* PostgreSQL SQL

Visualization

* Power BI

Version Control

* Git

Documentation

* Markdown

Optional

* dbt
* Docker

---

# Questions the Product Team Wants Answered

## Acquisition

How many users signed up?

Where do users come from?

Which referral source works best?

---

## Activation

How many users completed onboarding?

How many failed KYC?

Average onboarding time?

Biggest drop-off stage?

---

## Engagement

Daily Active Users (DAU)

Weekly Active Users (WAU)

Monthly Active Users (MAU)

Average sessions per user

Most used feature

Least used feature

---

## Transactions

Average transaction amount

Transaction success rate

Failed transfers

Most popular payment type

Revenue from transaction fees

---

## Retention

Day 1 retention

Day 7 retention

Day 30 retention

Repeat users

Dormant users

---

## User Behavior

Average time before first transfer

Average time before first bill payment

Average number of transfers

Average session duration

---

# SQL Skills You'll Demonstrate

* Joins
* CTEs
* Window functions
* CASE WHEN
* Aggregations
* Date functions
* Ranking
* Cohort analysis
* Funnel analysis

---

# Python Skills

* Data cleaning
* Feature engineering
* Exploratory Data Analysis (EDA)
* Statistical summaries
* Time-series analysis
* Outlier detection

---

# Dashboard Deliverables

Your Power BI dashboard could include:

### Executive Overview

* Total users
* Active users
* Total transactions
* Transaction volume
* Revenue
* Growth trends

### Onboarding Funnel

* Sign-up started
* Email verified
* BVN verified
* KYC completed
* Account created
* Funnel conversion rates

### User Engagement

* DAU / WAU / MAU
* Session trends
* Feature usage
* Active user segments

### Transactions

* Transaction types
* Success vs. failed payments
* Transaction volume over time
* Revenue by service

### Retention

* Cohort heatmap
* Returning users
* Churn trends
* User lifetime metrics

### Product Recommendations

A final page summarizing key insights and recommended product improvements.

---

# Deliverables

A recruiter should be able to see a complete analytics workflow, not just a dashboard. Consider including:

1. **Data Generation or Collection**

   * Python scripts (or documentation if using public data)
   * Relational schema
   * Data dictionary

2. **Database**

   * PostgreSQL database with normalized tables
   * SQL schema and import scripts

3. **SQL Analysis**

   * Well-organized SQL queries answering business questions
   * README explaining each analysis

4. **Python Analysis**

   * Jupyter notebook for cleaning, EDA, and additional metrics

5. **Power BI Dashboard**

   * Interactive dashboard with multiple report pages
   * Screenshots and a short demo video or GIF (optional)

6. **Documentation**

   * Clear README covering:

     * Business problem
     * Dataset
     * Tech stack
     * Analysis process
     * Key findings
     * Product recommendations

7. **Repository Structure**

```text
digital-banking-product-analytics/
│
├── data/
├── sql/
├── notebooks/
├── dashboard/
├── docs/
├── images/
├── README.md
└── requirements.txt
```

## What Makes This Stand Out

Many portfolio projects stop at "analyze a CSV and build a dashboard." This project goes much further by simulating an actual fintech analytics environment: multiple normalized tables, event logs, SQL-first analysis, product metrics, and business recommendations. That closely mirrors the workflow of Product Data Analysts at modern digital banking and payments companies.
