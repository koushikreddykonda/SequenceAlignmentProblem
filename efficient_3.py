import sys
from resource import *
import time
import psutil

delta=30
alphas = [[0,110,48,94],[110,0,118,48],[48,118,0,110],[94,48,110,0]]

def findCharacter(c):
    if c=='A':
        return 0
    elif c=='C':
        return 1
    elif c=='G':
        return 2
    elif c=='T':
        return 3

def sequenceAlignment(firstString,secondString):
    firstStringLength=len(firstString)
    i=firstStringLength
    secondStringLength=len(secondString)
    j=secondStringLength
    firstStringAlignmentVal=""
    secondStringAlignmentVal=""
    
    opt=list(0 for i in range(0, secondStringLength+1))
    opt=list(opt.copy() for i in range(0,firstStringLength+1))
    
    for idx in range(secondStringLength+1):
        opt[0][idx]=idx*delta
    for idx in range(firstStringLength+1):
        opt[idx][0]=idx*delta
        
    for i in range(1,firstStringLength+1):
        for j in range(1,secondStringLength+1):
            if(secondString[j-1]==firstString[i-1]):
                opt[i][j]=opt[i-1][j-1]
            else:
                alphaCost = alphas[findCharacter(firstString[i-1])][findCharacter(secondString[j-1])]
                var1=opt[i-1][j-1]+alphaCost
                var2=opt[i-1][j]+delta
                var3=opt[i][j-1]+delta
                opt[i][j]=min(var3,var2,var1)
    
    while(i>0 and j>0):
        alphaCost = alphas[findCharacter(firstString[i-1])][findCharacter(secondString[j-1])]
        if secondString[j-1]==firstString[i-1]:
            secondStringAlignmentVal=secondString[j-1]+secondStringAlignmentVal
            j-=1
            firstStringAlignmentVal=firstString[i-1]+firstStringAlignmentVal
            i-=1

        elif opt[i][j]==opt[i-1][j-1]+alphaCost:
            secondStringAlignmentVal=secondString[j-1]+secondStringAlignmentVal
            j-=1
            firstStringAlignmentVal=firstString[i-1]+firstStringAlignmentVal
            i-=1

        elif opt[i][j]==opt[i-1][j]+delta:
            secondStringAlignmentVal="_"+secondStringAlignmentVal
            firstStringAlignmentVal=firstString[i-1]+firstStringAlignmentVal
            i-=1
        elif opt[i][j]==opt[i][j-1]+delta:
            firstStringAlignmentVal="_"+firstStringAlignmentVal
            secondStringAlignmentVal=secondString[j-1]+secondStringAlignmentVal
            j-=1
    while i>0:
        secondStringAlignmentVal="_"+secondStringAlignmentVal
        firstStringAlignmentVal=firstString[i-1]+firstStringAlignmentVal
        i-=1
    while j>0:
        firstStringAlignmentVal="_"+firstStringAlignmentVal
        secondStringAlignmentVal=secondString[j-1]+secondStringAlignmentVal
        j-=1
   
    return firstStringAlignmentVal,secondStringAlignmentVal,opt[firstStringLength][secondStringLength]


def sequenceAlignmentWithEfficientMemory(firstStr,secondStr,isReverseBool):
    firstStrLength=len(firstStr)
    secondStrLength=len(secondStr)
    opt=list(0 for i in range(0, secondStrLength+1))
    opt=list(opt.copy() for i in range(2))
    for i in range(secondStrLength+1):
        opt[0][i]=i*delta
    for i in range(1, firstStrLength+1):
        opt[1][0] = opt[0][0]+ delta
        stringCompare=False
        var1=""
        var2=""
        for j in range(1,secondStrLength+1):
            if isReverseBool:
                stringCompare=True if secondStr[secondStrLength-j]==firstStr[firstStrLength-i] else False
                var1=firstStr[firstStrLength-i]
                var2=secondStr[secondStrLength-j]
            else:
                stringCompare=True if secondStr[j-1]==firstStr[i-1] else False
                var1=firstStr[i-1]
                var2=secondStr[j-1]
            if(stringCompare):
                opt[1][j]=opt[0][j-1]
            else:
                alphaCost = alphas[findCharacter(var1)][findCharacter(var2)]
                ans1=opt[1][j-1]+delta
                ans2=opt[0][j]+delta
                ans3=opt[0][j-1]+alphaCost
                opt[1][j] = min(ans1,ans2,ans3)
        for i in range(0,secondStrLength+1):
            opt[0][i] = opt[1][i]
    return opt[1]


