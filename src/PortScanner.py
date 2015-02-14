# Simple port scanner
import concurrent.futures as concftr
import socket as sk

# Destination to scan
ipAddress = "127.0.0.1"
# Range to scan:
# Port numbers are assigned in various ways, based on three ranges: System
# Ports (0-1023), User Ports (1024-49151), and the Dynamic and/or Private
# Ports (49152-65535)
# http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml
rangeMin = 0
rangeMax = 1023
# List of all open ports
openPorts = []
# Maximum number of threads/connections
connectionsMax = 200
timeout = 60

def Scan(port):
    s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((ipAddress, port))
        openPorts.append(port)
        print(str(port) + " open")
        s.shutdown()
        s.close()
    except:
        pass

if __name__ == "__main__":
    print("Port scanner\n")
    
    with concftr.ThreadPoolExecutor(max_workers=connectionsMax) as executor:
        executor.map(Scan, range(rangeMin, rangeMax + 1))

    f = open("ports.txt", "w")
    try:
        f.write("Open ports on IP: " + ipAddress + "\n")
        for x in openPorts:
            f.write(str(x) + "\n")
    except:
        print("Error writing to file!")
    finally:
        f.close()
    print("Done!")
