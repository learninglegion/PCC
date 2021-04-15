from restaurant import Restaurant
from restaurant import IceCreamStand

my_restaurant = Restaurant('bojo', 'chinese')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.read_number_served()
my_restaurant.set_number_served(50)
my_restaurant.read_number_served()
my_restaurant.increment_number_served(25)
my_restaurant.read_number_served()
my_stand = IceCreamStand('baskin robins', 'ice cream')
my_stand.display_flavors()