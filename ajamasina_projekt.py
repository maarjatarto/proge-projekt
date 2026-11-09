#proge projekt "Ajareis Eesti rahas"

input("Teretulemast mängu Ajareis Eesti rahas!")
input("Siin on sul võimalik sisestada summa mille soovid reisile kaasa võtta ja aasta kuhu soovid reisida. ")
while True:
    raha = float(input("SUMMA EURODES: "))
    aasta = int(input("AASTA, KUHU SOOVID REISIDA: "))

    #dramaatilisteks pausideks
    from time import *

    if aasta <= 1200:
        print("Ahhaa, sa soovid reisida eesti muinasaega...")
        sleep(1)
        print("...")
        sleep(1)
        if aasta <= 800:
            print("Sellel ajal ei kasutatud veel Eesti aladel raha ning sinu raha oleks lõkesse pandud ja sind ilmselt varda otsas sinna samma lõkke peale.")
            sleep(1)
            print("...")
            sleep(1)
            algusesse = input("Kas soovid tagasi algusesse minna ja uuesti mängida? ")
        if algusesse.lower() == "jah" or algusesse.lower() == "ja" or algusesse.lower() == "jaa" :
            print("")  
        elif aasta > 800:
            print("Sellel ajal leidus Eestis vaid üksikuid hõbemünte võõrastelt maadelt ja süsteeme valuutavahetuseks polnud.")
            print("...")
            algusesse = input("Kas soovid tagasi algusesse minna ja uuesti mängida? ")
        if algusesse.lower() == "jah" or algusesse.lower() == "ja" or algusesse.lower() == "jaa" :
            print("")  
    elif aasta <= 1558:
        print("Ahhaa, sa soovid reisida Eesti keskaega...")
        sleep(1)
        print("...")
        algusesse = input("Kas soovid tagasi algusesse minna ja uuesti mängida? ")
        if algusesse.lower() == "jah" or algusesse.lower() == "ja" or algusesse.lower() == "jaa" :
            print("")  
    elif aasta <= 1782:
        print("Ahhaa, sa soovid reisida Eesti varauusaega...")
        sleep(1)
        print("...")
        algusesse = input("Kas soovid tagasi algusesse minna ja uuesti mängida? ")
        if algusesse.lower() == "jah" or algusesse.lower() == "ja" or algusesse.lower() == "jaa" :
            print("")  
    elif aasta <= 1917:
        print("Ahhaa, sa soovid reisida Eesti uusaega...")
        sleep(1)
        print("...")
        algusesse = input("Kas soovid tagasi algusesse minna ja uuesti mängida? ")
        if algusesse.lower() == "jah" or algusesse.lower() == "ja" or algusesse.lower() == "jaa" :
            print("")  
    elif aasta <= 1939:
        print("Ahhaa, sa soovid reisida Eesti esimese vabariigi aega...")
        sleep(1)
        print("...")
        algusesse = input("Kas soovid tagasi algusesse minna ja uuesti mängida? ")
        if algusesse.lower() == "jah" or algusesse.lower() == "ja" or algusesse.lower() == "jaa" :
            print("")  
    elif aasta <= 1940:
        print("Ahhaa, sa soovid reisida esimese Nõukogude okupatsiooni aega...")
        sleep(1)
        print("...")
        algusesse = input("Kas soovid tagasi algusesse minna ja uuesti mängida? ")
        if algusesse.lower() == "jah" or algusesse.lower() == "ja" or algusesse.lower() == "jaa" :
            print("")  
    elif aasta <= 1944:
        print("Ahhaa, sa soovid reisida Saksa okupatsiooni aega...")
        sleep(1)
        print("...")
        algusesse = input("Kas soovid tagasi algusesse minna ja uuesti mängida? ")
        if algusesse.lower() == "jah" or algusesse.lower() == "ja" or algusesse.lower() == "jaa" :
            print("")  
    elif aasta <= 1991:
        print("Ahhaa, sa soovid reisida Nõukogude okupatsiooni aega...")
        sleep(1)
        print("...")
        algusesse = input("Kas soovid tagasi algusesse minna ja uuesti mängida? ")
        if algusesse.lower() == "jah" or algusesse.lower() == "ja" or algusesse.lower() == "jaa" :
            print("")  
    elif aasta <= 2026:
        print("Ahhaa, sa soovid reisida taasiseseisvunud Eesti vabariiki...")
        sleep(1)
        print("...")
        algusesse = input("Kas soovid tagasi algusesse minna ja uuesti mängida? ")
        if algusesse.lower() == "jah" or algusesse.lower() == "ja" or algusesse.lower() == "jaa" :
            print("")  
    else:
        print("Ahhaa, sa soovid reisida tulevikku...")
        sleep(1)
        print("...")
        algusesse = input("Kas soovid tagasi algusesse minna ja uuesti mängida? ")
        if algusesse.lower() == "jah" or algusesse.lower() == "ja" or algusesse.lower() == "jaa" :
            print("")        
    
