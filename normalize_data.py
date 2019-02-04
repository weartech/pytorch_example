'''
    Normalize the data, save as ./data/normalized_data.npy
'''
import numpy as np

if __name__ == "__main__":
    instances = np.load("./data/instances.npy")
    for i in range(0, instances.shape[0]):
        for j in range(1, 7):
            mean = np.sum(instances[i][:,j])
            mean /= 100
            std_dev = 0
            for k in range(0, 100):
                std_dev += (instances[i][k][j] - mean) ** 2
            std_dev /= 100
            std_dev = std_dev ** (1/2)

            for k in range(0, 100):
                instances[i][k][j] = (instances[i][k][j] - mean) / std_dev

    np.save("./data/normalized_data", instances)
