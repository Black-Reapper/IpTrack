#!/usr/bin/env python3

import os
import sys
import json
try:
    import requests
except Exception as e:
    print("[*] {0}".format(e))

if sys.version_info[0] < 3:
    print("require python3.x.x\nare you using python {0}.{1}.{2}".fomat(sys.version_info[0], sys.version_info[1], sys.version_info[2]))
    sys.exit(0)

red, white = "\x1b[1;91m", "\x1b[1;97m"

clear = "clear"
os.system(clear)

banner = """
{0}ooooo           {1}     .                                oooo
{0}`888'           {1}   .o8                                `888
{0} 888  oo.ooooo. {1} .o888oo oooo d8b  .oooo.    .ooooo.   888  oooo
{0} 888   888' `88b{1}   888   `888""8P `P  )88b  d88' `"Y8  888 .8P'
{0} 888   888   888{1}   888    888      .oP"888  888        888888.
{0} 888   888   888{1}   888 .  888     d8(  888  888   .o8  888 `88b.
{0}o888o  888bod8P'{1}   "888" d888b    `Y888""8o `Y8bod8P' o888o o888o
{0}       888
{0}      o888o     {0}IP Tracker 2019 Version 1.5 Code By CyberSec
      """.format(red, white)

print(banner)

def tracker(ip):
    print("\n{0}Target : {1}".format(white, ip))
    r = requests.get("http://ip-api.com/" + ip)
    result = r.text
    result = result.replace(",", "").replace("{", "").replace("}", "")
    print(result)

def main():
    ip = input("{0}[{1}#{0}]{1} Enter IP or URL : ".format(red, white))
    if not ip:
        print("{0}What? Enter Valid IP or URL.".format(red))
        return main()
    ip_clean = ip.replace("http://", "").replace("https://", "")
    ip = ip_clean
    tracker(ip)

if __name__ == "__main__":
    try:
        main()
    except requests.exceptions.ConnectionError:
        print("\n{0}Not Internet Connection. Failed Track".format(red))
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt. Exiting....")
    except EOFError as eof:
        print(eof)
