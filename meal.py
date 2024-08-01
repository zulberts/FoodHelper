import requests
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Meal:
    idMeal: str
    strMeal: str
    strCategory: str
    strArea: str
    strInstructions: str
    strMealThumb: str
    strTags: Optional[str]
    strYoutube: Optional[str]
    ingredients: List[str] = field(default_factory=list)
    measures: List[str] = field(default_factory=list)


def get_random_meal() -> Optional[Meal]:
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    response = requests.get(url)
    if response.status_code == 200:
        meal_data = response.json()["meals"][0]
        ingredients = [
            meal_data[f"strIngredient{i}"]
            for i in range(1, 21)
            if meal_data[f"strIngredient{i}"]
        ]
        measures = [
            meal_data[f"strMeasure{i}"]
            for i in range(1, 21)
            if meal_data[f"strMeasure{i}"]
        ]
        meal = Meal(
            idMeal=meal_data["idMeal"],
            strMeal=meal_data["strMeal"],
            strCategory=meal_data["strCategory"],
            strArea=meal_data["strArea"],
            strInstructions=meal_data["strInstructions"],
            strMealThumb=meal_data["strMealThumb"],
            strTags=meal_data.get("strTags"),
            strYoutube=meal_data.get("strYoutube"),
            ingredients=ingredients,
            measures=measures,
        )
        return meal
    else:
        print("Failed to retrieve meal details.")
        return None
