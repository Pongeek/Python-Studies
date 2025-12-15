import time
def main():
    severity_counts = {"timestamp":0,"INFO": 0, "WARN": 0, "ERROR": 0}
    try:
        with open('/var/log/syslog', 'r') as f:
            for line in f:
                if "INFO" in line:
                    severity_counts["INFO"] += 1
                elif "WARN" in line:
                    severity_counts["WARN"] += 1
                elif "ERROR" in line:
                    severity_counts["ERROR"] += 1
        severity_counts["timestamp"] += time.time()
        print(severity_counts)
    except FileNotFoundError:
        print("File not found")

if __name__ == '__main__':
    main()
