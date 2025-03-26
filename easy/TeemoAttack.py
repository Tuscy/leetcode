class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        previous = timeSeries[0] #Set initial attack time
        
        for i in timeSeries[1:]:
            if i - previous >= duration: #Find if the duration is longer than the time between attacks
                total += duration #Add duration to total if so
            else:
                total += i - previous #Otherwise add the time between attacks
            previous = i #Set the new previous attack time

        total += duration #Add the duration after final attack

        return total