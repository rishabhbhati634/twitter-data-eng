# twitter-data-eng
Short Description: Automated Twitter data pipeline using Python, Airflow, and AWS. Extracts tweets, transforms them to CSV, and stores results in Amazon S3—integrating cloud orchestration and best practices for scalable, real-time data engineering.

Project Overview:
This end-to-end data engineering project focuses on building an automated data pipeline to extract, transform, and store real-time Twitter data. The pipeline is architected using Python, Apache Airflow (an open-source workflow orchestration system), and various AWS services, notably EC2 and S3.

Key Components & Steps:

Data Extraction:
The process begins by authenticating to the Twitter API using custom keys and tokens. With the help of Python and the tweepy library, the pipeline programmatically fetches posts (tweets) from a specified Twitter account. Data such as tweet content, like counts, retweet counts, and timestamps are gathered in JSON format.

Data Transformation:
Raw JSON data is transformed by parsing and converting it into a structured format using the pandas library, producing a clean DataFrame. Essential information—username, tweet text, engagement metrics, and creation date—is extracted for each post. The transformed data is then serialized and stored in CSV format, ready for further analysis.

Airflow Orchestration (Workflow Automation):
The core pipeline logic, including extraction and transformation functions, is encapsulated within Python modules for modularity. Airflow DAGs (Directed Acyclic Graphs) define each step as a task, allowing for scheduled and monitored pipeline execution. Apache Airflow is installed and managed on an AWS EC2 instance (Ubuntu), and the pipeline code is deployed to this cloud server.

AWS Integration:
The final, processed data is uploaded to an Amazon S3 bucket instead of being stored only locally. Full permissions are configured using AWS IAM roles to allow EC2 (running Airflow) secure access to write to S3 buckets.
The pipeline project demonstrates how to set up and configure AWS infrastructure (EC2, S3, IAM) and securely deploy, manage, and run Airflow DAGs in the cloud.

Automation & Monitoring:
With Airflow’s web UI, users can monitor the status of each task, rerun failed jobs, access detailed logs, and view the DAG graph. The workflow includes automated retry logic to handle failures robustly.

Learning & Practical Outcomes:

Learn how to set up and manage a Python-based ETL pipeline on the cloud using industry-standard tools.

Understand real-world challenges such as cloud authentication, troubleshooting permissions, and working with workflow orchestration.

Gain hands-on experience working with Twitter’s API, data wrangling in Python, Airflow automation, and AWS services.

The project demonstrates not only the technical build but also best practices for modular code design and infrastructure-as-a-service integration.

