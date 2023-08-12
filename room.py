import itertools


class Room:
    id_obj = itertools.count()

    def __init__(self, name):
        self._id = next(Room.id_obj)+1
        self.name = name
        self.bookings = []

    def book(self, booking):
        self.bookings.append(booking)

    def valid_date(self, start, end):
        for booking in self.bookings:
            if (booking.start <= start <= booking.end or booking.start <= end <= booking.end):
                return False
        return True

    def delete_booking(self, booking_id):
        for booking in self.bookings:
            if booking_id == booking.get_id():
                # delete from self.bookings
                self.bookings.remove(booking)
                # delete actual object
                del booking
                return True
        return False
