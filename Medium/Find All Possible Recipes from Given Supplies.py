# Find All Possible Recipes from Given Supplies
# O(n) time complexity, O(n) space complexity
from collections import defaultdict
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ingred_to_recipes = defaultdict(list)
        recipes_to_ingredients_count = defaultdict(int)
        res = []
        queue = supplies
        for i in range(len(recipes)):
            recipe = recipes[i]
            
            for ingredient in ingredients[i]:
                ingred_to_recipes[ingredient].append(recipe)
            
            recipes_to_ingredients_count[recipe] = len(ingredients[i])

        while queue:
            supply = queue.pop()
            for recipe in ingred_to_recipes[supply]:
                recipes_to_ingredients_count[recipe] -= 1
                if recipes_to_ingredients_count[recipe] == 0:
                    queue.append(recipe)
                    res.append(recipe)
        return res