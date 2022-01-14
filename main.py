import os
import humanize

root = "C:/users/paker/Downloads"
listdir = os.listdir(root)
for file in listdir:
    full = os.path.join(root, file)
    os.path.isfile(full)
    fileSize = os.path.getsize(full)
    humanSize = humanize.naturalsize(fileSize)
    print(file, 'Es un archivo', 'y su tamaño es', humanSize)


for root, dir, file in os.walk(root):
    for name in dir:
        print(os.path.join(root, name))
    for name in file:
        print(os.path.join(root, name))

        
        





    
   


