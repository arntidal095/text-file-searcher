import os, shutil, sys

back = "backup_folder"
word = input("Enter a the word u wanna search for: ")
os.makedirs("backup_folder", exist_ok=True)
n = 0

for foldername, subfolders, filenames in os.walk("."):
    for f in filenames:
        if os.path.splitext(f)[1]== ".txt":
            filename = os.path.join(foldername, f)
            with open(filename, "r",encoding="utf-8") as file:
                for i, line in enumerate(file, start=1):
                    if word.lower() in line.lower():
                        n += 1
                        print("found in " + filename + "in line no " + str(i) +"including with the words " + line.strip())
                        dst = os.path.join(back, f)
                        if os.path.abspath(filename) != os.path.abspath(dst):
                            shutil.copy(filename, dst)

if n > 0:
    print("found " + str(n) + " lines ")
else:
    print("no lines found")


