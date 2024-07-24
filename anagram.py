

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s)==sorted(t) 1st method
        #return Counter(s)==Counter(t) 2nd method
        if len(s)!=len(t):
            return False
        countS,countT={},{}
        for i in range(len(s)):
            countS[s[i]]=1+countS.get(s[i],0)
            countT[t[i]]=1+countT.get(t[i],0)
        return countS==countT
    s=str(input("word1"))
    t=str(input("word2"))
    isAnagram(s,t)