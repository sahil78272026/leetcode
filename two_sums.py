nums = [3,3]
target = 6
newList =[]

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            newList.append(i)
            newList.append(j)
            break
        break

print(newList)

