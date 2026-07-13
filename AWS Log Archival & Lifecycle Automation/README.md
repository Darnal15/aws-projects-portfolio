<img width="1045" height="404" alt="uploaded2s3" src="https://github.com/user-attachments/assets/4f4a32fc-a118-4955-94f0-ce65117c1145" /># EC2 Log Archiver with Automated S3 Backup

Automated log archival solution built on AWS that compresses application logs, uploads them to Amazon S3, and automatically transitions archived logs to Glacier using Lifecycle Policies for long-term cost optimization.

---

# Project Overview

In production environments, application logs continuously grow and consume storage.

This project automates the complete lifecycle of log management:

- Generate application logs
- Compress logs into ZIP archives
- Upload archives to Amazon S3
- Delete local archive after successful upload
- Automatically transition old archives to Amazon Glacier
- Schedule the entire workflow using Cron

---

# Architecture

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

# Project Tree

<img width="714" height="408" alt="tree" src="https://github.com/user-attachments/assets/c051a4e7-78c0-400a-b19d-fd1e5b7e688a" />


# Workflow

1. Application writes logs to `app.log`
2. Cron executes `archive_logs.py`
3. Log file is compressed into a timestamped ZIP archive
4. Archive uploads to Amazon S3 using an IAM Role
5. Upload status is written to `upload.log`
6. Local ZIP file is deleted after successful upload
7. S3 Lifecycle Policy moves old archives to Glacier

---

# Project Walkthrough

## 1️⃣ EC2 Instance

*EC2 instance hosting the application.*

<img width="910" height="793" alt="ec2" src="https://github.com/user-attachments/assets/d3e6e3ae-9b49-4e17-bab7-4d04917a3094" />

---

## 2️⃣ Python Application Generating Logs

<img width="898" height="727" alt="py-gen-logs" src="https://github.com/user-attachments/assets/a2f32ec4-e12e-4817-9e94-b8fcc9353df4" />

---

## 3️⃣ Archive Created

Timestamped ZIP archive generated.

<img width="926" height="268" alt="archive-created" src="https://github.com/user-attachments/assets/581633a2-09d7-47be-ab2b-8e3fcd2cf3cf" />

---

## 4️⃣ Upload to Amazon S3

Successful upload to the S3 bucket.

<img width="1045" height="404" alt="uploaded2s3" src="https://github.com/user-attachments/assets/cea66465-b7dc-4cd4-bdea-a74980539097" />

---

## 5️⃣ S3 Bucket Contents

Archived ZIP files stored in S3.

<img width="1221" height="857" alt="logs-in-s3" src="https://github.com/user-attachments/assets/4cc89ec2-03b5-493f-ab1c-4bbd061bc112" />

---

## 6️⃣ Lifecycle Policy

Objects automatically transition to Glacier.

<img width="910" height="793" alt="glacier" src="https://github.com/user-attachments/assets/e852f524-9b90-422c-9aa3-1e6dc22b17d9" />

---

## 7️⃣ Cron Job

Automation configured using Linux Cron.

<img width="925" height="206" alt="crontab-l" src="https://github.com/user-attachments/assets/52642459-645f-43b5-a211-c221910f31c0" />

---

## 8️⃣ Upload Log

Operational logs showing successful executions.

<img width="1045" height="404" alt="uploaded2s3" src="https://github.com/user-attachments/assets/2985e5a7-7d51-474d-90f1-55f7f0c7256f" />

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
