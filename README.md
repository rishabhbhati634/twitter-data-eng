# 🚀 Automated Twitter Data Pipeline

**Short Description:**  
Automated Twitter data pipeline using **Python**, **Airflow**, and **AWS**. Extracts tweets, transforms them to CSV, and stores results in **Amazon S3**—integrating cloud orchestration and best practices for scalable, real-time data engineering.

---

## 🧰 Key Technologies Used
- 🐍 **Python:** Data extraction, transformation, and scripting  
- 🐦 **Twitter API (tweepy):** Fetching real-time tweets  
- 📄 **Xquik exports:** Replaying CSV, JSON, or JSONL tweet exports
- 🧹 **Pandas:** Data cleaning and CSV export  
- ⚙️ **Apache Airflow:** Workflow orchestration and automation  
- ☁️ **AWS EC2:** Cloud server for running Airflow  
- 💾 **AWS S3:** Cloud data storage for outputs  
- 🔐 **IAM Roles:** Secure AWS resource access configuration  

---
<img width="773" height="325" alt="image" src="https://github.com/user-attachments/assets/f12af930-9245-4d89-b809-ecfc4ac3a626" />

---

## 📊 Project Overview

This end-to-end data engineering project focuses on building an automated data pipeline to extract, transform, and store real-time Twitter data. The pipeline is architected using **Python**, **Apache Airflow** (an open-source workflow orchestration system), and **AWS services** such as **EC2** and **S3**.

---

## 🧩 Key Components & Steps

### 1️⃣ Data Extraction  
Authenticates to the **Twitter API** using custom keys and tokens. With **Python** and the **tweepy** library, the pipeline programmatically fetches posts (tweets) from a specified Twitter account. Data such as tweet content, like counts, retweet counts, and timestamps are gathered in **JSON** format.

For offline or repeatable analysis, set `XQUIK_EXPORT_PATH` to a Xquik CSV,
JSON, or JSONL export. The ETL maps common tweet text, engagement, author, and
timestamp fields into the same `refined_tweets.csv` output schema used by the
live API path.

### 2️⃣ Data Transformation  
Raw JSON data is cleaned and structured using **pandas**, producing a clean DataFrame. Essential information—username, tweet text, engagement metrics, and creation date—is extracted, then serialized and stored in **CSV** format for further analysis.

Configure credentials and output paths with environment variables:

```bash
export TWITTER_CONSUMER_KEY='your_consumer_key'
export TWITTER_CONSUMER_SECRET='your_consumer_secret'
export TWITTER_ACCESS_TOKEN='your_access_token'
export TWITTER_ACCESS_TOKEN_SECRET='your_access_token_secret'
export TWITTER_USERNAME='elonmusk'
export TWITTER_MAX_RESULTS='200'
export TWITTER_OUTPUT_PATH='refined_tweets.csv'
```

Replay a Xquik export without live Twitter credentials:

```bash
export XQUIK_EXPORT_PATH='data/xquik-export.jsonl'
export TWITTER_OUTPUT_PATH='refined_tweets.csv'
python twitter_etl.py
```

### 3️⃣ Airflow Orchestration (Workflow Automation)  
The core pipeline logic is modularized in Python scripts. **Airflow DAGs (Directed Acyclic Graphs)** define each step as a task, allowing scheduled and monitored execution. Airflow runs on an **AWS EC2** instance (Ubuntu), deploying the pipeline code to the cloud server.

### 4️⃣ AWS Integration  
The final processed data is uploaded to an **Amazon S3** bucket. Full permissions using **IAM Roles** allow secure EC2-to-S3 access. The project demonstrates AWS infrastructure setup and secure Airflow DAG management in the cloud.

### 5️⃣ Automation & Monitoring  
The **Airflow web UI** enables monitoring of task status, log access, rerunning failed jobs, and visual DAG graphs. Automated retries enhance reliability.

---

## 🎯 Learning & Practical Outcomes

- Set up and manage a **Python-based ETL pipeline** on cloud infrastructure.  
- Understand real-world challenges like **cloud authentication**, **permissions troubleshooting**, and **workflow orchestration**.  
- Gain hands-on experience with **Twitter API**, **data wrangling**, **Airflow automation**, and **AWS cloud services**.  
- Apply best practices for **modular code design** and **cloud infrastructure integration**.

---
