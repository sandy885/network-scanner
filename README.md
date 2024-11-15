# network-scanner
Network Scanner is a simple yet powerful tool written in Python that allows users to discover devices connected to their local network. Utilizing the scapy library, this tool performs an ARP scan to identify active devices, displaying their IP addresses and MAC addresses in a user-friendly format. 
This is a Python script that scans a network for hosts using the scapy library. It sends ARP requests to all IP addresses in the specified range and captures the responses.

Requirements
Python 3.x

    Python 3.x
    Scapy library (install using pip install scapy)

Usage

    Clone the repository:

    bash

git clone https://github.com/sandy885/network-scanner.git

Navigate to the repository directory:

bash

cd network-scanner

Run the script:

bash

    python network_scanner.py

    Enter the network IP address (e.g., 192.168.1.0) and the number of hosts to scan.

Example

Enter the network IP address (e.g., 192.168.1.0): 192.168.1.0

Enter the number of hosts to scan: 254


Scanning network 192.168.1.0/24

Host found: 192.168.1.1 (MAC: 00:11:22:33:44:55)

Host found: 192.168.1.10 (MAC: AA:BB:CC:DD:EE:FF)

Host found: 192.168.1.11 (MAC: 11:22:33:44:55:66)

...
