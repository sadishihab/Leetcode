class MyCalendar(object):

    def __init__(self):
        # store all booked intervals
        self.bookings = []

    def book(self, startTime, endTime):

        # check overlap with existing bookings
        for start, end in self.bookings:

            # overlap condition
            if startTime < end and endTime > start:
                return False

        # if no overlap, add booking
        self.bookings.append((startTime, endTime))

        return True
