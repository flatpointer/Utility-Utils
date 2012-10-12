from optparse import OptionParser

#since I'm running 2.6, gotta use OptionParser and not argparse. :(
if __name__ == "__main__":
  parser = OptionParser(description='Process relative or absolute file location.')
  parser.add_option('-f','--filePath', dest="filePath", help="Enter a path (relative or absolute) to the file you want to run through my stupid parser")
  (options, args) = parser.parse_args()
  lines = open(options.filePath).readlines()
  for line in lines:
    beforeColon = True
    finalString = ""
    for char in line:
      if (char == ":"):
        beforeColon = False
      if (char != '"' and beforeColon):
        finalString += char
      elif(beforeColon == False):
        finalString += char
    if finalString.strip() != "":
      print finalString.rstrip('\n')
