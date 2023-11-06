import heapq
class SeatManager(object):

    def __init__(self, n):
        self.available_seats = list(range(1, n+1))
        heapq.heapify(self.available_seats)

    def reserve(self):
        if self.available_seats:
            return heapq.heappop(self.available_seats)
        return -1  # No available seats left

    def unreserve(self, seatNumber):
        heapq.heappush(self.available_seats, seatNumber)