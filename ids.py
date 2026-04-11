from collections import defaultdict

connection_count = defaultdict(int)


def log_event(message):
    with open("ids_log.txt", "a") as file:
        file.write(message + "\n")


def detect_intrusion(ip):
    connection_count[ip] += 1

    if connection_count[ip] > 5:
        alert_msg = f"[ALERT] Suspicious activity from {ip} (Count: {connection_count[ip]})"
        print(alert_msg)
        log_event(alert_msg)


def start_monitoring():
    print("Starting IDS monitoring...")

    while True:
        ip = input("Enter incoming IP (or type 'exit'): ")

        if ip.lower() == 'exit':
            break

        detect_intrusion(ip)


if __name__ == "__main__":
    start_monitoring()
