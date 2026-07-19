-- MAU
SELECT
    DATE_TRUNC('month', login_time) AS active_month,
    COUNT(DISTINCT user_id) AS monthly_active_users
FROM sessions
GROUP BY active_month
ORDER BY active_month;


-- WAU
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


-- DAU
WITH daily_active AS (
    SELECT
        login_time::DATE AS active_date,
        COUNT(DISTINCT user_id) AS daily_users
    FROM sessions
    GROUP BY active_date
)
SELECT 
    ROUND(AVG(daily_users), 1) AS avg_daily_users
FROM daily_active;


-- App Stickiness Ratio DAU/MAU
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