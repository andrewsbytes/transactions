\set TABLE tx_transactions

CREATE TABLE IF NOT EXISTS :TABLE (
  date DATE,
  description TEXT,
  original_description TEXT,
  amount FLOAT,
  transaction_type TEXT,
  category TEXT,
  account_name TEXT,
  labels TEXT,
  notes TEXT
)
;

COPY :TABLE
FROM '/home/andrew/code/transactions/transactions.csv'
DELIMITER ','
HEADER
QUOTE '"'
CSV
;
