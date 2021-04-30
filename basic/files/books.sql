CREATE TABLE IF NOT EXISTS Metadata(
    _id UUID PRIMARY KEY UNIQUE,
    account_email VARCHAR(255) NOT NULL,
    symbol VARCHAR(255) NOT NULL,
    last_sync_timestamp BIGINT NOT NULL,
    last_record_timestamp BIGINT NOT NULL,
    last_record_id VARCHAR(255) NOT NULL,
    table_name VARCHAR(255) NOT NULL,
    _created_at TIMESTAMPTZ DEFAULT NOW(),
    _updated_at TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS TransactionHistory(
    _id UUID PRIMARY KEY UNIQUE,
    status VARCHAR(255) NOT NULL,
    amount_total VARCHAR(255) NOT NULL,
    fee VARCHAR(255) NOT NULL,
    amount VARCHAR(255) NOT NULL,
	submit_time VARCHAR(225),
	success_time VARCHAR(225) NOT NULL,
	withdraw_id VARCHAR(255) NOT NULL,
    deposit_id  VARCHAR(255) NOT NULL,
	tx VARCHAR(255) NOT NULL,
	used_by VARCHAR(255) NOT NULL,
    asset VARCHAR(255) NOT NULL,
    tx_type VARCHAR(255) NOT NULL,
    _success_time_dt TIMESTAMPTZ NOT NULL,
    _account VARCHAR(255) NOT NULL,
    _created_at TIMESTAMPTZ DEFAULT NOW(),
    _updated_at TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS GetInfo(
    _id UUID PRIMARY KEY UNIQUE,
    server_time BIGINT NOT NULL,
    asset VARCHAR(255) NOT NULL,
    balance VARCHAR(255) NOT NULL,
    balance_hold VARCHAR(255) NOT NULL,
	address VARCHAR(255),
    user_id  VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    profile_picture VARCHAR(255),
    verification_status VARCHAR(255) NOT NULL,
    gauth_enable BOOLEAN NOT NULL,
    _server_time_dt TIMESTAMPTZ NOT NULL,
    _account VARCHAR(255) NOT NULL,
    _created_at  TIMESTAMPTZ DEFAULT NOW(),
    _updated_at  TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS TradeHistory(
    _id UUID PRIMARY KEY UNIQUE,
    trade_id VARCHAR(255) NOT NULL,
    order_id VARCHAR(255) NOT NULL,
	trade_type VARCHAR(50) NOT NULL,
    amount VARCHAR(255) NOT NULL,
    asset VARCHAR(255) NOT NULL,
    price VARCHAR(255) NOT NULL,
    fee VARCHAR(255) NOT NULL,
    trade_time VARCHAR(255) NOT NULL,
    _trade_time_dt TIMESTAMPTZ NOT NULL,
	_pair VARCHAR(255) NOT NULL,
    _account VARCHAR(255) NOT NULL,
    _created_at  TIMESTAMPTZ DEFAULT NOW(),
    _updated_at  TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS OrderHistory (
    _id UUID PRIMARY KEY UNIQUE,
    order_id VARCHAR(255) NOT NULL,
    order_type VARCHAR(255) NOT NULL,
    price VARCHAR(255) NOT NULL,
    submit_time VARCHAR(255) NOT NULL,
    finish_time VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL,
    order_amount VARCHAR(255) NOT NULL,
    remain_amount VARCHAR(255) NOT NULL,
    order_asset VARCHAR(255) NOT NULL,
    _submit_time_dt TIMESTAMPTZ NOT NULL,
	_pair VARCHAR(255) NOT NULL,
    _account VARCHAR(255) NOT NULL,
    _created_at  TIMESTAMPTZ DEFAULT NOW(),
    _updated_at  TIMESTAMPTZ
);