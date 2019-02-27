import requests
import os

def reverseiplookup(main):
    site = input("Digite o ip ou a host: ")
    r = requests.get('http://api.hackertarget.com/reverseiplookup/?q={}'.format(site))
    print(r.text)
    input("Press Enter")    
    main()

def nmap(main):
    site = input("Digite o ip ou a host: ")
    r = requests.get('http://api.hackertarget.com/nmap/?q={}'.format(site))
    print(r.text)
    input("Press Enter")
    main()    

def geoip(main):
    site = input("Digite o ip ou a host: ")
    r = requests.get('http://api.hackertarget.com/geoip/?q={}'.format(site))
    print(r.text)
    input("Press Enter")
    main()

def reversedns(main):
    site = input("Digite o ip ou a host: ")
    r = requests.get('https://api.hackertarget.com/reversedns/?q={}'.format(site))
    print(r.text)
    input("Press Enter")
    main()

def dns(main):
    site = input("Digite o ip ou a host: ")
    r = requests.get('http://api.hackertarget.com/dnslookup/?q={}'.format(site))
    print(r.text)
    input("Press Enter")
    main()

def whois(main):
    site = input("Digite o ip ou a host: ")
    r = requests.get('http://api.hackertarget.com/whois/?q={}'.format(site))
    #os.system("cls")
    print(r.text)
    input("Press Enter")
    main()

def main():
    print("----------------------------------")
    print("\n           MENU INICIO\n")
    print("----------------------------------")
    menu = int(input("\n{1} Whois \n{2} DNSLookup\n{3} ReverseDNS\n{4} GeopIP\n{5} nmap\n{6} ReverseIPLookup\n{00} Quit\n\n"))
    if menu == 1:
        os.system("cls")
        whois(main)
    elif menu == 2:
        os.system("cls")
        dns(main)
    elif menu == 3:
        os.system("cls")
        reversedns(main)
    elif menu == 4:
        os.system("cls")
        geoip(main)
    elif menu == 5:
        os.system("cls")
        nmap(main)
    elif menu == 6:
        os.system("cls")
        reverseiplookup(main)
    elif menu == 00:
        os.system("cls")
        quit
    else:
        os.system("cls")
        main()
main()