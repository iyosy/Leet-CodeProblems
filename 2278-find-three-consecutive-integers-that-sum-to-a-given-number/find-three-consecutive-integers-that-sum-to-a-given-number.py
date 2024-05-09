class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        val = num//3
        if num % 3 != 0:
            return []
        else:
            lis = [val]*3
            lis[0] -=1
            lis[2] +=1
            return lis

        

        



        