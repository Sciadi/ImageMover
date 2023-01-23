""" Classes containing global values accessibles via stathic method get_value() """

##############################################################
class DirectoryValues:
    pathin = '\\\chstwin.twin-set.it\\plm-img'
    #pathout='\\\sr-msfe-prod01\\e$\\Microstrategy_repo\\ts_img_repo\\'
    pathout= 'prova\\'
    # pathin='C:\\Users\\daniele.nigro\\Pictures\\PythonIn\\'
    # pathin = '\\\sr-msfe-prod01\\e$\\Microstrategy_repo\\ts_img_repo\\'
    # pathout='C:\\Users\\daniele.nigro\\Pictures\\PythonOut\\'
    # pathout='\\\sr-msfe-prod01\\e$\\Microstrategy_repo\\ts_img_repo_test\\'
    dir_wildcards = ['20','99']
    dir_length = 5

    @staticmethod
    def get_values():
        values = list()
        for key in DirectoryValues.__dict__.keys():
            if not key.startswith('__'): 
                if key != 'get_values':
                    values.append(DirectoryValues.__dict__[key])
                
                # No more atttributes function names list is starting
                else: 
                    return values


class FileValues:
    file_excl_wildcards = ['._']
    file_wildcards = ['.jpg','.jpeg','.png']
    img_max_size = 50000000
    img_max_reso = (200,1000)
    
    file_wildcards = file_wildcards + list(map(lambda item: str.upper(item), file_wildcards))
    
    @staticmethod
    def get_values():
        values = list()
        for key in FileValues.__dict__.keys():
            if not key.startswith('__'):
                if key != 'get_values':
                    values.append(FileValues.__dict__[key])
                # No more atttributes function names list is starting
                else: 
                    return values