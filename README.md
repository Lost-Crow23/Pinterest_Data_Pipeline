# Pinterest Data Pipeline

AWS Data Pipeline

# Table of Contents

- Description
- Prequisites
- Usage Instructions
  - Milestone 1
  - Milestone 2
    - Download Pinterest Infrastructure
    - AWS console sign in
  - Milestone 3
    - Batch Processing: Configuring the EC2 Kafka Client
  - Milestone 4
    - Batch Processing: Connecting a MSK Cluster To A S3 Bucket
  - Milestone 5
    - Batch Processing: Configuring an API in API Gateway
  - Milestone 6
    - Batch Processing: Databricks
  - Milestone 7
    - Batch Processing: Spark on Databricks
  - Milestone 8
    - Batch Processing: AWS MWAA
  - Milestone 9
    - Stream Processing: AWS Kinesis
- File Structure
- License Information

# Description

Build an integrated system that Pinterest uses to analyse real-time and historical data generation
by posts from their users.

In this project, which is a pipeline integration based project set by Aicore forming part of the
data engineeing bootcamp. Pinterest has built an phenomenal machine learning engineering system, which has
billions of users interacting by uploading images or clicking on posts/images which need processing every day
to make informed decisions. A similar infrastructure is built via a system in the cloud that takes in those
events and runs them through two seperate pipelines. 1. A pipeline for the computing metrics that depend on historical data such, "most trendy or popular category" for the year, 2. A pipeline for the computing real-time metrics such as "profile popularity".

# Prequisites

You may use HomeBrew (macos) to install an distribution for central software called "miniconda" which is an environment can created to have all the dependencies and packages installed all in one.

Many list of packages are required to fulfil this project which can be found in the prerequisites.txt file.

But main packages include: 

- IDE = Vscode 
- Python version 3.11.9 (Installed within the environment(conda)) 
- Linux (Macos uses Linux(bash or zrc) integrated on terminal) 
- AWS IAM console login with necessary credentials 
- Kafka-python
`pip install kafka-python` 
- Pymysql 
- PyYaml
`pip install PyYaml`

## Apache Kafka

- An event streaming platform. Full documentation can be found here: # Link

Event streaming is essentially the practice of capturing data in real-time from event sources like databases, sensors,
mobile devices, cloud services and software applications in the form of streams of events; storing these events durably for later
retrieval; manipulating, processing, and reacting to event streams in real-time as well as retrospectively and routing to different
destination technologies. Ensures continious flow and interpretation of data so the correct information is at the right place and time.

## AWS MSK (Amazon Managed Streaming Kafka)

- Full documentation can be found here: # Link

Fully managed service that enables you to build and run applications that use Apache Kafka to process streaming data.

## AWS MSK Connet (Amazon Managed Streaming Kafka Connect)

- A feature of MSK that makes it easy for developers to stream data to and from their Apache Kafka clusters. Full documentation can be found here: # Link

MSK connect allows you to deploy fully managed connectors built for Kafka Connect that move data into or pull data from popular data stores like Amazon S3. Use source connectors to import data from external systems into your topics. With sink connectors, export of data can be done from your topics to external systems.

## Kafka REST Proxy

- Full documentation can be found here: Link

Confluent REST Proxy providing a RESTful interface to an Apache Kafka cluster.

## AWS API Gateway

- Full documentation can be found here: Link

A fully managed service that makes it easy for developers to create, publish, maintain, monitor and secure APIs at any scale.

## Apache Spark

- Full documentation can be found here: Link

Multi-language engine for executing data engineering, data science, and machine learning on single-node machines or clusters.

## PySpark

- Full documentation can be found here: Link

Python API for Apache Spark. Enabling you to perform real-time, large-scale data processing in a distributed environment using Python.

## Databricks

- Full documention can be found here: Link

Used the platform to perform Spark Processing of batch and streaming data. Unified, open analytics platform for building, deploying, sharing, and maintaining grade data and AI solutions at scale. Databricks Lakehouse integrates with cloud storage.

## Managed Workflows for Apache Airflows (MWAA)

- Full documentatoin can be found here: Link

With MWAA, you can use Apache Airflow and Python to create workflows without having to manage the underlying infastructure for scalability, availability and security. Enables users to use Python to build scheduling workflows for batch-orientated processes. Orchestates batch processing on the Databricks platform.

## AWS Kinesis

- Full documentation can be found here: Link

An managed service for processing and analysing streaming data. I've used Kinesis Data Streams to collect and store data temporarily before using Spark on Databricks to read and process the stream.

# Usage Instructions

## Milestone 1

### Step 1

Setting up the environment:

Create the Github repo, thus clones to the local machine.

Image of new repo

## Milestone 2

### Step 1

- Downloading the Pinterest Infrastructure:

  - To emulate a similar data that Pinterest's engineers are likely to work with, the project contains a script, `user_posting_emulation.py` that when run from the terminal, it resembles the stream of random data points received by the Pinterest API when POST requests are made by users uploading data to Pinterest.

  - Running such a script, instantiates a database connector class, which connects to an AWS RDS database containing the following tables:

    - `pinterest_data` contains data about posts being updating to Pinterest
    - `geolocation_data` contains data about the geolocation of each Pinterest post within `pinterest_data`
    - `user_data` contains data about the user that has uploaded each post found in `pinterest_data`

  - `run_infinite_post_data_loop()` method infinitely iterates at random intervals between 0 and 2 seconds, selecting columns of a random row from each of the three tables and writing the data to a dictionary. Three dictionaries are then printed to console.

- Examples of data generated:

- pinterest_data:

    `{'index': 2863, 'unique_id': '9bf39437-42a6-4f02-99a0-9a0383d8cd70', 'title': '25 Super Fun Summer Crafts for Kids - Of Life and Lisa', 'description': 'Keep the kids busy this summer with these easy diy crafts and projects. Creative and…', 'poster_name': 'Of Life & Lisa | Lifestyle Blog', 'follower_count': '124k', 'tag_list': 'Summer Crafts For Kids,Fun Crafts For Kids,Summer Kids,Toddler Crafts,Crafts To Do,Diy For Kids,Summer Snow,Diys For Summer,Craft Ideas For Girls', 'is_image_or_video': 'image', 'image_src': 'https://i.pinimg.com/originals/b3/bc/e2/b3bce2964e8c8975387b39660eed5f16.jpg', 'downloaded': 1, 'save_location': 'Local save in /data/diy-and-crafts', 'category': 'diy-and-crafts'}`

- geolocation_data:

    `{'ind': 2863, 'timestamp': datetime.datetime(2020, 4, 27, 13, 34, 16), 'latitude': -5.34445, 'longitude': -177.924, 'country': 'Armenia'}`

- user_data:

    `{'ind': 2863, 'first_name': 'Dylan', 'last_name': 'Holmes', 'age': 32, 'date_joined': datetime.datetime(2016, 10, 23, 14, 6, 51)}`

### Step 2

- AWS sign-in Console (Credentials)

  - `IAM user` and `password` along with the `key pair name.pem` were given by Aicore. Also given `SSH Keypair ID`
  - Login to you're given account

## Milestone 3 - Batch Processing: Configuring the EC2 Kafka Client
