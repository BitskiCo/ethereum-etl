CREATE EXTERNAL TABLE IF NOT EXISTS tokens (
    address STRING,
    symbol STRING,
    name STRING,
    decimals BIGINT,
    total_supply DECIMAL(38,0),
    chain_id BIGINT
)
PARTITIONED BY (date STRING, chain_id BIGINT)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
    'serialization.format' = ',',
    'field.delim' = ',',
    'escape.delim' = '\\'
)
STORED AS TEXTFILE
LOCATION 's3://<your_bucket>/ethereumetl/export/tokens'
TBLPROPERTIES (
  'skip.header.line.count' = '1'
);

MSCK REPAIR TABLE tokens;
