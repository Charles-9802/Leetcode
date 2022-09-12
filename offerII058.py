class MyCalendar:

    def __init__(self):
        self.result = []

    def book(self, start: int, end: int) -> bool:
        if not self.result:
            self.result.append([start, end])
            return True
        else:
            i = 0
            while i < len(self.result):
                if (start >= self.result[i][0] and start < self.result[i][1]) or (end > self.result[i][0] and end <= self.result[i][1]) or (start < self.result[i][0] and end >= self.result[i][1]):
                    return False
                else:
                    i += 1
            self.result.append([start, end])
            return True


# class MyCalendar:
#     def __init__(self):
#         self.booked = []
#
#     def book(self, start: int, end: int) -> bool:
#         if any(l < end and start < r for l, r in self.booked):
#             return False
#         self.booked.append((start, end))
#         return True
