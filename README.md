# Cybersecurity Lab – Kali Linux Network Asset Scanner

## Project Overview

This project demonstrates a basic cybersecurity laboratory environment using Kali Linux running inside VirtualBox. The project covers Linux system administration, networking fundamentals, system information gathering, network configuration, and development of a Python-based system information and network asset scanner.

## Objectives

- Set up Kali Linux in VirtualBox.
- Practice essential Linux commands.
- Understand basic networking concepts.
- Configure and test virtual networking.
- Collect system and network information.
- Develop a Python-based network asset and system information scanner.
- Document the laboratory architecture and networking models.
- Maintain project files and screenshots for demonstration.

## Lab Environment

- Host Platform: VirtualBox
- Operating System: Kali Linux
- Network Interface: eth0
- Network Mode: NAT
- Default Gateway: 10.0.2.2
- Programming Language: Python
- Python Version: 3.14.17

## Linux Commands Practiced

The following commands were practiced during the laboratory:

- pwd – displays the current working directory
- ls – lists files and directories
- mkdir – creates a directory
- whoami – displays the current user
- uname -a – displays system information
- date – displays the current date and time
- uptime – displays system uptime
- free -h – displays memory information
- df -h – displays disk usage
- ip a – displays network interfaces and IP addresses
- ip route – displays routing information
- cat /etc/resolv.conf – displays DNS configuration
- ping – tests network connectivity
- ss -tuln – displays listening network ports

## Network Testing

Network connectivity was tested using:

    ping -c 4 8.8.8.8

DNS connectivity was tested using:

    ping -c 4 google.com

Both tests successfully received responses during the laboratory session.

## Python Scanner

The project includes a Python script named `scanner.py`.

The scanner collects:

- Hostname
- Operating system
- OS release
- Kernel information
- System architecture
- Python version
- IP address
- Network interfaces
- Default gateway
- DNS configuration
- Listening TCP/UDP ports

### Run the Scanner

    python3 scanner.py

The output can also be saved to a file using:

    python3 scanner.py > scanner_output.txt

## Project Structure

    cyber_project/
    ├── scanner.py
    ├── scanner_output.txt
    ├── README.md
    └── screenshots/
        └── scanner_execution.png

## Screenshots

The screenshots folder contains evidence of the project execution, including the Python scanner execution.

## Networking Models

The project documentation includes diagrams of:

1. OSI Model
2. TCP/IP Model
3. Cybersecurity Lab Architecture

## Lab Architecture

The laboratory uses a Kali Linux virtual machine running inside VirtualBox. The Kali virtual machine uses the `eth0` network interface and NAT-based virtual networking to communicate with the external network.

## Result

The laboratory environment was successfully configured. Linux commands were practiced, network connectivity and DNS resolution were tested, and a Python-based system information and network asset scanner was successfully developed and executed.

## Conclusion

This project provided practical experience with Kali Linux, Linux command-line operations, networking fundamentals, virtual machine networking, and basic Python-based cybersecurity automation. The developed scanner demonstrates how system and network information can be collected and documented in a controlled laboratory environment.

# Task 2 – Reconnaissance, Information Gathering, Network Scanning & Enumeration

## Project Objective
The objective of Task 2 was to perform network reconnaissance, information gathering, network scanning and enumeration in an authorized lab environment. The project also included developing a Python-based network scanner and documenting the results.

## Tools Used
- Kali Linux
- Nmap
- Python 3
- Wireshark
- Netcat
- nslookup
- dig
- whois
- traceroute
- Linux networking commands

## Reconnaissance and Scanning Activities

### 1. Host Discovery
Nmap host discovery was performed using:
`nmap -sn 10.0.0.2`

This was used to check whether the authorized lab target was reachable and identify active hosts.

### 2. Port Scanning
A basic Nmap port scan was performed to identify available TCP ports:
`nmap 10.0.0.2`

### 3. Service and Version Detection
Service/version detection was performed using:
`nmap -sV 10.0.0.2`

### 4. OS Detection
OS detection was tested using:
`sudo nmap -O 10.0.0.2`

The results were documented with screenshots. Since the target did not expose sufficient open/closed ports, reliable OS identification was not possible.

### 5. DNS and Domain Information
The following tools were used for information gathering:
- `nslookup google.com`
- `dig google.com`
- `whois google.com`

### 6. Traceroute
Network path information was collected using:
`traceroute google.com`

### 7. Wireshark Packet Capture
Wireshark was used to capture network traffic on the `eth0` interface while generating traffic using ping. The packet capture was saved as a `.pcapng.gz` file.

### 8. Netcat
Netcat was used to test connectivity to the authorized lab target and observe the response from port 80.

### 9. Python Network Scanner
A Python network scanner was developed to check TCP ports and identify their status. The scanner was tested against the authorized lab target.

The scanner generated:
- CSV results
- JSON results
- HTML results

### 10. Documentation and Visualization
Network topology and reconnaissance workflow diagrams were created to explain the laboratory setup and the overall reconnaissance process.

## Project Outputs
The repository contains:
- Reconnaissance and scanning screenshots
- Network topology diagram
- Reconnaissance workflow diagram
- Wireshark packet capture
- Python scanner
- CSV, JSON and HTML scan results
- Task 1 and Task 2 documentation

## Ethical Consideration
All scanning and testing activities were performed only in an authorized laboratory environment for educational and cybersecurity learning purposes. The techniques demonstrated in this project should only be used on systems where explicit permission has been provided.

## Conclusion
Task 2 provided practical experience with reconnaissance, information gathering, network scanning, enumeration, packet analysis and Python-based network scanning. The project demonstrates the use of common cybersecurity tools in a controlled and authorized environment.
