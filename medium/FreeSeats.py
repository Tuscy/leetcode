class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
        order = sorted(range(len(times)), key = lambda x: times[x][0])  # Order friends by arrival time - key usage 
        emptySeats, takenSeats = list(range(len(times))), []            # Initialise available seats and taken seats as heaps

        for i in order:                                                 # Tracking seats that become free 
            ar, lv = times[i]

            while takenSeats and takenSeats[0][0] <= ar:                # While takenseats is valid and less than maximum
                heappush(emptySeats, heappop(takenSeats)[1])            
            seat = heappop(emptySeats)                                  # Assigning lowest number to the next friend

            if i == targetFriend: return seat                           # Output the seat value when its the target

            heappush(takenSeats,(lv, seat))                             # Adding the chair to taken seats as well as when they leave