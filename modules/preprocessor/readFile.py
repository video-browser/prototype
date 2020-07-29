import os

def fileRead(fileName):
    f = open(fileName)
    out = readCont(f)
    print(out)
    raw = open(fileName, "w")
    # raw.write(str(out))
    for item in out:
        raw.write("%s" % item)
    raw.close()
    print("reading...")
    # f = open(fileName)
    # print(f.readlines())

def readCont(f):
    contents = []
    for cont in f:
        contents.append(cont)
    
    if len(contents)<=1:
        return contents
    else:
        return rank(contents)

def rank(contents):
    # print(contents)
    s = sorted(contents, key = lambda x: float(x[2]),reverse=True)
    print(s)
    return s
    # contents.sort(key=lambda x: x[2],reverse=True)

# def sorting(filename):
#     # filename = ("food.txt")   
#     file_handle = open(filename, "r")
#     words = []
#     for line in file_handle:
#         words += line.split()
#     file_handle.close()
#     print sorted(words)

path = "/Users/chinmayees/work/prototype/database/num_id/"
# for subdir, dirs, mod_files in os.walk(path):
    # print(subdir, dirs)
# fileRead(path)
# print("hi",os.walk(path))
for subdir, dirs, mod_files in os.walk(path):
    # print(files[0])
    for files in mod_files:
        print("File:",files)
    # print(len(mod_files))
        fileRead(os.path.join(path,files))
        break