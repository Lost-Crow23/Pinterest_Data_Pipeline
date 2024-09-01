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
events and runs them through two seperate pipelines.

1. A pipeline for the computing metrics that depend on historical data such, "most trendy or popular category" for the year,
2. A pipeline for the computing real-time metrics such as "profile popularity".

During this process, the steps were mainly split into three parts:

    - Initial set-up
    - Batch Processing
    - Stream Processing

An proficience in the following was gained:

    - Apache Kafka: event streaming platform.
    - AWS MSK (Amazon Managed Streaming for Apache Kafka): Fully managed service for Apache Kafka.
    - AWS MSK Connect: Simplification of streaming data to / from Kafka clusters.
    - Kafka REST Proxy: RESTful interface to Kafka Clusters.
    - AWS API Gateway: Monitors, Manages and Secures APIs.
    - Apache Spark and PySpark: Multi Language engine for data engineeering and machine learning.
    - Databricks: Platform for Spark processing of batch streaming data.

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

# Add image.

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

## Milestone 3

### Batch Processing: Configuring the EC2 Kafka Client

#### To create three topics with MSK

##### Setting up the EC2 instance & Apache Kafka

EC2 instances are essentially remote computers capabale of executing code on a cluster or a single machine. They serve as the foundational components of cloud computing. They can be accessed via a terminal (Bash, ~zsh or linux(windows)).

### Step 1

- Detailed process of this milestone are prescribed in the corresponding pre-requisite lessons. General steps are as follows:

1. Key Pair File Creation:
   - In the AWS console, create a key-pair file for authentication (in our case, it was created for us)

### Step 2

2. Security Group Configuration
   - Create a security group with the following inbound rules:
     - `HTTP: Anywhere IPv4`
     - `HTTPS: Anywhere IPv4`
     - `SSH: My IP`

### Step 3

- Create an EC2 instance by selecting the Amazon Linux 2 AMI.

### Step 4

- Connect your local device into the AWS instance by running the following code within the terminal:

  `ssh -i "your-key-pair.pem" ec2-user@ec2-123-45-678-90.compute-1.amazonaws.com`

- Install Kafka and IAM MSK authentication package on the client EC2 machine.

  `pip install kafka-python`

  `wget https://archive.apache.org/dist/kafka/2.8.1/kafka_2.12-2.8.1.tgz tar -xzf kafka_2.12-2.8.1.tgz`

- Navigate to your Kafka installation folder and then in the libs folder.

  `wget https://github.com/aws/aws-msk-iam-auth/releases/download/v1.1.5/aws-msk-iam-auth-1.1.5-all.jar`

- Export this CLASSPATH to `.bashrc`.

  `export CLASSPATH=/home/ec2-user/kafka_2.12-2.8.1/libs/aws-msk-iam-auth-1.1.5-all.jar`

### Step 5

- Creation of Kafka Topics
- Once the EC2 is connected, we navigate and create our `nano client.properties` to configure Kafka Client to use AWS IAM authentication to the cluster.

- client.properties file is as below:

  ```
  # Sets up TLS for encryption and SASL for authN.
  security.protocol = SASL_SSL

  # Identifies the SASL mechanism to use.
  sasl.mechanism = AWS_MSK_IAM

  # Binds SASL client implementation.
  sasl.jaas.config = software.amazon.msk.auth.iam.IAMLoginModule required awsRoleArn="arn:aws:iam::12345678:role/123456--ec2-access-role";

  # Encapsulates constructing a SigV4 signature based on extracted credentials.
  # The SASL client bound by "sasl.jaas.config" invokes this class.
  sasl.client.callback.handler.class = software.amazon.msk.auth.iam.IAMClientCallbackHandler

  ```

- Before a topic was created, the specific Bootstrap servers string and the plaintext Apache Zookeeper connection string was to be utilized from the MSK cluster.

- Using the strings as below:

  - user.pin
  - user.geo
  - user.user

- The topics were created using the code below:

  `./kafka-topics.sh --bootstrap-server BootstrapServerString --command-config client.properties --create --topic <topic_name>`

## Milestone 4

### Batch Processing: Connecting a MSK Cluster To A S3 Bucket

- Using MSK Connect to connect the MSK cluster to a S3 bucket, such that any data going through the cluster will be automatically saved and stored in a dedicated S3 bucket.

- Detailed process of this milestone are prescribed in the corresponding pre-requisite lessons. General steps are as follows:

### Step 1

1. **Amazon S3 bucket creation:**

   - In the Amazon S3 console, create an S3 bucket. This bucket will serve as the destination for data extracted from Amazon RDS.

2. **IAM Role Creation:**

   - Create an IAM role with write permissions to the designated S3 bucket.

3. **VPC Endpoint Creation for S3:**

   - Create a VPC endpoint to establish a direct connection from the MSK cluster to S3, improving efficiency and security.

### Step 2

