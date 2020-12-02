filename="input.txt"

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
        
        occurence=0
        for char in password: 
            if (char == letter): 
                occurence = occurence + 1
        print(rangeValue)
        print(letter)

        if (occurence in range(int(rangeValue[0]), int(rangeValue[1])+1)):
            print(password)
            count=count+1
    return count





print(getCorrectPassword(input))

file.close()