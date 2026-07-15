# Vortex Tech Cyber Security Internship — Week 2
### Password Strength Checker & Network Port Scanning

A two-part cybersecurity project combining a Python-based password strength analyzer with hands-on Nmap network reconnaissance, completed as the Week 2 deliverable for the Vortex Tech Cyber Security Internship.

---

## Project Overview

This repository documents two applied security exercises:

1. **Password Strength Checker** — a modular Python CLI tool that scores passwords against length, character-variety, and common-password blacklist criteria, returning a five-tier strength rating with personalized feedback.
2. **Nmap Port Scanning** — a hands-on network reconnaissance exercise performed against a localhost machine and a personal home network, documenting open/closed ports, running services, and their associated security implications.

Both components were built to reinforce practical, applied security skills — writing defensive tooling on one side, and performing reconnaissance/enumeration on the other — which together mirror the two sides of real-world security work.

---

## Features

- Rule-based password evaluator with a transparent 0–6 scoring system
- Five-tier strength classification: Very Weak, Weak, Medium, Strong, Very Strong
- Common-password blacklist detection that overrides complexity scoring
- Personalized, human-readable improvement feedback for every result
- Password masking in terminal output for safe demonstration/sharing
- Real, reproducible sample output captured from 8 test passwords (no fabricated results)
- Authorized Nmap scans of a localhost machine and a personal home network
- Documented open ports, service identification, and security implications
- Actionable, prioritized remediation recommendations

---

## Repository Structure

```
vortextech-cybersecurity-internship-week2/
│
├── password_checker.py
├── run_tests.py
├── README.md
│
├── report/
│   ├── Week2-Report.md
│   ├── Week2-Report.pdf
│   ├── Password_Checker_Report.md
│   ├── Nmap_Report.md
│   └── sample_outputs.md
│
├── screenshots/
│   ├── image-1.png
│   ├── image-2.png
│   └── image.png
```

---

## Requirements

- **Python:** 3.8 or higher (standard library only — no external dependencies)
- **Nmap:** Installed and available on the system PATH ([nmap.org](https://nmap.org/download.html))
- **Operating System:** Cross-platform — tested on Linux; compatible with macOS and Windows (WSL recommended for Nmap OS-detection features)

---

## Installation

```bash
# Clone the repository
git clone https://github.com/Iam-Prajwal/vortextech-cybersecurity-internship-week2.git

# Navigate into the project folder
cd vortextech-cybersecurity-internship-week2
```

No package installation is required for the password checker. To run the Nmap portion yourself, ensure Nmap is installed:

```bash
# Debian/Ubuntu
sudo apt install nmap

# macOS (Homebrew)
brew install nmap
```

---

## Usage

### Running the Password Strength Checker

```bash
python3 password_checker.py
```

You will be prompted to enter a password. The tool returns a strength rating, numeric score, and personalized feedback in the terminal.

### How the Nmap Scan Was Performed

Two scans were conducted, both against systems owned by the author:

```bash
# Localhost service/OS detection scan
sudo nmap -sV -O localhost

# Home network sweep
nmap 192.168.1.69/24
```

Full commands, raw output, and analysis are documented in [`report/nmap_report.md`](./report/nmap_report.md).

---

## Screenshots

**Password Strength Checker**

![Password Tests](./screenshots/image.png)

**Nmap Scans**

![Localhost Scan](./screenshots/image-2.png)
![Network Scan](./screenshots/image-1.png)

---

## Documentation

Detailed write-ups for each component are available in the `report/` directory:

- [Week2-Report.md](./report/Week2-Report.md) — high-level project summary and navigation page
- [password_checker_report.md](./report/password_checker_report.md) — full algorithm, design, and discussion for the password checker
- [nmap_report.md](./report/nmap_report.md) — complete Nmap scan documentation, findings, and recommendations
- [sample_outputs.md](./report/sample_outputs.md) — real, reproducible terminal output across 8 test passwords

---

## Learning Outcomes

Through this project, the following skills and concepts were applied:

- Designing modular, testable Python code following PEP 8 conventions
- Translating password security best practices (length, entropy, blacklisting) into working logic
- Understanding why complexity rules alone are insufficient without blacklist checks
- Performing authorized network reconnaissance using Nmap
- Interpreting open/closed port states and mapping them to running services
- Assessing security implications of exposed services (SSH, HTTPS, and unidentified services)
- Writing clear, evidence-based security recommendations for remediation
- Structuring a project for professional presentation as an open-source security portfolio piece

---

## Author

**Prajwal Sah**

---

## Disclaimer

All network scans documented in this repository were performed exclusively against systems owned by the author (a personal localhost machine and a personal home network). No third-party systems, networks, or unauthorized targets were scanned at any point. This project is intended for educational and portfolio purposes only.
