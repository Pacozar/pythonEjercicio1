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


if file is os.walk(root):
    if name is file:
        print(file)