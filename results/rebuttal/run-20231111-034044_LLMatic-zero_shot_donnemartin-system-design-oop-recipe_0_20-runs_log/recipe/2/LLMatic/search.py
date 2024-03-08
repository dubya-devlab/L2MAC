class Search:
	def __init__(self, recipes):
		self.recipes = recipes

	def search_by_ingredient(self, ingredient):
		return [recipe for recipe in self.recipes if ingredient in recipe.ingredients]

	def search_by_name(self, name):
		return [recipe for recipe in self.recipes if name in recipe.name]

	def search_by_category(self, category):
		return [recipe for recipe in self.recipes if category in recipe.type]

	def categorize_by_type(self, type):
		return [recipe for recipe in self.recipes if type in recipe.type]

	def categorize_by_cuisine(self, cuisine):
		return [recipe for recipe in self.recipes if cuisine in recipe.cuisine]

	def categorize_by_diet(self, diet):
		return [recipe for recipe in self.recipes if diet in recipe.diet]
