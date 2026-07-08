# Python TCP Port Scanner

A lightweight TCP port scanner built from scratch in Python, developed as part of my 
home lab practice on Metasploitable 2. The goal was to understand what tools like Nmap 
actually do under the hood before relying on them.

## How It Works

The scanner creates a TCP socket for each port in the range 1-1024 and attempts a 
connection using connect_ex(), which returns 0 if the port is open and a non-zero value 
if closed. A one second timeout is set per port to handle unresponsive hosts, and each 
socket is closed after the attempt to free system resources.

## Usage
```bash
python3 portscanner.py
```

## Results Against Metasploitable 2 (192.168.56.101)

**Port 21 — FTP** — vsftpd, known vulnerable version  
**Port 22 — SSH** — Secure remote access  
**Port 23 — Telnet** — Plaintext credentials, no encryption  
**Port 25 — SMTP** — Mail transfer  
**Port 53 — DNS** — Domain resolution  
**Port 80 — HTTP** — Web server  
**Port 111 — RPC** — Remote procedure calls  
**Port 139/445 — Samba/SMB** — Historically critical attack surface  
**Port 512/513/514 — R-Services** — Legacy Unix remote execution, no authentication  

## What I Learned

Building this scanner made the TCP handshake click in a way that reading about it never 
did. Every tool in a pentester's arsenal is just an automated version of a concept you 
should be able to reproduce manually. Telnet appearing on port 23 is an immediate red 
flag on any real engagement — credentials travel in plaintext, making interception 
trivial. The SMB ports at 139 and 445 stood out as well, given their history as some of 
the most exploited services in network pentesting.
