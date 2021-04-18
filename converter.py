import os
import sys
import pathlib

alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for char in alphabet:

    for path in pathlib.Path(r"YOUR_PATH_HERE").iterdir():
        if path.is_file():
            if "desktop.ini" in str(path):
                break


            fin = open(path, "rt", encoding= "ANSI")

            data = fin.read()

            if f"{char}:\\" in data:

                data = data.replace(f"{char}:\\", f"/home/user/media/{char}:/")
                fin.close()

                fin = open(path, "wt", encoding= "ANSI")
                fin.write(data)
                fin.close()

                fin = open(path, "rt", encoding= "ANSI")
                data = fin.read()
                data = data.replace("\\", "/")
                fin.close()

                fin = open(path, "wt", encoding= "ANSI")
                fin.write(data)
                fin.close()
                
            fin.close()


















