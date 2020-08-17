import os
import csv

print("starting...")
# def fileWrite(fileName,data):
#   # file2write=open(fileName,'w')
#   #file2write.write(data)
#   with open(fileName, 'w') as f:
#     print(data, file=f)
#   # print(data, file=file2write)
#   f.close()

def fileWrite(fileName,data):

  filename = '/Users/chinmayees/work/prototype/data/v3c1/classifications/num_id/'+fileName+'.txt'

  if os.path.exists(filename):
      append_write = 'a' # append if already exists
  else:
      append_write = 'w' # make a new file if not

  with open(filename, append_write) as f:
    print(data, file=f)
  f.close()

dataDict = {}
dataList = []
# 'numerical_id',['video_id','frame_id','confidence_score']
src = "/Users/chinmayees/work/prototype/data/v3c1/classifications/folders/7500"
print("SRC:",src)
for subdir, dirs, mod_files in os.walk(src):
  for dir in dirs:
    print("Dir:",dir)
    path1 = os.path.join(src,dir)
    # print("Dir:",dir)
    print("Path1:",path1)
    for mod_files in os.walk(path1):
      # print("Files:",mod_files)
      files = mod_files[2]
      for file in files:
        # print("File:",file)
        path2 = os.path.join(path1,file)
        with open(path2, 'r') as f:
          reader = csv.reader(f)
          for row in reader:
            for i in range(0,len(row),2):
              # value = @'numerical_id' -> ['video_id','frame_id','confidence_score']
              value = [str(dir),str(file),row[i+1]]
            #   print("Value:",value)
              if (row[i] not in dataDict.keys()):
                dataDict[row[i]] = []
              dataDict[row[i]].append(value)
            #   fileWrite(str(row[i]),dataDict[row[i]])
              fileWrite(str(row[i]),value)
              print(dataDict[row[i]])
            #   i+=2
          # print("file read.....")
        #   fileWrite(str(dir),dataDict)
        break
      print("files read.....")
    print("folder read.....")