filename = "new 13"
sumValue = 2020


with open(filename) as file:
    numbers =  file.readlines()

def check_sum(nums, k):
    #print("sum is : "+k)   
    for i in range(len(nums)-2):
        #print("first number :"+nums[i])
        for j in range(i+1, len(nums)-1):
            #print("Second number :"+nums[j])
             
             for l in range(j+2,len(nums)):

                if( (int(nums[i]) + int(nums[j]) + int(nums[l]) ) == k):
                    print("First number"+nums[i])
                    print("Second number"+nums[j])
                    print("Second number"+nums[l])
                    print((int(nums[j]) * int(nums[i]) * int(nums[l]) ))
                



print(check_sum(numbers,sumValue))


    

file.close()