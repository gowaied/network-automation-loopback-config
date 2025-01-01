# network-automation-loopback-config
Python script for automating loopback configuration on Cisco devices using Netmiko

# Network Automation - Loopback Configuration

This Python script automates the configuration of loopback interfaces on Cisco devices using the Netmiko library. It includes  error handling for authentication failures, unreachable devices, and other exceptions.

## Features
- Validates input for IP addresses, loopback IDs, and credentials.
- Configures loopback interfaces with specified IP addresses and IDs.
- Verifies the configuration using the `show ip interface brief` command.
- Handles authentication errors and unreachable hosts gracefully.

## Requirements
- Python 3.x
- Netmiko library
- Cisco IOS devices

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/network-automation-loopback-config-v2.git

