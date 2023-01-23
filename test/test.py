import os 

files = os.listdir("prova\\20202")

for file in files:
    if "(1)" in file :
        print(f"{file} è una copia\n")



