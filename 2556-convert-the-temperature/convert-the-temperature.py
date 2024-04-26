class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        lis = []
        kel = celsius + 273.15
        far = celsius * 1.80 + 32.00
        lis.append(kel)
        lis.append(far)
        return lis

        