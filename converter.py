print("Welcome to the qBittorrent fastresume Windows to Linux converter!\n")
print("Follow the on-screen instructions. Type the drive letters and its name one by one when prompted, and press Enter.\n\n")
print("NOTE 1: Type only the drive letter, don't include colons, slashes or anything.")
print("NOTE 2: Fastresume files path should be like this C:\\Users\\username\\Desktop\\BT_BACKUP\\ (Path of the folder where you have copied it.")
print("NOTE 3: Mount location should be like this /home/user/media/   KEEP a slash / at the end.\n\n")


print("So, let's start!!! :D\n\n\n")

folder_path = input("\nWhat is the path of the fastresume files?\n")



import os, sys, pathlib

partitions = int(input("How many NTFS partitions do you have?\n"))

for partition in range(partitions):

    print("\n")

    char = input("What is the drive letter? (e.g. C, D etc.)\n").upper()
    name = input("What is the name of the drive? (In Windows)\n")
    mount_path = input("What is the mounting location of the drive?\n")

    for path in pathlib.Path(folder_path).iterdir():
        if path.is_file():
            if ".fastresume" in str(path):

                fin = open(path, "rt", encoding= "ANSI")

                data = fin.read()

                if f"{char}:\\" in data:

                    data = data.replace(f"{char}:\\", f"{mount_path}{name}/")
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


print("\n\n\n\nCompleted!")
input("Press any key to continue...")
