#### Docker & SQL 🐳🚕 
- Prepare Postgres then run Postgres and load data as shown in the videos We'll use the green taxi trips from September 2019:
<!-- Side Note: Additional Information -->
> Note: The available data now is parquet so I added a small transformation process to read the data from its format and then transform it into CSV. (review the pipeline script)
> 
```bash
wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet
```
You will also need the dataset with zones:

wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv
