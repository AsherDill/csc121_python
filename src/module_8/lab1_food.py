# Refer to this module's readme
class Food:

    base_hearts = 1

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.hearts = Food.calculate_hearts(ingredients)


    @classmethod
    def calculate_hearts(csl, ingredients):
        hearts = csl.base_hearts
        for ingredient in ingredients:
            if "hearty" in ingredient.lower():
                hearts += 2
            else:
                hearts += 1
        return hearts

    @classmethod
    def from_nothing(csl, hearts):
        food = csl(ingredients=[])
        food.hearts = hearts
        return food

def main():
    mushroom_skewer = Food(ingredients=["Mushroom", "Hearty Mushroom"])
    print(f"This Mushroom Skewer heals {mushroom_skewer.hearts} hearts! ðŸ’•")

    mushroom_skewer = Food(ingredients=["Hearty Mushroom", "Hearty Mushroom"])
    print(f"This Mushroom Skewer heals {mushroom_skewer.hearts} hearts! ðŸ’•")

    mushroom_skewer = Food.from_nothing(hearts=2)
    print(f"This Mushroom Skewer heals {mushroom_skewer.hearts} hearts! ðŸ’•")

main()