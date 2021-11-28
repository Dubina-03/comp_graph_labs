import pandas as pd
import numpy as np
from PIL import Image, ImageDraw

x = np.radians(100)
data = pd.read_csv("DS9.txt", sep=" ", names=["x", "y"])
table_T1 = np.array([1, 0, 0, 0, 1, 0, -480, -480, 1]).reshape(3, 3)
table_T2 = np.array([np.cos(x), np.sin(x), 0, -np.sin(x), np.cos(x), 0, 0, 0, 1]).reshape(3, 3)
table_T3 = np.array([1, 0, 0, 0, 1, 0, 480, 480, 1]).reshape(3, 3)

def multiply(r):
    new_coord = [r[0],r[1],1]@table_T1@table_T2@table_T3
    return new_coord[0], new_coord[1]

image = Image.new("RGB", (960, 960), "white")
draw = ImageDraw.Draw(image)
data.apply(lambda r: draw.text(multiply(r),text=".", fill="black"), axis=1)
image.save("lab3.png")