1. **MSK Connect Custom Plug-in:**

   - Creating a connector using the custom plug-in, associating it with the IAM role. This connector will enable the extraction and storage of data from Amazon RDS to the specified S3 bucket.

2. Before a custom plug-in can be created inside the MSK, `confluent.io` Amazon S3 connector needs to be downloaded inside the EC2 client machine:

   `wget https://d2p6pa21dvn84.cloudfront.net/api/plugins/confluentinc/kafka-connect-s3/versions/10.5.13/confluentinc-kafka-connect-s3-10.5.13.zip`

   - Inside the MSK connect console, a custom plug-in can be set with the Confluent connector ZIP file inside the the bucket/

3. **Creating a connector with MSK connect**

   - Within the MSK console, the connector config settings has been tweaked so it links to our own `UUID` and a specific S3 bucket.

    ```
    connector.class=io.confluent.connect.s3.S3SinkConnector
    # same region as our bucket and cluster
    s3.region=us-east-1
    flush.size=1
    schema.compatibility=NONE
    tasks.max=3
    # include nomeclature of topic name, given here as an example will read all data from topic names starting with msk.topic....
    topics.regex=<YOUR_UUID>.*
    format.class=io.confluent.connect.s3.format.json.JsonFormat
    partitioner.class=io.confluent.connect.storage.partitioner.DefaultPartitioner
    value.converter.schemas.enable=false
    value.converter=org.apache.kafka.connect.json.JsonConverter
    storage.class=io.confluent.connect.s3.storage.S3Storage
    key.converter=org.apache.kafka.connect.storage.StringConverter
    s3.bucket.name=<BUCKET_NAME>
    ```

## Milestone 5

### Batch Processing: Configuring an API in API Gateway

To build our own API that will send data to the MSK cluster, which will be then stored in an S3 bucket.

- Detailed process of this milestone are prescribed in the corresponding pre-requisite lessons. General steps are as follows:

#### Step 1

1. AWS API Gateway Setup:

- Create an API in AWS Gateway using the REST API configuration

2. Create of a New Child Resource:

- API functionailty is extended by creating a new resource allowing a PROXY integration. Choose the Proxy resource for the newly created child resource, setting the resource path to `/{proxy+}`.

3. Configuration of ANY Method:

- Handling various HTTP methods is used by creating an ANY method for the chosen proxy resource, that will have the EC2 PublicDNS as its Endpoint URL.

#### Step 2: Setting up Kafka REST Proxy on the EC2 Client

1. Confleunt Package Installation:

- Install the Confluent package for the Kafka REST Proxy on the EC2 client

  `sudo wget https://packages.confluent.io/archive/7.2/confluent-7.2.0.tar.gz`

2. Modify of the Kafka-rest.properties:

- Modify the `Kafka-rest.properties` file, specifying the bootstrap server, IAM role, and Zookeeper connection string. This performs an IAM Authentication to the MSK Cluster.

  ```
  # Sets up TLS for encryption and SASL for authN.
  client.security.protocol = SASL_SSL

  # Identifies the SASL mechanism to use.
  client.sasl.mechanism = AWS_MSK_IAM

  # Binds SASL client implementation.
  client.sasl.jaas.config = software.amazon.msk.auth.iam.IAMLoginModule required awsRoleArn="arn:aws:iam...-ec2-access-role";

  # Encapsulates constructing a SigV4 signature based on extracted credentials.
  # The SASL client bound by "sasl.jaas.config" invokes this class.
  client.sasl.client.callback.handler.class = software.amazon.msk.auth.iam.IAMClientCallbackHandler

  ```

3. REST proxy can be then run within the EC2 Client with the code review:
   ```
   # This code needs to be run inside confluent/bin folder
   ./kafka-rest-start /home/ec2-user/confluent-7.2.0/etc/kafka-rest/kafka-rest.properties
   ```

#### Step 3

1. API Configuration in AWS API Gateway:

- In the previous created API:
  - Choose HTTP Proxy as the integration type.
  - Set the Endpoint URL to your Kafka Client Amazon EC2 Instance PublicDNS and include the `":8082"` port number.

2. Deploy the API to obtain the invoke URL.

#### Step 4

Data Emulation Python script:

- Tweaking the `user_posting_emulation.py`, which sends data to the Kafka topics using the API Invoke URL.

link to the user_posting

#### Step 5

- Finally store the data in the created S3 bucket in JSON format using the Kafka REST proxy and the API invoke URL.

## Milestone 6

### Batch Processing: Databricks

- Detailed process of this milestone are prescribed in the corresponding pre-requisite lessons. General steps are as follows:

To perform batch processing of the data in Databricks, it is essential to establish the mounting of the S3 Bucket within the platform. The notebook `Mount_to_s3_create_dfs.ipynb` was executed on Databricks. The following steps are as below:

#### Step 1

1. AWS Access Key and Secret Access Key setup:

- Create AWS Access Key and Secret Key for Databricks in AWS.
- Upload the read the Delta Table

