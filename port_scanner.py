from socket import *
import time
import threading
from urllib.parse import urlparse

print_lock = threading.Lock()                       #Used to synchronise the access to prevent garbled output


def port_scan(target,port):
    try:
        t_IP = gethostbyname(target)                #gethostbyname helps in hostname resolution
    except gaierror:                                # gaierror represents the error in host name resolution
        print("Invalid host unable to resolve. (Remove http or https)")
        return

    s = socket(AF_INET, SOCK_STREAM)            #creating new socket object and AF_INET shows IPv4 and SOCK_STREAM showd TCP scan
    s.settimeout(2)
    time.sleep(0.5)
    try:
        conn = s.connect_ex((t_IP,port))               #connect_ex is used to initiate a connection 
        if conn == 0:                               #Checks if the connection was successful or not
            try:
                service_name =getservbyport(port)   #Trying to get the service name
            except OSError:                         #If didn't get any service name then handled by this
                service_name = "Unknown"
            with print_lock:
                print("Port %d: OPEN (%s)" % (port, service_name))
    except Exception as e:
        print("Error:", e)
    finally:
        s.close()                                   #Closes the previous opened connection

def scan_port(target, ports):
    try:
        t_IP = gethostbyname(target)
    except:
        print("Invalid host unable to resolve. (Remove http or https)")
        return
    
    print("Starting scan of the host:", t_IP)
    
    threads = []
    for port in ports:
        t = threading.Thread(target=port_scan, args=(target, port)) #Creating thead object
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == '__main__':
    startTime = time.time()
    while True:
        target = input("Enter the target:")
        if target:
            break
        else:
            ("Target IP cannot be empty. Please try again.")
    try:
        target = target.replace('http://','')
        target = target.replace('https://','')
    finally:
        ports = range(1,1000)
        scan_port(target, ports)
        print("Time taken: ",time.time() - startTime)

