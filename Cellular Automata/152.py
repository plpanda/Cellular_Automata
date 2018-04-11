import numpy as np
import random
from PIL import Image

# Creates a random image 100*100 pixels
#mat = np.random.random((100,100))
mat=[[random.randint(0,255) for i in range(10)] for j in range(21)]

#print mat
mat=np.array(mat)

# Creates PIL image
img = Image.fromarray(mat, 'L')
img.save('out.bmp')
img.show()