#### Step 2

1. Extraction of the Access and Secret Key is required as shown in the file.

2. Mount S3 bucket into Databricks:

- Load the data stored in the bucket, and create DataFrames for the three tables.

#### Step 3

1. Creating the dataframe for each topic:

- Firstly, find the path of the file locations, set its file type, and read with the code found in the `Mount_to_s3.ipynb`

## Milestone 7

### Batch Processing: Spark on Databricks

- Detailed process of this milestone are prescribed in the corresponding pre-requisite lessons. General steps are as follows:

#### Step 1

Data Cleaning with PySpark and performing analysis to the data.

The DataFrames needing to be cleaned are:

    ```
    df_pin -> df_pin_clean
    df_geo -> df_geo_clean
    df_user -> df_user_clean
    ```

1. The file code `Datacleaning & Queries with spark.ipynb` consists of:

- All three DataFrames cleaned by removing the duplicates rows.
- Removing NULL values.
- Replacing values when necessary.
- Converting data types.
- Renaming and re-ordering columns when necessary.

#### Step 2 : Querying the data

Querying the data can be seen in the file `Datacleaning & Queries with spark.ipynb`. Before querying the data, a creation of temporary view in Spark SQL with the specified name "pin", "geo", and "user" to simplify the queries. This is shown in the file.

## Milestone 8

### Batch Processing: AWS MWAA

- Detailed process of this milestone are prescribed in the corresponding pre-requisite lessons. General steps are as follows:

Automation with AWS MWAA (Managed Workflows for Apache Airflow)

#### Step 1

- Create an API token in Databricks.
- Initialize a connection between MWAA and Databricks.

#### Step 2

1. Create and upload a DAG (Directed Acyclic Graph) file into MWAA environment.
- Develop a DAG file in Python. DAG created as seen in the `124eb5889d67_dag.py`. Specifying the Cluster ID in AWS.
- This is uploaded inside the S3 Bucket name "mwaa-dag-bucket"

2. Manually trigger the DAG to run a Databricks Notebook.
- Inside MWAA, the DAG is triggered to check if it runs successfully.

#### Step 3

- Customize the DAG to run regularly based on the incoming data rate.
- At the specified intervals, the notebook specified in the DAG will run automatically , executing the defined queries.

## Milestone 9 

### Stream Processing: AWS Kinesis

- Detailed process of this milestone are prescribed in the corresponding pre-requisite lessons. General steps are as follows:

Sending streaming data to Kinesis and read this data Databricks.

#### Step 1

1. Create three streams on AWS Kinesis for pin, geo, and user data.

2. In the Kinesis dashboard, select "Create data streams"

3. Give the streams the names:
- `streaming-<user_id>-pin,`
- `streaming-<user_id>-geo`
- `streaming-<user_id>-user`

4. Select "Provisioned" capacity mode. 

5. Create a data stream

#### Step 2

Configure API with Kinesis proxy integration. To interact with the Kinesis using HTTP requests, create new API resources on AWS API Gateway.

1. A new resource is made inside AWS API Gateway to Integrate Kinesis
- In "Resource name", type 'streams'.
- Added HTTP Headers
- Added Mapping Templates

#### Step 3

2. Create a GET method in `/streams' resource with the following configuration (amend the Execution role with your Kinesis access role):

#### Step 4

- In the 'Integration Request" tab click 'Edit' and add the following:

#### Step 5

- In /streams, create resource - a child resource - and call it '/{stream-name}'.
- In /{stream-name}, create DELETE, GET, and POST methods with the following conifguration:

- DELETE:

- GET:

- POST:

#### Step 6

- In /{stream-name}, create two more child resources: /record, and /records using the same config as before.

#### Step 7

- In /record, create PUT method using the configuration below:

#### Step 8

- In /records, create PUT method using the configuration below:

#### Step 9 

Send data into the Kinesis Streams, based `user_posting_emulation.py`, you have to create Python script to send requests to your API, which adds one record at a time to the streams you have made. You should send data from the three Pinterest tables to their corresponding Kinesis streams.

- A new file named `user_posting_emulation_streaming.py` is created to send data into Kinesis stream.
- After converting each data into the correct data type, the file is run to send it into the API. 

#### Read data from Kinesis streams in Databricks

Create a notebook in Databricks and follow the same process as the batch processing to read the `authentication_credentials`, ingest the data into Kinesis Data Streams, and read data from the three streams in Databricks Notebook.

#### Data Cleaning 

Clean the streaming data using the same methods as with the batch data. 

#### Write the data to Delta Table

Before it can be sent into the delta tables, the checkpoint folder needs to be deleted. 

    dbutils.fs.rm("/tmp/kinesis/_checkpoints/", True)

Then a clean DataFrame can be written inside the Delta Tables

## File Structure

## Licence Information

MIT License

Copyright (c) 2023 Lost-Crow23

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS"WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.






