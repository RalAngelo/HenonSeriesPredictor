import matplotlib.pyplot as plt
from windowResources.PredictionPresentationResources.resources.prediction import*
from windowResources.PredictionPresentationResources.resources.codeResources.generate_500 import*

x = np.arange(0, 20, dtype=int)
def y():
    val_y = np.empty(20)
    for j in range(20):
        val_y[j] = liste_X_n[1 + j]
    return val_y
def z():
    val_z = np.empty(20)
    for j in range(20):
        val_z[j] = iteration(20, 1)[0][j]
    return val_z

y = y()
z = z()
def courbe_pred_20():        
    plt.plot(x, y, label = r'Values to predict')
    plt.plot(x, z, label = r'Values given by the network')
    plt.xlabel('INDEX')
    plt.ylabel('VALUE')
    plt.title('twenty-step-ahead prediction')
    plt.legend(loc=0)
    plt.show()
