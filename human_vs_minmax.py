
from copy import deepcopy
from minmax import minimax
from time import time
from state import *


    

def igra():
    hash_map = mapiranje()

    printTable(hash_map)

    for i in range(9):
        
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
                                
                                lista_za_obrisati = moguce_obrisati(hash_map)

                                if polje_za_brisanje1 in lista_za_obrisati:
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
        hash_map_copy = deepcopy(hash_map)
        
        while igrac2:
            
            vreme1 = time()
            hash_map = minimax(hash_map,2,1)
            vreme2 = time()
            
            printTable(hash_map)


            print('Vreme izvrsavanja poteza:',vreme2 - vreme1)
            polje21 = poslednji_potez(hash_map_copy,hash_map)

            print('\nIgrac 2 je ODIGRAO polje:' + str(polje21))

            if mica(polje21,hash_map):
                print('\nIGRAC 2 JE SKLOPIO MICU!\n')
                brisanje2= True

                hash_map_copy = deepcopy(hash_map)

                while brisanje2:
                    
                    vreme1 = time()
                    hash_map = minimax(hash_map,2,2)
                    vreme2 = time()
                
                    printTable(hash_map)
                    
                    print('Vreme brisanja figure:',vreme2 - vreme1)

                    polje21 = potez_brisanje(hash_map_copy,hash_map)

                    print('\nIgrac 2 je OBRISAO polje:' + str(polje21))

                    brisanje2 = False


            igrac2=False


    print("\n")    
    print('--FAZA 2--')
    print('\n')

    # Igrac1 na potezu
   
    printTable(hash_map)

    while True:

        igrac1 = True
        while igrac1:
            try:
                polje1= int(input('Igrac 1, unesite polje koje zelite da pomerate:'))
                if  polje1 > 23:
                    print("\nBroj koji ste uneli ne oznacava nijedno polje\n")
                    continue

                if hash_map[polje1] == '1':

                    moguce_pozicije = provera_pozicije(polje1)
                    if potencijalno_blokiran(hash_map,moguce_pozicije):
                        
                        stampanje_poteza = moguci_potezi(hash_map,moguce_pozicije)
                        print('moguce pozicije su:' ,stampanje_poteza)

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
                                
                                lista_za_obrisati = moguce_obrisati(hash_map)

                                if polje_za_brisanje1 in lista_za_obrisati:

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

        hash_map_copy = deepcopy(hash_map)
        

        while igrac2:
            
            vreme1 = time()
            hash_map = minimax(hash_map,3,3)
            vreme2 = time()
            printTable(hash_map)
            print('Vreme izvrsavanja poteza:',vreme2 - vreme1)


            polje21 = poslednji_potez(hash_map_copy,hash_map)

            print('\nIgrac 2 je ODIGRAO polje:' + str(polje21))


            if mica(polje21,hash_map):
                print('\nIGRAC 2 JE SKLOPIO MICU!\n')
                brisanje2= True

                hash_map_copy = deepcopy(hash_map)

                while brisanje2:
                    vreme1 = time()
                    hash_map = minimax(hash_map,2,2)
                    vreme2 = time()

                    printTable(hash_map)
                    print('Vreme brisanja figure:',vreme2 - vreme1)
                    polje21 = potez_brisanje(hash_map_copy,hash_map)

                    print('\nIgrac 2 je OBRISAO polje:' + str(polje21))

                    brisanje2 = False


            igrac2=False

        
        simbol1 = '1'
        if broj_preostalih(simbol1,hash_map) < 3:
            print('\n--POBEDNIK JE IGRAC 2--\n')
            break

        if provera_svih_blokiranih(hash_map,simbol1):
            print('\n--POBEDNIK JE IGRAC 2--\n')
            break