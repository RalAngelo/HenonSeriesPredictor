from windowResources.PredictionPresentationResources.resources.codeResources.generate_500 import*
import numpy as np
import math
from windowResources.PredictionPresentationResources.resources.codeResources.apprentissage_2 import*

poid_1_2 = b2[indice_min_loc_nmse]
poid_2_3 = c2[indice_min_loc_nmse]

def sigmoide(x):
    return 1 / (1 + math.exp(-x))

def identite(x):
    return x

def prediction(prot_1, prot_2):
    
    predit = 0
    v_cacher = np.zeros(2)
    prot = np.array([prot_1, prot_2])
    
    def val_couche_cacher():
        v_1 = 0
        for i in range(2):
            v_1 += poid_1_2[0, i] * prot[i]
            v_cacher[0] = sigmoide(v_1)
        v_2 = 0
        for i in range(2):
            v_2 += poid_1_2[1, i] * prot[i]
            v_cacher[1] = sigmoide(v_2)
        return v_cacher
    
    def val_couche_sortie():
        v_s_1 = 0
        for i in range(2):
            v_s_1 += poid_2_3[0, i] * val_couche_cacher()[i]
        return identite(v_s_1)
    
    predit = val_couche_sortie()

    return predit

# la fonction suivante presente 2 paramètre "nbr" et "debut"
# dont "nbr" represente le nombre de pas d' apprentissage en avant pour 
# la prediction. Et "debut" represente l' indice du premier prototype
# ou l' on veut commencer. 
def iteration(nbr, debut):
    val = np.empty(nbr)
    prototype = np.empty((nbr, 2))
    val[0] = prediction(liste_X_n[debut], liste_X_n[debut + 1])
    val[1] = prediction(val[0], liste_X_n[debut])
    
    for i in range(nbr):
        for j in range(2):
            if i == 0:
                prototype[i, j] = liste_X_n[debut + j]
            if i == 1:
                if j == 0:
                    prototype[i, j] = val[0]
                if j == 1:
                    prototype[i, j] = liste_X_n[debut]
            if i != 0 and i != 1:
                prototype[i, j] = val[i - (j + 1)] 
        if i != 0 and i != 1:
            val[i] = prediction(val[i - 1], val[i - 2])
    return val, prototype