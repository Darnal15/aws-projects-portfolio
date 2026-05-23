# Launching VPC Resources — Public & Private EC2 Instances

## Overview
Deployed two EC2 instances inside a custom AWS VPC — one in a 
public subnet and one in a private subnet. Demonstrated network 
isolation by proving the private server is only reachable through 
the public server (Bastion Host pattern), and not directly from 
the internet.

---

## Architecture
Internet
↓
Internet Gateway
↓
Public Route Table
↓
Public Subnet (172.16.0.0/24)
└── Public Server (172.16.12.17)
↓ SSH only
Private Subnet (172.16.128.0/24)
└── Private Server (172.16.135.82)


---

## Services Used
- Amazon VPC
- Amazon EC2
- Internet Gateway
- Route Tables
- Security Groups
- Network ACLs

---

## Objectives Completed

| Objective | Status |
|---|---|
| Create custom VPC with CIDR 172.16.0.0/16 | ✅ |
| Create public and private subnets | ✅ |
| Configure Internet Gateway and route tables | ✅ |
| Launch EC2 in public subnet | ✅ |
| Launch EC2 in private subnet | ✅ |
| SSH into public server from internet | ✅ |
| SSH into private server via public server (bastion) | ✅ |
| Prove private server unreachable from internet | ✅ |
| Prove private server has no internet access | ✅ |

---

## Step by Step Process

### 1. Created VPC Using Wizard
- Used VPC and more wizard for fast setup
- CIDR: 172.16.0.0/16
- 1 public subnet, 1 private subnet
- No NAT Gateway (cost saving)
- Enabled DNS hostnames and DNS resolution

### 2. Created Security Groups

**public-sg:**
| Type | Port | Source |
|---|---|---|
| SSH | 22 | My IP |
| HTTP | 80 | 0.0.0.0/0 |

**private-sg:**
| Type | Port | Source |
|---|---|---|
| SSH | 22 | public-sg only |
| All ICMP | All | public-sg only |

Private security group only accepts traffic from public-sg —
not from the internet directly.

### 3. Launched EC2 Instances

**public-server:**
- Subnet: public subnet
- Auto-assign public IP: Enabled
- Security group: public-sg

**private-server:**
- Subnet: private subnet
- Auto-assign public IP: Disabled
- Security group: private-sg

### 4. Tested Connectivity

**Test 1 — SSH to public server:**
```bash
ssh -i lock.pem ec2-user@3.6.90.237
# Result: Connected successfully ✅
```

**Test 2 — Internet access from public server:**
```bash
ping google.com
# Result: 0% packet loss ✅
```

**Test 3 — SSH from public to private (Bastion hop):**
```bash
# From inside public server:
ssh -i lock.pem ec2-user@172.16.135.82
# Result: Connected successfully ✅
```

**Test 4 — Direct SSH to private from internet:**
```bash
ssh -i lock.pem ec2-user@172.16.135.82
# Result: Connection timed out ✅ (expected)
```

**Test 5 — Internet access from private server:**
```bash
ping google.com
# Result: Request timeout ✅ (expected)
```

---

## Results

| Test | Expected | Result |
|---|---|---|
| SSH to public server | ✅ Works | ✅ Connected |
| Ping internet from public | ✅ Works | ✅ 0% packet loss |
| SSH public → private (bastion) | ✅ Works | ✅ Connected |
| Direct SSH to private from internet | ❌ Blocked | ❌ Timed out |
| Ping internet from private | ❌ Blocked | ❌ Timed out |

Tests 4 and 5 failing is the intended result — 
proving the private subnet is completely isolated.

---

## Key Concepts Demonstrated

**Bastion Host Pattern**
The public server acts as a jump server — the only way 
to reach the private server is by SSHing into the public 
server first, then hopping to the private server. This is 
the standard pattern used in production AWS environments.

**Security Group Chaining**
private-sg only allows SSH from public-sg — not from 
0.0.0.0/0. This means even if someone knew the private 
IP, they could not connect without going through the 
public server first.

**Public vs Private Subnet**
- Public subnet has a route to IGW → internet accessible
- Private subnet has no IGW route → completely isolated

---

## Screenshots
![EC2 Instances](<img width="773" height="218" alt="ec2s" src="https://github.com/user-attachments/assets/9b4a96e0-73e4-49fc-94cf-def8dd97adfb" />
.png)
![VPC Subnets](<img width="779" height="236" alt="subnets" src="https://github.com/user-attachments/assets/e6328263-9de1-40e7-93ac-46968c62fc0e" />
.png)
![Route Table](<img width="768" height="218" alt="route table" src="https://github.com/user-attachments/assets/0dc536b0-a01a-470a-8bd7-4392002085e7" />
.png)
![SSH Public Server](<img width="950" height="418" alt="public server" src="https://github.com/user-attachments/assets/67c53578-c156-4f45-b3d9-6f1c7c413efc" />
.png)
![Private Blocked](<img width="473" height="286" alt="private server" src="https://github.com/user-attachments/assets/94ff7150-edf8-4f7f-89e6-09d36154db92" />
.png)

---

## Key Learnings
- Port 22 (SSH) is commonly blocked on college/office WiFi
  — always use mobile hotspot for SSH in AWS
- Private subnet isolation is proved by connection timeout
  not just absence of public IP
- Security group chaining is more secure than IP-based rules
- VPC Wizard creates all networking resources automatically
  saving significant setup time
- DNS hostnames must be enabled on custom VPCs for 
  EC2 Instance Connect to work

---
