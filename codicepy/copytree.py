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
import re


file_excl_wildcards, file_wildcards, img_max_size, img_max_reso = FileValues.get_values()
Image.MAX_IMAGE_PIXELS = None



def is_from_mac(file_name: str)-> bool:
    """Returns True if file is from mac

    Args:
        file_name (str): file name

    Returns:
        bool: True if file is from mac
    """
    return file_name.startswith(tuple(file_excl_wildcards))


def is_image(file_path: str)-> bool:
    """Returns True if file is image 

    Args:
        file_path (str): file path

    Returns:
        bool: True if file is image 
    """
    return file_path.endswith(tuple(file_wildcards))


def is_copy(file_path: str)-> bool:
    """Returns True if file is a copy

    Args:
        file_path (str): file path

    Returns:
        bool: True if file is a copy
    """
    return re.search(r'\(\d+\)', file_path) 

def check_max_dimension(image: Image) ->bool:
    """Returns True if file smaller than img_max_size

    Args:
        image (Image): image

    Returns:
        bool: True if file smaller than img_max_size
    """
    return image.height*image.width < img_max_size


def has_jpgs(folder: str)-> bool:
    """Function to check if a directory contains JPG files

    Args:
        folder (str): _description_

    Returns:
        bool: True if files in folder contains image extension (jpgs or pngs)
    """
    for file_name in listdir(folder):
        return is_image(file_name)
    

def wait_for_file(filepath: str):
    """Waits 1 second to open the image

    Args:
        filepath (str): file path
    """
    wait_time = 1
    while not Image.open(filepath, 'r'):
        time.sleep(wait_time)


def copy_item(item_name: str, src_folder: str, dst_folder: str):
    """Copies item_name from src_folder to _dst_folder

    Args:
        item_name (str): file name
        src_folder (str): src path
        dst_folder (str): dst path
    """
    
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
                # it's executing in parallel so it does not stop execution flow
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


@time_it
def copy_images(src_folder: str, dst_folder: str):
    """Copies only image files from src_folder to dst_folder

    Args:
        src_folder (str): src folder
        dst_folder (str): dst folder
    """    

    all_items = listdir(src_folder)


    partial_func = partial(copy_item, src_folder=src_folder, dst_folder=dst_folder)
    with Pool(cpu_count()) as pool:
        pool.map(partial_func, all_items)

    return

