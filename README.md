# Port Scanner

A multithreaded Python-based port scanner to detect open ports on a given target host. The script scans a range of ports (default 1–1000) and identifies the associated service where possible.

## Features

- **Multithreading**: Speeds up scanning by concurrently scanning multiple ports.
- **Hostname Resolution**: Supports resolving target domains to IP addresses.
- **Service Identification**: Detects the service name running on the open ports (where available).
- **Custom Input**: Prompts the user for a target hostname or IP address.

## Requirements

- Python 3.x
- Basic understanding of TCP and ports.

## How to Run

1. Clone or download this repository:
   ```bash
   git clone https://github.com/jaiswar-yash/port-scanner.git
   cd port-scanner
2. Run the script:
   ```bash
   python3 port_scanner.py
3. Enter the target hostname or IP address when prompted.<br>
   Example input:
   ```bash
   Enter the target: google.com
4. The output will display open ports and their associated services:
   ```bash
   Starting scan of the host: 142.250.192.142
   Port 80: OPEN (http)
   Port 443: OPEN (https)
   Time taken:  7.315438508987427
