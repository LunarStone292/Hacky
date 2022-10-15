import os, time

try:
    import requests
except:
    r = os.system("pip3 install requests")
    if(r == 1):
        os.system("pip install requests")

def alive():
    sito = input("\n Enter the URL: ")
    try:
        r = requests.get(sito)
        if(r.status_code == 200):
            print(" Host is alive")
        elif(r.status_code == 403):
            print(" Connection refused!")
        time.sleep(.5)
    except:
        print(" Server seems down!!!")

alive