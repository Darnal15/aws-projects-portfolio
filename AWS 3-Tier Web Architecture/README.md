# AWS 3-Tier Web Architecture

A production-style 3-tier web application deployed on AWS using **Amazon VPC, EC2, Nginx, Flask, and Amazon RDS**.

The project demonstrates secure communication between application tiers using private networking, Security Groups, NAT Gateway, and a reverse proxy.

---

# Architecture

<img width="1536" height="1024" alt="3tierArch" src="https://github.com/user-attachments/assets/37583160-21fa-48a1-b592-528b0e9943a5" />

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

<img width="1491" height="802" alt="3tier-VPC" src="https://github.com/user-attachments/assets/2fa7d9af-9c62-45cf-bfc9-ede993a639a8" />

---

## Web EC2 Instance

<img width="1212" height="783" alt="webec2" src="https://github.com/user-attachments/assets/32065253-8695-42b6-9801-5942414a93c7" />

---

## Application EC2

<img width="1212" height="783" alt="app-ec2" src="https://github.com/user-attachments/assets/0b2f918b-1382-43aa-af30-0166865aa4ad" />

---

## Amazon RDS

<img width="1830" height="879" alt="mSQL-DB" src="https://github.com/user-attachments/assets/3891fc82-042f-4bc1-b410-bfd463175d56" />

---

## Nginx Reverse Proxy

<img width="1677" height="934" alt="weblayer_nginx" src="https://github.com/user-attachments/assets/01662395-f9e2-46f7-b2e8-9f5bf44d5eb5" />

---

## Final Browser Output

<img width="1855" height="722" alt="final-nginx-app" src="https://github.com/user-attachments/assets/34b78fb7-7c1c-484b-9cf8-900636a4638e" />


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
