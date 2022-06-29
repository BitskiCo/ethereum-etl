CREATE EXTERNAL TABLE IF NOT EXISTS token_transfers_v2 (
    contract_address STRING,
    from_address STRING,
    to_address STRING,
    amount STRING,
    token_type STRING,
    token_id STRING,
    transaction_hash STRING,
    log_index BIGINT,
    block_number BIGINT
)
PARTITIONED BY (start_block BIGINT, end_block BIGINT)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
    'serialization.format' = ',',
    'field.delim' = ',',
    'escape.delim' = '\\'
)
STORED AS TEXTFILE
LOCATION 's3://<your_bucket>/ethereumetl/export/token_transfers_v2'
TBLPROPERTIES (
  'skip.header.line.count' = '1'
);

MSCK REPAIR TABLE token_transfers_v2;