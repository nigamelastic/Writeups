filename = "new 13"
sumValue = 2020


with open(filename) as file:
    numbers =  file.readlines()

def check_sum(nums, k):
    #print("sum is : "+k)   
    for i in range(len(nums)):
        #print("first number :"+nums[i])
        for j in range(i+1, len(nums)):
            #print("Second number :"+nums[j])
             
            if((int(nums[i]) + int(nums[j])) == k):
                print("First number"+nums[i])
                print("Second number"+nums[j])
                print((int(nums[j])*int(nums[i])))
                



print(check_sum(numbers,sumValue))


    

file.close()