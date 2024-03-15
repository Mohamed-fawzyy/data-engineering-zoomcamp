FROM python:3.9

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2 pyarrow

WORKDIR /app
COPY ingest_data.py ingest_data.py

ENTRYPOINT [ "python", "ingest_data.py" ]

#So, when you run this command, Docker will look for a Dockerfile in the current directory 
#(the directory where you run the command), and it will use the instructions in the Dockerfile to build an image.
#The resulting image will be tagged as "any_name". You can later use this image to create and run Docker containers.



