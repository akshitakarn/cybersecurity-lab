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
