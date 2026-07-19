-- Activation conversion Rates
SELECT
	(SELECT COUNT(DISTINCT(user_id)) FROM users) AS total_users,
	(SELECT COUNT(DISTINCT(account_id)) FROM accounts) AS total_accounts,
	ROUND((SELECT COUNT(DISTINCT(account_id))
FROM accounts)::NUMERIC / (SELECT COUNT(DISTINCT(user_id)) FROM users) * 100, 2) AS conversion_rate_percentage;

-- Onboarding Funnel Stage counts
SELECT
	COUNT(DISTINCT CASE WHEN event_name = 'App Opened' THEN user_id END) AS open_stage,
	COUNT(DISTINCT CASE WHEN event_name = 'Sign Up Started' THEN user_id END) AS signup_stage,
	COUNT(DISTINCT CASE WHEN event_name = 'Email Verified' THEN user_id END) AS email_verified_stage,
	COUNT(DISTINCT CASE WHEN event_name = 'BVN Submitted' THEN user_id END) AS bvn_submitted_stage,
	COUNT(DISTINCT CASE WHEN event_name = 'BVN Verified' THEN user_id END) AS bvn_verified_stage,
	COUNT(DISTINCT CASE WHEN event_name = 'KYC Completed' THEN user_id END) AS kyc_complete_stage,
	COUNT(DISTINCT CASE WHEN event_name = 'Account Created' THEN user_id END) AS account_created_stage
FROM events;