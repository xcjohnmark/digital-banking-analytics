app_opened = 5000
signup_started = 5000
email_verified = 4496
bvn_submitted = 3355
bvn_verified = 3355
kyc_completed = 2675
account_created = 2558

dropoff_rate = {
    "email_verification": ((app_opened - email_verified) / app_opened) * 100,
    "bvn_submission": ((email_verified - bvn_submitted) / email_verified) * 100,
    "bvn_verification": ((bvn_submitted - bvn_verified) / bvn_submitted) * 100,
    "kyc_completion": ((bvn_verified - kyc_completed) / bvn_verified) * 100,
    "account_creation": ((kyc_completed - account_created) / kyc_completed) * 100,
}

print(f"Email Verification Dropoff Rate: {dropoff_rate['email_verification']:.2f}%")
print(f"BVN Submission Dropoff Rate: {dropoff_rate['bvn_submission']:.2f}%")
print(f"BVN Verification Dropoff Rate: {dropoff_rate['bvn_verification']:.2f}%")
print(f"KYC Completion Dropoff Rate: {dropoff_rate['kyc_completion']:.2f}%")
print(f"Account Creation Dropoff Rate: {dropoff_rate['account_creation']:.2f}%")