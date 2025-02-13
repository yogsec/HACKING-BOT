#!/bin/bash

# Update package lists
sudo apt update -y

# Install Reconnaissance Tools
sudo apt install -y subfinder amass
GO111MODULE=on go install github.com/tomnomnom/httprobe@latest

# Install Port Scanning Tools
sudo apt install -y nmap masscan

# Install Web Scanning Tools
sudo apt install -y nikto whatweb wafw00f

# Install Directory and File Enumeration Tools
sudo apt install -y gobuster
cargo install feroxbuster

# Install Vulnerability Scanning Tools
sudo apt install -y sqlmap
GO111MODULE=on go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest

# Install Exploitation Tools
git clone https://github.com/s0md3v/XSStrike.git && cd XSStrike && pip install -r requirements.txt
GO111MODULE=on go install github.com/ffuf/ffuf@latest

# Install Post-Exploitation Analysis Tools
GO111MODULE=on go install github.com/tomnomnom/waybackurls@latest
GO111MODULE=on go install github.com/tomnomnom/gf@latest

# Refresh shell environment
source ~/.bashrc

echo "All tools installed successfully!"
