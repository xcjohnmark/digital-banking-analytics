# Digital Banking Product Analytics Case Study

## 1. Onboarding Funnel Analysis
*   **Business Goal:** Identify drop-off points in the new app version's onboarding flow to improve activation rates.
*   **Raw Funnel Counts:**
    *   App Opened: 5000
    *   Sign Up Started: 5000
    *   Email Verified: 4496
    *   BVN Submitted: 3355
    *   BVN Verified: 3355
    *   KYC Completed: 2675
    *   Account Created: 2558
*   **Calculations (Onboarding Stage Drop-off Rates):**
    *   Email Verification Drop-off Rate: 10.08%
    *   BVN Submission Drop-off Rate: 25.38%
    *   BVN Verification Drop-off Rate: 0.00%
    *   KYC Completion Drop-off Rate: 20.27%
    *   Account Creation Drop-off Rate: 4.37%
*   **My Hypotheses & Insights:**
    *   *BVN Submission Drop-off (25.38%):* Users exhibit high skepticism about sharing sensitive governmental identity numbers (like the BVN) in a new app due to security risks and fear of scam/impersonation.
    *   *KYC Completion Drop-off (20.27%):* High physical and operational friction. Users drop off because they do not have physical ID documents nearby, encounter lighting issues during selfie capture, or face camera/upload failures within the app interface.

## 2. User Engagement Analysis
*   **Business Goal:** Measure how habit-forming our digital banking product is and analyze active user trends.
*   **Metrics Calculated:**
    *   Average Monthly Active Users (MAU): 1023.8
    *   Average Weekly Active Users (WAU): 656.4
    *   Average Daily Active Users (DAU): 128.9
    *   Overall App Stickiness Ratio (DAU / MAU): 12.59%
*   **My Hypotheses & Insights:**
    *   *Stickiness Evaluation (12.59%):* The 12.59% stickiness is below the 20% healthy industry benchmark. A key hypothesis is that users treat our product as a "secondary bank account" rather than their primary bank (where salaries are deposited). They likely find competitor apps more convenient for daily transactions and only use our app occasionally. We should benchmark competitor features (e.g., daily interest, bill payment rewards, automated savings) to build habit-forming features.
    *   *MAU Growth Trend & Stickiness Impact:* Although absolute user numbers are small (395 to 1,494), this represents a **278% growth rate** over 5 months. During rapid user acquisition, stickiness artificially drops. This is because new signups register as Monthly Active Users (inflating the MAU denominator) but have not yet established a daily login habit (keeping the DAU numerator low). As the acquisition rate stabilizes, we must monitor if these cohorts begin logging in more frequently.

## 3. Financial Ledger & Transaction Analysis
*   **Business Goal:** Evaluate transaction metrics, platform reliability, and fee-based revenue generation.
*   **Metrics Calculated:**
    *   *Volume & Size by Type:*
        *   Transfer: 1,173 transactions | Total Vol: 29,447,253.21 | Avg Size: 25,104.22
        *   Deposit: 1,188 transactions | Total Vol: 3,086,245.67 | Avg Size: 2,598.00
        *   Airtime: 1,176 transactions | Total Vol: 3,075,113.52 | Avg Size: 2,614.89
        *   Card payment: 1,163 transactions | Total Vol: 2,932,936.03 | Avg Size: 2,521.87
        *   Bill payment: 1,138 transactions | Total Vol: 2,903,016.75 | Avg Size: 2,550.98
        *   Savings: 1,114 transactions | Total Vol: 2,893,040.40 | Avg Size: 2,596.98
    *   *Success Rates:*
        *   Transfer: 93.69% Success (6.31% Failure)
        *   Card payment: 95.36% Success (4.64% Failure)
        *   Others (Deposit, Airtime, Savings, Bill payment): 100.00% Success
    *   *Fee Revenue:*
        *   Transfer Fees: 441,708.85
        *   Bill Payment Fees: 43,545.41
        *   Others: 0.00
        *   **Grand Total Fee Revenue:** 485,254.26
