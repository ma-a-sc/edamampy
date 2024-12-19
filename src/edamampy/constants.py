INCLUDED_FIELDS = (
    "uri",
    "label",
    "image",
    "images",
    "source",
    "url",
    "shareAs",
    "yield",
    "dietLabels",
    "healthLabels",
    "cautions",
    "ingredientLines",
    "ingredients",
    "calories",
    "glycemicIndex",
    "inflammatoryIndex",
    "totalCO2Emissions",
    "totalWeight",
    "totalTime",
    "cuisineType",
    "mealType",
    "dishType",
    "totalNutrients",
    "totalDaily",
    "digest",
    "tags",
    "externalId",
)
RANDOM_FIELD = ("true", "false")
IMAGE_SIZE = ("LARGE", "REGULAR", "SMALL", "THUMBNAIL")
DISH_TYPE = (
    "Biscuits and cookies",
    "Bread",
    "Cereals",
    "Condiments and sauces",
    "Desserts",
    "Drinks",
    "Main course",
    "Pancake",
    "Preps",
    "Preserve",
    "Salad",
    "Sandwiches",
    "Side dish",
    "Soup",
    "Starter",
    "Sweets",
)
MEAL_TYPE = ("Breakfast", "Dinner", "Lunch", "Snack", "Teatime")
HEALTH_TYPE = (
    "alcohol-cocktail",
    "alcohol-free",
    "celery-free",
    "crustacean-free",
    "dairy-free",
    "DASH",
    "egg-free",
    "fish-free",
    "fodmap-free",
    "gluten-free",
    "immuno-supportive",
    "keto-friendly",
    "kidney-friendly",
    "kosher",
    "low-fat-abs",
    "low-potassium",
    "low-sugar",
    "lupine-free",
    "Mediterranean",
    "mollusk-free",
    "mustard-free",
    "no-oil-added",
    "paleo",
    "peanut-free",
    "pescatarian",
    "pork-free",
    "red-meat-free",
    "sesame-free",
    "shellfish-free",
    "soy-free",
    "sugar-conscious",
    "sulfite-free",
    "tree-nut-free",
    "vegan",
    "vegetarian",
    "wheat-free",
)
CUISINE_TYPE = (
    "American",
    "Asian",
    "British",
    "Caribbean",
    "Central Europe",
    "Chinese",
    "Eastern Europe",
    "French",
    "Indian",
    "Italian",
    "Japanese",
    "Kosher",
    "Mediterranean",
    "Mexican",
    "Middle Eastern",
    "Nordic",
    "South American",
    "South East Asian",
)
DIET_TYPE = (
    "balanced",
    "high-fiber",
    "high-protein",
    "low-carb",
    "low-fat",
    "low-sodium",
)

##### Allergies ######
# maps different allergies to the health_type
ALLERGIES_MAPPING = {
    "celery": "celery-free",
    "gluten": "gluten-free",
    "crustaceans": "crustacean-free",
    "eggs": "egg-free",
    "fish": "fish-free",
    "lupins": "lupine-free",
    "dairy": "dairy-free",
    "molluscs": "mollusk-free",
    "mustard": "mustard-free",
    "nuts": "tree-nut-free",
    "peanuts": "peanut-free",
    "sesame": "sesame-free",
    "soy": "soy-free",
    "sulfites": "sulfite-free",
    "shellfish": "shellfish-free",
    "fodmap": "fodmap-free",
}

API_FIELD_VALIDATOR_MAPPING = {
    "q": "_validate_q",
    "ingr": "_validate_ingr",
    "diet": "_validate_diet",
    "health": "_validate_health",
    "cuisineType": "_validate_cuisineType",
    "mealType": "_validate_mealType",
    "dishType": "_validate_dishType",
    "calories": "_validate_floating_point_range",
    "time": "_validate_time",
    "imageSize": "_validate_imageSize",
    "glycemicIndex": "_validate_floating_point_range",
    "inflammatoryIndex": "_validate_floating_point_range",
    "nutrients[CA]": "_validate_nutrients",
    "nutrients[CHOCDF]": "_validate_nutrients",
    "nutrients[CHOCDF.net]": "_validate_nutrients",
    "nutrients[CHOLE]": "_validate_nutrients",
    "nutrients[ENERC_KCAL]": "_validate_nutrients",
    "nutrients[FAMS]": "_validate_nutrients",
    "nutrients[FAPU]": "_validate_nutrients",
    "nutrients[FASAT]": "_validate_nutrients",
    "nutrients[FAT]": "_validate_nutrients",
    "nutrients[FATRN]": "_validate_nutrients",
    "nutrients[FE]": "_validate_nutrients",
    "nutrients[FIBTG]": "_validate_nutrients",
    "nutrients[FOLAC]": "_validate_nutrients",
    "nutrients[FOLDFE]": "_validate_nutrients",
    "nutrients[FOLFD]": "_validate_nutrients",
    "nutrients[K]": "_validate_nutrients",
    "nutrients[MG]": "_validate_nutrients",
    "nutrients[NA]": "_validate_nutrients",
    "nutrients[NIA]": "_validate_nutrients",
    "nutrients[P]": "_validate_nutrients",
    "nutrients[PROCNT]": "_validate_nutrients",
    "nutrients[RIBF]": "_validate_nutrients",
    "nutrients[SUGAR]": "_validate_nutrients",
    "nutrients[SUGAR.added]": "_validate_nutrients",
    "nutrients[Sugar.alcohol]": "_validate_nutrients",
    "nutrients[THIA]": "_validate_nutrients",
    "nutrients[TOCPHA]": "_validate_nutrients",
    "nutrients[VITA_RAE]": "_validate_nutrients",
    "nutrients[VITB12]": "_validate_nutrients",
    "nutrients[VITB6A]": "_validate_nutrients",
    "nutrients[VITC]": "_validate_nutrients",
    "nutrients[VITD]": "_validate_nutrients",
    "nutrients[VITK1]": "_validate_nutrients",
    "nutrients[WATER]": "_validate_nutrients",
    "nutrients[ZN]": "_validate_nutrients",
    "co2EmissionsClass": "_validate_co2_emissions_class",
    "tag": "_validate_tag",
    "sysTag": "_validate_sys_tag",
    "Edamam-Account-User": "_validate_edamam_account_user",
    "Accept-Language": "_validate_accept_language",
    "excluded": "_validate_excluded",
    "random": "_validate_random",
    "field": "_validate_field",
}