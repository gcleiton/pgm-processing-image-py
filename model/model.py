import sys
from math import ceil

def getTotalLines(file):
    count = 0
    for i in file:
        count += 1
    file.seek(0)
    return count

def getRow(file):
    row = int()
    for count, line in enumerate(file):
        if count == 1:
            row = line.strip().split(" ")[1]
    file.seek(0)
    return int(row)

def getColumn(file):
    column = int()
    for count, line in enumerate(file):
        if count == 1:
            column = line.strip().split(" ")[0]
    file.seek(0)
    return int(column)

def getDimension(file):
    dimension = list()
    for count, line in enumerate(file):
        if count == 1:
            row = line.strip().split(" ")[1]
            column = line.strip().split(" ")[0]
            dimension.append(int(column))
            dimension.append(int(row))
    file.seek(0)
    return dimension

def convertToList(file):
    dataList = []
    for count, line in enumerate(file):
        if count > 2:
            for i in line.strip().split(" "):
                dataList.append(i)

    file.seek(0)
    return dataList

def resizeToMatrix(dataList, column):
    newMatrix = []
    for i in range(0, len(dataList), column):
        newMatrix.append(dataList[i:i+column])
    return newMatrix

def rotate90DegreesRight(dimension, dataMatrix):
    width, height = dimension[1], dimension[0]
    newMatrix = []
    for i in range(height):
        newMatrix.append([])
        for j in range(width):
            newMatrix[i].append("")

    for i in range(height):
        for j in range(width):
            newMatrix[i][j] = dataMatrix[width-1-j][i]
    return newMatrix

def rotate90DegreesLeft(dimension, dataMatrix):
    width, height = dimension[1], dimension[0]
    newMatrix = []
    for i in range(height):
        newMatrix.append([])
        for j in range(width):
            newMatrix[i].append("")

    for i in range(height):
        for j in range(width):
            newMatrix[i][j] = dataMatrix[j][height-1-i]

    return newMatrix

def rotate180Degrees(dimension, dataMatrix):
    width, height = dimension[0], dimension[1]
    newMatrix = []
    for i in range(height):
        newMatrix.append([])
        for j in range(width):
            newMatrix[i].append("")

    for i in range(height):
        for j in range(width):
            newMatrix[i][j] = dataMatrix[height-1-i][width-1-j]
    
    return newMatrix

def flipVertically(dimension, dataMatrix):
    width, height = dimension[0], dimension[1]
    newMatrix = []
    for i in range(height):
        newMatrix.append([])
        for j in range(width):
            newMatrix[i].append("")

    for i in range(height):
        for j in range(width):
            newMatrix[i][j] = dataMatrix[height-1-i][j]
    
    return newMatrix

def flipHorizontally(dimension, dataMatrix):
    width, height = dimension[0], dimension[1]
    newMatrix = []
    for i in range(height):
        newMatrix.append([])
        for j in range(width):
            newMatrix[i].append("")

    for i in range(height):
        for j in range(width):
            newMatrix[i][j] = dataMatrix[i][width-1-j]
    
    return newMatrix

def applyMeanFilter(dimension, dataMatrix):
    width, height = dimension[0], dimension[1]
    nPerN = 9
    newMatrix = []
    for i in range(height):
        newMatrix.append([])
        for j in range(width):
            amount = 0
            possibleMoves = [[i,j], [i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1], [i, j+1], [i+1, j-1], [i+1, j], [i+1, j+1]]
            for x, y in possibleMoves:
                if 0 <= x < height and 0 <= y < width:
                    amount += int(dataMatrix[x][y])
                else:
                    amount += 0

            newMatrix[i].append(str(ceil(amount / nPerN)))
    
    return newMatrix

def applyMedianFilter(dimension, dataMatrix):
    width, height = dimension[0], dimension[1]
    newMatrix = []
    for i in range(height):
        newMatrix.append([])
        for j in range(width):
            tempList = []
            possibleMoves = [[i,j], [i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1], [i, j+1], [i+1, j-1], [i+1, j], [i+1, j+1]]
            for x, y in possibleMoves:
                if 0 <= x < height and 0 <= y < width:
                    tempList.append(int(dataMatrix[x][y]))
                else:
                    tempList.append(0)
            tempList.sort()
            newMatrix[i].append(str(tempList[4]))
    
    return newMatrix

def makeTransformation(dimension, dataMatrix, option):
    if option == "r90r":
        return rotate90DegreesRight(dimension, dataMatrix)
    elif option == "r90l":
        return rotate90DegreesLeft(dimension, dataMatrix)
    elif option == "r180":
        return rotate180Degrees(dimension, dataMatrix)
    elif option == "fv":
        return flipVertically(dimension, dataMatrix)
    elif option == "fh":
        return flipHorizontally(dimension, dataMatrix)
    elif option == "af":
        return applyMeanFilter(dimension, dataMatrix)
    elif option == "mf":
        return applyMedianFilter(dimension, dataMatrix)

def writeToFile(dimension, dataMatrix, file, option):
    dimensionStr = str()
    fileName = file.name
    newFile = None

    if option == "r90r":
        width, height = dimension[1], dimension[0]        
        dimensionStr = str(width) + " " + str(height) 
        newFile = open(fileName.strip(".pgm") + "-90degrees-right.pgm",  "w+")
    
    elif option == "r90l":
        width, height = dimension[1], dimension[0]        
        dimensionStr = str(width) + " " + str(height) 
        newFile = open(fileName.strip(".pgm") + "-90degrees-left.pgm",  "w+")

    elif option == "r180":
        width, height = dimension[0], dimension[1]
        dimensionStr = str(width) + " " + str(height)
        newFile = open(fileName.strip(".pgm") + "-180degrees.pgm", "w+")

    elif option == "fv":
        width, height = dimension[0], dimension[1]
        dimensionStr = str(width) + " " + str(height)
        newFile = open(fileName.strip(".pgm") + "-flip-vertically.pgm", "w+")

    elif option == "fh":
        width, height = dimension[0], dimension[1]
        dimensionStr = str(width) + " " + str(height)
        newFile = open(fileName.strip(".pgm") + "-flip-horizontally.pgm", "w+")

    elif option == "af":
        width, height = dimension[0], dimension[1]
        dimensionStr = str(width) + " " + str(height)
        newFile = open(fileName.strip(".pgm") + "-mean-filter.pgm", "w+")

    elif option == "mf":
        width, height = dimension[0], dimension[1]
        dimensionStr = str(width) + " " + str(height)
        newFile = open(fileName.strip(".pgm") + "-median-filter.pgm", "w+")

    newFile.write("P2\n" + dimensionStr + "\n255\n")
    for i in range(len(dataMatrix)):
        for j in dataMatrix[i]:
            newFile.write(j + " ")
        newFile.write("\n")

    return newFile.close()

def displayMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = " ")
        print()

def init(directory, option):
    with open(directory) as image:
        dimension = getDimension(image)
        dataList = convertToList(image)
        dataMatrix = resizeToMatrix(dataList, getColumn(image))
        transformation = makeTransformation(dimension, dataMatrix, option)      
        writeToFile(dimension, transformation, image, option)

    return image.close()