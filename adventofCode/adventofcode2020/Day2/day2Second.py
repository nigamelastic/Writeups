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
        firstIndex = int(rangeValue[0])
        secondIndex = int(rangeValue[1])
        print(password[firstIndex])
        print(password[secondIndex])
        print(password)
        if( (letter==password[firstIndex]) ^ (letter==password[secondIndex]) ):
            count+=1
            print("above is correct")
        
      
    return count





print(getCorrectPassword(input))

file.close()