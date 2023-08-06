# ---------------------------------------------------------------------------- #
#                                    Import                                    #
# ---------------------------------------------------------------------------- #
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------- #
#                                   Constants                                  #
# ---------------------------------------------------------------------------- #
SETOSA = 0
VERSICOLOR = 1
VIRGINICA = 2

FLOWER_LIST = ['Iris-setosa','Iris-versicolor','Iris-virginica']

# ---------------------------------------------------------------------------- #
#                                   Functions                                  #
# ---------------------------------------------------------------------------- #



# --------------------- Determine distance another flower -------------------- #
def determine_dist(array1,array2):
    temp_array = array1 - array2
    
    res = 0
    for i in temp_array:
        res += i*i

    return res

# ---------------------------- Categorize flowers ---------------------------- #
def categorize(training,category):
    temp = np.array([])

    for i in training:
        if i[4] == category:
            temp = np.append(temp,i)

    temp = np.split(temp,len(temp)/5)

    return temp


# ------------------------- Find number of neighbours ------------------------ #
def find_number_of_neighbours(data, element, k):

    neighbours = 0

    for i in data:
        if determine_dist(i[0:4],element[0:4]) < k*k:
            neighbours += 1

    return neighbours


# ------------------ Nearest neighbouring flower in radius k ----------------- #
def nearest_flower(flower, k):
    global setosa
    global versicolor
    global virginica

    res = []

    # Find number of neighbours for the current element
    numb_setosa = find_number_of_neighbours(setosa,flower,k)
    numb_versicolor = find_number_of_neighbours(versicolor,flower,k)
    numb_virginica = find_number_of_neighbours(virginica,flower,k)

    # Find the flower with the most neighbours 
    # (if this number is the same for two flower the flower with lowest index in the list will be chosen)
    max_idx = np.argmax([numb_setosa,numb_versicolor, numb_virginica])

 
    
    return FLOWER_LIST[max_idx]


# ---------------------------- Accuracy of k value --------------------------- #
def k_nearest_nb_accuracy(k_start,k_end,k_step):
    global data_training
    global data_test

    res = []

    k_list = np.arange(k_start, k_end, k_step)

    for k in k_list:
        true_cnt = 0
        for i in data_test:
            if nearest_flower(i, k) == i[4]:
                true_cnt += 1
            

        accuracy = 100 * true_cnt / len(data_training)
        res.append(accuracy)
    return res
    
    
    # ------------------------- Add labels in matplotlib ------------------------- #
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')
    





# ---------------------------------------------------------------------------- #
#                                   Variables                                  #
# ---------------------------------------------------------------------------- #
data = pd.read_csv('iris.csv').to_numpy()
setosa = np.array([])
versicolor = np.array([])
virginica = np.array([])

#print(len(data))

data_training = []
data_test = []

# ---------------------------------------------------------------------------- #
#                                     Main                                     #
# ---------------------------------------------------------------------------- #



def main():
    global data

    global setosa
    global versicolor
    global virginica

    global data_training
    global data_test

    
    # As there are equally many flowers of each group 
    # they will be split by every other element.
    for i in range(len(data)):
        if i % 2 == 0:
            data_training = np.append(data_training,data[i])
        else:
            data_test = np.append(data_test,data[i])


 

    data_test = np.split(data_test,len(data_test)/5)
    data_training = np.split(data_training,len(data_training)/5)




    setosa = categorize(data_training,'Iris-setosa')
    versicolor = categorize(data_training,'Iris-versicolor')
    virginica = categorize(data_training,'Iris-virginica')



    # Calculate accuracy
    k_start = 0
    k_end = 2
    k_step = 0.2

    k_range = np.around(np.arange(k_start,k_end,k_step),2)
    accuracy = np.around(k_nearest_nb_accuracy(k_start,k_end,k_step),2)


 
    # Plot data
    x = np.array(list(map(str,k_range)))
    y = np.array(accuracy)
    plt.xlabel("K")
    plt.ylabel("Accuracy (%)")
    addlabels(x,y)
    plt.title("Accuracy for different values of k")
    plt.bar(x,y)

    plt.show()







    







if __name__ == "__main__":
    main()
