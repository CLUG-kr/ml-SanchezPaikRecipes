import os
from PIL import Image

label_dir = os.path.join('data', 'custom', 'labels')
image_dir = os.path.join('data', 'custom', 'images')
out_path = 'out.csv'
dataset_dir = 'images'
label_path = 'label.txt'

os.makedirs(label_dir, exist_ok=True)
os.makedirs(image_dir, exist_ok=True)

train_txt = open(out_path, 'w')

label_txt = open(label_path, 'r')
object_name = label_txt.readlines()
label_txt.close()


train_txt.write('image,id,name,xMin,xMax,yMin,yMax\n')

for file_name in os.listdir(dataset_dir):
    index = int(file_name.split('_')[0])
    image = Image.open(os.path.join(dataset_dir, file_name))
    width, height = image.size
    train_txt.write(f"{file_name},{index},{object_name[index]},{0},{width},{0},{height}\n")

train_txt.close()