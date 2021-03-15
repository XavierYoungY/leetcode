class Solution:
    def duplicate(self , numbers ):
        # write code here
        length=len(numbers)
        for i in range(length):
            if i+1>length:break
            if numbers[i] in numbers[i + 1:]:
                return numbers[i]
        return -1
if __name__ == "__main__":
    f = Solution()
    a = f.duplicate([2, 4, 3, 1, 4])
    print(a)
