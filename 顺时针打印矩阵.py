class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        arr = []
        while(len(matrix)):
            arr.extend(matrix[0])
            matrix.pop(0)
            matrix=self.trans(matrix)
        return arr

    def trans(self,matrix):
        tmp = list(zip(*matrix))[::-1]
        tmp=list(map(list,tmp))
        return tmp


S = Solution()
print(S.printMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
