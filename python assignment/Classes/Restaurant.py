# Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: 
# a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of information, 
# and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, 
# and then call both methods

class Restaurant:
	"""creating a resturant class"""
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print("Delicious foods!")

	def open_restaurant(self):
		print("We are now open!")


restaurant = Restaurant("Colab_foods", "Best nigerian dishes")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print("\n")
restaurant.describe_restaurant()
restaurant.open_restaurant()