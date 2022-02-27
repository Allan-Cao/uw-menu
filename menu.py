import requests as r
from bs4 import BeautifulSoup
import datetime

dish_types = {
    "Soup Bar": "Soup",
    "Hot Dish": "Hot Dish",
    "THEME NIGHT!": "Holiday Menu",
    "Dessert": "Dessert",
    "Creation Station": "Cooking Station",
    "Induction Station": "Cooking Station",
    "Induction Station 7:30pm to 9:30pm": "Specialty Service",
    "Station 57": "Cooking Station",
}

intolerances = {
    "Halal": "halal",
    "Made without dairy": "dairy-free",
    "Made without Gluten": "gluten-free",
    "Vegetarian": "vegetarian",
    "Vegan": "vegan",
}

locations = {
    "Village 1 - Mudie’s - OPEN": "V1",
    "Ron Eydt Village - REVelation -OPEN": "REV",
    "The Market - OPEN": "CMH",
}

class dish():
    def __init__(self, name, restrictions, station):
        self.name = name
        self.restrictions = [intolerances[restriction] for restriction in restrictions]
        self.station = station
        self.dish_type = dish_types[station]
class cafeteria(dish):
    def __init__(self, res, dishes):
        self.location = locations[' '.join(res.text.split())]
        self.dishes = dishes
class menu(cafeteria):
    def __init__(self, year, month, day):
        self.date = datetime.date(year,month,day)
        self.locations = self.__get_menu()
    def get_menu(self):
        locations = []
        if type(self.date) is not datetime.date:
            raise ValueError("Invalid Date object given")
        raw_menu = r.get(f"https://uwaterloo.ca/food-services/locations-and-hours/daily-menu?field_uw_fs_dm_date_value%5Bvalue%5D%5Bdate%5D={self.date.year}-{self.date.month}-{self.date.day}")
        soup = BeautifulSoup(raw_menu.content, 'html.parser')
        verify_date = soup.find(class_ = "view-empty")
        if verify_date != None:
            self.date = None
            self.dishes = []
        else:
            daily_menu = soup.find_all(class_ = "paragraphs-item-uw-fs-para-daily-menu")
            for location in daily_menu:
                residence_location = location.find(class_="dm-location")
                dishes = location.find_all(class_="paragraphs-item-uw-fs-dm-daily-outlet-menu")
                for menu_types in dishes:
                    menu_name = menu_types.find(class_="dm-menu-type").text
                    menu_items = []
                    # Individual Items
                    for item in menu_types.find_all(class_="dm-menu-item"):
                        menu_items.append(dish(item.text.strip(),[img['title'] for img in item.find_all('img', alt=True)], menu_name))
                locations.append(cafeteria(residence_location, menu_items))
        return locations
    __get_menu = get_menu

daily_menu = menu(2022,2,23)
print(daily_menu)