import numpy as np
import matplotlib.pyplot as plt
import os


class ImageProcessor:
    def __init__(self):
        pass

    def load(self, path):
        img_array = plt.imread(path)
        print('Loading image of dimensions {} x {}'.format(
              img_array.shape[0],
              img_array.shape[1]))
        return img_array

    def display(self, array):
        _, ax = plt.subplots()
        ax.imshow(array)
        ax.set_axis_off()
        plt.show()


if __name__ == "__main__":
    imp = ImageProcessor()

    arr = imp.load("../resources/42AI.png")
    print(arr)
    print(type(arr))
    imp.display(arr)
