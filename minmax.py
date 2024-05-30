from copy import deepcopy
from json.encoder import INFINITY
from sys import api_version
from heuristics import heuristika1,heuristika2
from state import mica,provera_pozicije

def svi_potezi(hash_map,igrac,faza):
    lista_poteza = []
    if faza == 1:
        for item in hash_map:
            if hash_map[item]=='X':
                hash_map_copy = deepcopy(hash_map)
                hash_map_copy[item] = igrac
                lista_poteza.append(hash_map_copy)
        
        return lista_poteza
    
    elif faza== 2:
        lista_poteza1 = []
        brojac_piuna = 0
        brojac_mica = 0
        for item in hash_map:
            
            if hash_map[item]!=igrac and hash_map[item]!='X':
                brojac_piuna += 1
                if mica(item,hash_map):
                    brojac_mica += 1
                    hash_map_copy1 = deepcopy(hash_map)
                    hash_map_copy1[item] = 'X'
                    lista_poteza1.append(hash_map_copy1)
                else:
                    hash_map_copy = deepcopy(hash_map)
                    hash_map_copy[item] = 'X'
                    lista_poteza.append(hash_map_copy)
        
        if brojac_mica == brojac_piuna:
            return lista_poteza1

        else:
            return lista_poteza
    
    elif faza == 3:
        for item in hash_map:
            if hash_map[item]==igrac:
                moguce_pozicije = provera_pozicije(item)
                for pozicija in moguce_pozicije:
                    if hash_map[pozicija]=='X':
                        hash_map_copy = deepcopy(hash_map)
                        hash_map_copy[pozicija]= igrac
                        hash_map_copy[item]='X'
                        lista_poteza.append(hash_map_copy)
        
        return lista_poteza



def max1(hash_map,dubina,alfa,beta,faza):
    igrac = '1'

    if dubina == 0 and (faza==1 or faza==2):
        return heuristika1(hash_map)

    if dubina == 0 and (faza==3 or faza==2):
        return heuristika2(hash_map)

    potezi = svi_potezi(hash_map,igrac,faza)

    
    for move in potezi:
        skor = min1(move,dubina-1,alfa,beta,faza)
        alfa = max(alfa,skor)

        if alfa >= beta:
            return beta
    
    return alfa

def min1(hash_map,dubina,alfa,beta,faza):
    igrac = '2'

    if dubina == 0 and (faza==1 or faza==2):
        return heuristika1(hash_map)

    if dubina == 0 and (faza==3 or faza==2):
        return heuristika2(hash_map)

    potezi = svi_potezi(hash_map,igrac,faza)

    
    for move in potezi:
        skor = max1(move,dubina-1,alfa,beta,faza)
        beta = min(beta,skor)

        if alfa >= beta:
            return alfa
    
    return beta



def minimax(hash_map,dubina,faza):
    najbolji_potez = None
    alfa = -INFINITY
    beta = INFINITY
    igrac =  '2'
    potezi = svi_potezi(hash_map,igrac,faza)
    

    for potez in potezi:
        rezultat = max1(potez,dubina-1,alfa,beta,faza)
        if rezultat > alfa:
            alfa = rezultat
            najbolji_potez = potez
    
    return najbolji_potez

