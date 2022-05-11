def isStringPermutation(str1, str2) :
    if ("".join(sorted(str1)) == "".join(sorted(str2))) :
        return true
    return false

def pairsThatEqualSum(inputArr, targetSum) :
    ret = []
    hashSet = {}
    # iterate thru input arr, storing nums and checking for diff
    for i in range(len(inputArr)) :
        hashSet.add(inputArr[i])
        # if diff found, add to return result
        if ((targetSum - inputArr[i]) in hashSet) :
            ret.append([inputArr[i], targetSum-inputArr[i]])
    return ret
    
