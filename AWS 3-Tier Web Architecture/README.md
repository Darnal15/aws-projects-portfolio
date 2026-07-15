# AWS 3-Tier Web Architecture

## Project Overview

This project demonstrates the deployment of a **production-style 3-tier web application** on AWS using secure networking principles.

The architecture separates the application into three layers:

- **Presentation Tier** – Nginx running on an EC2 instance in a Public Subnet
- **Application Tier** – Flask application running on an EC2 instance in a Private Subnet
- **Database Tier** – Amazon RDS MySQL deployed in Private Database Subnets

The application securely communicates between each tier while following AWS networking best practices.

---

# Architecture Diagram

<img width="1536" height="1024" alt="3tier-main-arch" src="https://github.com/user-attachments/assets/99d566ec-8f31-46f0-a09e-9709e6557782" />

---

# AWS Services Used

- Amazon VPC
- Amazon EC2
- Amazon RDS (MySQL)
- Internet Gateway
- NAT Gateway
- Route Tables
- Security Groups
- Nginx
- Flask
- PyMySQL

---

# Architecture

- 1 VPC
- 2 Availability Zones
- 2 Public Subnets
- 2 Private Application Subnets
- 2 Private Database Subnets
- 1 Internet Gateway
- 1 NAT Gateway
- 1 Web EC2
- 1 App EC2
- Amazon RDS (Multi-AZ)

---

# Request Flow

```text
User
 │
 ▼
Internet
 │
 ▼
Internet Gateway
 │
 ▼
Web EC2 (Nginx)
 │
 ▼
App EC2 (Flask)
 │
 ▼
Amazon RDS (MySQL)
 │
 ▼
SQL Query
 │
 ▼
Response
```

---

# Project Structure

```text
AWS 3-Tier Web Architecture
│
├── README.md
├── app.py
├── requirements.txt
├── config
│   └── flask.conf
├── diagrams
│   └── aws-3tier-architecture.png
└── screenshots
```

---

# Deployment Steps

### 1. Create Networking

- Create VPC
- Create Public and Private Subnets
- Attach Internet Gateway
- Create NAT Gateway
- Configure Route Tables

---

### 2. Launch Infrastructure

- Launch Web EC2
- Launch App EC2
- Launch Amazon RDS
- Configure Security Groups

---

### 3. Configure Web Tier

- Install Nginx
- Configure Reverse Proxy
- Start Nginx

---

### 4. Configure Application Tier

- Install Python
- Create Virtual Environment
- Install Flask
- Install PyMySQL
- Deploy Flask Application

---

### 5.Configure Database

- Create Amazon RDS
- Allow MySQL traffic from App EC2 Security Group
- Connect Flask to MySQL

---

# Screenshots

## VPC

<img width="1543" height="740" alt="vpc-new" src="https://github.com/user-attachments/assets/b65c15c4-6c3a-4a74-80ff-f9f51aff90e0" />

---

## Subnets

<img width="1611" height="417" alt="02-subnets" src="https://github.com/user-attachments/assets/97ca9270-5477-478f-8c54-afe36023057d" />

---

## Route Tables

<img width="1611" height="417" alt="route-tables" src="https://github.com/user-attachments/assets/8a19e459-8af3-4227-8a18-36641f35518b" />

---

## Security Groups

<img width="1611" height="417" alt="sec-gs" src="https://github.com/user-attachments/assets/ace72e3c-e3ef-4330-92ee-648fdb6266ce" />

---

## Amazon RDS

<img width="1827" height="874" alt="mySQL-db" src="https://github.com/user-attachments/assets/faee9b6b-43ac-4d7f-87d0-96aa3240dfdb" />

---

## Flask Running

<img width="917" height="512" alt="flas-running-web2" src="https://github.com/user-attachments/assets/76584fd2-7e25-4be7-8d6c-4cb3edfe4a30" />

---

## Nginx Reverse Proxy

<img width="1823" height="834" alt="web-to-app-connectivity png" src="https://github.com/user-attachments/assets/69c2de19-b089-47e3-85fa-8d71f6135bd7" />

---

## Database Connectivity

<img width="951" height="799" alt="flask-rds-connect" src="https://github.com/user-attachments/assets/be348cbf-9f34-4139-83ad-8e944408e621" />

---

## Final Output

<img width="1823" height="1030" alt="final-3-tier" src="https://github.com/user-attachments/assets/b6fe043d-6f46-46b5-aa53-99e715e17c6c" />

---

# 📈 Skills Demonstrated

- AWS Networking
- VPC Design
- Public & Private Subnets
- Route Tables
- Security Groups
- NAT Gateway
- Internet Gateway
- EC2 Administration
- Nginx Reverse Proxy
- Python Flask
- Amazon RDS
- MySQL Connectivity
- Linux Administration
- SSH Agent Forwarding
- Troubleshooting Multi-Tier Architectures

---

# Author

**Abhishek (Darnal15)**

AWS | DevOps | Cloud Enthusiast
