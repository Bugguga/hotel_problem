class Hotel:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def find_room(self, room_id):
        return self.rooms[room_id-1]

    def cancel_booking(self, booking_id):
        for room in self.rooms:
            if room.delete_booking(booking_id):
                return
        return
