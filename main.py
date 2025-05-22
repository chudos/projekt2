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

def vyhodnot_tip(tajny, tip):
    bulls = 0
    for p, h in zip(tajny, tip):
        if p == h:
            bulls += 1
    cows = 0
    for h in tip:
        if h in tajny:
            cows += 1
    cows -= bulls
    return bulls, cows

def vypis_vysledek(tip, bulls, cows):
    print(f">>> {tip}")
    print(f"{bulls} bulls, {cows} cows")
    print("-----------------------------------------------")

def main():
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
                print("Wrong input, try again")
        pocet_pokusu += 1
        bulls, cows = vyhodnot_tip(spravne_cislo, volba_hrace)
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
            vypis_vysledek(volba_hrace, bulls, cows)

if __name__ == "__main__":
    main()