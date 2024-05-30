from state import mica,provera_pozicije,brojac_svih_mica,mica_dupla,broj_preostalih,provera_svih_blokiranih

def blokirana_mica(hash_map):

    igrac1 = '1'
    brojac1 = blokirana_polu_mica(igrac1,hash_map)

    igrac2 = '2'
    brojac2 = blokirana_polu_mica(igrac2,hash_map)

    brojac = brojac1 - brojac2

    return brojac


def broj_mica(hash_map):
    igrac1 = '1'
    brojac1 = brojac_svih_mica(igrac1,hash_map)

    igrac2 = '2'
    brojac2 = brojac_svih_mica(igrac2,hash_map)

    brojac = brojac2 - brojac1


    return brojac



def broj_blokiranih(hash_map):
    brojac1 = 0
    brojac2 = 0
    for item in hash_map:
        if hash_map[item]== '1':

            lista_pozicija = provera_pozicije(item)
            broj1 = 0
            for pozicija in lista_pozicija:
                if hash_map[pozicija]=='2':
                    broj1 +=1 
                
            if broj1 == len(lista_pozicija):
                brojac1 += 1

        elif hash_map[item]=='2':

            lista_pozicija = provera_pozicije(item)
            broj2 = 0
            for pozicija in lista_pozicija:
                if hash_map[pozicija]=='1':
                    broj2 +=1
            
            if broj2 ==len(lista_pozicija):
                brojac2 += 1

    
    brojac = brojac1 - brojac2

    return brojac

def broj_piuna(hash_map):
    brojac1 = 0
    brojac2 = 0
    for item in hash_map:
        if hash_map[item]=='1':
            brojac1 +=1
        
        elif hash_map[item]=='2':
            brojac2 += 1

        else: 
            pass

    brojac = brojac2 - brojac1
    return brojac


def polu_mica_jednog_igraca(igrac,hash_map):
    brojac = 0
    sve_mice=[
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [9,10,11],
        [12,13,14],
        [15,16,17],
        [18,19,20],
        [21,22,23],
        [0,9,21],
        [3,10,18],
        [6,11,15],
        [1,4,7],
        [16,19,22],
        [8,12,17],
        [5,13,20],
        [2,14,23],
    ]
    for mica in sve_mice:
        if (hash_map[mica[0]]==hash_map[mica[1]]==igrac and hash_map[mica[2]]=='X') or (hash_map[mica[0]]==hash_map[mica[2]]==igrac and hash_map[mica[1]]=='X') or (hash_map[mica[1]]==hash_map[mica[2]]==igrac and hash_map[mica[0]]=='X'):
            brojac += 1

    return brojac

def blokirana_polu_mica(igrac,hash_map):
    brojac = 0
    sve_mice=[
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [9,10,11],
        [12,13,14],
        [15,16,17],
        [18,19,20],
        [21,22,23],
        [0,9,21],
        [3,10,18],
        [6,11,15],
        [1,4,7],
        [16,19,22],
        [8,12,17],
        [5,13,20],
        [2,14,23],
    ]
    for mica in sve_mice:
        if (hash_map[mica[0]]==hash_map[mica[1]]==igrac and hash_map[mica[2]]!='X' and hash_map[mica[2]]!=igrac) or (hash_map[mica[0]]==hash_map[mica[2]]==igrac and hash_map[mica[1]]!='X' and hash_map[mica[1]]!=igrac ) or (hash_map[mica[1]]==hash_map[mica[2]]==igrac and hash_map[mica[0]]!='X' and hash_map[mica[0]]!=igrac):
            brojac += 1

    return brojac


def potencijalna_mica(hash_map):
    igrac1 = '1'
    brojac1 = polu_mica_jednog_igraca(igrac1,hash_map)

    igrac2 = '2'
    brojac2 = polu_mica_jednog_igraca(igrac2,hash_map)

    brojac = brojac2 -brojac1

    return brojac
 

