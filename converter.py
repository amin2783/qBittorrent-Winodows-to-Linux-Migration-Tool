import os, sys, pathlib

alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for char in alphabet:

    for path in pathlib.Path(r"YOUR_PATH_HERE").iterdir():  #Path should be like this "C:\Users\username\Desktop\New folder\\"
                                                            #Keep the quotes, and note the double backslash \\ at the end
        if path.is_file():
            if ".fastresume" in str(path):

                fin = open(path, "rt", encoding= "ANSI")

                data = fin.read()

                if f"{char}:\\" in data:

                    data = data.replace(f"{char}:\\", f"MOUNT_LOCATION_HERE{char}:/") #Mount location should be like this /home/user/media/
                                                                                      #Keep the original quotes, keep a slash / at the end
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


















