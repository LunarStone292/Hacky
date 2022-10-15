import os

try:
    import requests
except:
    try:
        os.system("pip3 install requests")
    except:
        try:
            os.system("pip install requests")
        except:
            print("\n Error...")
            exit()

def get_ip():
    r = requests.get('https://jsonip.com')
    print(r.json())

get_ip()