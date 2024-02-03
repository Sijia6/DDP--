class Account:

    def __init__(self, given_name, surname, user_id, contact, area):
        self.given_name = given_name.capitalize()
        self.surname = surname.capitalize()
        self.user_id = user_id
        self.contact = contact
        self.area = area.capitalize()

    def display_info(self):
        print(f"\nName: {self.given_name} {self.surname}")
        print(f"  User ID: {self.user_id}")
        print(f"  Contact: {self.contact}")
        print(f"  Area: {self.area}")

    def welcome_message(self):
        print(f"\nHello again, {self.user_id}!")

# Example usage
user1 = Account('mary', 'he', 'maryhe', 'my@example.com', 'alaska')
user1.display_info()
user1.welcome_message()

user2 = Account('iris', 'he', 'irishe', 'is@example.com', 'alaska')
user2.display_info()
user2.welcome_message()