def potencijalne_dve_mice(hash_map):
    brojac1 = 0
    brojac2 = 0

    for item in hash_map:

        if hash_map[item]=='1':

            polja_za_micu = mica_dupla(item)
            broj_piuna = 0
            broj_piuna1 = 0
            polje_protivnika = 0
            polje_protivnika1 = 0
            for i in polja_za_micu[0]:
                if hash_map[i]=='1':
                    broj_piuna += 1
                
                if hash_map[i]=='2':
                    polje_protivnika += 1

            for i in polja_za_micu[1]:
                if hash_map[i]=='1':
                    broj_piuna1 += 1

                if hash_map[i]=='2':
                    polje_protivnika1 += 1

            if broj_piuna == 2 and broj_piuna1 ==2 and polje_protivnika==0 and polje_protivnika1==0 :
                brojac1 += 1
        
        if hash_map[item]=='2':

            polja_za_micu = mica_dupla(item)
            broj_piuna = 0
            broj_piuna2 = 0
            polje_protivnika = 0
            polje_protivnika2 = 0
            for i in polja_za_micu[0]:
                if hash_map[i]=='2':
                    broj_piuna += 1
                
                if hash_map[i]=='1':
                    polje_protivnika += 1
            
            for i in polja_za_micu[1]:
                if hash_map[i] == '2':
                    broj_piuna2 += 1

                if hash_map[i]=='1':
                    polje_protivnika2 += 1
            
            if broj_piuna== 2 and broj_piuna2 == 2 and polje_protivnika==0 and polje_protivnika2==0:
                brojac2 += 1
    
    brojac = brojac2 - brojac1
    
    return brojac



def dve_mice(hash_map):
    brojac1 = 0
    brojac2 = 0

    for item in hash_map:

        if hash_map[item]=='1':

            polja_za_micu = mica_dupla(item)
            broj_piuna = 0
            broj_piuna1 = 0
            for i in polja_za_micu[0]:
                if hash_map[i]=='1':
                    broj_piuna += 1

            for i in polja_za_micu[1]:
                if hash_map[i]=='1':
                    broj_piuna1 += 1

            if broj_piuna == 3 and broj_piuna1 == 3 :
                brojac1 += 1
        
        if hash_map[item]=='2':

            polja_za_micu = mica_dupla(item)
            broj_piuna = 0
            broj_piuna2 = 0
            for i in polja_za_micu[0]:
                if hash_map[i]=='2':
                    broj_piuna += 1
            
            for i in polja_za_micu[1]:
                if hash_map[i] == '2':
                    broj_piuna2 += 1
            
            if broj_piuna== 3 and broj_piuna2 == 3:
                brojac2 += 1
    
    brojac = brojac2 - brojac1
    
    return brojac
        
def pobeda(hash_map):
    igrac1 = '2'
    igrac2 = '1'

    if broj_preostalih(igrac1,hash_map) < 3:
        return 1

    if broj_preostalih(igrac2,hash_map) < 3:
        return -1

    if provera_svih_blokiranih(hash_map,igrac1):
        return 1
    
    if provera_svih_blokiranih(hash_map,igrac2):
        return -1
    
    return 0
    
#  18 * (1) + 26 * (2) + 1 * (3) + 9 * (4) + 10 * (5) + 7 * (6)

def heuristika1(hash_map):
    mica_blok = blokirana_mica(hash_map)
    mica = broj_mica(hash_map)
    blokiranih = broj_blokiranih(hash_map)
    piuna = broj_piuna(hash_map)
    pot_mica = potencijalna_mica(hash_map)
    pot_2_mice = potencijalne_dve_mice(hash_map)
    
    heuristika =18*mica_blok + 30*mica + 1*blokiranih + 9*piuna + 7*pot_mica + 5*pot_2_mice

    return heuristika


# 14 * (1) + 43 * (2) + 10 * (3) + 11 * (4) + 8 * (7) + 1086 * (8)
def heuristika2(hash_map):
    mica_blok = blokirana_mica(hash_map)
    mica = broj_mica(hash_map)
    blokiranih = broj_blokiranih(hash_map)
    piuna = broj_piuna(hash_map)
    mice_2 = dve_mice(hash_map)
    status_igre = pobeda(hash_map)

    heuristika = 14*mica_blok + 43*mica + 10*blokiranih + 11*piuna + 8*mice_2 + 1086*status_igre

    return heuristika
    



