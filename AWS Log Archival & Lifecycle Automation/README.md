# 📦 EC2 Log Archiver with Automated S3 Backup

Automated log archival solution built on AWS that compresses application logs, uploads them to Amazon S3, and automatically transitions archived logs to Glacier using Lifecycle Policies for long-term cost optimization.

---

# 📌 Project Overview

In production environments, application logs continuously grow and consume storage.

This project automates the complete lifecycle of log management:

- Generate application logs
- Compress logs into ZIP archives
- Upload archives to Amazon S3
- Delete local archive after successful upload
- Automatically transition old archives to Amazon Glacier
- Schedule the entire workflow using Cron

---

# 🏗️ Architecture

<img width="1536" height="1024" alt="log-arch" src="https://github.com/user-attachments/assets/98a19fd4-b697-49d2-bcf6-d2c51ac1972e" />

---

# Services Used

1. Amazon EC2 ----> Application Host
2. Amazon S3 ---> Archive Storage
3. Amazon Glacier ---> Long-term archival
4. IAM Role ---> Secure authentication
5. Cron ---> Automation Scheduler
6. Python ---> Log processing
7. boto3 ---> AWS SDK

---

# 📂 Project Tree

<img width="714" height="408" alt="tree" src="https://github.com/user-attachments/assets/c051a4e7-78c0-400a-b19d-fd1e5b7e688a" />
```text
ec2-log-archiver/
│
├── app.py
├── config.json
├── requirements.txt
├── README.md
├── .gitignore
│
├── utils/
│   └── archive_logs.py
│
├── logs/
│
└── archive/
```

---

# ⚙️ Workflow

1. Application writes logs to `app.log`
2. Cron executes `archive_logs.py`
3. Log file is compressed into a timestamped ZIP archive
4. Archive uploads to Amazon S3 using an IAM Role
5. Upload status is written to `upload.log`
6. Local ZIP file is deleted after successful upload
7. S3 Lifecycle Policy moves old archives to Glacier

---

# 📸 Project Walkthrough

## 1️⃣ EC2 Instance

*EC2 instance hosting the application.*

![EC2](images/ec2-instance.png)

---

## 2️⃣ Python Application Generating Logs

![Application](images/app-running.png)

---

## 3️⃣ Archive Created

Timestamped ZIP archive generated.

![Archive](images/archive-created.png)

---

## 4️⃣ Upload to Amazon S3

Successful upload to the S3 bucket.

![S3 Upload](images/s3-upload.png)

---

## 5️⃣ S3 Bucket Contents

Archived ZIP files stored in S3.

![Bucket](images/s3-bucket.png)

---

## 6️⃣ Lifecycle Policy

Objects automatically transition to Glacier.

![Lifecycle](images/lifecycle.png)

---

## 7️⃣ Cron Job

Automation configured using Linux Cron.

![Cron](images/cron.png)

---

## 8️⃣ Upload Log

Operational logs showing successful executions.

![Upload Log](images/upload-log.png)

---

# 🔒 Security

- IAM Role used instead of hardcoded AWS credentials
- Configuration separated from source code
- No secrets stored in GitHub
- Upload verified before deleting local archive

---

# 💰 Cost Optimization

Amazon S3 Lifecycle Policies automatically transition archived log files to Glacier, reducing long-term storage costs while maintaining durability.

---

# 🛠 Engineering Decisions

### Why IAM Roles?

Avoid storing AWS credentials in code and use temporary credentials managed by AWS.

### Why compress logs?

Reduce upload time and storage consumption while preserving point-in-time snapshots.

### Why Cron?

Enable unattended automation without manual intervention.

### Why Lifecycle Policies?

Automatically optimize storage costs without modifying application code.

---

# 📈 Skills Demonstrated

### AWS

- Amazon EC2
- Amazon S3
- IAM Roles
- Lifecycle Policies
- Glacier

### Python

- boto3
- logging
- zipfile
- json
- datetime
- exception handling

### Linux

- Cron Jobs
- File Management
- Log Automation

### DevOps

- Automation
- Cost Optimization
- Operational Logging
- Configuration Management
- Secure Authentication

---

# 🚀 Future Enhancements

- CloudWatch integration
- SNS notifications
- Multi-instance support with Auto Scaling Groups
- Terraform deployment
- CI/CD pipeline
- Log rotation
- Monitoring dashboard

---

# 👨‍💻 Author

Developed as part of my AWS Cloud & DevOps portfolio to demonstrate automation, operational reliability, secure AWS practices, and production-oriented system design.
