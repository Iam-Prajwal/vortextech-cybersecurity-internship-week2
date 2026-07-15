# Nmap Scan Report

**Vortex Tech Cyber Security Internship — Week 2**

---

## Scan Command Used

### Localhost Scan

```bash
sudo nmap -sV -O localhost
```

**Target:** `localhost (127.0.0.1)`

**Date/Time of Scan:** `15 July 2026, 12:51 PM (NPT)`

**Authorization Note:**  
The scan was performed only on my own Linux machine (localhost), which I own and am fully authorized to test. No third-party systems or networks were scanned.

---

### Home Network Scan

```bash
nmap 192.168.1.69/24
```

**Target:** `My personal home network`

**Date/Time of Scan:** `15 July 2026, 12:54 PM (NPT)`

**Authorization Note:**  
This scan was conducted only on my own home network for educational purposes as part of the Vortex Tech Cyber Security Internship assignment. No unauthorized systems or third-party networks were scanned.

---

## Scan Output

### Localhost Scan

![Localhost Scan](./Screenshots/image-2.png)

### Home Network Scan

![Network Scan](./Screenshots/image-1.png)

---

## Open Ports

The network scan discovered several devices on my local network. Most devices had all scanned TCP ports closed, while my router exposed two commonly used management ports.

| Host | Port | State | Service | Version |
|------|------|-------|----------|---------|
| 192.168.1.64 | 6100/tcp | Open | synchronet-db | Not Detected |
| 192.168.1.254 | 22/tcp | Open | SSH | Not Detected |
| 192.168.1.254 | 443/tcp | Open | HTTPS | Not Detected |

The following ports were detected but found to be closed:

| Port | State | Service |
|------|-------|----------|
| 445 | Closed | Microsoft-DS |
| 631 | Closed | IPP |
| 49152 | Closed | Unknown |
| 49154 | Closed | Unknown |
| 49156 | Closed | Unknown |

---

## Common Services

### SSH (Port 22)

SSH (Secure Shell) is a secure protocol used for remote system administration. It encrypts communication between devices, allowing administrators to safely manage systems over a network.

### HTTPS (Port 443)

HTTPS (HyperText Transfer Protocol Secure) provides encrypted communication between web browsers and servers. In this case, it is likely used to securely access the router's web administration interface.

### Synchronet-db (Port 6100)

Port 6100 is commonly associated with the Synchronet database service or another application-specific service. Since version detection did not identify the exact software, further investigation would be required to determine its purpose.

### Microsoft-DS (Port 445)

Microsoft-DS supports SMB (Server Message Block) services for Windows file and printer sharing. During this scan, the port was closed, indicating that the service was not accepting incoming connections.

### IPP (Port 631)

IPP (Internet Printing Protocol) enables network printing services. Since the port was closed, no active printing service was available on the scanned host.

---

## Security Implications

- **SSH (Port 22):** SSH provides secure remote administration but can become a target for brute-force attacks if weak passwords or default credentials are used.

- **HTTPS (Port 443):** The router's management interface appears to be available through HTTPS. While encrypted communication improves security, administrators should use strong passwords, disable remote access if unnecessary, and keep firmware updated.

- **Synchronet-db (Port 6100):** Any unnecessary open service increases the attack surface. Unknown services should be identified and disabled if they are not required.

- **Closed Ports:** Most scanned ports were closed, reducing the system's exposure to unauthorized access and limiting potential attack vectors.

Overall, the scan indicates that only a small number of services are exposed, which is generally a good security practice.

---

## Recommendations

1. Use strong, unique passwords for router administration and SSH access.
2. Disable remote administration features if they are not required.
3. Keep router firmware and operating system software updated to protect against known vulnerabilities.
4. Restrict SSH access to trusted devices or internal networks whenever possible.
5. Disable unnecessary network services to minimize the attack surface.
6. Perform periodic network scans to monitor newly opened ports or unexpected services.
7. Use a firewall to restrict access to sensitive services from untrusted networks.

---

## Reflection

Conducting this Nmap scan helped me understand how security professionals identify active hosts and discover network services running on a system. I found it interesting that most devices on my network had no publicly accessible ports, while the router exposed only essential management services such as SSH and HTTPS. This exercise reinforced the idea that every open port represents a potential entry point and should therefore be intentionally configured, monitored, and secured. Overall, this practical activity strengthened my understanding of network reconnaissance and highlighted the importance of continuous security assessment in protecting systems from unauthorized access.
