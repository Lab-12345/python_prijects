import requests
import socket
import ipaddress
import argparse

API_KEY = "Enter the api key"

def ipvalid(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def reversedns(ip):
    try:
        domain = socket.gethostbyaddr(ip)
        return domain[0]
    except socket.herror:
        return None

def websites_on_same_server(ip):
    url = f"https://api.viewdns.info/reverseip/?host={ip}&apikey={API_KEY}&output=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "response" in data and "domains" in data["response"]:
            websites = data["response"]["domains"]
            return websites
    return []

def main():
    parser = argparse.ArgumentParser(description="Perform IP reverse lookup.")
    parser.add_argument("ips", nargs="+", help="IP address(es) to perform reverse lookup on.")
    parser.add_argument("--all", "-a", action="store_true", help="Print all other websites on the same server.")
    args = parser.parse_args()

    for ip in args.ips:
        if not ipvalid(ip):
            print(f"[-] Invalid IP address: {ip}")
            continue
        domain = reversedns(ip)
        if domain:
            print(f"[+] IP: {ip}, Domain: {domain}")
            if args.all:
                websites = websites_on_same_server(ip)
                if websites:
                    print("\nOther websites on the same server:")
                    for website in websites:
                        print(f"[+] {website}")
                    print('\n')
                else:
                    print("[-] No other websites found on the same server.")
        else:
            print(f"[-] No domain found for IP: {ip}")

if __name__ == "__main__":
    main()
