CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    signup_date TIMESTAMP WITH TIME ZONE NOT NULL,
    country VARCHAR(50) NOT NULL,
    device_type VARCHAR(100) NOT NULL,
    os VARCHAR(50) NOT NULL,
    referral_source VARCHAR(100) NOT NULL
);

CREATE TABLE accounts (
    account_id UUID PRIMARY KEY,
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    account_type VARCHAR(50) NOT NULL,
    account_created TIMESTAMP WITH TIME ZONE NOT NULL,
    kyc_level VARCHAR(20) NOT NULL,
    status VARCHAR(20) NOT NULL,
    CONSTRAINT chk_status CHECK (status IN ('Active', 'Dormant'))
);

CREATE TABLE transactions (
    transaction_id UUID PRIMARY KEY,
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    date TIMESTAMP WITH TIME ZONE NOT NULL,
    amount DECIMAL(15, 2) NOT NULL CHECK (amount > 0),
    merchant VARCHAR(100) NOT NULL,
    type VARCHAR(50) NOT NULL,
    status VARCHAR(20) NOT NULL,
    fee DECIMAL(10, 2) NOT NULL DEFAULT 0.00 CHECK (fee >= 0),
    CONSTRAINT chk_tx_status CHECK (status IN ('Successful', 'Failed'))
);

CREATE TABLE events (
    event_id UUID PRIMARY KEY,
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    timestamp TIMESTAMP WITH TIME ZONE NOT NULL,
    event_name VARCHAR(100) NOT NULL
);

CREATE TABLE sessions (
    session_id UUID PRIMARY KEY,
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    login_time TIMESTAMP WITH TIME ZONE NOT NULL,
    logout_time TIMESTAMP WITH TIME ZONE NULL,
    device VARCHAR(100) NOT NULL,
    CONSTRAINT chk_session_times CHECK (logout_time IS NULL OR logout_time >= login_time)
);