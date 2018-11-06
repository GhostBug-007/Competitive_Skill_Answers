def anagram(nInput):
    if nInput == 0:
        return 0
    else:
        str1=list(input())
        str2=list(input())
        totalAlphabets=len(str1+str2)
        count=0
        lStr1=len(str1)
        lStr2=len(str2)
        for alphabet in range(lStr1):
            for char in range(lStr2):
                if str1[alphabet] == str2[char]:
                    count+=1
                    str2[char]=""
                    break
        remAlphabet=totalAlphabets - (2*count)
        print(remAlphabet)
        return (anagram(nInput-1))

nInputs=int(input())
str1=[]
str2=[]
anagram(nInputs)
