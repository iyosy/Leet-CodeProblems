class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop(0)
        salary.pop(len(salary)-1)
        sum = 0
        for i in range(len(salary)):
            sum += salary[i]
        ave = sum/len(salary) 
        return ave   
        
       


        