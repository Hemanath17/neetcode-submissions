class Solution:

    def encode(self, strs: List[str]) -> str:
        res= []
        for s in strs: #loop trough every string 
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # to track where are we in the encoded string
        while i< len(s):
            j = i
            while s[j] != '#': #j' forward until it finds the '#' delimiter
                j += 1
            length = int(s[i:j])
            #Slice out the number string and convert it to an integer
            i = j+ 1
            j = i+ length
            res.append(s[i:j])
            i = j
        return res


