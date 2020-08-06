import requests, colorama, time, random, os, subprocess, threading
from colorama import Fore, init

title = ('Nighty Checker')
init()

request_url = "https://canary.discordapp.com/api/v6/users/@me"

def doIntro():
    os.system("cls")

banner = """
   ███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗██╗   ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
   ████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝╚██╗ ██╔╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
   ██╔██╗ ██║██║██║  ███╗███████║   ██║    ╚████╔╝     ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
   ██║╚██╗██║██║██║   ██║██╔══██║   ██║     ╚██╔╝      ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
   ██║ ╚████║██║╚██████╔╝██║  ██║   ██║      ██║       ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
   ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝        ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""

print(banner)
time.sleep(1)
def center(length):
    spaces = ""
    for i in range(int((120/2-length/2))):
        spaces += " "

    return spaces

def HorizontalLine():
    line = ""
    for i in range(120):
        line += "="

    print(Fore.GREEN + line + Fore.WHITE)

def println(text):
    print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] {text}")

def printlnr(text):
    return f"{Fore.WHITE}[{Fore.CYAN}!{Fore.WHITE}] {text}"

def main():
    doIntro()

    tokenFileName = input(printlnr("Enter the name of the file in wich are the unchecked tokens (without .txt) : "))

    doIntro()

    if not os.path.exists(tokenFileName + ".txt"):
        open(tokenFileName + '.txt', 'a+') # create the .txt file instead of exiting the program
    
    try:
        for item in open(tokenFileName + ".txt", "r").readlines():
            CheckToken(item.strip())

        println("Every token have been checked.")
        input()
        exit()

    except Exception as e:
        print(e)
        println("An unexepted error occurred !")
        input()
        exit()

def CheckToken(token):
    req = requests.get(request_url, headers={'authorization': token})
    if req.status_code == 401:
        println(f"Invalid : {token}")
    elif req.status_code == 200:
        println(f"Valid   : {token}")
        with open("Valid Tokens.txt", "a") as f:
            f.write(token + "\n")
    else:
        println("An unexepted error occurred !")
        input()
        exit()
main()