import os
import shutil
import time
from PIL import Image

pathin = '\\\chstwin.twin-set.it\\plm-img'
pathout='\\\sr-msfe-prod01\\e$\\Microstrategy_repo\\ts_img_repo\\'
# pathin='C:\\Users\\daniele.nigro\\Pictures\\PythonIn\\'
# pathin = '\\\sr-msfe-prod01\\e$\\Microstrategy_repo\\ts_img_repo\\'
# pathout='C:\\Users\\daniele.nigro\\Pictures\\PythonOut\\'
# pathout='\\\sr-msfe-prod01\\e$\\Microstrategy_repo\\ts_img_repo_test\\'
file_wildcards = ['.jpg','.jpeg','.png']
file_excl_wildcards = ['._']
dir_wildcards = ['20','99']
dir_length = 5
img_max_reso = (200,1000)
img_max_size = 50000000

def Mcstr_copytree(src, dst, file_wildcards, file_excl_wildcards, dir_wildcards,dir_length, img_max_reso, img_max_size, symlinks=False, ignore=None):
    
    Image.MAX_IMAGE_PIXELS = None
    #===========================================================================
    # CREO LA DIRECTORY DI DESTINAZIONE SE NON LA TROVO
    #===========================================================================
    if not os.path.exists(dst):
        os.makedirs(dst)
        shutil.copystat(src,dst)
    srclst=sorted(os.listdir(src), reverse=True)
    #===========================================================================
    if ignore:
        excl=ignore(src,srclst)
        srclst=[x for x in srclst if x not in excl]
    for item in srclst:
        s = os.path.join(src, item)
        #=======================================================================
        # SOSTITUISCO LA DIRECTORY 99999 CON CCCCC
        #=======================================================================
        d = os.path.join(dst, item.replace('99999','CCCCC'))
        #=======================================================================
        # CONSIDERO SOLO LE DIRECTORIES IL CUI NOME HA 5 CHAR
        #=======================================================================
        if (os.path.isdir(s) and len(item)==dir_length):
            #===========================================================================
            # CONSIDERO SOLTANTO I FOLDER CHE RISPETTANO DETERMINATE CONDIZIONI
            #===========================================================================
            for wildcard in dir_wildcards:
                if (item.startswith(wildcard)):
                #===============================================================================
                # CONSIDERO SOLO LE DIRECTORY CHE CONTENGONO ANCHE UN SOLO FILE CON LE ESTENSIONI DESIDERATE
                #===============================================================================
                    for file_wildcard in file_wildcards:
                        #=======================================================================
                        # CREO LE SUBDIRECTORIES E COPIO I FILES AL LORO INTERNO SE NON LE TROVO
                        #=======================================================================
                        if not os.path.exists(d):
                            shutil.copytree(s, d, symlinks, ignore=shutil.include_patterns('*.'+file_wildcard))
                            srclstfile=sorted(os.listdir(s), reverse=True)
                            for srclstfile in srclstfile:
                                #=======================================================================
                                # ENUMERO LE INCLUSIONI E LE ESCLUSIONI
                                #=======================================================================
                                for file_wildcard in file_wildcards:
                                    for file_excl_wildcard in file_excl_wildcards:
                                        #=======================================================================
                                        # VERIFICARE CHE IL PROSSIMO CICLO NON SIA RIDONDANTE
                                        #=======================================================================
                                        if (srclstfile.endswith(file_wildcard) and not srclstfile.startswith(file_excl_wildcard)):
                                            srclstfile=str.upper(srclstfile)
                                            srcfile=os.path.join(s,srclstfile)
                                            dstfile=os.path.join(d,srclstfile)
                                            srcfileopen=Image.open(srcfile,'r')
                                            if srcfileopen.height*srcfileopen.width < img_max_size:
                                                #=======================================================================
                                                # Controllo che il file non sia in lock
                                                #=======================================================================
                                                def is_locked(srcfile):
                                                    locked = None
                                                    file_object = None
                                                    try:
                                                        buffer_size = 8
                                                        #=======================================================================
                                                        # Apro il file in append mode e leggo i primi 8 chars
                                                        #=======================================================================
                                                        file_object = open(srcfile, 'a', buffer_size)
                                                        if file_object:
                                                            locked = False
                                                    except IOError as message:
                                                        locked = True
                                                    finally:
                                                        if file_object:
                                                            file_object.close()
                                                    return locked
                                                def wait_for_file(srcfile):
                                                    wait_time = 1
                                                    while is_locked(srcfile):
                                                        time.sleep(wait_time)
                                                shutil.copy2(srcfile, dstfile)
                                                try:
                                                    print(dstfile)
                                                    image=Image.open(dstfile,'r')
                                                except AttributeError:
                                                    print("Couldn't open image{}".format(image))
                                                try: 
                                                    image=image.convert('RGB')
                                                except AttributeError:
                                                    print("Couldn't convert image{}".format(image))
                                                try:
                                                    image.thumbnail(img_max_reso)
                                                except AttributeError:
                                                    print("Couldn't resize image{}".format(image))
                                                try:
                                                    image.save(dstfile,optimizer=True,quality=65)
                                                except AttributeError:
                                                    print("Couldn't optimize image{}".format(image))
                                                except:
                                                    print("Al va mia 'n cas")
                                                finally:
                                                    image.close()
                                                exit
                                            #else:
                                            #     print("vecchifiles")
                                            exit
                                        exit
                                    exit
                                exit
                            exit
                        exit
                        if os.path.exists(d):
                            srclstfile=sorted(os.listdir(s), reverse=True)
                            for srclstfile in srclstfile:
                                for file_wildcard in file_wildcards:
                                    for file_excl_wildcard in file_excl_wildcards:
                                        if (srclstfile.endswith(file_wildcard) and not srclstfile.startswith(file_excl_wildcard)):
                                            srclstfile=str.upper(srclstfile)
                                            srcfile=os.path.join(s,srclstfile)
                                            dstfile=os.path.join(d,srclstfile)
                                            srcfileopen=Image.open(srcfile,'r')
                                            if (not os.path.exists(dstfile)
                                                and srcfileopen.height*srcfileopen.width < img_max_size):
                                                #=======================================================================
                                                # Controllo che il file non sia in lock
                                                #=======================================================================
                                                def is_locked(srcfile):
                                                    locked = None
                                                    file_object = None
                                                    try:
                                                        buffer_size = 8
                                                        #=======================================================================
                                                        # Apro il file in append mode e leggo i primi 8 chars
                                                        #=======================================================================
                                                        file_object = open(srcfile, 'a', buffer_size)
                                                        if file_object:
                                                            locked = False
                                                    except IOError as message:
                                                        locked = True
                                                    finally:
                                                        if file_object:
                                                            file_object.close()
                                                    return locked
                                                def wait_for_file(srcfile):
                                                    wait_time = 1
                                                    while is_locked(srcfile):
                                                        time.sleep(wait_time)
                                                shutil.copy2(srcfile, dstfile)
                                                try:
                                                    image=Image.open(dstfile,'r')
                                                except AttributeError:
                                                    print("Couldn't open image{}".format(image))
                                                try: 
                                                    image=image.convert('RGB')
                                                except AttributeError:
                                                    print("Couldn't convert image{}".format(image))
                                                try:
                                                    image.thumbnail(img_max_reso)
                                                except AttributeError:
                                                    print("Couldn't resize image{}".format(image))
                                                try:
                                                    image.save(dstfile,optimizer=True,quality=65)
                                                except AttributeError:
                                                    print("Couldn't optimize image{}".format(image))
                                                except:
                                                    print("Al va mia 'n cas")
                                                finally:
                                                    image.close()
                                                exit
                                            #else:
                                            #    print(srcfile+' - FILE ESISTENTE')
                                            exit
                                        exit                               
                                    exit
                                exit
                            exit
                        exit
                    exit
                exit
            exit 
        exit
    exit
Mcstr_copytree(pathin,pathout,file_wildcards,file_excl_wildcards,dir_wildcards,dir_length,img_max_reso,img_max_size,True)
