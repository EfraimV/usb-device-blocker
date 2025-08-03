# usb-device-blocker
Made by a network/security enthusiast learning to bridge infrastructure and automation.

# 🔐 USB Device Blocker

A lightweight Python script that monitors connected USB devices and blocks any that are not explicitly allowed. Built on top of [`usbguard`](https://usbguard.github.io/), this tool helps enforce USB device control for Linux systems — useful in security labs, home networks, or workstations.

---

## 🛠 Features

- Whitelist known USB devices by Vendor:Product ID (e.g. `0781:5567`)
- Automatically blocks all unauthorized USB devices
- Logs each block event to `/var/log/usbblocker.log`
- Runs in the background every few seconds
- Easily extendable (e.g. send Telegram/email alerts)

---

## 📦 Requirements

- Python 3.6+
- `usbguard`

Install dependencies:

```bash
sudo apt update
sudo apt install usbguard python3

