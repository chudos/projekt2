"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Adam Krejčí
email: adam.krejci.1915@gmail.com
"""

import random
import time

def generuj_spravne_cislo():
    while True:
        cislo = random.choice(range (1000, 10000))
        if len(set(str(cislo))) == 4:
            return str(cislo)

def kontrola_hrace(hrac):
    hrac_str = str(hrac)
    if (
        len(set(hrac_str)) == 4 and 
        hrac_str[0] != '0' and 
        hrac_str.isdigit()
    ):
        return True
    else:
        return False
    
print(
"Hi there! \n"
"-----------------------------------------------\n"
"I've generated a random 4 digit number for you.\n"
"Let's play a bulls and cows game.\n"
"-----------------------------------------------\n"
"Enter a number:\n"
"-----------------------------------------------"
)

spravne_cislo = generuj_spravne_cislo()
pocet_pokusu = 0
start = time.time()

while True:
    while True:
        volba_hrace = input("Enter a 4-digit number with unique digits:")
        if kontrola_hrace(volba_hrace):
            break
        else:
            print ("Wrong input, try again")
    pocet_pokusu += 1
    bulls = 0
    for pocitac, hrac in zip(spravne_cislo, volba_hrace):
        if pocitac == hrac:
            bulls += 1
    cows = 0
    for hrac in volba_hrace:
        if hrac in spravne_cislo:
            cows += 1
    cows -= bulls
    if bulls == 4:
        end = time.time()
        cas = end - start
        print(
        ">>>", volba_hrace, "\n"
        "Correct, you've guessed the right number\n"
        "in", pocet_pokusu, "guesses\n"
        "-----------------------------------------------"
        )
        if cas > 60:
            minuty = int(cas//60)
            sekundy = round(cas % 60)
            print(
                "You did it in", minuty, "minutes", sekundy, "seconds\n"
                "That's not bad!"
            )
        else:
            print(
                "You did it in", round(cas), "seconds\n"
                "That's amazing!"
            )
        break
    else:
        print( ">>>", volba_hrace)
        print(bulls, "bulls", cows, "cows")
        print("-----------------------------------------------")
