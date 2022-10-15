import os, platform

def sys_info():
    if(platform.system() == "Windows"):
        print("\n\n======================system_info======================\n\n")
        os.system("systeminfo")
    else:
        r = os.system("neofetch")
        if(r == 1):
            s = os.system("sudo apt install neofetch")
            if(s == 1):
                l = os.system("sudo pacman -S neofetch")
                if(l == 1):
                    os.system("yum install neofetch")
                    os.system("clear && neofetch")
                else:
                    os.system("clear && neofetch")
            else:
                os.system("clear && neofetch")

sys_info()