class Solution:
    def match(self , str , pattern ):
        p=pattern
        s=str
        if not s and not p:
            return True
        elif s and not p:
            return False
        elif not s and p:
            if len(p)>1 and p[1]=='*':
                return self.match(s,p[2:])
            else: return False
        else:
            if s[0]==p[0]:
                return self.match(s[1:],p[1:])
            if s[0]!=p[0]:
                
                if len(p)<=1:
                    return False
                else:
                    if p[0]=='.':
                        if p[1]!='*':
                            return self.match(s[1:],p[1:])
                        else:
                            return self.match(s,p[2:]) or self.match(s[1:],p[2:]) or self.match(s[2:],p[2:])
                            
            
            
if __name__ == '__main__':
    s=Solution()
    print(s.match("a",".*"))
    