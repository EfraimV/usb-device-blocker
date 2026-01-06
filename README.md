# 🔐 USB Device Blocker (Linux)

**USB Device Blocker** is a lightweight Linux utility that helps enforce USB device control by automatically blocking any connected USB devices that are not explicitly allowed.

It is built on top of [`usbguard`](https://usbguard.github.io/) and is intended for security labs, home servers, and workstations where strict control over USB peripherals is required.

---

## 🎯 Who This Tool Is For

This project is useful for:
- Security and networking enthusiasts running Linux labs
- System administrators managing shared or sensitive machines
- Anyone who wants to prevent unauthorized USB devices from being used on a Linux system

No deep security background is required — basic Linux familiarity is enough.

---

## 🚨 Why This Exists

USB devices are a common attack vector. In lab or semi-production environments, it’s easy to forget that *any* USB device can be plugged in and accessed by the system.

This tool provides a simple safeguard:
- **Known devices** continue to work
- **Unknown devices** are automatically blocked
- All actions are logged for later review

---

## 🛠 How It Works (High-Level)

1. The script periodically checks currently connected USB devices.
2. Each device is identified by its **Vendor ID and Product ID**.
3. Devices that match the whitelist are allowed.
4. All other devices are blocked via `usbguard`.
5. Every block event is written to a log file for auditing.

This approach keeps the logic simple while relying on `usbguard` for enforcement.

---

## ✨ Features

- Allow USB devices using a Vendor:Product ID whitelist (e.g. `0781:5567`)
- Automatically block all unauthorized USB devices
- Log block events to `/var/log/usbblocker.log`
- Run continuously in the background
- Designed to be easily extended with alerts or integrations

---

## 📦 Requirements

- Linux system
- Python 3.6+
- `usbguard`

### Install dependencies

sudo apt update
sudo apt install usbguard python3

'''
⚙️ Configuration

Before running the script, define the list of allowed USB devices by their Vendor and Product IDs.

Example:

ALLOWED_DEVICES = [
    "0781:5567",  # SanDisk USB drive
    "046d:c534",  # Logitech USB receiver
]


You can find a device’s Vendor and Product ID using:

lsusb

▶️ Running the Script

Once configured, run the script with sufficient privileges:

sudo python3 usb_device_blocker.py


The script will:

Run in the background

Continuously monitor USB connections

Block unauthorized devices automatically

🧾 Logging & Auditing

All blocked devices are logged to:

/var/log/usbblocker.log


Each log entry includes:

Timestamp

Vendor ID

Product ID

Action taken

This makes it easy to review USB activity over time.

⚠️ Limitations & Notes

This tool is designed for Linux only

It relies on usbguard being correctly installed and running

It is not a replacement for full endpoint protection or enterprise device control solutions

🔧 Extending the Tool

The script is intentionally simple and can be extended to:

Send Telegram or email alerts when a device is blocked

Integrate with SIEM or logging pipelines

Adjust polling intervals or enforcement logic

📚 Learning Notes

This project was built as part of my ongoing learning in Linux security, system automation, and documentation-as-code practices.

📜 License

MIT
sudo apt update
sudo apt install usbguard python3
