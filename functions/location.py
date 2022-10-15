import os
from platform import platform
try:
    import webbrowser
except:
    print("")

def location():
    llocation = input("\n Enter the location: ")
    my = ""
    if(llocation == my):
        print("\n Invalid command")
    else:
        if(platform.system() == "Windows"):
            webbrowser.open('https://www.google.com/maps/search/' + location)
        else:
            l = os.system("firefox https://www.google.com/maps/search/" + location)
            if(l == 1):
                print("\n Error, firefox is not installed...")
location()