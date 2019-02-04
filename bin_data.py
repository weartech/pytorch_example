'''
    Visualize some basic statistics of our dataset.
'''
import numpy as np
import string
import matplotlib.pyplot as plt

if __name__ == "__main__":
    instances = np.load("./data/instances.npy")
    labels = np.load("./data/labels.npy")

    alphabet = list(string.ascii_lowercase) # Get all letters

    averages = np.zeros((len(alphabet), 6))
    std_devs = np.zeros((len(alphabet), 6))

    for letter_index in range(0, len(alphabet)):
        x = np.array([])
        y = np.array([])
        z = np.array([])
        w1 = np.array([])
        w2 = np.array([])
        w3 = np.array([])

        parameters = [x, y, z, w1, w2, w3]

        for i in range(len(labels)):
            if(labels[i] == alphabet[letter_index]):
                # Update average and standard deviation corresponding to letter
                for j in range(0, 6):
                    parameters[j] = np.append(parameters[j], instances[i][:,j + 1])

        for i in range(0, 6):
            averages[letter_index][i] = np.mean(parameters[i])
            std_devs[letter_index][i] = np.std(parameters[i])

    # Choosing letters c, p, and x:
    letters = [2, 15, 23] # Indexes corresponding to letter c, p, and x
    x_labels = ["x Acceleration", "y Acceleration", "z Acceleration", "Pitch", "Roll", "Yaw"]

    for letter in letters:
        y_averages = [averages[letter][0], averages[letter][1], averages[letter][2], averages[letter][3], averages[letter][4], averages[letter][5]]
        y_std_devs = [std_devs[letter][0], std_devs[letter][1], std_devs[letter][2], std_devs[letter][3], std_devs[letter][4], std_devs[letter][5]]

        plt.figure()
        plt.title(alphabet[letter])
        plt.bar(x_labels, y_averages, yerr=y_std_devs)
        plt.savefig(alphabet[letter] + "_bar.png")
