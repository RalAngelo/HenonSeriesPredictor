from windowResources.PredictionPresentationResources.resources.codeResources.generate_500 import*
import numpy as np
import math
from windowResources.PredictionPresentationResources.resources.codeResources.apprentissage_2 import*

poid_1_2 = b2[indice_min_loc_nmse]
poid_2_3 = c2[indice_min_loc_nmse]

#g(somme_j(W_ij^m * V_j^m-1))

def sigmoide(x):
    return 1 / (1 + math.exp(-x))

def identite(x):
    return x

def prediction_un_pas():
    prototype = np.zeros((501, 2))
    valeur_predite = np.zeros(500)
    v_cacher = np.zeros(2)
    #creation prototype:
    for j in range(501):
        for i in range(2):
            if i == 0:
                prototype[j, i] = liste_X_n[j]
            if i == 1:
                prototype[j, i] = liste_X_n[j + 1]
    #prediction
    def val_couche_cacher(nbr):
        
        v_1 = 0
        for i in range(2):
            v_1 += poid_1_2[0, i] * prototype[nbr, i]
            v_cacher[0] = sigmoide(v_1)

        v_2 = 0
        for i in range(2):
            v_2 += poid_1_2[1, i] * prototype[nbr, i]
            v_cacher[1] = sigmoide(v_2)
        
        return v_cacher
    
    def val_couche_sortie(nbr):
        v_s_1 = 0
        for i in range(2):
            v_s_1 += poid_2_3[0, i] * val_couche_cacher(nbr)[i]
        return identite(v_s_1)

    for i in range(500):
        valeur_predite[i] = val_couche_sortie(i)
    return  valeur_predite, prototype    
