import requests
import sys

url = "https://extreme-ip-lookup.com/json/"
vpn_url = "https://ipqualityscore.com/api/json/ip/<your private key goes here/"

def get_info():
	r = requests.get(url+ip)
	json = r.json()
	vpn = check_vpn()

	try:
		print(f"-----------------------------")
		print(f"| IP: {json['query']}")
		print(f"| ISP: {json['isp']}")
		print(f"| VPN: {vpn['vpn']}")
		print(f"| TOR: {vpn['tor']}")
		print(f"| CITY: {vpn['city']}")
		print(f"| PROXY: {vpn['proxy']}")
		print(f"| STATUS: {json['status']}")
		print(f"| COUNTRY: {json['country']}")
		print(f"| IP-TYPE: {json['ipType']}")
		print(f"-----------------------------")

	except:
		print("Error: Invalid IP")


def check_vpn():
	r = requests.get(vpn_url+ip)
	return r.json()


if __name__ == "__main__":
	ip = sys.argv[1] if len(sys.argv) > 1 else str(input("What ip do you want to look up? "))
	get_info()