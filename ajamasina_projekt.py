# projekt "Ajareis Eesti rahas"
# valuutavahetus programm, mis töötab Eesti ajaloo kontekstis ja toimib nagu ajamasin
# autorid Maarja Tarto ja Huko Orro

# inspiratsiooni saime siit https://www.nationalarchives.gov.uk/currency-converter/

# TEHISARU: eesti_ajastud.csv on loodud tehisaruga, andes talle ette Eesti Entsüklopeedia lehel olnud Eesti ajaloo kronoloogia.
        #   Ajastute vahemike arvutamise skeemi parandamiseks kasutasime tehisaru ja ka tsükli lõpetamise parandamiseks.
        #   Veel tehisaru: 

#Kuidas senine koostöö sujunud? Kuidas on rollid jagatud? Koostöö on sujunud hästi. Maarja on teinud praegu rohkem sissejuhatavat osa 
# ja Huko valuutakonverteerimise osa.

#Kui palju aega projektile on kulunud? Maarja: minul on projektile praegu kokku kulunud umbes 6 tundi.

#Millised on projektiga seoses edasised plaanid ja edasiarendused? Tahaks ajastuid veel lisada ja konteksti täpsemaks teha. Raha väärtuse
# kohta võiks olla ühine süsteem, mis ütleks iga ajastu kohta nt et selle raha eest saaksid sa osta nii mitu liitrit piima või nii mitu
# pätsi leiba. Samuti tuleks neid erinevaid käibel olnud raha ühikuid lisada ja proovida suuremat täpsust saada. Tahaks kindlasti ka 
# kasutada kasutajaliidest ja pildi- ja helitöötlust.

