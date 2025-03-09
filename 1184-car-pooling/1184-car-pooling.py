class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengerTrips =[]

        for trip in trips:
            passengers, start, end = trip
            heapq.heappush(passengerTrips, (start, end, passengers))
        
        destinations = [] # (end, passengers)
        while passengerTrips:
            start, end, passengers = heapq.heappop(passengerTrips)
            
            while destinations and destinations[0][0] <= start:
                _, cap = heapq.heappop(destinations)
                capacity += cap
            
            if passengers <= capacity:
                heapq.heappush(destinations, (end, passengers))
                capacity -= passengers
            else:
                return False

        return True