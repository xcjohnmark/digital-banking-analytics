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