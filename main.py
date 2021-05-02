from python_imagesearch.imagesearch import imagesearch
import mouse
import time
from termcolor import cprint
import colorama

colorama.init()

def printc(text, texttype="normal", end=None):
    if texttype == "normal":
        if end != None:
            cprint(text, 'green', end=end)
        else:
            cprint(text, 'green')
    elif texttype == "error":
        if end != None:
            cprint(text, 'red', end=end)
        else:
            cprint(text, 'red')

def search(path):
    pos = imagesearch(path)
    if pos[0] != -1:
        return pos
    else:
        return None

def isok():
    found = search("img/lanebutons.png")
    if found != None:
        return True
    else:
        return False

def champselect():
    timecount = 0
    while timecount < 10:
        ok = isok()
        if ok == True:
            return True
        timecount += 1
        time.sleep(1)
    return False

def main():
    printc("[KRAL4]")
    while 1:
        printc("[i] Waiting for match...", end="\r")
        found = search("img/accept.png")
        if found != None:
            printc("\n[+] Match found")
            mouse.move(found[0], found[1]+40)
            mouse.click()
            printc("[+] Match accepted\n[i] Waiting for pick phase...")
            ok = champselect()
            if ok:
                printc("[+] Pick phase")
                break
            else:
                printc("[-] Game dodged", "error")

main()