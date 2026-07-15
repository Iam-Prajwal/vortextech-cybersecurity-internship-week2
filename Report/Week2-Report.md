# Week 2 Report — Vortex Tech Cyber Security Internship

## Introduction

Week 2 of the Cyber Security Internship focused on two complementary skill areas: building a piece of defensive security tooling from scratch, and performing hands-on network reconnaissance using industry-standard tools. The objective was to move beyond theory and produce working, testable artifacts — a Python program that actively helps users choose safer passwords, and a documented Nmap assessment of real (authorized) network targets — while practicing the habits of a working security professional: authorization awareness, evidence-based reporting, and clear remediation guidance.

This document serves as the central navigation page for the Week 2 submission. Full implementation details, algorithms, and raw findings are intentionally kept in their respective component reports rather than repeated here.

## Assignment Summary

**Password Strength Checker**
A command-line Python tool was built to evaluate passwords against length requirements, character-type variety (uppercase, lowercase, digits, special symbols), and a blacklist of common/leaked passwords. Rather than a simple pass/fail result, the tool produces a five-tier strength rating with a transparent score and specific, personalized feedback explaining what to improve.

**Nmap Port Scan**
Two authorized network scans were performed: a service and OS-detection scan against a personal localhost machine, and a network sweep across a personal home network. The exercise involved identifying live hosts, open and closed ports, associated services, and documenting the security implications of what was found — along with practical recommendations to reduce exposure.

## Project Components

- [`password_checker_report.md`](./Password_Checker_Report.md) — full design, algorithm, and discussion of the password strength checker
- [`nmap_report.md`](./Nmap_Report.md) — complete scan commands, output, findings, and recommendations from the network reconnaissance exercise
- [`sample_outputs.md`](./sample_outputs.md) — real, reproducible terminal output from 8 test passwords covering all strength tiers

## Screenshots

**Password Strength Checker**

[Password Tests](../screenshots/image.png)

**Nmap Scans**

[Localhost Scan](../screenshots/image-2.png)
[Network Scan](../screenshots/image-1.png)

## Key Learning Outcomes

- Translating password security theory (entropy, complexity, blacklisting) into working, modular code
- Recognizing that character-complexity rules alone do not guarantee a strong password without blacklist checks
- Designing feedback systems that guide users toward better security decisions rather than simply rejecting weak input
- Practicing authorized, scoped network reconnaissance using Nmap
- Mapping open ports to real services and reasoning about the risk each exposed service introduces
- Distinguishing between necessary and unnecessary network exposure as a core attack-surface-reduction principle
- Writing security findings and recommendations in a clear, professional, evidence-based format

## Reflection

Working on these two exercises side by side made the connection between password security and network security more concrete than either topic would have been on its own. A password checker is, at its core, about reducing the odds that a single compromised credential leads to account takeover. A network scan is about understanding — from an attacker's perspective — which doors into a system are actually open, and whether they need to be. Both exercises are really asking the same underlying question: *what is exposed, and does it need to be?*

The Nmap scan reinforced this directly. Most devices on the home network had no open ports at all, while the router exposed only SSH and HTTPS — services that were actually needed for management. That is attack surface reduction in practice: not "lock everything down blindly," but "only expose what serves a real purpose, and secure whatever you do expose." The password checker mirrors that same philosophy on the credential side — a strong password reduces the odds that an otherwise well-secured system gets bypassed simply because a login was easy to guess.

This week also reinforced the importance of secure system administration as an ongoing discipline rather than a one-time setup task. Services get added and forgotten, default credentials get left in place, and firmware goes unpatched — not usually out of carelessness, but because there's no built-in prompt reminding administrators to check. Both the password checker's feedback loop and the practice of periodic Nmap scanning serve that same role: creating a repeatable habit of checking assumptions instead of trusting that "it was secure when we set it up" still holds true.

## Conclusion

Week 2 combined defensive tool-building with hands-on reconnaissance to reinforce a core security principle: minimizing and securing every point of exposure, whether that exposure is a weak password or an unnecessarily open network port. The password strength checker demonstrates how thoughtful, rule-based logic can meaningfully guide users toward safer credentials, while the Nmap assessment demonstrated how straightforward, authorized reconnaissance can reveal exactly what a network exposes to the outside world. Together, these exercises provided a practical foundation in both secure software design and network security assessment — two skill sets that this internship continues to build toward a more complete, applied understanding of cybersecurity.
