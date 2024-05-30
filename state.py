from operator import truediv
from hashmap import ChainedHashMap

def mapiranje():
    hash_map = ChainedHashMap()
    
    for i in range(24):
        hash_map[i]='X'

    return hash_map


def printTable(hash_map):
    
    print(hash_map[0] + "(0)----------------------" + hash_map[1] +
          "(1)------------------------" + hash_map[2] + "(2)")
    print("|                           |                           |")
    print("|                           |                           |")
    print("|       " + hash_map[3] + "(3)--------------" +
          hash_map[4] + "(4)-----------------" + hash_map[5] + "(5)     |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       |        " + hash_map[6] + "(6)-----" +
          hash_map[7] + "(7)-----" + hash_map[8] + "(8)          |      |")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print(hash_map[9] + "(9)---" + hash_map[10] + "(10)----" + hash_map[11] + "(11)               " +
          hash_map[12] + "(12)----" + hash_map[13] + "(13)---" + hash_map[14] + "(14)")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print("|       |        " + hash_map[15] + "(15)-----" +
          hash_map[16] + "(16)-----" + hash_map[17] + "(17)       |      |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       " + hash_map[18] + "(18)--------------" +
          hash_map[19] + "(19)--------------" + hash_map[20] + "(20)     |")
    print("|                           |                           |")
    print("|                           |                           |")
    print(hash_map[21] + "(21)----------------------" + hash_map[22] +
          "(22)----------------------" + hash_map[23] + "(23)")
    print("\n")



def slobodno_polje(polje,hash_map):

    if not  0<= int(polje) <=24:
        print("Niste pravilno uneli polje za igru, unesite opet")
        return False

    if  hash_map[polje]!="X":
        print("Izabrano polje je vec zauzeto, probajte ponovo sa unosom.")
        return False

    
    return True


def mica_dupla(polje):
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
    polja_za_micu = []
    for mica in sve_mice:
        if polje in mica:
            polja_za_micu.append(mica)

    return polja_za_micu
        

def brojac_svih_mica(igrac,hash_map):
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
    brojac = 0 
    for mica in sve_mice:

        if  hash_map[mica[0]]==hash_map[mica[1]]==hash_map[mica[2]] == igrac:
            brojac += 1

    return brojac

def moguce_obrisati(hash_map):
    lista_poteza = []
    lista_poteza1 = [] 
    brojac_piuna = 0
    brojac_mica = 0
    for item in hash_map:
            
        if hash_map[item]=='2':
            brojac_piuna += 1
            if mica(item,hash_map):
                brojac_mica += 1
                lista_poteza.append(item)

            else:
                lista_poteza1.append(item)
        

    if brojac_mica == brojac_piuna:
        return lista_poteza

    else:
        return lista_poteza1

    
def mica(polje,hash_map):
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
        if polje in mica:
            if hash_map[mica[0]]==hash_map[mica[1]]==hash_map[mica[2]]:
                return True
    
    return False

def poslednji_potez(hash_map1,hash_map2):
    for item in hash_map2:

        if hash_map1[item] != hash_map2[item] and hash_map2[item] =='2':
            return item


def potez_brisanje(hash_map1,hash_map2):

    for item in hash_map2:

        if hash_map1[item] != hash_map2[item] and hash_map2[item] =='X':
            return item
    


def provera_pozicije(pozicija):
    moguce_pozicije = [
        [9,1],
        [0,4,2],
        [1,4],
        [10,4],
        [1,3,7,5],
        [4,13],
        [11,7],
        [6,4,8],
        [7,12],
        [0,21,10],
        [9,3,18,11],
        [10,6,15],
        [8,17,13],
        [12,5,20,14],
        [13,2,23],
        [11,16],
        [15,17,19],
        [12,16],
        [10,19],
        [18,16,20,22],
        [19,13],
        [9,22],
        [21,19,23],
        [22,14]
        
    ]
    return moguce_pozicije[pozicija]

def potencijalno_blokiran(hash_map,pozicije):
    for pozicija in pozicije:
        if hash_map[pozicija]=='X':
            return True
    
    return False

def moguci_potezi(hash_map,moguce_pozicije):
    lista_pozicija = []
    for pozicije in moguce_pozicije:
        if hash_map[pozicije] == 'X':
            lista_pozicija.append(pozicije)
    
    return lista_pozicija



def broj_preostalih(simbol,hash_map):
    brojac = 0
    for item in hash_map:
        if hash_map[item]==simbol:
            brojac +=1

    return brojac

def provera_svih_blokiranih(hash_map,igrac):
    lista_svih_piuna = []
    for piun in hash_map:
        if hash_map[piun]==igrac:
            lista_svih_piuna.append(piun)

    brojac_blokiranih = 0
    for piun in lista_svih_piuna:
        mogouci_potezi = provera_pozicije(piun)
        if not potencijalno_blokiran(hash_map,mogouci_potezi):
            brojac_blokiranih += 1        

    if brojac_blokiranih== len(lista_svih_piuna):
        return True

    else:
        return False    