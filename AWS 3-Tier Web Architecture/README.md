# AWS 3-Tier Web Architecture

A production-style 3-tier web application deployed on AWS using **Amazon VPC, EC2, Nginx, Flask, and Amazon RDS**.

The project demonstrates secure communication between application tiers using private networking, Security Groups, NAT Gateway, and a reverse proxy.

---

# Architecture

<img width="1536" height="1024" alt="3tierArch" src="https://github.com/user-attachments/assets/fc543629-406b-4f1e-aab9-af46499bd4d1" />

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

<img width="1491" height="802" alt="3tier-VPC" src="https://github.com/user-attachments/assets/4f3b8240-a081-4e69-9838-a98929d3bcf3" />

---

## Web EC2 Instance

<img width="1212" height="783" alt="webec2" src="https://github.com/user-attachments/assets/1a1f400e-a52f-48a5-9530-df7a369f219f" />

---

## Application EC2

<img width="1212" height="783" alt="app-ec2" src="https://github.com/user-attachments/assets/65b57734-bbde-4e57-93e0-ead374aed996" />

---

## Amazon RDS

<img width="1830" height="879" alt="mSQL-DB" src="https://github.com/user-attachments/assets/a29381ce-12bd-4e5d-bcb7-a0b09af2805f" />

---

## Nginx Reverse Proxy

<img width="1677" height="934" alt="weblayer_nginx" src="https://github.com/user-attachments/assets/d7f676d5-1c9d-4e3a-ab79-cf477a38fd59" />

<img width="1843" height="1070" alt="applayerr-privateSSH" src="https://github.com/user-attachments/assets/1a104234-a643-4ae1-bcf3-5d7e20c7fdb6" />

---

## Final Browser Output

<img width="1855" height="722" alt="final-nginx-app" src="https://github.com/user-attachments/assets/0310654c-c6da-448d-8ef2-40acd29e6a7f" />

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
