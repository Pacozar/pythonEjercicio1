
import os
import humanize


ruta = "C:/users/paker/Downloads"
listdir = os.listdir(ruta)
for file in listdir:
    full = os.path.join(ruta, file)
    os.path.isfile(full)
    fileSize = os.path.getsize(full)
    humanSize = humanize.naturalsize(fileSize)
    print(file, 'Es un archivo', 'y su tamaño es', humanSize)
