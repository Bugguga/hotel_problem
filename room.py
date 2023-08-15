import itertools


class Room:
    id_obj = itertools.count()

    def __init__(self, name):
        self._id = next(Room.id_obj)+1
        self.name = name
        self.bookings = dict()

    def book(self, booking):
        self.bookings[booking.get_id()]=(booking)

    def valid_date(self, start, end):
        for keys ,values in self.bookings.items():
            if (values.start <= start <= values.end or values.start <= end <= values.end):
                return False
        return True

    def delete_booking(self, booking_id):
        self.bookings.pop(booking_id)