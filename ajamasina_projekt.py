#proge projekt "Ajareis Eesti rahas"

input("Teretulemast mängu Ajareis Eesti rahas!\n")
#tutvustus kasutajale
input("Siin on sul võimalik sisestada summa, mille soovid reisile kaasa võtta ja aasta kuhu soovid reisida. ")
while True:
    raha = float(input("SUMMA EURODES: "))
    aasta = int(input("AASTA, KUHU SOOVID REISIDA: "))
    
    #dramaatilisteks pausideks
    from time import *
    
    
    #seda võib kindlasti täiendada ja teha põhjalikumaks
    eesti_ajastud = {"Eesti jääaega": (-10000000,-9000),
                     "Eesti muinasaega": (-9000,1200),
                     "Eesti keskaega": (1201,1558),
                     "Eesti varauusaega": (1559,1782),
                     "Eesti uusaega": (1783,1917),
                     "Eesti Vabariigi aega": (1918,1939),
                     "I NK okupatsiooni aega": (1940,1941),
                     "Saksa okupatsiooni aega": (1942,1944),
                     "sügavasse Nõukogude aega": (1945,1991),
                     "taasiseseisvunud Eesti vabariiki": (1991, 2026),
                     "tulevikku": (2027,1000000000000)
                     }  
    
    
    for ajastu, (algus,lõpp) in eesti_ajastud.items():
        if algus <= aasta <= lõpp:
            print(f"Ahhaa, sa soovid reisida {ajastu}...")
            sleep(2)
            print("Kui nii siis nii...")
            sleep(3)
            print("...Käivitame ajamasina...")
            sleep(3)
            print("   ...Hakkame startima...")
            sleep(2)
            for i in range(1,4):
                print(f"       {i}\n")
                sleep(2)
            
            
            if aasta < 800:
                print("AJAMASIN HOIATAB:\nSellel ajal ei kasutatud veel Eesti aladel raha ning sinu eurod pandaks ilmselt lõkesse ja sind ennast ilmselt varda otsas sinna samma lõkke peale küpsema.")
                sleep(1)
                print("...")
                sleep(1)
                küsimus_1 = input("   ... Oled kindel, et soovid siiski sinna reisida? ")
                if küsimus_1.lower() == "ei":
                    print(" Hästi. Alustame algusest. Vali uus aasta ")
                    continue
                else:
                    print(" Okei. Jätkame. ")
                    
            print("Reis õnnestus!!")
            
            

