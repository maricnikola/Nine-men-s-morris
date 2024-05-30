from re import A
from human_vs_minmax import mapiranje,printTable,slobodno_polje,mica,provera_pozicije,potencijalno_blokiran,broj_preostalih,provera_svih_blokiranih

from heuristics import broj_mica,dve_mice,broj_piuna,potencijalne_dve_mice,potencijalna_mica

def human_v_human():
    hash_map = mapiranje()

    printTable(hash_map)

    for i in range(4):
        
        igrac1= True
        while igrac1:

            try:
                polje = int(input("Igrac 1 unesite broj polja koje zelite da odigrate:"))
                if  polje > 23:
                    print("Broj koji ste uneli ne oznacava nijedno polje")
                    continue

                if hash_map[polje]=='X':
                    hash_map[polje]="1"
                    printTable(hash_map)

                    if mica(polje,hash_map):
                        print('\nCestitamo sklopili ste micu!\n')
                        brisanje2= True

                        while brisanje2:
                            try:
                                polje_za_brisanje1= int(input('\nUnesite polje da bi obrisali protivnikovog igraca:'))

                                if polje_za_brisanje1>23:
                                    print('Broj koji ste uneli ne oznacava nijedno polje!')
                                
                                if hash_map[polje_za_brisanje1]=='2':
                                    hash_map[polje_za_brisanje1]='X'
                                    printTable(hash_map)
                                    brisanje2=False
                                
                                else:
                                    print('\nNiste uneli pravilno polje!')
                            except:
                                print('Niste pravilno uneli polje!')
                            
                            
                    igrac1=False

                else:
                    print("\nPolje koje zelite da odigrate je zauzeto.\n")

            except:
                print("Broj koji ste uneli ne oznacava nijedno polje.")


        igrac2=True

        while igrac2:

            try:
                polje = int(input("Igrac 2 unesite broj polja koje zelite da odigrate:"))

                if  polje>24:
                    print("\nBroj koji ste uneli ne oznacava nijedno polje\n")
                    continue

                if hash_map[polje]=='X':
                    hash_map[polje]="2"
                    printTable(hash_map)


                    if mica(polje,hash_map):
                        print('\nCestitamo igrac 2 sklopili ste micu!\n')
                        brisanje1= True
                        while brisanje1:
                            try:
                                polje_za_brisanje2= int(input('\nUnesite polje da bi obrisali piuna igraca 1:'))

                                if polje_za_brisanje2>23:
                                    print('\nBroj koji ste uneli ne oznacava nijedno polje!\n')
                                
                                if hash_map[polje_za_brisanje2]=='1':
                                    hash_map[polje_za_brisanje2]='X'
                                    printTable(hash_map)
                                    brisanje1=False
                                else:
                                    print('\nNiste uneli pravilno polje!\n')

                            except:
                                print('\nNiste pravilno uneli polje!\n')

                    igrac2=False

                else:
                    print("\nPolje koje zelite da odigrate je zauzeto.\n")

            except:
                print("\nBroj koji ste uneli ne oznacava nijedno polje.\n")

    print("\n")    
    print('--Faza 2--')
    print('\n')

    print('Jednostruka pot mica:')
    print(potencijalna_mica(hash_map))
    # Igrac1 na potezu
    print('\nDvostruka pot mica')
    print(potencijalne_dve_mice(hash_map))
    print('\nBroj obicnih mica:')
    print(broj_mica(hash_map))
    print('\ndvostruka mica:')
    print(dve_mice(hash_map))


    printTable(hash_map)

    while True:

        igrac1 = True
        while igrac1:
            try:
                polje1= int(input('Igrac 1, unesite polje koje zelite da pomerate:'))
                if  polje1 > 23:
                    print("\nBroj koji ste uneli ne oznacava nijedno polje\n")
                    continue
                if hash_map[polje1]=='1':

                    moguce_pozicije = provera_pozicije(polje1)
                    if potencijalno_blokiran(hash_map,moguce_pozicije):

                        igrac1_pozicija = True

                        while igrac1_pozicija:
                            try:
                                pozicija = int(input('\nUnesite poziciju gde zelite da pomerite polje:'))

                                
                                if pozicija > 23:
                                    print('\nBroj koji ste uneli ne oznacava nijedno polje!\n')
                                    continue
                                
                                if hash_map[pozicija]=='X':

                                    moguce_pozicije = provera_pozicije(polje1)
                                    brojac1 = 0
                                    for i in moguce_pozicije:
                                        if i==pozicija:
                                            brojac1 += 1
                                            hash_map[pozicija]='1'
                                            hash_map[polje1]='X'
                                            igrac1_pozicija=False
                                

                                if brojac1 ==0:
                                    print('\nNepravilan unos polja za pomeranje!\n')

                                else:
                                    printTable(hash_map)
                                
                            except:
                                print('\nNepravilan unos polja!\n')
                    else:
                        print('\nNe mozete izabrati dato polje!\n')
                        continue

                    if mica(pozicija,hash_map):
                        print('\nCestitamo sklopili ste micu!\n')

                        brisanje2= True

                        while brisanje2:
                            try:
                                polje_za_brisanje1= int(input('\nUnesite polje da bi obrisali protivnikovog igraca:'))

                                if polje_za_brisanje1>23:
                                    print('Broj koji ste uneli ne oznacava nijedno polje!')
                                
                                if hash_map[polje_za_brisanje1]=='2':
                                    hash_map[polje_za_brisanje1]='X'
                                    printTable(hash_map)
                                    brisanje2=False
                                    igrac1 = False
                                
                                else:
                                    print('\nNiste uneli pravilno polje!')
                            except:
                                print('Niste pravilno uneli polje!')
               
                    else:
                        igrac1 = False
                else:
                    print("\nNepravilan unos polja!\n")

            except:
                print('\nBroj koji ste uneli ne oznacava nijedno polje.\n')

        simbol2 = '2'
        if broj_preostalih(simbol2,hash_map) < 3:
            print('\n--POBEDNIK JE IGRAC 1--\n')
            break

        if provera_svih_blokiranih(hash_map,simbol2):
            print('\n--POBEDNIK JE IGRAC 1--\n')
            break

        igrac2 = True

        while igrac2:
            try:
                polje2= int(input('Igrac 2, unesite polje koje zelite da pomerate:'))

                if  polje2 > 23:
                    print("\nBroj koji ste uneli ne oznacava nijedno polje\n")
                    continue

                if hash_map[polje2]=='2':
                    
                    moguce_pozicije = provera_pozicije(polje2)
                    if potencijalno_blokiran(hash_map,moguce_pozicije):

                        igrac1_pozicija = True

                        while igrac1_pozicija:
                            try:
                                pozicija = int(input('\nUnesite poziciju gde zelite da pomerite polje:'))

                                if pozicija > 23:
                                    print('\nBroj koji ste uneli ne oznacava nijedno polje!\n')
                                    continue
                                
                                if hash_map[pozicija]=='X':

                                    moguce_pozicije = provera_pozicije(polje2)
                                    brojac2 = 0
                                    for i in moguce_pozicije:
                                        if i==pozicija:
                                            brojac2 += 1
                                            hash_map[pozicija]='2'
                                            hash_map[polje2]='X'
                                            igrac1_pozicija=False
                                

                                if brojac2 ==0:
                                    print('\nNepravilan unos polja za pomeranje!\n')
                                
                                else:
                                    printTable(hash_map)

                            except:
                                print('\nNepravilan unos polja!\n')
                    else:
                        print('\nNe mozete izabrati dato polje!\n')
                        continue

                    if mica(pozicija,hash_map):

                        print('\nCestitamo sklopili ste micu!\n')

                        brisanje1= True

                        while brisanje1:
                            try:
                                polje_za_brisanje2= int(input('\nUnesite polje da bi obrisali protivnikovog igraca:'))

                                if polje_za_brisanje2>23:
                                    print('Broj koji ste uneli ne oznacava nijedno polje!')
                                
                                if hash_map[polje_za_brisanje2]=='1':
                                    hash_map[polje_za_brisanje2]='X'
                                    printTable(hash_map)
                                    brisanje1=False
                                    
                                
                                else:
                                    print('\nNiste uneli pravilno polje!')
                            except:
                                print('Niste pravilno uneli polje!')
                    
                    igrac2 = False

                else:
                    print("\nNepravilan unos polja!\n")

            except:
                print('\nBroj koji ste uneli ne oznacava nijedno polje.\n')
        
        simbol1 = '1'
        if broj_preostalih(simbol1,hash_map) < 3:
            print('\n--POBEDNIK JE IGRAC 2--\n')
            break

        if provera_svih_blokiranih(hash_map,simbol1):
            print('\n--POBEDNIK JE IGRAC 2--\n')
            break


if __name__=='__main__':
    human_v_human()
  


    
  
    