from rembg import remove #The remove function is called from rembg library
from PIL import Image #The Image function is called from PIL library
import easygui as eg #The easygui library is renamed eg
input_path = eg.fileopenbox(title="Select image file") #The input path is translated in fileopenbox function
output_path = eg.filesavebox(title="Save file to..") #The output path is translated in filesavebox function
input = Image.open(input_path) #The Image is opened from input path
output = remove(input) #The background is removed from input
output.save(output_path) #The output is saved using a .png extension 