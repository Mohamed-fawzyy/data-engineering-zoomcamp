#!/usr/bin/env python
# coding: utf-8

# If you are importing a package that is not installed, you can install it by running the following 
# command in an activated terminal: pip3 install {package_name}.

import pandas as pd
import argparse
import os

from sqlalchemy import create_engine
from time import time


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    user = params.user
    db = params.db
    table_name = params.table_name
    url = params.url
    parquet_name = 'output.parquet'
    csv_name = 'output.csv'
    
    # download parquet file the convert into csv file
    
    os.system(f"wget {url} -O {parquet_name}")
    
    if os.path.exists(parquet_name) and os.path.getsize(parquet_name) > 0:
        # Read the Parquet file into a DataFrame
        df = pd.read_parquet(parquet_name)

        # Convert DataFrame to CSV
        df.to_csv(csv_name, index=False)
        # df.head()
        
        df = pd.read_parquet(parquet_name)
        df.to_csv(csv_name)
        
        
        engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
        engine.connect()

        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        #print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))

        df_iterate = pd.read_csv(csv_name, iterator=True, chunksize=100000)
        df = next(df_iterate)

        df.head(n=0).to_sql(name=table_name, con=engine, index=False, if_exists='replace')
        df.to_sql(name=table_name, con=engine, index=False, if_exists='append')


        counter = 0
        while True:
            start_date = time()

            df = next(df_iterate)
            df.to_sql(name=table_name, con=engine, index=False, if_exists='append')

            counter += 1
            end_date = time()

            print(f'Inserted the {counter} chunk in time %.3f seconds' % (end_date - start_date))
    else:
        print(f"Error: Failed to download {url}. Check your URL and try again.")


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', help='user name of postgres')
    parser.add_argument('--password', help='password name of postgres')
    parser.add_argument('--host', help='host of postgres')
    parser.add_argument('--port', help='port of postgres')
    parser.add_argument('--db', help='database name of postgres')
    parser.add_argument('--table_name', help='name of the table where we will write the results to postgres')
    parser.add_argument('--url', help='url of the parquet file that we will transform it into csv')

    args = parser.parse_args()
    main(args)






