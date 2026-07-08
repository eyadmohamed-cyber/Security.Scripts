import socket

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            return True
        else:
            return False
    except:
        return False

target = "192.168.56.101"
ports = range(1, 1025)

print(f"Scanning {target}...")

for port in ports:
    if scan_port(target, port):
        print(f"Port {port} is OPEN")

print("Scan complete.")