*   **My Hypotheses & Insights:**
    *   *Transaction Failure Rates (Transfers & Card Payments):* Transfers and card payments exhibit failure rates because they rely heavily on external dependencies (third-party payment switches, card networks like Visa/Mastercard, and destination bank APIs) for verification and approval. Internal transactions like deposits and savings are handled within our own closed-loop ledgers, yielding a 100% success rate. The ~6.31% transfer failure rate is a high trust risk: users whose transfers fail (especially during in-store payments) are highly likely to immediately abandon the app.
    *   *Revenue Model Analysis:* Relying on transfer fees for **91% of our total revenue** is a high-risk strategy. In the competitive digital banking landscape, price-wars can force transaction fees to zero. If competitors offer free transfers, our core revenue stream collapses. To mitigate this risk, the product team should explore diversifying revenue through value-added services (e.g., micro-lending, card maintenance fees, or interest spreads from deposits).

## 4. Cohort Retention Analysis
*   **Business Goal:** Track user retention behavior over time to see if product stickiness is improving with newer signup groups.
*   **Metrics Calculated (Retention Grid):**
    *   *January Cohort (395 users):* Month 0: 100.00% | Month 1: 84.05% | Month 2: 60.00% | Month 3: 49.11% | Month 4: 40.25% | Month 5: 29.62%
    *   *February Cohort (389 users):* Month 0: 100.00% | Month 1: 87.92% | Month 2: 65.04% | Month 3: 55.53% | Month 4: 43.70%
    *   *March Cohort (405 users):* Month 0: 100.00% | Month 1: 81.48% | Month 2: 58.77% | Month 3: 50.62%
    *   *April Cohort (390 users):* Month 0: 100.00% | Month 1: 84.62% | Month 2: 61.03%
    *   *May Cohort (439 users):* Month 0: 100.00% | Month 1: 84.05%
    *   *June Cohort (395 users):* Month 0: 100.00%
*   **My Hypotheses & Insights:**
    *   *Cohort Retention Trends:* Comparing cohorts at identical intervals (Month 1, 2, and 3 active lifespans) reveals that the **February Cohort** performed the best (e.g., 87.92% Month 1 retention vs. January's 84.05%). The **March Cohort** performed the worst (e.g., 81.48% Month 1 retention). 
    *   *Potential Root Causes:* The drop in March retention could correlate with our earlier transaction analysis—if March was a month where transfer or card payment failure rates spiked due to server issues, users joining in March would have had a poor first-week experience, leading to higher churn. Conversely, February may have benefited from a successful marketing campaign attracting highly targeted primary-account users, or a period of high platform stability.

## 5. Outlier & Behavioral Deep Dive
*   **Business Goal:** Flag statistical transactional anomalies and study the relationship between onboarding duration and long-term user value.
*   **Metrics Calculated:**
    *   *Global Outlier Threshold:* 8,785.88 NGN (flagged 983 transactions, or 14.14% of the database, as outliers).
    *   *Segmented Outlier Count:* 0 outliers identified when calculated per transaction type.
    *   *Correlation (Onboarding Duration vs. Transaction Count):* $r = -0.0237$
*   **My Hypotheses & Insights:**
    *   *Outlier Segmentation:* Analytically, the global outliers were a statistical illusion. Because transfers naturally have higher ranges (up to 50k NGN) than airtime/bill payments (up to 5k NGN), analyzing the data globally just flagged standard transfers. Segmenting the data by type reveals that all transactions are uniformly distributed and outlier-free. 
    *   *Onboarding Duration Correlation ($r = -0.0237$):* A correlation coefficient of -0.0237 is mathematically equivalent to **zero correlation**. This means there is no relationship between how long a user takes to complete onboarding and how active they are once activated. 
    *   *Product Action:* While onboarding friction (delays in KYC or BVN) causes severe drop-offs *during* the sign-up funnel, it does not linger to impact the transaction frequency of users who successfully activate. The product team should focus onboarding optimization purely on funnel completion (preventing user churn at sign up), knowing that once a user completes the account setup, their historical signup friction will not affect their transaction habits.