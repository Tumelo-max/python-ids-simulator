import time
from collections import defaultdict

# Configuration
THRESHOLD = 5
TIME_WINDOW = 10  # seconds
COOLDOWN = 15  # seconds

# Data storage
ip_log = defaultdict(list)
last_alert_time = {}

# Logging function
def log_event(message):
    with open("ids_log.txt", "a") as file:
        file.write(f"{time.ctime()} - {message}\n")

# Core detection logic
def process_ip(ip):
    now = time.time()

    # Track request timestamps
    ip_log[ip].append(now)

    # Keep only recent requests within TIME_WINDOW
    ip_log[ip] = [t for t in ip_log[ip] if now - t <= TIME_WINDOW]

    count = len(ip_log[ip])

    # Cooldown check
    if ip in last_alert_time and now - last_alert_time[ip] < COOLDOWN:
        print(f"[INFO] {ip} ignored (cooldown active)")
        return

    # Detection levels
    if count >= THRESHOLD:
        print(f"[HIGH] Suspicious activity from {ip} ({count} requests in {TIME_WINDOW}s)")
        log_event(f"HIGH ALERT - {ip} - {count} requests")
        last_alert_time[ip] = now

    elif count >= THRESHOLD - 2:
        print(f"[MEDIUM] Unusual activity from {ip} ({count} requests)")
        log_event(f"MEDIUM ALERT - {ip} - {count} requests")

    else:
        print(f"[NORMAL] Traffic from {ip} ({count})")
        log_event(f"NORMAL - {ip} - {count}")

# Main runner
def run():
    print("🚀 Starting IDS monitoring...\n")

    while True:
        ip = input("Enter incoming IP (or type 'exit'): ")

        if ip.lower() == "exit":
            print("🛑 IDS stopped.")
            break

        process_ip(ip)

# Entry point
if __name__ == "__main__":
    run()

