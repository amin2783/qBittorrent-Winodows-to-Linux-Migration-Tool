import os, sys, pathlib

alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for char in alphabet:

    for path in pathlib.Path(r"YOUR_PATH_HERE").iterdir():  #Path should be like this "C:\Users\username\Desktop\New folder\\"
                                                            #Keep the quotes, and note the double \\ at the end
        if path.is_file():
            if ".fastresume" in str(path):

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


















