# AWS 3-Tier Web Application

## Overview

Designed and deployed a classic AWS 3-tier web architecture consisting of:

- Web Tier (Nginx)
- Application Tier (Flask)
- Database Tier (Amazon RDS)

The architecture follows AWS networking best practices using public and private subnets.

---

## Architecture

![Architecture](<img width="1536" height="1024" alt="3tierArch" src="https://github.com/user-attachments/assets/17cf1680-41c9-4cea-9213-c33eec25553d" />)

---

## Services Used

- Amazon VPC
- Public & Private Subnets
- Internet Gateway
- NAT Gateway
- EC2
- Security Groups
- Amazon RDS (MySQL)
- Nginx
- Flask

---

## Architecture Flow

Internet

↓

Public EC2 (Nginx Reverse Proxy)

↓

Private EC2 (Flask Application)

↓

Amazon RDS

---

## Features

- Bastion-style SSH access
- Reverse proxy using Nginx
- Flask application hosted in private subnet
- Database hosted in RDS
- Secure Security Group communication
- Private subnet internet access using NAT Gateway

---

## Challenges Solved

- SSH Agent Forwarding
- Security Group communication
- Nginx Reverse Proxy configuration
- 504 Bad Gateway troubleshooting
- Private subnet connectivity
- NAT Gateway routing

---

## Screenshots

See the `screenshots` folder.

---

## Skills Demonstrated

- AWS Networking
- EC2
- Linux Administration
- Nginx
- Flask
- SSH
- RDS
- Troubleshooting
