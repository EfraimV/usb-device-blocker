#!/usr/bin/env python3

import subprocess
import time
import os

ALLOWED_IDS_FILE = "/etc/usbguard/allowed_usb.txt"
LOG_FILE = "/var/log/usbblocker.log"

def get_connected_usb_ids():
    result = subprocess.run(["usbguard", "list-devices"], capture_output=True, text=True)
    lines = result.stdout.strip().splitlines()
    device_ids = [line.split()[1] for line in lines if "present" in line]
    return device_ids

def load_allowed_ids():
    if not os.path.exists(ALLOWED_IDS_FILE):
        return []
    with open(ALLOWED_IDS_FILE) as f:
        return [line.strip() for line in f if line.strip()]

def block_device(device_id):
    subprocess.run(["usbguard", "block-device", device_id])
    with open(LOG_FILE, "a") as log:
        log.write(f"Blocked unknown USB device: {device_id}\n")
    print(f"[!] Blocked USB device: {device_id}")

def main():
    print("[+] Starting USBBlocker...")
    allowed = load_allowed_ids()
    while True:
        connected = get_connected_usb_ids()
        for dev_id in connected:
            if dev_id not in allowed:
                block_device(dev_id)
        time.sleep(5)

if __name__ == "__main__":
    main()
