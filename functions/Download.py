import os, time

try:
    import requests
except:
    try:
        os.system("pip3 install requests")
    except:
        os.system("pip install requests")

def download():
    modd = int(input("\n How to download?\n\n 1. Wget\n\n 2. Curl\n\n Mode => "))
    if(modd == 1):
        downloadd = input("\n\n Enter the link to download: ")
        out_name = input("\n Enter the output name: ")
        try:
            print("\n Downloading...")
            dd = os.system("start downloads/wget.exe " + downloadd + " -o downloads/" + out_name)
            if(dd == 1):
                print("\n Downaloding wget...")
                os.system("curl -L https://eternallybored.org/misc/wget/1.21.3/64/wget.exe -o downloads/wget.exe")
                time.sleep(2)
                print("\n\n Downloading...")
                os.system("start downloads/wget " + downloadd + " -o downloads/" + out_name)
                print("\n Done")
            else:
                print("\n Done")
        except:
            print("\n Error")
    elif(modd == 2):
        downloadd = input("\n\n Enter the link to download: ")
        out_name = input("\n Enter the output name: ")
        try:
            print("\n Downloading...")
            os.system("curl -L " + downloadd + " -o " + out_name)
        except:
            print("\n Error")

download()