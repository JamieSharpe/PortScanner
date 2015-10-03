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
# Maximum number of threads/connections
connectionsMax = 200
timeout = 60


# Returns the IP and Port if it can reach it.
def scan(port):

    connected = False

    s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((ipAddress, port))
        s.shutdown(sk.SHUT_RDWR)
        s.close()

        # Connect didn't error
        connected = True

    except:
        pass

    return {"port": port, "connected": connected}


def port_scanner():
    print("Port scanner\n")

    with concftr.ThreadPoolExecutor(max_workers=connectionsMax) as executor:
        result_ips = executor.map(scan, range(rangeMin, rangeMax + 1))

    with open("IPs.txt", "w") as f:
        f.write("Open ports on IP: {}\n".format(ipAddress))

        for vuln_address in [x for x in result_ips if x["connected"] == True]:
            f.write("{}\n".format(vuln_address["port"]))

    print("Port Scan Complete!")


def ip_scanner():
    print("IP Scanner")
    pass # TODO: Implement me.
    print("IP Scan Complete!")


def main():
    print("Main Entry point of application")

    port_scanner()
    #ip_scanner()

    print("End of application")


if __name__ == "__main__":
    main()
