class User:
    def __init__(self, name, age):
      self.name = name
      self.age = age
    def login(self):
        print("User logged in")

class Room:
    def __init__(self, room_number):
        self.room_number = room_number 
    def reserve(self):
        print("Room reserved")
room = Room(124)
room.reserve()