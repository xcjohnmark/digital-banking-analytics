# Project Security Audit & Code Quality Review

This document contains the findings of a security scan performed on the codebase. It details hardcoded credentials, code bugs related to environment variables, and recommendations for industry-standard security.

---

## 🚨 Critical Findings

### 1. Hardcoded Plaintext Password in Jupyter Notebook
*   **File:** [`notebooks/product_analytics.ipynb`](file:///C:/Users/ADMIN/Documents/portfolio/product-data-analyst/digital-banking/notebooks/product_analytics.ipynb)
*   **Severity:** **High**
*   **Description:** The database password `xcj_post57044` is written in plaintext inside the connection cells:
    *   **Cell 2 (Connection):** `password = 'xcj_post57044'`
    *   **Cell 5 (Outlier Connection):** `password = 'xcj_post57044'`
    *   **Cell 7 (Behavior Connection):** `password = 'xcj_post57044'`
*   **Risk:** If this file is committed and pushed to GitHub, the database password will be leaked publicly.
*   **Fix:** Replace the plaintext password with an environment variable lookup or a prompt.

---

### 2. Literal String Bug in Environment Variable Lookup
*   **File:** [`scripts/db_setup.py`](file:///C:/Users/ADMIN/Documents/portfolio/product-data-analyst/digital-banking/scripts/db_setup.py)
*   **Severity:** **Medium (Logic Error)**
*   **Description:** On **Line 5**, the password is set as:
    ```python
    PASSWORD = "os.getenv('DB_PASSWORD')"
    ```
    Because this is wrapped in double quotes, Python treats it as a **literal text string** rather than running the `os.getenv()` function. Additionally, `import os` is missing at the top of the file.
*   **Risk:** The database connection will fail when run because it tries to send the raw text `"os.getenv('DB_PASSWORD')"` as the password to PostgreSQL.
*   **Fix:** Import the `os` library and remove the double quotes so Python executes the function:
    ```python
    import os
    # ...
    PASSWORD = os.getenv('DB_PASSWORD', 'default_password')
    ```

---

## 🔒 Security Best Practices for Data Projects

To make this project production-ready and secure, implement these two changes:

### Recommendation A: Use `.env` and `python-dotenv`
Instead of hardcoding database credentials or running environment exports manually in the shell, use a `.env` file (which is already ignored by your `.gitignore`!).

1.  Install `python-dotenv` in your virtual environment:
    ```bash
    pip install python-dotenv
    ```
2.  Create a file named **`.env`** in your root directory:
    ```env
    DB_NAME=digital_banking_analytics
    DB_USER=postgres
    DB_PASSWORD=xcj_post57044
    DB_HOST=127.0.0.1
    DB_PORT=5432
    ```
3.  Load the credentials securely in Python:
    ```python
    import os
    from dotenv import load_dotenv

    load_dotenv()  # Load variables from .env file

    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    ```

### Recommendation B: Check Staged Files Before Committing
Always run `git diff --cached` before committing your changes. This lets you review the exact lines of code you are about to upload to GitHub, ensuring no temporary passwords or secrets slip through.
