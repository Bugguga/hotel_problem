import itertools


class Booking:
    id_obj = itertools.count()

    def __init__(self, start, end):
        self._id = next(Booking.id_obj)+1
        self.start = start
        self.end = end

    def get_id(self):
        return self._id
