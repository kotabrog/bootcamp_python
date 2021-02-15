import numpy as np
import matplotlib.pyplot as plt


class ScrapBooker:
    def __init__(self):
        pass

    def crop(self, array, dimensions, position=(0, 0)):
        if array.shape[0] < dimensions[0] + position[0] or\
           array.shape[1] < dimensions[1] + position[1]:
            return None
        return array[position[0]: position[0] + dimensions[0],
                     position[1]: position[1] + dimensions[1]]

    def thin(self, array, n, axis):
        opposite_axis = not axis
        if array.shape[opposite_axis] < n:
            return array.copy()
        return np.delete(
            array,
            [i * n - 1 for i in range(1, array.shape[opposite_axis] // n + 1)],
            axis=opposite_axis
        )

    def juxtapose(self, array, n, axis):
        return np.concatenate([array for i in range(n)], axis)

    def mosaic(self, array, dimensions):
        juxtapose_array = self.juxtapose(array, dimensions[0], 0)
        return self.juxtapose(juxtapose_array, dimensions[1], 1)


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
    sb = ScrapBooker()

    arr = imp.load("../resources/42AI.png")
    print(arr)
    print(arr.shape)
    imp.display(arr)

    arr_crop = sb.crop(arr, (100, 50))
    print(arr_crop)
    print(arr_crop.shape)
    imp.display(arr_crop)

    arr_crop2 = sb.crop(arr, (100, 100), (100, 100))
    print(arr_crop2)
    print(arr_crop2.shape)
    imp.display(arr_crop2)

    # arr_crop3 = sb.crop(arr, (100, 100), (101, 100))
    # print(arr_crop3)
    # print(arr_crop3.shape)
    # imp.display(arr_crop3)

    arr_thin = sb.thin(arr, 3, 0)
    print(arr_thin)
    print(arr_thin.shape)
    imp.display(arr_thin)

    arr_thin2 = sb.thin(arr, 4, 1)
    print(arr_thin2)
    print(arr_thin2.shape)
    imp.display(arr_thin2)

    arr_thin3 = sb.thin(arr, 10000, 1)
    arr_thin3[:, :, :] = 0
    imp.display(arr_thin3)
    imp.display(arr)

    arr_juxtapose = sb.juxtapose(arr, 3, 0)
    print(arr_juxtapose)
    print(arr_juxtapose.shape)
    imp.display(arr_juxtapose)

    arr_juxtapose2 = sb.juxtapose(arr, 4, 1)
    print(arr_juxtapose2)
    print(arr_juxtapose2.shape)
    imp.display(arr_juxtapose2)

    arr_mosaic = sb.mosaic(arr, (2, 3))
    print(arr_mosaic)
    print(arr_mosaic.shape)
    imp.display(arr_mosaic)

    arr_mosaic2 = sb.mosaic(arr, (1, 4))
    print(arr_mosaic2)
    print(arr_mosaic2.shape)
    imp.display(arr_mosaic2)
