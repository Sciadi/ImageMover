## IMPORT VARIABLES ##
from global_vars import DirectoryValues 

## IMPORTS ##
import os
import shutil
from elapsed_time import time_it


## MY SCRIPTS IMPORTS ##
from copytree import copy_images


## Seleziono solo le cartelle che devo
def filter_items(src, item):
    s = os.path.join(src, item)
    #=======================================================================
    # CONSIDERO SOLO LE DIRECTORIES IL CUI NOME HA 5 CHAR
    #=======================================================================
    if len(item) == dir_length and os.path.isdir(s):
        #===========================================================================
        # CONSIDERO SOLTANTO I FOLDER CHE RISPETTANO DETERMINATE CONDIZIONI
        # (inizia con dir_wildcard)
        #===========================================================================    
        if any(item.startswith(wildcard) for wildcard in dir_wildcards):
            return item 


def Mcstr_copytree(src, dst):
    
    #===========================================================================
    # CREO LA DIRECTORY DI DESTINAZIONE SE NON LA TROVO
    #===========================================================================
    if not os.path.exists(dst):
        os.makedirs(dst)
        shutil.copystat(src,dst)
    #srclst=sorted(os.listdir(src), reverse=True)
    #===========================================================================
    
    srclst = os.listdir(src)
    
    # Filtra tutti gli item secondo i criteri in filter_items
    # PUO ESSERE PARALLELIZZATO, senza particolari guadagni
 
    srclst = list(filter(lambda item :filter_items(src, item), srclst))

    
    

    print(srclst)
    # Ho tutti percorsi che mi servono non devo filtrare
    # PUO ESSERE PARALLELIZZATO
    for folder_name in srclst:
          
        
        #FULL PATH
        src_folder = os.path.join(src, folder_name)
    

        print(folder_name)


    #=======================================================================
    # SOSTITUISCO LA DIRECTORY 99999 CON CCCCC
    #=======================================================================        
        #FULL PATH
        dst_folder = os.path.join(dst, folder_name.replace('99999','CCCCC'))


#===============================================================================
# CONSIDERO SOLO LE DIRECTORY CHE CONTENGONO ANCHE UN SOLO FILE CON LE ESTENSIONI DESIDERATE
#===============================================================================
#=======================================================================
# CREO LE SUBDIRECTORIES E COPIO I FILES AL LORO INTERNO SE NON LE TROVO
#=======================================================================
        #Se non esiste la cartella la creo
        if not os.path.exists(dst_folder):
            os.mkdir(dst_folder)
            shutil.copystat(src_folder, dst_folder)
        
        copy_images(src_folder, dst_folder)
    
    return
    
@time_it
def main():   
    Mcstr_copytree(pathin,pathout)
     


if __name__ == '__main__':
    pathin, pathout, dir_wildcards, dir_length = DirectoryValues.get_values() 
    main()
    
     
        
   