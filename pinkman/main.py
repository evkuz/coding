#
import os


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def get_file_count():
    path = '/home/ubuntu/pyprojects/pinkman/src/'
    folder = os.fsencode(path)
    filenames = []
    for file in os.listdir(path):
        f = os.path.join(path,file)
        # filename = os.fsdecode(file)
        # if filename.startswith("PM_points_*"):
        if os.path.isfile(f):
            filenames.append(f)
    count = len(filenames)
    from pathlib import Path
    #p = Path(path)
    new_file_name = "points"
    for i in range(count):
        #from pathlib import Path
        newfile = str(filenames[i])
        #p = Path(path)+filenames[i]
        p = Path(newfile)
        if i <= 8:
            p.rename(Path(p.parent, new_file_name + str(0) + str(i+1) + ".txt"))
        else:
            p.rename(Path(p.parent, new_file_name+str(i+1)+".txt"))
    print("There is ", count, "files")


#def GetQxyz


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    fname='myErrX.lst'
    #fname='src/points01.txt'
    inFile = open(fname, 'r', encoding='utf8')
    lst = []
    for line in inFile:
        myQ = int(float(line.strip('\n')))
        lst.append(myQ*myQ)
        # myQ = int(float(myline))
        # print(myQ*myQ)
    inFile.close()
    print("The Q-sum value is",sum(lst))
    print(sum(lst))
    get_file_count()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# +++++++++++++++++++++++


