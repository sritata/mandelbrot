import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("zoom_000.png")
plt.imshow(img)
plt.axis("off")

def onclick(event):
    print(event.xdata, event.ydata)

plt.gcf().canvas.mpl_connect("button_press_event", onclick)
plt.show()