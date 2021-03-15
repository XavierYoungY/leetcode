# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        a=s.split(' ')[::-1]
        b=' '.join(a)
        return b
    
    
if __name__ == '__main__':
    s=Solution()
    print(s.ReverseSentence("nowcoder. a am I"))
        