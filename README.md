# Digital Banking Product Analytics Case Study

### Goal
This project analyzes user behavior on a digital banking application, tracking user activation through the onboarding funnel, user engagement metrics, transaction health, and cohort retention.

### Data Source
*   **users.csv**: Contains user demographic and registration details (`user_id`, `signup_date`, `country`, `device_type`, `os`, `referral_source`).
*   **accounts.csv**: Contains user account profiles (`account_id`, `user_id`, `account_type`, `account_created`, `kyc_level`, `status`).
*   **transactions.csv**: Contains transaction ledger details (`transaction_id`, `user_id`, `date`, `amount`, `merchant`, `type`, `status`, `fee`).
*   **events.csv**: Contains in-app activity and event tracking (`event_id`, `user_id`, `timestamp`, `event_name`).
*   **sessions.csv**: Contains user login and session logs (`session_id`, `user_id`, `login_time`, `logout_time`, `device`).

### Questions to Answer
1. What is the overall conversion rate from App Opened to Account Created?
2. What are the drop-off rates at each stage of the onboarding funnel?
3. What is the DAU, WAU, and MAU of the app?
4. What is the App Stickiness Ratio?
5. What is the average transaction size and transaction volume split by payment type?
6. What is the transaction success rate and the total fee revenue collected by the platform?
7. What is the monthly cohort retention rate?

---

### Solution

#### Question 1 & 2: Funnel & Activation
The overall conversion rate across the 7 onboarding stages is **51.16%** (2,558 out of 5,000 users completed account creation).

