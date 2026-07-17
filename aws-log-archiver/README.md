# AWS Log Archival Lifecycle Automation

## Overview

This project automates the lifecycle of application logs using Python and AWS.

The automation performs the following workflow:

- Generates application logs
- Archives logs into timestamped ZIP files
- Uploads archives to Amazon S3
- Deletes the local archive after successful upload
- Runs automatically using Cron

---

# Features

- Automated log generation
- Timestamp-based ZIP archival
- Amazon S3 integration using Boto3
- Automatic cleanup after upload
- Cron job scheduling
- Python virtual environment support

---

# Technologies Used

- Python 3
- AWS S3
- Boto3
- AWS CLI
- Cron
- Git & GitHub
- Ubuntu Linux

---

# Project Structure

<img width="1350" height="1165" alt="log-project-architecture" src="https://github.com/user-attachments/assets/1f8a19a5-0b53-4c24-a393-060d9b464b43" />

---

# Setup

Clone the repository

```bash
git clone <your-repository-url>
cd aws-log-archiver
```

Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Configure AWS CLI

```bash
aws configure
```

---

# Run Log Generator

```bash
python3 app.py
```

Example

<img width="1525" height="981" alt="log-generated" src="https://github.com/user-attachments/assets/9c84f4e3-b55b-4c10-846d-7b5d7112ff5f" />

---

# Archive & Upload Logs

```bash
python3 archive_logs.py
```

Example

![Archive Upload](screenshots/03-archive-upload.png)

---

# ☁️ Amazon S3 Upload

Uploaded ZIP archives are stored in an Amazon S3 bucket.

<img width="1525" height="981" alt="s3-upload" src="https://github.com/user-attachments/assets/6f0742b8-9311-4aa7-a77b-eec6a224fcc9" />

AWS CLI Verification

![AWS CLI](screenshots/07-s3-cli.png)

---

# ⏰ Cron Automation

The archival script is executed automatically every 5 minutes.

![Cron Job](screenshots/05-cron-job.png)

---

# 📄 Upload Logs

Execution logs are stored in:

```
upload.log
```

![Upload Log](screenshots/06-upload-log.png)

---

# 🔄 Workflow

```
Generate Logs
      │
      ▼
Archive Logs
      │
      ▼
Upload to Amazon S3
      │
      ▼
Delete Local Archive
      │
      ▼
Repeat via Cron
```

---

# 📚 Learning Outcomes

Through this project I gained hands-on experience with:

- Python Automation
- AWS S3
- Boto3 SDK
- AWS CLI
- Linux Cron Jobs
- Git & GitHub
- Virtual Environments
- Log Archival Automation

---

# 👤 Author

Abhishek