def sequenceAlignmentMinMethod(firstString,secondString):
    firstStringLength=len(firstString)
    secondStringLength=len(secondString)
    if firstStringLength<=2 or secondStringLength<=2:
        return sequenceAlignment(firstString,secondString)
    else:
        firstStringRight=sequenceAlignmentWithEfficientMemory(firstString[firstStringLength//2:],secondString,True)
        firstStringLeft=sequenceAlignmentWithEfficientMemory(firstString[:firstStringLength//2],secondString,False)
        
        firstStringOptimalVal = [firstStringLeft[index]+firstStringRight[secondStringLength-index] for index in range(secondStringLength+1)] 
        secondStringMiddleIndex=firstStringOptimalVal.index(min(firstStringOptimalVal))

        secondStringRight=sequenceAlignmentMinMethod(firstString[firstStringLength//2:],secondString[secondStringMiddleIndex:])  
        secondStringLeft=sequenceAlignmentMinMethod(firstString[:firstStringLength//2],secondString[:secondStringMiddleIndex])    
        
        secondStringAns=secondStringRight[2]+secondStringLeft[2]
        firstStringAns=secondStringRight[1]+secondStringLeft[1]
        optimalAnsValue=secondStringRight[0]+secondStringLeft[0]
        return optimalAnsValue,firstStringAns,secondStringAns

def writeDataToOutputFile(totalTime,totalMemoryUsed,outputFileName,optimalValue,firstStirngAns,secondStirngAns,):
    with open(outputFileName, 'w') as outfile:
        outfile.write(str(optimalValue))
        outfile.write('\n')
        outfile.write(str(firstStirngAns))
        outfile.write('\n')
        outfile.write(str(secondStirngAns))
        outfile.write('\n')
        outfile.write(str(totalTime))
        outfile.write('\n')
        outfile.write(str(totalMemoryUsed))

def readInputFile(inpFileName):
    openedFile = open(inpFileName, "r")
    stringInFile=openedFile.readlines()
    boolCheck=0
    first_str_indxs=[]
    first_str=""
    second_str_indxs=[]
    second_str=""
    for counter in stringInFile:
        counter=counter.strip()
        if(counter.isdigit() and boolCheck==1):
            cur=int(counter)
            first_str_indxs.append(cur)
        elif(counter.isdigit()):
            cur=int(counter)
            second_str_indxs.append(cur)
        elif(boolCheck==0):
            boolCheck=1
            first_str+=counter
        else:
            boolCheck=2
            second_str+=counter
    return first_str,first_str_indxs,second_str,second_str_indxs

def validateStringLength(originalLength, newLineCnt, newLength):
    return (2**newLineCnt)*originalLength == newLength

def generateString(inputStr,indexesList):
    oldStrLength = len(inputStr)
    prevStr=inputStr
    for curIdx in indexesList:
        idx=curIdx+1
        inputStr=prevStr[:idx]+prevStr+prevStr[idx:]
        prevStr=inputStr
    operationsCount = len(indexesList)
    newStrLength = len(inputStr)
    if validateStringLength(oldStrLength,operationsCount,newStrLength):
        return inputStr
    return None

#Read input file name and output file name as arguments
input_file_name=sys.argv[1]
output_file_name=sys.argv[2]
#reading given input file and storing 2 strings and indexes seperately for string one and string two
firstStr,firstStrIndexesList,secondStr,secondStrIndexesList=readInputFile(input_file_name)
#Here we regenerate string one and string two based on the indexes provided and update two strings
firstStr=generateString(firstStr,firstStrIndexesList)
secondStr=generateString(secondStr,secondStrIndexesList)

#calculation of time starts from here
timeBegin = time.time()

#here actual computation of sequence alignment method will be done by storing the results : optimalValue cost
#and two strings constructed
strOneAlignmentAns,strTwoAlignmentAns,optimalValAns=sequenceAlignmentMinMethod(firstStr,secondStr)
completedTime = time.time()

#computed total time as execution of the program logic ends here
totalTime = (completedTime-timeBegin)*1000

#computing the memory used
process = psutil.Process()
memoryInfo = process.memory_info()
totalMemoryUsed = int(memoryInfo.rss/1024)

#writing to output file : total time used, memory required, optimal value, two string alignments
writeDataToOutputFile(totalTime,totalMemoryUsed,output_file_name,optimalValAns,strOneAlignmentAns,strTwoAlignmentAns)
