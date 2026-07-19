SELECT
	type,
	COUNT(*) AS total_transaction,
	SUM(amount) AS total_volume,
	ROUND(AVG(amount), 2) AS avg_transaction_amount
FROM transactions
GROUP BY type
ORDER BY total_volume DESC;


SELECT 
	type, COUNT(*) AS total_transactions,
	ROUND(SUM(CASE WHEN status = 'Successful' THEN 1 ELSE 0 END)::NUMERIC /
	COUNT(*) * 100, 2) AS success_rate
FROM transactions
GROUP BY type
ORDER BY success_rate ASC;


SELECT type, SUM(fee) AS total_revenue
FROM transactions
GROUP BY type
ORDER BY total_revenue DESC;


SELECT SUM(fee) AS total_revenue
FROM transactions;