input("Teretulemast mängu Ajareis Eesti rahas!\n")
#tutvustus kasutajale
input("Siin on sul võimalik sisestada summa, mille soovid reisile kaasa võtta ja aasta kuhu soovid reisida.")
while True:
    raha = float(input("SUMMA EURODES: "))
    aasta = int(input("AASTA, KUHU SOOVID REISIDA: "))
    lõpeta = False
    
    #dramaatilisteks pausideks
    from time import *
    
    
    #seda võib kindlasti täiendada ja lisada ajastuid
    eesti_ajastud = {"Eesti jääaega": (float("-inf"),-9000),
                     "Eesti muinasaega": (-9000,1200),
                     "Eesti keskaega": (1201,1558),
                     "Eesti varauusaega": (1559,1782),
                     "Eesti uusaega": (1783,1917),
                     "esimesse Eesti Vabariigi aega": (1918,1939),
                     "I NK okupatsiooni aega": (1940,1941),
                     "Saksa okupatsiooni aega": (1942,1944),
                     "sügavasse Nõukogude aega": (1945,1991),
                     "taasiseseisvunud Eesti vabariiki": (1991, 2026),
                     "tulevikku": (2027,float("inf"))
                     }  
    
    # ajamasina käivitamine
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
            
            # ma leidsin mingi allika mis ütles et enne u seda aega ei olnud üldse raha kasutusel aga see ei pruugi väga täpne loomulikult olla
            if aasta < 800:
                print("AJAMASIN HOIATAB:\nSellel ajal ei kasutatud veel Eesti aladel rahatähti ning sinu eurod pandaks ilmselt lõkesse ja sind ennast ilmselt varda otsas sinna samma lõkke peale küpsema.")
                sleep(1)
                print("...")
                sleep(1)
                küsimus_1 = input("   ... Oled kindel, et soovid siiski sinna reisida? ")
                if küsimus_1.lower() == "ei":
                    print(" Hästi. Alustame algusest. Vali uus aasta ")
                    continue
                else:
                    print(" Okei. Jätkame. ")
                    
            print(f"Reis õnnestus!! Sa oled aastas {aasta}.")

            # ajastu konteksti natuke
            # programm avab csv faili, mis on lisatud siia main branchi alla
            with open("eesti_ajastud.csv", encoding = "utf-8") as fail:
                for rida in fail:
                    vahemik, märksõnad = rida.strip().split(";")
                    ajastu_kirjeldus = märksõnad.strip().split(",")
                    algus, lõpp = (vahemik.strip().split(","))
                    if int(algus) <= aasta <= int(lõpp):
                        
                        print(f"Eestis valitseb {ajastu_kirjeldus[0]} ning eestlasi kimbutavad{ajastu_kirjeldus[1]} ja{ajastu_kirjeldus[2]}, aga kõik ei ole halvasti ka, sest{ajastu_kirjeldus[3]}  ")
           
            küsimus_2 = input("Oled valmis ajamasinast välja astuma? ")
            if küsimus_2 == "ei":
                küs_3 = input("Lähme algusesse? ")
                if küs_3 == "ei":
                    lõpeta = True
                    break

            print("Väga tore. Alustame rahavahetusega.")
            sleep(2)
            print(". . .")
            sleep(2)      
            
            #valuutavahetuse süsteem ja ostujõu arvutamine
            print("-" * 55)
            if aasta < 800:
                print(f"Aastal {aasta} rahatähti veel ei tuntud.")
                print(f"Sinu {raha} € asemel kaupleksid sa hoopis hõbevalge, karusnahkade või viljaga!")
            elif 800 <= aasta <= 1917:
                väärtus = round(raha * 15, 2)
                print(f"Aastal {aasta} kehtisid Eestis erinevad mündid (nt tsaarirublad, taalrid või killingid).")
                print(f"Sinu {raha} € ostujõud oleks umbes {väärtus} hõberubla või kuldmünti.")
                print("Ajalooline kontekst: Talupoja jaoks oli see suur varandus, millega sai osta kariloomi või maad.")
            elif 1918 <= aasta <= 1927:
                väärtus = round(raha * 350, 2)
                print(f"Aastal {aasta} oli kasutusel Eesti mark.")
                print(f"Sinu {raha} € on väärt umbes {väärtus} Eesti marka.")
                print("Ajalooline kontekst: Noor Eesti vabariik – selle raha eest sai turult korraliku toidukorvi.")
            elif 1928 <= aasta <= 1940:
                väärtus = round(raha * 3.5, 2)
                print(f"Aastal {aasta} oli kasutusel esimene Eesti kroon (EEK I).")
                print(f"Sinu {raha} € on väärt umbes {väärtus} Eesti krooni.")
                print("Ajalooline kontekst: Stabiilne majandusaeg – leib maksis umbes 15–20 senti.")
            elif 1941 <= aasta <= 1991:
                väärtus = round(raha * 2.5, 2)
                print(f"Aastal {aasta} oli kasutusel Nõukogude rubla (või lühiajaliselt Saksa riigimark).")
                print(f"Sinu {raha} € ostujõud on umbes {väärtus} rubla.")
                print("Ajalooline kontekst: Hinnad olid riiklikult määratud – kinopilet maksis 20–50 kopikat.")
            elif 1992 <= aasta <= 2010:
                väärtus = round(raha * 15.6466, 2)
                print(f"Aastal {aasta} oli kasutusel taasiseseisvunud Eesti kroon (EEK II).")
                print(f"Sinu {raha} € on täpselt {väärtus} Eesti krooni.")
                print("Ajalooline kontekst: Ametlik kurss oli 1 EUR = 15,6466 EEK. 1990ndatel sai selle eest palju rohkem kui 2010. aastal!")
            elif 2011 <= aasta <= 2026:
                print(f"Aastal {aasta} on Eestis kasutusel euro (€).")
                print(f"Sinu {raha} € ongi {raha} €, kuid varasematel aastatel (nt 2011) sai selle eest umbes poole rohkem kaupa kui täna!")
            else:
                väärtus = round(raha * 0.4, 2)
                print(f"Aastal {aasta} (tulevikus) on inflatsioon oma töö teinud.")
                print(f"Sinu tänase {raha} € ostujõud on tulevikus umbes {väärtus} tänast eurot (või krüptokrediiti).")
            print("-" * 55)

            uuesti = input("\nKas soovid teha uue ajareisi? (jah/ei): ")
            if uuesti.lower() == "ei":
                print("Aitäh ajareisil osalemast! Kohtumiseni tulevikus!")
                lõpeta = True
                break
    if lõpeta:
        break            
print("Aitäh ajareisil osalemast! Kohtumiseni tulevikus!")