**SQL Query (View source in [onboarding_funnel.sql](https://github.com/xcjohnmark/digital-banking-analytics/blob/main/sql/onboarding_funnel.sql#L9-L17)):**
```sql
SELECT
	COUNT(DISTINCT CASE WHEN event_name = 'App Opened' THEN user_id END) AS open_stage,
	COUNT(DISTINCT CASE WHEN event_name = 'Sign Up Started' THEN user_id END) AS signup_stage,
	COUNT(DISTINCT CASE WHEN event_name = 'Email Verified' THEN user_id END) AS email_verified_stage,
	COUNT(DISTINCT CASE WHEN event_name = 'BVN Submitted' THEN user_id END) AS bvn_submitted_stage,
	COUNT(DISTINCT CASE WHEN event_name = 'BVN Verified' THEN user_id END) AS bvn_verified_stage,
	COUNT(DISTINCT CASE WHEN event_name = 'KYC Completed' THEN user_id END) AS kyc_complete_stage,
	COUNT(DISTINCT CASE WHEN event_name = 'Account Created' THEN user_id END) AS account_created_stage
FROM events;
```

**Drop-off Percentages:**
| Stage | Drop-off Rate |
| :--- | :---: |
| Email Verified | 10.08% |
| BVN Submitted | 25.38% |
| KYC Completed | 20.27% |

**Insights:**
We observed significant user drop-off at two critical friction points in the onboarding funnel:
*   **BVN Submission (25.38%):** A quarter of the users who verified their email dropped off at this stage. This suggests high user skepticism and security concerns about sharing sensitive government identification numbers (like the BVN) on a new, untrusted application.
*   **KYC Completion (20.27%):** One in five users dropped off during identity verification. This points to high operational friction—such as document upload failures, camera formatting issues, or poor lighting conditions during selfie capture.

---

#### Question 3 & 4: User Engagement & Stickiness
The app's active user metrics indicate an average of **128.9 Daily Active Users (DAU)**, **656.4 Weekly Active Users (WAU)**, and **1,023.8 Monthly Active Users (MAU)**. The overall **App Stickiness Ratio (DAU / MAU) is 12.59%**.

**SQL Query (View WAU calculation in [user_engagement.sql](https://github.com/xcjohnmark/digital-banking-analytics/blob/main/sql/user_engagement.sql#L11-L20)):**
```sql
WITH weekly_active AS (
	SELECT
		DATE_TRUNC('week', login_time) AS active_week,
		COUNT(DISTINCT user_id) AS weekly_users
	FROM sessions
	GROUP BY active_week
)
SELECT
	ROUND(AVG(weekly_users), 1) AS avg_weekly_users
FROM weekly_active;
```

**SQL Query (View DAU, MAU, and Stickiness calculations in [user_engagement.sql](https://github.com/xcjohnmark/digital-banking-analytics/blob/main/sql/user_engagement.sql#L37-L57)):**
```sql
WITH
    daily_active AS (
        SELECT login_time::DATE as active_day,
            COUNT(DISTINCT user_id) AS daily_users
        FROM sessions
        GROUP BY active_day
    ),
    monthly_active AS (
        SELECT DATE_TRUNC('month', login_time) AS active_month,
            COUNT(DISTINCT user_id) AS monthly_users
        FROM sessions
        GROUP BY active_month
    )
SELECT
    (SELECT ROUND(AVG(daily_users), 1) FROM daily_active) AS avg_dau,   
    (SELECT ROUND(AVG(monthly_users), 1) FROM monthly_active) AS avg_mau,
    ROUND(
        (SELECT AVG(daily_users) FROM daily_active)::NUMERIC /
        (SELECT AVG(monthly_users) FROM monthly_active) * 100, 
        2
    ) AS stickiness_percentage;
```

**Insights:**
*   **App Stickiness Evaluation (12.59%):** Having a stickiness ratio of 12.59% is below the healthy industry standard of 20%+. A primary hypothesis is that users find alternative digital banking apps more convenient for daily transactions and treat our app as a secondary account. To counter this, we should study competitors and introduce habit-forming features (like savings goals or card promotions).
*   **Growth vs. Habit Formation:** While the user base grew from 395 to 1,494 active users (a rapid 278% growth rate over 5 months), this acquisition spikes the monthly user count (MAU) but does not immediately reflect in daily active habits (DAU). This temporarily dilutes the stickiness ratio. We need to monitor how retention matures as onboarding growth stabilizes.

---

#### Question 5 & 6: Transaction Performance & Revenue
Our financial metrics show a total fee revenue of **485,254.26**, with **over 91%** of it coming from transfers. `Transfer` transactions have a significantly higher ticket size (average **25,104.22**) compared to other channels (averaging around **2,500**).

**SQL Query (View volume & average size in [transactions_analysis.sql](https://github.com/xcjohnmark/digital-banking-analytics/blob/main/sql/transactions_analysis.sql#L1-L8)):**
```sql
SELECT
	type,
	COUNT(*) AS total_transaction,
	SUM(amount) AS total_volume,
	ROUND(AVG(amount), 2) AS avg_transaction_amount
FROM transactions
GROUP BY type
ORDER BY total_volume DESC;
```

**SQL Query (View success rates in [transactions_analysis.sql](https://github.com/xcjohnmark/digital-banking-analytics/blob/main/sql/transactions_analysis.sql#L11-L17)):**
```sql
SELECT 
	type, COUNT(*) AS total_transactions,
	ROUND(SUM(CASE WHEN status = 'Successful' THEN 1 ELSE 0 END)::NUMERIC /
	COUNT(*) * 100, 2) AS success_rate
FROM transactions
GROUP BY type
ORDER BY success_rate ASC;
```

**SQL Query (View fee & grand total calculations in [transactions_analysis.sql](https://github.com/xcjohnmark/digital-banking-analytics/blob/main/sql/transactions_analysis.sql#L20-L27)):**
```sql
-- Fee revenue by category
SELECT type, SUM(fee) AS total_revenue
FROM transactions
GROUP BY type
ORDER BY total_revenue DESC;

-- Grand total fee revenue
SELECT SUM(fee) AS total_revenue
FROM transactions;
```

**Insights:**
*   **The Cost of Transaction Failures:** Deposits, Airtime, Savings, and Bill payments have a perfect 100% success rate because they are handled within our internal ledgers. However, `Transfer` (93.69% success) and `Card payment` (95.36% success) have noticeable failure rates. Because these rely on external banking switches and APIs, they fail when external systems time out. A ~6% transfer failure rate is highly problematic—users who experience failed transfers, especially in public/merchant settings, quickly lose trust and churn.
*   **Revenue Model Risk:** Transfers account for **441,708.85** (91%) of our total fee revenue, while card payments, deposits, airtime, and savings generate **0.00** in fees. This makes our business model highly vulnerable. If a competitor introduces free transfers, our primary revenue engine collapses. We must diversify our streams by looking at value-added options, like card maintenance charges, merchant APIs, or lending options.

---

#### Question 7: Cohort Retention Analysis
We tracked returning active users over a 6-month period to analyze user retention decay.

**SQL Query (View source in [cohort_retention.sql](https://github.com/xcjohnmark/digital-banking-analytics/blob/main/sql/cohort_retention.sql#L1-L39)):**
```sql
WITH user_activity AS (
	SELECT
		users.user_id,
		DATE_TRUNC('month', users.signup_date) AS cohort_month,
		DATE_TRUNC('month', sessions.login_time) AS active_month,
		(EXTRACT(YEAR FROM sessions.login_time) - EXTRACT(YEAR FROM users.signup_date))
		* 12 + 
		(EXTRACT(MONTH FROM sessions.login_time) - EXTRACT(MONTH FROM users.signup_date)) AS month_number
	FROM users
	JOIN sessions
	ON users.user_id = sessions.user_id
),
cohort_sizes AS (
	SELECT
		cohort_month,
		COUNT(DISTINCT user_id) AS total_cohort_size
	FROM user_activity
	WHERE month_number = 0
	GROUP BY cohort_month
),
active_users_by_period AS (
	SELECT
		cohort_month,
		month_number,
		COUNT(DISTINCT user_id) AS active_users
	FROM user_activity
	GROUP BY cohort_month, month_number
)

SELECT
	a.cohort_month,
	c.total_cohort_size,
	a.month_number,
	active_users,
	ROUND(a.active_users::NUMERIC / c.total_cohort_size * 100, 2) AS retention_rate
FROM active_users_by_period AS a
JOIN cohort_sizes AS c
ON a.cohort_month = c.cohort_month
ORDER BY a.cohort_month, a.month_number;
```

**Retention Rates by Cohort:**
*   **January Cohort (395 users):** Month 0: 100.0% | Month 1: 84.05% | Month 2: 60.00% | Month 3: 49.11% | Month 4: 40.25% | Month 5: 29.62%
*   **February Cohort (389 users):** Month 0: 100.0% | Month 1: 87.92% | Month 2: 65.04% | Month 3: 55.53% | Month 4: 43.70%
*   **March Cohort (405 users):** Month 0: 100.0% | Month 1: 81.48% | Month 2: 58.77% | Month 3: 50.62%

**Insights:**
*   **Cohort Comparison:** Comparing cohorts at the same lifespan stages (Month 1, Month 2, and Month 3) shows that the **February Cohort** had the highest user retention (e.g. 87.92% in Month 1 vs January's 84.05%). The **March Cohort** was the worst-performing cohort (retaining only 81.48% in Month 1).
*   **Connecting Failures to Retention:** The steep drop in March retention suggests a systemic issue during that month. Since we found that transfers fail at a high rate (6.31%), a server or gateway issue in March likely led to failed transactions for new signups. Users who experience transaction failures during their first week have a poor user experience, leading to immediate churn.

---

### Outlier & Behavioral Deep Dive (Python Jupyter Notebook)

We used Python (Pandas) inside our [Jupyter Notebook](https://github.com/xcjohnmark/digital-banking-analytics/blob/main/notebooks/product_analytics.ipynb) to run advanced statistical reviews on transaction amounts and calculate behavioral correlations.

#### 1. Transaction Outliers (IQR Method)
Using the Interquartile Range (IQR) method on the global dataset, any transaction above **8,785.88** was flagged as an outlier, resulting in **14.14%** of the database being labeled as "anomalies." 

However, segmenting the analysis by transaction type revealed **zero outliers** in each group:
*   **The Finding:** The global outliers were a statistical illusion. Because transfers naturally have much higher ticket sizes (up to 50k NGN) than daily utility payments (up to 5k NGN), analyzing them together globally just flagged standard transfers. Segmented analysis proved that each transaction type follows a clean, uniform distribution.

#### 2. Onboarding Friction vs. Usage Correlation
We calculated the Pearson correlation coefficient ($r$) between the time it took a user to complete onboarding (onboarding duration) and their subsequent transaction count:
*   **Result:** $r = -0.0237$
*   **The Finding:** A correlation coefficient of -0.0237 represents **zero correlation**. While onboarding friction (BVN/KYC delays) causes users to drop off *during* setup, it has no impact on their transaction habits *once they successfully activate*. Product managers should focus onboarding optimization purely on funnel completion (getting users set up), knowing that historical signup delays will not suppress active transaction habits.
