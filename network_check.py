import json
import os
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

INVENTORY_FILE = "inventory.json"
OUTPUT_FILE = "output.json"

def check_device_status(device):
    """
    Checks HTTPS/RESTCONF reachability for a device.
    """
    ip = device.get("ip")
    url = f"https://{ip}/restconf/data/ietf-interfaces:interfaces"
    
    try:
        response = requests.get(
            url,
            auth=("admin", "Cisco123!"),
            verify=False,
            timeout=3
        )
        if response.status_code == 200:
            return "UP"
        else:
            return "DOWN"
    except requests.exceptions.RequestException:
        return "DOWN"

def main():
    print("=" * 65)
    print("STARTING NETWORK AUTOMATION HEALTH CHECK")
    print("=" * 65)

    # 1. Read device information from inventory.json with error handling
    if not os.path.exists(INVENTORY_FILE):
        print(f"[ERROR] Inventory file '{INVENTORY_FILE}' not found!")
        return

    try:
        with open(INVENTORY_FILE, "r") as f:
            devices = json.load(f)
    except json.JSONDecodeError as err:
        print(f"[ERROR] Failed to parse {INVENTORY_FILE}: {err}")
        return
    except Exception as err:
        print(f"[ERROR] Unexpected error reading inventory: {err}")
        return

    results = []

    # 2. Check each device and determine status
    for device in devices:
        hostname = device.get("hostname", "Unknown")
        ip = device.get("ip", "N/A")
        
        print(f"Checking status for {hostname} ({ip})...", end=" ", flush=True)
        status = check_device_status(device)
        print(f"[{status}]")

        result_entry = {
            "hostname": hostname,
            "ip": ip,
            "device_type": device.get("device_type", "N/A"),
            "location": device.get("location", "N/A"),
            "status": status
        }
        results.append(result_entry)

    # 3. Display formatted summary result on screen
    print("\n" + "=" * 65)
    print("HEALTH CHECK RESULTS SUMMARY")
    print("=" * 65)
    print(f"{'Hostname':<18} {'IP Address':<32} {'Status':<6}")
    print("-" * 65)
    for res in results:
        print(f"{res['hostname']:<18} {res['ip']:<32} {res['status']:<6}")
    print("=" * 65)

    # 4. Save results to output.json with error handling
    try:
        with open(OUTPUT_FILE, "w") as f:
            json.dump(results, f, indent=4)
        print(f"\n[SUCCESS] Results successfully written to '{OUTPUT_FILE}'.")
    except Exception as err:
        print(f"[ERROR] Could not save results to {OUTPUT_FILE}: {err}")

if __name__ == "__main__":
    main()