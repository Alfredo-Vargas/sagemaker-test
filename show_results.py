import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Rectangle
import numpy as np
import os
import json


def main():

    output_file = "./detected_faces.txt"
    with open(output_file) as file_object:
        json_data = file_object.read()
    
    output = json.loads(json_data)

    width = output[1]['FaceDetails'][0]['BoundingBox']["Width"]
    height = output[1]['FaceDetails'][0]['BoundingBox']["Height"]
    px = output[1]['FaceDetails'][0]['BoundingBox']["Left"]
    py = output[1]['FaceDetails'][0]['BoundingBox']["Top"]


    print(width, height, px, py)
    print(len(output))
    # Create figure and axes
    fig, ax = plt.subplots()

    # base_name = "elon-musk"  # 0
    base_name = "lionel-messi"  # 1
    # base_name = "peter-paul-rubens"  # 2
    # base_name = "rene-magritte"  # 3
    img = mpimg.imread("./initial_images/" + base_name + ".jpg") 
    h = int(len(img) * height)
    w = int(len(img[0]) * width)
    x = int(len(img[0]) * px)
    y = int(len(img) * height - 30)
    # print(h)
    # print(w)
    ax.imshow(img)
    # (px, py), w, h
    rect = Rectangle((x, y), w, h, linewidth=1, edgecolor='r', facecolor='none')
    ax.add_patch(rect)
    plt.savefig("./output_images/" + base_name + "-detected.jpg")
    plt.show()


if __name__ == "__main__":
    main()