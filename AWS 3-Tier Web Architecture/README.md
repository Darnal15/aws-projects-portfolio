# AWS 3-Tier Web Architecture

A production-style 3-tier web application deployed on AWS using **Amazon VPC, EC2, Nginx, Flask, and Amazon RDS**.

The project demonstrates secure communication between application tiers using private networking, Security Groups, NAT Gateway, and a reverse proxy.

---

# Architecture

![Architecture](<img width="1536" height="1024" alt="3tierArch" src="https://github.com/user-attachments/assets/fc543629-406b-4f1e-aab9-af46499bd4d1" />
.png)

---

# Architecture Overview

```
                    Internet
                        │
                        ▼
               Internet Gateway (IGW)
                        │
        ┌──────────────────────────────────┐
        │            Public Subnet         │
        │                                  │
        │  Web EC2                         │
        │  Amazon Linux                    │
        │  Nginx Reverse Proxy             │
        └──────────────────────────────────┘
                        │
                Private IP Communication
                        │
        ┌──────────────────────────────────┐
        │           Private Subnet         │
        │                                  │
        │  App EC2                         │
        │  Flask Application               │
        └──────────────────────────────────┘
                        │
        ┌──────────────────────────────────┐
        │           Private Subnet         │
        │                                  │
        │  Amazon RDS (MySQL)              │
        └──────────────────────────────────┘
```

---

# AWS Services Used

- Amazon VPC
- Public & Private Subnets
- Internet Gateway
- NAT Gateway
- EC2
- Amazon RDS (MySQL)
- Security Groups
- Network ACLs
- Nginx
- Flask
- SSH Agent Forwarding

---

# Features

- Custom VPC
- Multi-AZ architecture
- Public and Private Subnets
- Bastion-style SSH access
- Reverse Proxy using Nginx
- Flask application hosted in Private EC2
- Amazon RDS Database
- NAT Gateway for outbound internet access
- Principle of Least Privilege using Security Groups

---

# Deployment Workflow

```
Browser
    │
    ▼
Public EC2 (Nginx)
    │
    ▼
Private EC2 (Flask)
    │
    ▼
Amazon RDS
```

---

# Security Architecture

### Web EC2

- Located inside Public Subnet
- Accepts HTTP traffic from Internet
- Accepts SSH only from my public IP
- Proxies requests to Application EC2

### Application EC2

- Located inside Private Subnet
- No Public IP
- Accessible only from Web EC2
- Flask listens on Port 5000

### Amazon RDS

- Private Database
- Accessible only from Application EC2
- MySQL Port 3306

---

# Challenges Faced

During the deployment several real-world issues were encountered and resolved:

- SSH connection timeout
- SSH Agent Forwarding configuration
- Security Group communication
- NAT Gateway routing
- Flask not listening on port 5000
- Nginx returning Welcome Page
- 504 Bad Gateway troubleshooting
- Private subnet connectivity
- RDS deployment limitations
- Reverse Proxy configuration

---

# Project Screenshots

## VPC Architecture

![](screenshots/01-vpc.png)

---

## Web EC2 Instance

![](screenshots/02-web-ec2.png)

---

## Application EC2

![](screenshots/03-app-ec2.png)

---

## Amazon RDS

![](screenshots/04-rds.png)

---

## Nginx Reverse Proxy

![](screenshots/05-nginx-success.png)

---

## Flask Application Response

![](screenshots/06-app-response.png)

---

## Final Browser Output

![](screenshots/07-browser-output.png)

---

# Skills Demonstrated

- AWS Networking
- Amazon EC2
- Amazon RDS
- Linux Administration
- Nginx
- Reverse Proxy
- Flask Deployment
- SSH Agent Forwarding
- Security Groups
- Network Troubleshooting
- Private Networking
- NAT Gateway
- VPC Design

---

# Project Outcome

Successfully deployed a secure **3-Tier Web Architecture** on AWS where:

- Users access the Web Tier through the Internet.
- Nginx forwards requests to the Application Tier.
- Flask communicates securely with Amazon RDS.
- All internal communication occurs through private networking.

This project demonstrates practical cloud infrastructure deployment following AWS networking best practices.
