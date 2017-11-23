#Fare Thee Well Voice Parser 1.0.1
print('Please enter the file to be parsed. Include the file path.')
inputFilePath = input()

inputFileName = inputFilePath.rsplit('\\', 1)[1]
filePath = inputFilePath.rsplit('\\', 1)[0]

outputFileName = '\\parsed_' + inputFileName
outputFilePath = filePath + outputFileName

print('Please enter the scene\'s route tag.')
routeTag = input()

print('Please enter the scene number.')
sceneNumber = input()

lineCount = 1

with open(inputFilePath, encoding="utf8") as infile, open(outputFilePath, 'w') as outfile:
    for line in infile:
        if '    pro' in line[:7]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Makoto (Reece Bridger)\n')
            outfile.write(line)
            lineCount += 1
        elif '    bp' in line[:6]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Beepy (Hikari)\n')
            outfile.write(line)
            lineCount += 1
        elif '    st' in line[:6]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #STan (Dani)\n')
            outfile.write(line)
            lineCount += 1
        elif '    riv' in line[:7]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Misaki (Kikari)\n')
            outfile.write(line)
            lineCount += 1
        elif '    sis' in line[:7]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Yumi (Kaito)\n')
            outfile.write(line)
            lineCount += 1
        elif '    mm' in line[:6]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Mami \n')
            outfile.write(line)
            lineCount += 1
        elif '    bb' in line[:6]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Bubble \n')
            outfile.write(line)
            lineCount += 1
        elif '    lu' in line[:6]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Lucy (Vivi)\n')
            outfile.write(line)
            lineCount += 1
        elif '    co' in line[:6]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Councillor \n')
            outfile.write(line)
            lineCount += 1
        elif '    q' in line[:5]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #??? \n')
            outfile.write(line)
            lineCount += 1
        elif '    hm' in line[:6]:
            outfile.write('    voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Hall Monitor \n')
            outfile.write(line)
            lineCount += 1
        else:
            outfile.write(line)

print('Scene has been successfully parsed! Output location: ')
print(outputFilePath)
