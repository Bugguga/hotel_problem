class Hotel:
    def __init__(self):
        self.rooms = []
        self.bookMap = dict()  # booking_id => room_id

    def add_room(self, room):
        self.rooms.append(room)

    def add_book(self, room_id, booking_id):
        self.bookMap[booking_id] = room_id

    def find_room(self, room_id):
        return self.rooms[room_id-1]

    def cancel_booking(self, booking_id):
        self.rooms[self.bookMap[booking_id]-1].delete_booking(booking_id)
