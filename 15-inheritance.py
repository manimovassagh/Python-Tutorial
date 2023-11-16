class User:
    def __init__(self, name, age):
      self.name = name
      self.age = age
    def __str__(self):
        return f"User: {self.name}, {self.age} years old"
    def login(self):
        print(f"{self.name} logged in")

class Admin(User):
          def __init__(self, name, age,is_admin):
              super().__init__(name, age)
              self.is_admin = is_admin
          def login(self):
              print(f"{self.name} logged in as admin")

admin = Admin("John", 25, True)
admin.login()
user = User("Mani", 30)
user.login()
   
