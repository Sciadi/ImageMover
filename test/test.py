from os import listdir, path
import pprint
pathin = '\\\chstwin.twin-set.it\\plm-img'

path_dani = '\\\sr-msfe-prod01\\e$\\Microstrategy_repo\\ts_img_repo\\'

folders_dani = listdir(path_dani) 
prova_sciadi = listdir('prova\\')

folders_to_be_tested = list()

for elem in prova_sciadi:
    path_test = path_dani + elem 
    if path.exists(path_test):
        folders_to_be_tested.append(path_test)
    else:
        print(path_test+' non esiste.' )


print(folders_to_be_tested)

not_passed_test_folder = []
not_passed_test_file = {}

i=0
for folder in folders_to_be_tested:
    print(folder)
    sciadi = set(listdir('prova\\'+prova_sciadi[i]))
    dani = set(listdir(folder))

    danimanonsciadi = dani-sciadi

    if '20222' in danimanonsciadi:
        print('----')
        
    copy_elem_set = set()



    # for elem in danimanonsciadi:
    #     if ('(1)') in elem or '(2)' in elem or '(4)':
    #         copy_elem_set.add(elem)
            
    
    danimanonsciadi -= copy_elem_set

    
    if len(danimanonsciadi)!=0:        
        not_passed_test_folder.append(sciadi)
        not_passed_test_file[prova_sciadi[i]] = list(danimanonsciadi)
        print(danimanonsciadi)

    sciadimanondani = sciadi-dani

    print('----------------------------------')
    i+=1


pprint.pprint(not_passed_test_file)

file_not_in_src = []
for folder in not_passed_test_file:
    src_path = pathin + folder.replace('CCCCC','99999')
    for file in not_passed_test_file[folder]:
        if file not in src_path:
            print(file+' non in sorgente')
            file_not_in_src.append(file)

print(len(file_not_in_src))



print(sum(len(val) for val in not_passed_test_file.values()))

all_elem = list(set([item for sublist in not_passed_test_file.values() for item in sublist]))

print(set(all_elem)  - set(file_not_in_src))

for key in not_passed_test_file:
    if '20222' in not_passed_test_file[key]:
        print(key)