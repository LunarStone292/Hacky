import platform, os

try:
    import requests
except:
    try:
        os.system("pip3 install requests")
    except:
        os.system("pip install requests")

def online_check():
    try:
        r = requests.get('http://www.google.com')
        if(r.status_code == 200):
            print("\n You are connected!")
        else:
            print("\n Connection refused")
    except:
        print("\n You are not connected...\n")
    
online_check()