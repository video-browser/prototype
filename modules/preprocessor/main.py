import argparse
import csv
import os
from pathlib import Path

CLASSIFICATION_RESULTS_PATH = os.getcwd() + '/../../data/v3c1/classifications/results'

def processClassifications(videoId):
  # value = @'numerical_id' -> ['video_id','frame_id','confidence_score']
  dataDict = {} # { lineNumber: [ [001, 0001, 0.1], [002, 0001, 0.15] ] }
  dataList = []
  resultsPath = os.path.join(CLASSIFICATION_RESULTS_PATH, videoId)
  print("processClassifications(): videoId: %s, resultsPath: %s" % (videoId, resultsPath))

  if os.path.exists(resultsPath) != True:
    print("processClassifications(): error, path doesn't exist, videoId: %s" % videoId)
    raise Exception("resultsPath does not exist")

  for resultsDir, dirPaths, _ in os.walk(resultsPath):
    print("processClassifications(): processing resultsDir: %s, dirPaths: %s" % (resultsDir, dirPaths))
    for videoId in dirPaths:
      videoPath = os.path.join(str(resultsPath), videoId)
      for videoDir, _, csvFiles in os.walk(videoPath):
        print("processClassifications(): processing csvs for video. videoId: %s" % videoId)
        for csvFile in csvFiles:
          csvFilePath = os.path.join(videoPath, csvFile)
          print("processClassifications(): processing csvFile, csvFilePath: %s" % csvFilePath)
          with open(csvFilePath, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
              for i in range(len(row)-1):
                value = [videoDir, csvFile, row[i + 1]]
                dataDict[row[i]] = [[]]
                dataDict[row[i]].append(dataList.append(value))
                i += 1
                print(dataDict)
            return
          break;
        break;
      break;
    break;

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='later to be descripted...')
  parser.add_argument('--videoId', action='store', type=str, help='The text to parse.')
  args = parser.parse_args()
  print("app.py: input from command line: %s" % repr(args))
  processClassifications(args.videoId)
