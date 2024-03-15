# Data-Engineering-zoom camp 🧰
* For the first week of the course, we are asked to prepare environments on Google using Terraform and Postgres instances using Docker. Then we must ingest some taxi trip data from (https://lnkd.in/gdAuf2SB) to Postgres using Python.

# Reach/Follow me on 🚀<br>
<p align="left">
  <a href="https://www.linkedin.com/in/mohamed-fawzy-936b661b8/" target="_blank" rel="noreferrer"> <img src="https://img.icons8.com/fluency/2x/linkedin.png" alt="linkedIn" width="50" height="50"/> </a>&nbsp&nbsp
  <a href="mailto:fwzymohamed90@gmail.com" target="_blank" rel="noreferrer"> <img src="https://img.icons8.com/fluency/2x/google-logo.png" alt="googleEmail" width="50" height="50"/> </a>&nbsp&nbsp
  <a href="https://www.facebook.com/mohamed.fwzy.14" target="_blank" rel="noreferrer"> <img src="https://cdn.iconscout.com/icon/free/png-256/facebook-262-721949.png" alt="facebook" width="50" height="50"/> </a>
</p>
<br>

# Module1 📂
- Creating a Python script which is pipeline ETL
- Extract a data from the parquet file
- Transform the data from parquet to CSV and change some data types of the existing columns
- Load this data into a PostgreSQL (which I run with docker image) by pgcli
- Creating a docker network to connect the 2 containers of Postres image and PgAdmin and that is called containerized ingestion
- Dockeraizing this 2 containers with docker-compose instead of the docker network

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


![de](https://github.com/Mohamed-fawzyy/data-engineering-zoomcamp/assets/111665714/deebf426-44e7-4478-b5ca-bc3b6bb4e7c8)
