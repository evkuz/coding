import os

# 406B
path = "/home/evkuz/py_project/pinkman/src"
folder = os.fsencode(path)
filenames = []
for file in os.listdir(folder):
    filename = os.fsdecode(file)
    if filename.startswith ("PM_points_*"):
        filenames.append(filename)
count=len(filenames)
print("There is ", count, "files")
# save current working directory
# saved_cwd = os.getcwd()
# # change your cwd to the directory which contains files
# os.chdir(path)