import os
import random
import uuid
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
from faker import Faker

# 1. Initialize Faker and set seeds for reproducibility
fake = Faker()
Faker.seed(42)
random.seed(42)
np.random.seed(42)

# Configuration settings
NUM_USERS = 5000  # Number of users to simulate
START_DATE = datetime(2026, 1, 1)
END_DATE = datetime(2026, 6, 30)

print(f"Generating synthetic digital banking data for {NUM_USERS} users...")

# Lists to store our final records
users_list = []
accounts_list = []
transactions_list = []
events_list = []
sessions_list = []

# Support lists for generating realistic data
countries = ["Nigeria", "Ghana", "Kenya"]
referrals = ["Google Ads", "Facebook Ads", "Instagram", "Friend Referral", "Organic", "Influencer"]
devices = [
    ("iOS", "iPhone 13"), ("iOS", "iPhone 14"), ("iOS", "iPhone 15"),
    ("Android", "Samsung Galaxy S22"), ("Android", "Samsung Galaxy A54"),
    ("Android", "Redmi Note 12"), ("Android", "Tecno Camon 20"), ("Android", "Infinix Hot 30")
]
merchants = ["Netflix", "Spotify", "Uber", "Jumia", "Bolt", "DSTV", "MTN", "Airtel", "Starlink", "Shoprite"]
transaction_types = ["Transfer", "Airtime", "Bill payment", "Card payment", "Savings", "Deposit"]

