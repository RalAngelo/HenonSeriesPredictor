import matplotlib.pyplot as plt
from windowResources.PredictionPresentationResources.resources.prediction import*
from windowResources.PredictionPresentationResources.resources.codeResources.generate_500 import*

x = np.arange(0, 10, dtype=int)
def y():
    val_y = np.empty(10)
    for j in range(10):
        val_y[j] = liste_X_n[1 + j]
    return val_y
def z():
    val_z = np.empty(10)
    for j in range(10):
        val_z[j] = iteration(10, 1)[0][j]
    return val_z

y = y()
z = z()
def courbe_pred_10():        
    plt.plot(x, y, label = r'Values to predict')
    plt.plot(x, z, label = r'Values given by the network')
    plt.xlabel('INDEX')
    plt.ylabel('VALUE')
    plt.title('ten-step-ahead prediction')
    plt.legend(loc=0)
    plt.show()
