import pandas as pd
from PIL import Image, ImageDraw

data=pd.read_csv("DS9.txt", sep=" ", names=["x", "y"])
image = Image.new("RGB", (540, 960), "white")
draw = ImageDraw.Draw(image)
for i in range(len(data)):
    draw.text((data.loc[i,"x"], data.loc[i,"y"]), text=".", fill="black")
image.save("lab2.png")