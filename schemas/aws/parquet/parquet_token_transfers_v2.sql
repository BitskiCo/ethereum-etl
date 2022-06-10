CREATE EXTERNAL TABLE IF NOT EXISTS parquet_token_transfers_v2 (
    contract_address STRING,
    from_address STRING,
    to_address STRING,
    amount STRING,
    token_type STRING,
    token_ids STRING,
    transaction_hash STRING,
    log_index BIGINT,
    block_number BIGINT
)
PARTITIONED BY (start_block BIGINT, end_block BIGINT)
STORED AS PARQUET
LOCATION 's3://<your_bucket>/ethereumetl/parquet/token_transfers_v2';

MSCK REPAIR TABLE parquet_token_transfers;