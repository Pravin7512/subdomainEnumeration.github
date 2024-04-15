import requests
import sys
import pyfiglet

def subdomains(url):
    with open(r"C:\Users\pravi\OneDrive\Desktop\Cyber project\subdomain Enumeration\subdmainwordlist.txt", "r") as subd:
        for line in subd:
            word = line.strip()
            test_url = word + "." + url
            try:
                response = requests.get("http://" + test_url)
                if response.status_code == 200:
                    print("[+] Subdomain Discovered --> " + test_url)
            except requests.exceptions.RequestException as e:
                print("Error:", e)

def directories(url):
    with open(r"C:\Users\pravi\OneDrive\Desktop\Cyber project\subdomain Enumeration\directory.txt", "r") as dirlist:
        for dir in dirlist:
            word = dir.strip()
            test_url = "http://" + url + "/" + word
            try:
                response = requests.get(test_url)
                if response.status_code == 200:
                    print("[+] Directory Discovered --> " + test_url)
            except requests.exceptions.RequestException as e:
                print("Error:", e)

def start():
    print("1. Subdomains\n2. Directories")
    try:
        option = int(input("\nChoose 1 or 2: "))
        if option == 1:
            print("<----------------Checking for Subdomains---------------->")
            subdomains(url)
        elif option == 2:
            print("<----------------Checking for Directories---------------->")
            directories(url)
        else:
            print("\n<----------Choose Correct Option---------->\n")
            start()
    except KeyboardInterrupt:
        sys.exit()
    except ValueError:
        print("\n<----------Choose Correct Option---------->\n")
        start()

print(pyfiglet.figlet_format("Subdomain Enumeration"))
print("By: Pravin Choudhary")

url = input("\nEnter the Domain Name (For example: google.com, yahoo.com): ")
try:
    check_url = requests.get("http://" + url)
    if check_url.status_code == 200:
        start()
    else:
        print("Invalid Domain name")
except requests.exceptions.RequestException as e:
    print("Error:", e)
