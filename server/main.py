import pickle
from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
#load the ickle object, to be refactored later
pickle_file = '/home/honey/Automated-Etl-tool/server/config/user_inputs.pickle'

count = dict()


with open(pickle_file, 'rb') as f:
    user_inputs = pickle.load(f)

print("user inputs = ", user_inputs)

input_path = Path(user_inputs['temp_input_path'])
print("input path = ", input_path)

output_path = Path(user_inputs['temp_output_path'])
print("output path = ", output_path)

files = os.listdir(input_path)
print("files = ", files)

#check for valid input paths
try:
    labels = os.listdir(input_path)
    print("type = ", type(labels), "indv sub dir type = ", type(labels[0]))
    print(labels)
except IOError:
    print("File not accessible")


#Set rotation range
if user_inputs['Aug-Rotate'] == 2:
    rotation_range = user_inputs['Rotate-Spin-Val']
else:
    Rotation_range = None

#Set flipping
if user_inputs['Aug-Flip'] == 2:
    horizontal_flip = True
    vertical_flip = True
else:
    horizontal_flip = None
    vertical_flip = None


#Set Brightness
if user_inputs['Aug-Brightness'] == 2:
    brightness_range = [0.4,1.5]
else:
    brightness_range = None

#Set resize
if user_inputs['Resize'] == 2:
    target_size = (user_inputs['Resize'], user_inputs['Resize'])
else:
    target_size = None

#Set zoom
if user_inputs['Aug-Scale'] == 2:
    zoom_range = user_inputs['Scale-Spin-Val']
else:
    zoom_range = None


#Set shift
width_shift_range=0.2
height_shift_range=0.2

# Set Normalization
if user_inputs['Normalizing'] == 2:
    rescale = 1.0/255.0
else:
    rescale = None


def Augment(path, class_name, num_of_images):
    dest = os.path.join('output', class_name)
    print("source path = ", path, "type = ", type(path))
    print("dest path = ", dest)

    src_path = Path(path)
    print("after conv path type = ", type(src_path), src_path)
    datagen = ImageDataGenerator(
    rotation_range = rotation_range,
    width_shift_range = width_shift_range ,
    height_shift_range= height_shift_range,
    zoom_range =  zoom_range,
    horizontal_flip = horizontal_flip,
    vertical_flip = vertical_flip)
    i = 0
    num_of_batches = num_of_images/40
    for batch in datagen.flow_from(src_path, batch_size=40, save_to_dir = dest, save_format='jpeg'):
        i += 1
        print("batch num = ", i)
        if i > num_of_batches :
            break
    return None


for each_class in labels:
    print("class = ", each_class)
    path = os.path.join(input_path, each_class)
    num_of_images = len(os.listdir(path))
    #print("num of images  = ", num_of_images)
    count[each_class] = num_of_images
    Augment(path, each_class, num_of_images)
