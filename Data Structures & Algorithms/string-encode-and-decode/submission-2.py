class Solution:

    def encode(self, strs: list[str]) -> str:
        return "".join(f"{len(word)}#{word}" for word in strs)
    
    def decode(self, s: str) -> list[str]:
        i = 0
        res = []
        while i < len(s):
            str_length = ""

            while s[i] != "#":
                str_length += (s[i])
                i += 1

            str_length = int(str_length)
            res.append(s[i+1:i+1+str_length])
            i = i+str_length+1

        return res