# 2. Loop to simulate each user
for i in range(NUM_USERS):
    user_id = str(uuid.uuid4())
    
    # Simulate signup date (randomly distributed between START_DATE and END_DATE)
    days_range = (END_DATE - START_DATE).days
    signup_date = START_DATE + timedelta(days=random.randint(0, days_range), 
                                         hours=random.randint(0, 23), 
                                         minutes=random.randint(0, 59))
    
    country = random.choice(countries)
    referral = random.choice(referrals)
    os_name, device = random.choice(devices)
    
    # Append User profile
    users_list.append({
        "user_id": user_id,
        "signup_date": signup_date,
        "country": country,
        "device_type": device,
        "os": os_name,
        "referral_source": referral
    })
    
    # 3. Simulate Onboarding Events & Activation Funnel
    current_time = signup_date
    
    # Every user opens app and starts sign up
    events_list.append({"event_id": str(uuid.uuid4()), "user_id": user_id, "timestamp": current_time, "event_name": "App Opened"})
    current_time += timedelta(minutes=random.randint(1, 3))
    events_list.append({"event_id": str(uuid.uuid4()), "user_id": user_id, "timestamp": current_time, "event_name": "Sign Up Started"})
    
    # Onboarding drop-off probabilities
    completed_email = random.random() < 0.90  # 90% verify email
    completed_bvn = completed_email and (random.random() < 0.75)  # 75% submit BVN
    completed_kyc = completed_bvn and (random.random() < 0.80)  # 80% pass KYC
    account_created = completed_kyc and (random.random() < 0.95)  # 95% create account
    
    if completed_email:
        current_time += timedelta(minutes=random.randint(1, 5))
        events_list.append({"event_id": str(uuid.uuid4()), "user_id": user_id, "timestamp": current_time, "event_name": "Email Verified"})
        
    if completed_bvn:
        current_time += timedelta(minutes=random.randint(2, 10))
        events_list.append({"event_id": str(uuid.uuid4()), "user_id": user_id, "timestamp": current_time, "event_name": "BVN Submitted"})
        current_time += timedelta(seconds=random.randint(10, 60))
        events_list.append({"event_id": str(uuid.uuid4()), "user_id": user_id, "timestamp": current_time, "event_name": "BVN Verified"})
        
    if completed_kyc:
        # KYC verification might take a few hours or days
        current_time += timedelta(hours=random.randint(1, 48))
        events_list.append({"event_id": str(uuid.uuid4()), "user_id": user_id, "timestamp": current_time, "event_name": "KYC Completed"})
        
    if account_created:
        current_time += timedelta(minutes=random.randint(1, 15))
        events_list.append({"event_id": str(uuid.uuid4()), "user_id": user_id, "timestamp": current_time, "event_name": "Account Created"})
        
        # Create an account record
        account_id = str(uuid.uuid4())
        kyc_level = random.choice(["Tier 1", "Tier 2", "Tier 3"])
        accounts_list.append({
            "account_id": account_id,
            "user_id": user_id,
            "account_type": "Savings" if random.random() < 0.3 else "Checking",
            "account_created": current_time,
            "kyc_level": kyc_level,
            "status": "Active" if random.random() < 0.9 else "Dormant"
        })
        
        # 4. Simulate Sessions and Transactions for activated users
        user_lifespan = (END_DATE - current_time).days
        if user_lifespan > 0:
            # More active users log in more frequently
            num_sessions = random.randint(3, 40) if random.random() < 0.7 else random.randint(1, 5)
            session_time = current_time + timedelta(hours=random.randint(1, 24))
            
            for _ in range(num_sessions):
                if session_time > END_DATE:
                    break
                
                # Session
                session_duration = random.randint(30, 900)  # 30 seconds to 15 minutes
                sessions_list.append({
                    "session_id": str(uuid.uuid4()),
                    "user_id": user_id,
                    "login_time": session_time,
                    "logout_time": session_time + timedelta(seconds=session_duration),
                    "device": device
                })
                
                # App Opened event during session
                events_list.append({"event_id": str(uuid.uuid4()), "user_id": user_id, "timestamp": session_time, "event_name": "App Opened"})
                
                # Decides to do a transaction (30% probability during a session)
                if random.random() < 0.30:
                    tx_type = random.choice(transaction_types)
                    tx_amount = round(random.uniform(500, 50000) if tx_type == "Transfer" else random.uniform(100, 5000), 2)
                    
                    # Transaction status and fees
                    # Card and Transfer might fail occasionally
                    tx_status = "Failed" if (tx_type in ["Card payment", "Transfer"] and random.random() < 0.05) else "Successful"
                    fee = round(tx_amount * 0.015, 2) if tx_type in ["Transfer", "Bill payment"] else 0.00
                    
                    transactions_list.append({
                        "transaction_id": str(uuid.uuid4()),
                        "user_id": user_id,
                        "date": session_time + timedelta(seconds=random.randint(10, 120)),
                        "amount": tx_amount,
                        "merchant": random.choice(merchants) if tx_type in ["Card payment", "Bill payment"] else "Self/Peer",
                        "type": tx_type,
                        "status": tx_status,
                        "fee": fee
                    })
                    
                    # Trigger corresponding transaction product events
                    events_list.append({
                        "event_id": str(uuid.uuid4()), 
                        "user_id": user_id, 
                        "timestamp": session_time, 
                        "event_name": f"{tx_type} Initiated"
                    })
                    events_list.append({
                        "event_id": str(uuid.uuid4()), 
                        "user_id": user_id, 
                        "timestamp": session_time + timedelta(seconds=10), 
                        "event_name": f"{tx_type} {tx_status}"
                    })

                # Move session time forward
                session_time += timedelta(days=random.randint(1, 10), hours=random.randint(0, 23))

# 5. Convert lists to pandas DataFrames and export to CSVs
os.makedirs("data", exist_ok=True)

df_users = pd.DataFrame(users_list)
df_accounts = pd.DataFrame(accounts_list)
df_transactions = pd.DataFrame(transactions_list)
df_events = pd.DataFrame(events_list)
df_sessions = pd.DataFrame(sessions_list)

df_users.to_csv("data/users.csv", index=False)
df_accounts.to_csv("data/accounts.csv", index=False)
df_transactions.to_csv("data/transactions.csv", index=False)
df_events.to_csv("data/events.csv", index=False)
df_sessions.to_csv("data/sessions.csv", index=False)

print("\n--- Data Generation Summary ---")
print(f"Users generated: {len(df_users)}")
print(f"Accounts generated: {len(df_accounts)} (Onboarding conversion rate: {len(df_accounts)/len(df_users)*100:.2f}%)")
print(f"Transactions generated: {len(df_transactions)} (Success rate: {len(df_transactions[df_transactions['status'] == 'Successful'])/len(df_transactions)*100:.2f}%)")
print(f"Product Events generated: {len(df_events)}")
print(f"User Sessions generated: {len(df_sessions)}")
print("\nAll files successfully saved under the 'data/' directory!")