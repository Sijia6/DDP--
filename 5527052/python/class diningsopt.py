class DiningSpot():

    def __init__(self, restaurant_name, food_style):
        self.restaurant_name = restaurant_name.title()
        self.food_style = food_style

    def display_details(self):
        message = f"{self.restaurant_name} offers excellent {self.food_style}."
        print("\n" + message)

    def announce_opening(self):
        message = f"{self.restaurant_name} is now open for business. Welcome!"
        print("\n" + message)

class DessertParlor(DiningSpot):

    def __init__(self, restaurant_name, food_style='dessert'):
        super().__init__(restaurant_name, food_style)
        self.dessert_flavors = [] 

    def display_flavors(self):
        print("\nAvailable dessert flavors:")
        for flavor in self.dessert_flavors:
            print(f"- {flavor.title()}")

sweet_spot = DessertParlor('Sweet Spot')
sweet_spot.dessert_flavors = ['strawberry', 'mint chocolate', 'lemon']

sweet_spot.display_details()
sweet_spot.display_flavors()
