# Power BI & PostgreSQL Connection Troubleshooting Guide

This guide provides step-by-step instructions to resolve the **"Class not registered"** error when attempting to connect Power BI Desktop directly to a PostgreSQL database on Windows.

---

## 🔍 Understanding the Root Cause
Power BI relies on a .NET data provider called **Npgsql** to communicate with PostgreSQL databases. 
The `"Class not registered"` error occurs when:
1. The Npgsql driver is not installed on your system.
2. The Npgsql driver was installed, but it was **not registered in the Windows Global Assembly Cache (GAC)**, preventing Power BI from calling its DLLs.
3. There is a 32-bit vs. 64-bit architecture mismatch.

---

## 🛠️ Step-by-Step Resolution Manual

### Method 1: Installing Npgsql and Registering to the GAC (Recommended)
This is the native way to fix the issue.

1. **Close Power BI Desktop** completely.
2. Go to the official Npgsql GitHub Releases page and download the **MSI Installer** (e.g., `Npgsql.msi` version 4.0.10 is widely compatible with Power BI):
   * [Npgsql Releases on GitHub](https://github.com/npgsql/npgsql/releases)
3. **Run the Installer** on Windows.
4. **CRITICAL STEP:** In the "Custom Setup" window of the installer, you will see a list of features. By default, the installer does **not** register Npgsql to the GAC. 
   * Click on the dropdown next to **"Npgsql GAC Installation"** (Global Assembly Cache).
   * Select **"Will be installed on local hard drive"**.
   * Do the same for **"DbProviderFactories registration"**.
   * Click Next and complete the installation.
5. **Restart your computer** (or restart the Power BI application) to force Windows to reload the GAC registry entries.
6. Open Power BI and attempt to connect to PostgreSQL again.

---

### Method 2: The ODBC Workaround (Bypassing GAC Entirely)
If Method 1 fails due to Windows permission policies or registry corruption, you can bypass the native Npgsql connector entirely using **ODBC**.

1. **Download the PostgreSQL ODBC Driver:**
   * Go to [PostgreSQL ODBC Downloads](https://www.postgresql.org/ftp/odbc/versions/msi/) and download the 64-bit MSI installer (`psqlodbc_x64.msi`).
   * Install it on your Windows machine.
2. **Configure the Data Source (DSN):**
   * Open the Windows Start Menu, search for **ODBC Data Sources (64-bit)**, and run it.
   * Go to the **System DSN** tab and click **Add...**
   * Select **PostgreSQL Unicode(x64)** from the list and click **Finish**.
   * Fill in the DSN configuration:
     * **Data Source:** `postgres_local` (or any name you prefer)
     * **Database:** `digital_banking_analytics`
     * **Server:** `127.0.0.1` (or `localhost`)
     * **Port:** `5432`
     * **User Name:** `postgres`
     * **Password:** `xcj_post57044`
   * Click **Test** to verify. If successful, click **Save**.
3. **Connect Power BI via ODBC:**
   * Open Power BI Desktop.
   * Click **Get Data** $\rightarrow$ **ODBC**.
   * In the dropdown, select the DSN you just created (`postgres_local`).
   * Under Advanced options, you can leave it blank or write your SQL query.
   * When prompted for credentials, select **Windows** or **Database** and click Connect.

---

### Method 3: Advanced .NET Configuration (`machine.config`)
If Npgsql is installed but still throwing the class error, the provider entry might be missing from your system's .NET configuration files.

1. Open the file browser and locate your 64-bit .NET configuration file:
   `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\machine.config`
2. Open this file in a text editor with **Administrator Privileges** (e.g., Notepad run as Admin).
3. Find the `<DbProviderFactories>` XML tag.
4. Check if the following entry is present. If it is missing, paste it inside the `<DbProviderFactories>` block:
   ```xml
   <add name="Npgsql Data Provider" 
        invariant="Npgsql" 
        description=".Net Data Provider for PostgreSQL" 
        type="Npgsql.NpgsqlFactory, Npgsql, Version=4.0.10.0, Culture=neutral, PublicKeyToken=5d8b90d52f46fda7" />
   ```
   *(Note: Ensure the `Version` matches the version of Npgsql you installed in Method 1)*.
5. Save the file and restart Power BI.
