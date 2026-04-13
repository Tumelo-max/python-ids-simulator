from collections import defaultdict
import time

ip_log = defaultdict(list)
last_alert_time = {}

THRESHOLD = 5
TIME_WINDOW = 10
COOLDOWN = 15

def process_ip(ip):
    now = time.time()

    # track requests
    ip_log[ip].append(now)

    # keep only last TIME_WINDOW seconds
    ip_log[ip] = [t for t in ip_log[ip] if now - t <= TIME_WINDOW]

    count = len(ip_log[ip])

    # cooldown prevents spam alerts
    if ip in last_alert_time and now - last_alert_time[ip] < COOLDOWN:
        print(f"[INFO] {ip} ignored (cooldown active)")
        return

    if count >= THRESHOLD:
        print(f"[HIGH] Suspicious activity from {ip} ({count} requests in {TIME_WINDOW}s)")
        last_alert_time[ip] = now

    elif count >= THRESHOLD - 2:
        print(f"[MEDIUM] Unusual activity from {ip} ({count} requests)")

def run():
    print("Starting IDS monitoring...")

    while True:
        ip = input("Enter incoming IP (or type 'exit'): ")

        if ip.lower() == "exit":
            break

        process_ip(ip)

if __name__ == "__main__":
    run()
