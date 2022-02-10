import requests as r
from bs4 import BeautifulSoup
import datetime

intolerances = {
    "Halal": "halal",
    "Made without dairy": "dairy-free",
    "Made without Gluten": "gluten-free",
    "Vegetarian": "vegetarian",
    "Vegan": "vegan",
}
def get_menus(date=None):
    if date == None:
        raw_menu = r.get("https://uwaterloo.ca/food-services/locations-and-hours/daily-menu")
        soup = BeautifulSoup(raw_menu.content, 'html.parser')
        menus = soup.find_all(class_ = "paragraphs-item-uw-fs-para-daily-menu")
        return menus
    else:
        # TODO: check valid date
        try:
            raw_menu = r.get(f"https://uwaterloo.ca/food-services/locations-and-hours/daily-menu?field_uw_fs_dm_date_value%5Bvalue%5D%5Bdate%5D={date.year}-{date.month}-{date.day}")
            soup = BeautifulSoup(raw_menu.content, 'html.parser')
            menus = soup.find_all(class_ = "paragraphs-item-uw-fs-para-daily-menu")
            return menus
        except:
            raise ValueError('Date does not work lmao')
def parse_daily_menu(daily_menu):
    for location in daily_menu:
        res = location.find(class_="dm-location")
        print(res.text)
        dishes = location.find_all(class_="paragraphs-item-uw-fs-dm-daily-outlet-menu")
        for menu_types in dishes:
            menu_name = menu_types.find(class_="dm-menu-type")
            print(menu_name.text)
            menu_items = []
            for item in menu_types.find_all(class_="dm-menu-item"):
                menu_items.append([item.text.strip(),[img['title'] for img in item.find_all('img', alt=True)]])
            print(menu_items)

parse_daily_menu(get_menus())
x = datetime.datetime(2022, 2, 9)
parse_daily_menu(get_menus(x))