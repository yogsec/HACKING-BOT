# HACKING BOT | Designed by YogSec 🚀

HACKING BOT is an **automated bug bounty tool** that streamlines security testing by running multiple cybersecurity tools in parallel. It allows you to customize the tools list and automate reconnaissance, scanning, exploitation, and post-exploitation analysis.

![HACKING BOT](https://github.com/yogsec/HACKING-BOT/blob/main/Screenshot%20from%202025-02-13%2017-16-44.png?raw=true)

---

## 🎯 Features
✅ **Automated Bug Bounty Process** – Scans, exploits, and gathers information with just one command.  
✅ **Concurrent Execution** – Runs multiple tools in parallel to save time.  
✅ **Customizable Tools List** – Modify `tools-list.txt` or provide your own list.  
✅ **Automatic Tool Detection** – Skips missing tools instead of terminating.  
✅ **Supports Multiple Cybersecurity Tools** – Nmap, Nikto, SQLMap, and more.  
✅ **Help and Version Options** – Easily check usage details and version info.  

---

## 📂 Files Description

### `bug_bounty.py` (Main Script)
- Runs bug bounty tools based on the tools list.
- Accepts domain input and custom tools file.
- Checks for missing tools and skips them.
- Executes commands concurrently.

### `tools-list.txt` (Default Tools Configuration)
- Contains a list of security tools and their commands.
- Can be modified to add or remove tools.

### `install_tools.sh` (Installation Script)
- Installs all required bug bounty tools.
- Supports package managers like `apt`, `go`, and `pip`.

---

## 🛠 Installation

### 🔹 Step 1: Clone the Repository
```bash
git clone https://github.com/YogSec/HACKING_BOT.git
cd HACKING-BOT
```

### 🔹 Step 2: Install Dependencies
```bash
pip install termcolor
chmod +x install_tools.sh
./install_tools.sh
```

### 🔹 Step 3: Run the Tool
```bash
python main.py -d example.com
```

---

## ⚙️ Usage

### 🏷 Basic Usage
```bash
python main.py -d <domain>
```
Example:
```bash
python main.py -d google.com
```

### 🔹 Advanced Options
| Option | Description |
|--------|-------------|
| `-h` | Show help menu |
| `-v` | Show version info |
| `-d <domain>` | Specify the target domain |
| `-c <file>` | Use a custom tools list file |

Example using a custom tools file:
```bash
python main.py -d example.com -c advanced-tools.txt
```

---

## 🔍 What This Tool Can Do
✅ **Reconnaissance** – Discover subdomains, live hosts, and information about the target.  
✅ **Port Scanning** – Identify open ports and services running on them.  
✅ **Web Scanning** – Detect security vulnerabilities in web applications.  
✅ **Directory & File Enumeration** – Find hidden files and directories.  
✅ **Vulnerability Scanning** – Identify SQLi, XSS, and other vulnerabilities.  
✅ **Exploitation & Post-Exploitation** – Run attacks and gather historical data.

---

## 📌 Example Tools List (`tools-list.txt`)
```
# Reconnaissance
subfinder -d (domain here) -o subdomains.txt
amass enum -d (domain here) -o amass_output.txt
cat subdomains.txt | httprobe > live_hosts.txt

# Port Scanning
nmap -p- -T4 -A -v (domain here) -oN nmap_scan.txt
```
Modify this file to add more tools!

---

## 🌟 Let's Connect!

Hello, Hacker! 👋 We'd love to stay connected with you. Reach out to us on any of these platforms and let's build something amazing together:

🌐 **Website:** [https://yogsec.github.io/yogsec/](https://yogsec.github.io/yogsec/)  
📜 **Linktree:** [https://linktr.ee/yogsec](https://linktr.ee/yogsec)  
🔗 **GitHub:** [https://github.com/yogsec](https://github.com/yogsec)  
💼 **LinkedIn (Company):** [https://www.linkedin.com/company/yogsec/](https://www.linkedin.com/company/yogsec/)  
📷 **Instagram:** [https://www.instagram.com/yogsec.io/](https://www.instagram.com/yogsec.io/)  
🐦 **Twitter (X):** [https://x.com/yogsec](https://x.com/yogsec)  
👨‍💼 **Personal LinkedIn:** [https://www.linkedin.com/in/bug-bounty-hunter/](https://www.linkedin.com/in/bug-bounty-hunter/)  
📧 **Email:** abhinavsingwal@gmail.com

---

## ☕ Buy Me a Coffee

If you find our work helpful and would like to support us, consider buying us a coffee. Your support keeps us motivated and helps us create more awesome content. ❤️

☕ **Support Us Here:** [https://buymeacoffee.com/yogsec](https://buymeacoffee.com/yogsec)

Thank you for your support! 🚀

---

## 🚀 Contribution & Support
Feel free to contribute by submitting pull requests or reporting issues! 😊

---

## ⚠️ Disclaimer
This tool is for educational and legal penetration testing purposes **only**. The author is not responsible for misuse.

---

💻 **Developed by YogSec** | 🚀 Stay Secure!

