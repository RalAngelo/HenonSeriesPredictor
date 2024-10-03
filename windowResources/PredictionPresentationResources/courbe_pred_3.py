import matplotlib.pyplot as plt
from windowResources.PredictionPresentationResources.resources.prediction import*
from windowResources.PredictionPresentationResources.resources.codeResources.generate_500 import*

x = np.arange(0, 3, dtype=int)
def y():
    val_y = np.empty(3)
    for j in range(3):
        val_y[j] = liste_X_n[15 + j]
    return val_y
def z():
    val_z = np.empty(3)
    for j in range(3):
        val_z[j] = iteration(3, 15)[0][j]
    return val_z

y = y()
z = z()
def courbe_pred_3():        
    plt.plot(x, y, label = r'Values to predict')
    plt.plot(x, z, label = r'Values given by the network')
    plt.xlabel('INDEX')
    plt.ylabel('VALUE')
    plt.title('three-step-ahead prediction')
    plt.legend(loc=0)
    plt.show()
