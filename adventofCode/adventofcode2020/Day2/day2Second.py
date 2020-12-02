filename="input.txt"
#filename="dummyinput.txt"
with open(filename) as file:
    input =  file.readlines()




def getCorrectPassword(stringInput):
    count=0
    for i in range(len(input)):
        
        #return stringInput
        stringInputLine = input[i].split(":")
        letter=stringInputLine[0].split()[1]
        rangeValue=stringInputLine[0].split()[0].split("-")
        password=stringInputLine[1]
        firstIndex = int(rangeValue[0])-1
        secondIndex = int(rangeValue[1])-1
        
        if( (letter==password[firstIndex]) ^ (letter==password[secondIndex]) ):
            count+=1
        
      
    return count





print(getCorrectPassword(input))

file.close()