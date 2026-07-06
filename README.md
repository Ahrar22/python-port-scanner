# Port Scanner

A simple port scanner tool that checks open ports on a target host within a given range.

## Features

- Scan a target IP or domain
- Custom port range support
- Fast TCP connection checking
- Simple CLI output
- Lightweight and easy to use

## How it works

The tool tries to establish a TCP connection to each port in the specified range.  
If the connection succeeds, the port is considered OPEN.

## Installation

```bash
git clone https://github.com/your-username/port-scanner.git
cd port-scanner
pip install -r requirements.txt
