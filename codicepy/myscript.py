"""Main Script: This script does not take into account that ther could be subfolders
                into processed folders
Returns:
void: if it terminates with no exception, no error has occured 
"""

## IMPORT VARIABLES ##
from global_vars import DirectoryValues 

## IMPORTS ##
import os
import shutil
from elapsed_time import time_it

## MY SCRIPTS IMPORTS ##
from copytree import copy_images

DEFAULT_DATE_MODIFICATION_TIME = None # datetime


def filter_items(src, item):
    """ Filters out folders that do not respect appropriate conditions

    Args:
        src (str): root path
        item (str): subfolder of path to be checked

    Returns:
        str: item if it's appropriate
    """
    s = os.path.join(src, item)
    #=======================================================================
    # Folder has to have max 5 char length name
    #=======================================================================
    if len(item) == dir_length and os.path.isdir(s):
        #===========================================================================
        # if start with wildcard
        #===========================================================================    
        if any(item.startswith(wildcard) for wildcard in dir_wildcards):
            return item 



def Mcstr_copytree(src, dst):
    """Copies images file in tree src into dst

    Args:
        src (str): path of root subfolder
        dst (str): path is the same as @src_subfolder with @dst_root  
    """
    #===========================================================================
    # Create destination directory if it does not exists
    #===========================================================================
    if not os.path.exists(dst):
        os.makedirs(dst)
        shutil.copystat(src,dst)
    #===========================================================================
    
    srclst = os.listdir(src)
    
    # Filter all items according to criteria
    srclst = list(filter(lambda item :filter_items(src, item), srclst))

    
    

    print(srclst)
    # Iter on all paths
    for folder_name in srclst:
          
        #FULL PATH
        src_folder = os.path.join(src, folder_name)
    
        print(folder_name)

    #=======================================================================
    # In destination replace 99999 folder with CCCCC -- continuativo
    # Si può usare un dictionary come ha fatto Ivan
    #=======================================================================        
        #FULL PATH
        dst_folder = os.path.join(dst, folder_name.replace('99999','CCCCC'))

        # Create folder if not exists
        if not os.path.exists(dst_folder):
            os.mkdir(dst_folder)
            # Set modification time to 1980
            os.utime(dst_folder, (DEFAULT_DATE_MODIFICATION_TIME, DEFAULT_DATE_MODIFICATION_TIME))

        #
        # Se la data di ultima modifica della source è più nuova della data 
        # di ultima modifica della dest devo chiamare la copy su quelle cartelle, 
        # se no no
        # Devo settare la data delle nuove cartelle a "0"   
        # Do per scontato che i file non vengano mai eliminati nella destinazione
        # La cartella di destinazione NON DEVE ESSERE TOCCATA
        # 
        # If src_folder's last modification date is newer than 
        # the dst_folder one, I have to call copy_images on those directories because 
        # src_folder has been modified and so dst_folder has to be. 
        src_folder_mod_date = os.path.getmtime(src_folder) #float
        dst_folder_mod_date = os.path.getmtime(dst_folder) #float
        if src_folder_mod_date > dst_folder_mod_date:
            copy_images(src_folder, dst_folder)
        
        #Uncomment this if files in dst_folder get deleted and run script to restore dst_folders 
        #copy_images(src_folder, dst_folder)
    return
    
@time_it
def main():   
    Mcstr_copytree(pathin,pathout)
     


#################################################################################################################
#                                       |\  /|   /\   | |\  |                                                   #
#                                       | \/ |  /__\  | | \ |                                                   #
#                                       |    | /    \ | |  \|                                                   #
#################################################################################################################

if __name__ == '__main__':

    # Non dovrei usare il metodo statico, dovrei usare un dictionary e non le clasi per i dati.
    pathin, pathout, dir_wildcards, dir_length, DEFAULT_DATE_MODIFICATION_TIME = DirectoryValues.get_values() 
    main()
    
     
        
   