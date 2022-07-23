import tkinter as tk
from tkinter.filedialog import askdirectory
import os
import shutil

root = tk.Tk()
root.withdraw()

path_D = askdirectory(title='Select folder with files to be replaced') 
path_S = askdirectory(title='Select folder that contains files that will be replacing old ones') 
path_B = askdirectory(title='Select a folder to place backup folders')

shutil.copytree(path_D, path_B + '/' + 'replacee_backup')
shutil.copytree(path_S, path_B + '/' + 'replacer_backup')

count = 0
file_list = list()


for file_name in os.listdir(path_D):

    file_list.append(file_name)

    os.remove(os.path.join(path_D, file_name))

for file_name in os.listdir(path_S):

    if count >= len(file_list):

        break

    full_path = path_S + '/' + file_name

    os.rename(full_path, path_D + '/' + file_list[count])

    count += 1

