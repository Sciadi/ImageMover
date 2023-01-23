## IMPORT VARIABLES ##
from global_vars import FileValues


## IMPORTS ##
from os.path import isfile, exists, join as joinpath
from os import listdir
from PIL import Image
import shutil 
from elapsed_time import time_it
from multiprocessing import Pool, cpu_count
from functools import partial
from time import time


file_excl_wildcards, file_wildcards, img_max_size, img_max_reso = FileValues.get_values()
Image.MAX_IMAGE_PIXELS = None


# Returns true if file is from mac
def is_from_mac(file_name):
    return file_name.startswith(tuple(file_excl_wildcards))

# Returns true if file is image 
def is_image(file_path):
    return file_path.endswith(tuple(file_wildcards))


#returns if a file is a copy
def is_copy(file_path):
    return "(1)" in file_path

def check_max_dimension(image: Image):
    return image.height*image.width < img_max_size

# Function to check if a directory contains JPG files
def has_jpgs(folder):
    for file_name in listdir(folder):
        return is_image(file_name)
    

def wait_for_file(filepath):
    wait_time = 1
    while not Image.open(filepath, 'r'):
        time.sleep(wait_time)


def copy_item(item_name, src_folder, dst_folder):
    #print(item_name+'\n')
    if not is_from_mac(item_name):
        # Construct the full path of the item in the source folder
        src_path = joinpath(src_folder, item_name)

        item_name = str.upper(item_name)
        # Construct the full path of the item in the destination folder
        dst_path = joinpath(dst_folder, item_name)
          
        if not exists(dst_path):
            # Check if the item is a file and is an image file. It must not be a copy of another file
            if isfile(src_path) and is_image(src_path) and not is_copy(src_path):



                # If open fails wait till it doesn't
                if not Image.open(src_path, 'r'):
                    wait_for_file(src_path)

                
                image = Image.open(src_path, 'r')


                # If it is smaller than max dimension
                if check_max_dimension(image):
                    converted_image = image.convert('RGB')
                    converted_image.thumbnail(img_max_reso)
                        
                    # Copy the resized image to destination 
                    converted_image.save(dst_path, optimizer=True, quality=65)

                    
                    shutil.copystat(src_path, dst_path)
                    converted_image.close()
                
                image.close()
    return

# Copy only image files from @src_folder to @dst_folder
@time_it
def copy_images(src_folder, dst_folder):

    all_items = listdir(src_folder)


    partial_func = partial(copy_item, src_folder=src_folder, dst_folder=dst_folder)
    with Pool(cpu_count()) as pool:
        pool.map(partial_func, all_items)

    return



    # Check if the item is a directory 
    # DO I EVER HAVE SUBFOLDERS?
    """elif os.path.isdir(src_path):
    # Check if the directory contains JPG files
    if has_jpgs(src_path):
    # Create the directory in the destination folder
    os.makedirs(dst_path, exist_ok=True)
    # Recursively copy the contents of the directory
    shutil.copytree(src_path, dst_path, False, None, None, None, None)
    """