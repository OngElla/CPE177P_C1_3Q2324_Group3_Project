import flet as ft

class Chat(ft.UserControl):
    def __init__(self, food_data):
        super().__init__()
        self.food_data = food_data

    def build(self):
        self.heading = ft.Text(value="Calorie Tracker Chatbot", size=24)
        self.text_input = ft.TextField(hint_text="Enter food item", expand=True, multiline=True)
        self.output_column = ft.Column()
        self.scroll = True

        return ft.Column(
            width=800,
            controls=[
                self.heading,
                ft.Row(
                    controls=[
                        self.text_input,
                        ft.ElevatedButton("Submit", height=60, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=1)), on_click=self.btn_clicked),
                    ],
                ),
                self.output_column,
            ],
        )

    def btn_clicked(self, event):
        user_input = self.text_input.value.lower()

        user_items = [item.strip() for item in user_input.split(',')]

        total_calories = 0
        food_items_found = []

        for category, items in self.food_data.items():
            for item in items:
                if item['FoodItem'].lower() in user_items:
                    calories = int(item['Cals_per100grams'].split()[0])  # Extracting the calorie count
                    total_calories += calories
                    food_items_found.append((item['FoodItem'], calories))

        if food_items_found:
            output_lines = [f"The calorie count for {food} is {calories} per 100 grams." for food, calories in food_items_found]
            output_lines.append(f"Total calories for all items: {total_calories} per 100 grams.")
            self.output = '\n'.join(output_lines)
        else:
            self.output = "Sorry, I couldn't find information for the entered food items."

        result = Output(self.output, self.text_input.value, self.outputDelete)
        self.output_column.controls.append(result)
        self.text_input.value = ""
        self.update()

    def outputDelete(self, result):
        self.output_column.controls.remove(result)
        self.update()


class Output(ft.UserControl):
    def __init__(self, myoutput, mytext_input, myoutput_delete):
        super().__init__()
        self.myoutput = myoutput 
        self.mytext_input = mytext_input
        self.myoutput_delete = myoutput_delete

    def build(self):
        self.output_display = ft.Text(value=self.myoutput, selectable=True)
        self.delete_button = ft.IconButton(ft.icons.DELETE_OUTLINE_SHARP, on_click=self.delete)
        self.input_display = ft.Container(ft.Text(value=self.mytext_input), bgcolor=ft.colors.BLUE_GREY_100, padding=10)
        self.display_view = ft.Column(controls=[self.input_display, self.output_display, self.delete_button])
        return self.display_view

    def delete(self, e):
        self.myoutput_delete(self)


def main(page):
    page.scroll = True
    page.window_width = 800
    page.window_height = 600

    food_data = {
        "CannedFruit": [
            {
                "FoodItem": "Applesauce",
                "per100grams": "100g",
                "Cals_per100grams": "62 cal",
                "KJ_per100grams": "260 kJ"
            },
            {
                "FoodItem": "Canned Apricots",
                "per100grams": "100g",
                "Cals_per100grams": "48 cal",
                "KJ_per100grams": "202 kJ"
            },
            {
                "FoodItem": "Blackberries",
                "per100grams": "100g",
                "Cals_per100grams": "92 cal",
                "KJ_per100grams": "386 kJ"
            },
            {
                "FoodItem": "Blueberries",
                "per100grams": "100g",
                "Cals_per100grams": "88 cal",
                "KJ_per100grams": "370 kJ"
            },
            {
                "FoodItem": "Canned Cherries",
                "per100grams": "100g",
                "Cals_per100grams": "54 cal",
                "KJ_per100grams": "227 kJ"
            },
            {
                "FoodItem": "Cranberries",
                "per100grams": "100g",
                "Cals_per100grams": "178 cal",
                "KJ_per100grams": "748 kJ"
            },
            {
                "FoodItem": "Canned Crushed Pineapple",
                "per100grams": "100g",
                "Cals_per100grams": "53 cal",
                "KJ_per100grams": "223 kJ"
            },
            {
                "FoodItem": "Canned Figs",
                "per100grams": "100g",
                "Cals_per100grams": "107 cal",
                "KJ_per100grams": "449 kJ"
            },
            {
                "FoodItem": "Cocktail",
                "per100grams": "100g",
                "Cals_per100grams": "81 cal",
                "KJ_per100grams": "340 kJ"
            },
            {
                "FoodItem": "Salad",
                "per100grams": "100g",
                "Cals_per100grams": "50 cal",
                "KJ_per100grams": "210 kJ"
            },
            {
                "FoodItem": "Gooseberries",
                "per100grams": "100g",
                "Cals_per100grams": "73 cal",
                "KJ_per100grams": "370 kJ"
            },
            {
                "FoodItem": "Grapefruit",
                "per100grams": "100g",
                "Cals_per100grams": "37 cal",
                "KJ_per100grams": "155 kJ"
            },
            {
                "FoodItem": "Grapes",
                "per100grams": "100g",
                "Cals_per100grams": "76 cal",
                "KJ_per100grams": "319 kJ"
            },
            {
                "FoodItem": "Orange",
                "per100grams": "100g",
                "Cals_per100grams": "71 cal",
                "KJ_per100grams": "298 kJ"
            },
            {
                "FoodItem": "Mango",
                "per100grams": "100g",
                "Cals_per100grams": "65 cal",
                "KJ_per100grams": "273 kJ"
            },
            {
                "FoodItem": "Mangosteen",
                "per100grams": "100g",
                "Cals_per100grams": "73 cal",
                "KJ_per100grams": "307 kJ"
            },
            {
                "FoodItem": "Canned mixed fruit",
                "per100grams": "100g",
                "Cals_per100grams": "71 cal",
                "KJ_per100grams": "298 kJ"
            },
            {
                "FoodItem": "Cherries",
                "per100grams": "100g",
                "Cals_per100grams": "81 cal",
                "KJ_per100grams": "340 kJ"
            },
            {
                "FoodItem": "Canned Orange",
                "per100grams": "100g",
                "Cals_per100grams": "62 cal",
                "KJ_per100grams": "260 kJ"
            },
            {
                "FoodItem": "Canned mixed fruit",
                "per100grams": "100g",
                "Cals_per100grams": "71 cal",
                "KJ_per100grams": "298 kJ"
            },
            {
                "Category": "CannedFruit",
                "FoodItem": "Canned Peaches",
                "per100grams": "100g",
                "Cals_per100grams": "54 cal",
                "KJ_per100grams": "227 kJ"
            },
            {
                "Category": "CannedFruit",
                "FoodItem": "Canned Pears",
                "per100grams": "100g",
                "Cals_per100grams": "35 cal",
                "KJ_per100grams": "147 kJ"
            },
            {
                "Category": "CannedFruit",
                "FoodItem": "Canned Pineapple",
                "per100grams": "100g",
                "Cals_per100grams": "60 cal",
                "KJ_per100grams": "252 kJ"
            },
            {
                "Category": "CannedFruit",
                "FoodItem": "Canned Plums",
                "per100grams": "100g",
                "Cals_per100grams": "58 cal",
                "KJ_per100grams": "244 kJ"
            },
            {
                "Category": "CannedFruit",
                "FoodItem": "Canned Raspberries",
                "per100grams": "100g",
                "Cals_per100grams": "91 cal",
                "KJ_per100grams": "382 kJ"
            },
            {
                "Category": "CannedFruit",
                "FoodItem": "Canned Sliced Pineapple",
                "per100grams": "100g",
                "Cals_per100grams": "53 cal",
                "KJ_per100grams": "223 kJ"
            },
            {
                "Category": "CannedFruit",
                "FoodItem": "Canned Sour Cherries",
                "per100grams": "100g",
                "Cals_per100grams": "114 cal",
                "KJ_per100grams": "479 kJ"
            },
            {
                "Category": "CannedFruit",
                "FoodItem": "Canned Strawberries",
                "per100grams": "100g",
                "Cals_per100grams": "92 cal",
                "KJ_per100grams": "386 kJ"
            },
            {
                "Category": "CannedFruit",
                "FoodItem": "Canned Tangerines",
                "per100grams": "100g",
                "Cals_per100grams": "61 cal",
                "KJ_per100grams": "256 kJ"
            },
            {
                "Category": "CannedFruit",
                "FoodItem": "Dried Fruit",
                "per100grams": "100g",
                "Cals_per100grams": "243 cal",
                "KJ_per100grams": "1021 kJ"
            }
        ],
        "Fruits" : [
            {
                "Category": "Fruits",
                "FoodItem": "Acai",
                "per100grams": "100g",
                "Cals_per100grams": "70 cal",
                "KJ_per100grams": "294 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Apple",
                "per100grams": "100g",
                "Cals_per100grams": "52 cal",
                "KJ_per100grams": "218 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Applesauce",
                "per100grams": "100g",
                "Cals_per100grams": "68 cal",
                "KJ_per100grams": "286 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Apricot",
                "per100grams": "100g",
                "Cals_per100grams": "48 cal",
                "KJ_per100grams": "202 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Avocado",
                "per100grams": "100g",
                "Cals_per100grams": "160 cal",
                "KJ_per100grams": "672 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Banana",
                "per100grams": "100g",
                "Cals_per100grams": "89 cal",
                "KJ_per100grams": "374 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Blackberries",
                "per100grams": "100g",
                "Cals_per100grams": "43 cal",
                "KJ_per100grams": "181 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Blood Oranges",
                "per100grams": "100g",
                "Cals_per100grams": "50 cal",
                "KJ_per100grams": "210 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Blueberries",
                "per100grams": "100g",
                "Cals_per100grams": "57 cal",
                "KJ_per100grams": "239 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Cantaloupe",
                "per100grams": "100g",
                "Cals_per100grams": "34 cal",
                "KJ_per100grams": "143 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Cherries",
                "per100grams": "100g",
                "Cals_per100grams": "50 cal",
                "KJ_per100grams": "210 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Clementine",
                "per100grams": "100g",
                "Cals_per100grams": "47 cal",
                "KJ_per100grams": "197 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Cranberries",
                "per100grams": "100g",
                "Cals_per100grams": "46 cal",
                "KJ_per100grams": "193 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Currants",
                "per100grams": "100g",
                "Cals_per100grams": "56 cal",
                "KJ_per100grams": "235 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Custard Apple",
                "per100grams": "100g",
                "Cals_per100grams": "101 cal",
                "KJ_per100grams": "424 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Dates",
                "per100grams": "100g",
                "Cals_per100grams": "282 cal",
                "KJ_per100grams": "1184 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Figs",
                "per100grams": "100g",
                "Cals_per100grams": "74 cal",
                "KJ_per100grams": "311 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Fruit salad",
                "per100grams": "100g",
                "Cals_per100grams": "50 cal",
                "KJ_per100grams": "210 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Grapes",
                "per100grams": "100g",
                "Cals_per100grams": "69 cal",
                "KJ_per100grams": "290 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Greengage",
                "per100grams": "100g",
                "Cals_per100grams": "41 cal",
                "KJ_per100grams": "172 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Guava",
                "per100grams": "100g",
                "Cals_per100grams": "68 cal",
                "KJ_per100grams": "286 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Jackfruit",
                "per100grams": "100g",
                "Cals_per100grams": "95 cal",
                "KJ_per100grams": "399 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Jujube",
                "per100grams": "100g",
                "Cals_per100grams": "79 cal",
                "KJ_per100grams": "332 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Kiwi",
                "per100grams": "100g",
                "Cals_per100grams": "61 cal",
                "KJ_per100grams": "256 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Lemon",
                "per100grams": "100g",
                "Cals_per100grams": "29 cal",
                "KJ_per100grams": "122 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Lime",
                "per100grams": "100g",
                "Cals_per100grams": "30 cal",
                "KJ_per100grams": "126 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Lychees",
                "per100grams": "100g",
                "Cals_per100grams": "66 cal",
                "KJ_per100grams": "277 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Mandarin Oranges",
                "per100grams": "100g",
                "Cals_per100grams": "53 cal",
                "KJ_per100grams": "223 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Mango",
                "per100grams": "100g",
                "Cals_per100grams": "60 cal",
                "KJ_per100grams": "252 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Minneola",
                "per100grams": "100g",
                "Cals_per100grams": "64 cal",
                "KJ_per100grams": "269 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Mulberries",
                "per100grams": "100g",
                "Cals_per100grams": "43 cal",
                "KJ_per100grams": "181 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Nectarine",
                "per100grams": "100g",
                "Cals_per100grams": "44 cal",
                "KJ_per100grams": "185 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Olives",
                "per100grams": "100g",
                "Cals_per100grams": "115 cal",
                "KJ_per100grams": "483 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Orange",
                "per100grams": "100g",
                "Cals_per100grams": "47 cal",
                "KJ_per100grams": "197 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Papaya",
                "per100grams": "100g",
                "Cals_per100grams": "43 cal",
                "KJ_per100grams": "181 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Passion Fruit",
                "per100grams": "100g",
                "Cals_per100grams": "97 cal",
                "KJ_per100grams": "407 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Peach",
                "per100grams": "100g",
                "Cals_per100grams": "39 cal",
                "KJ_per100grams": "164 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Pear",
                "per100grams": "100g",
                "Cals_per100grams": "57 cal",
                "KJ_per100grams": "239 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Persimmon",
                "per100grams": "100g",
                "Cals_per100grams": "127 cal",
                "KJ_per100grams": "533 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Physalis",
                "per100grams": "100g",
                "Cals_per100grams": "49 cal",
                "KJ_per100grams": "206 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Pineapple",
                "per100grams": "100g",
                "Cals_per100grams": "50 cal",
                "KJ_per100grams": "210 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Plantains",
                "per100grams": "100g",
                "Cals_per100grams": "122 cal",
                "KJ_per100grams": "512 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Plum",
                "per100grams": "100g",
                "Cals_per100grams": "46 cal",
                "KJ_per100grams": "193 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Pomegranate",
                "per100grams": "100g",
                "Cals_per100grams": "83 cal",
                "KJ_per100grams": "349 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Quince",
                "per100grams": "100g",
                "Cals_per100grams": "57 cal",
                "KJ_per100grams": "239 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Raisins",
                "per100grams": "100g",
                "Cals_per100grams": "299 cal",
                "KJ_per100grams": "1256 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Rambutan",
                "per100grams": "100g",
                "Cals_per100grams": "82 cal",
                "KJ_per100grams": "344 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Raspberries",
                "per100grams": "100g",
                "Cals_per100grams": "52 cal",
                "KJ_per100grams": "218 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Rhubarb",
                "per100grams": "100g",
                "Cals_per100grams": "21 cal",
                "KJ_per100grams": "88 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Starfruit",
                "per100grams": "100g",
                "Cals_per100grams": "31 cal",
                "KJ_per100grams": "130 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Strawberries",
                "per100grams": "100g",
                "Cals_per100grams": "32 cal",
                "KJ_per100grams": "134 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Tamarind",
                "per100grams": "100g",
                "Cals_per100grams": "239 cal",
                "KJ_per100grams": "1004 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Tangerine",
                "per100grams": "100g",
                "Cals_per100grams": "53 cal",
                "KJ_per100grams": "223 kJ"
            },
            {
                "Category": "Fruits",
                "FoodItem": "Watermelon",
                "per100grams": "100g",
                "Cals_per100grams": "30 cal",
                "KJ_per100grams": "126 kJ"
            }
        ],
        "Vegetables" : [
            {
                "Category": "Vegetables",
                "FoodItem": "Artichoke",
                "per100grams": "100g",
                "Cals_per100grams": "47 cal",
                "KJ_per100grams": "197 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Arugula",
                "per100grams": "100g",
                "Cals_per100grams": "25 cal",
                "KJ_per100grams": "105 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Asparagus",
                "per100grams": "100g",
                "Cals_per100grams": "20 cal",
                "KJ_per100grams": "84 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Aubergine",
                "per100grams": "100g",
                "Cals_per100grams": "25 cal",
                "KJ_per100grams": "105 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Beetroot",
                "per100grams": "100g",
                "Cals_per100grams": "43 cal",
                "KJ_per100grams": "181 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Bell Pepper",
                "per100grams": "100g",
                "Cals_per100grams": "20 cal",
                "KJ_per100grams": "84 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Black Olives",
                "per100grams": "100g",
                "Cals_per100grams": "115 cal",
                "KJ_per100grams": "483 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Broccoli",
                "per100grams": "100g",
                "Cals_per100grams": "34 cal",
                "KJ_per100grams": "143 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Brussels Sprouts",
                "per100grams": "100g",
                "Cals_per100grams": "43 cal",
                "KJ_per100grams": "181 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Cabbage",
                "per100grams": "100g",
                "Cals_per100grams": "25 cal",
                "KJ_per100grams": "105 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Capsicum",
                "per100grams": "100g",
                "Cals_per100grams": "27 cal",
                "KJ_per100grams": "113 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Carrot",
                "per100grams": "100g",
                "Cals_per100grams": "41 cal",
                "KJ_per100grams": "172 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Cauliflower",
                "per100grams": "100g",
                "Cals_per100grams": "25 cal",
                "KJ_per100grams": "105 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Celery",
                "per100grams": "100g",
                "Cals_per100grams": "16 cal",
                "KJ_per100grams": "67 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Chard",
                "per100grams": "100g",
                "Cals_per100grams": "19 cal",
                "KJ_per100grams": "80 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Cherry Tomato",
                "per100grams": "100g",
                "Cals_per100grams": "100 cal",
                "KJ_per100grams": "420 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Chicory",
                "per100grams": "100g",
                "Cals_per100grams": "72 cal",
                "KJ_per100grams": "302 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Chinese Cabbage",
                "per100grams": "100g",
                "Cals_per100grams": "16 cal",
                "KJ_per100grams": "67 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Chives",
                "per100grams": "100g",
                "Cals_per100grams": "30 cal",
                "KJ_per100grams": "126 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Collard Greens",
                "per100grams": "100g",
                "Cals_per100grams": "32 cal",
                "KJ_per100grams": "134 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Corn",
                "per100grams": "100g",
                "Cals_per100grams": "365 cal",
                "KJ_per100grams": "1533 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Courgette",
                "per100grams": "100g",
                "Cals_per100grams": "17 cal",
                "KJ_per100grams": "71 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Creamed Spinach",
                "per100grams": "100g",
                "Cals_per100grams": "74 cal",
                "KJ_per100grams": "311 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Cucumber",
                "per100grams": "100g",
                "Cals_per100grams": "16 cal",
                "KJ_per100grams": "67 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Eggplant",
                "per100grams": "100g",
                "Cals_per100grams": "25 cal",
                "KJ_per100grams": "105 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Endive",
                "per100grams": "100g",
                "Cals_per100grams": "17 cal",
                "KJ_per100grams": "71 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Fennel",
                "per100grams": "100g",
                "Cals_per100grams": "31 cal",
                "KJ_per100grams": "130 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Garlic",
                "per100grams": "100g",
                "Cals_per100grams": "149 cal",
                "KJ_per100grams": "626 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Gherkin",
                "per100grams": "100g",
                "Cals_per100grams": "14 cal",
                "KJ_per100grams": "59 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Gourd",
                "per100grams": "100g",
                "Cals_per100grams": "14 cal",
                "KJ_per100grams": "59 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Green Beans",
                "per100grams": "100g",
                "Cals_per100grams": "31 cal",
                "KJ_per100grams": "130 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Green Olives",
                "per100grams": "100g",
                "Cals_per100grams": "115 cal",
                "KJ_per100grams": "483 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Green Onion",
                "per100grams": "100g",
                "Cals_per100grams": "32 cal",
                "KJ_per100grams": "134 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Horseradish",
                "per100grams": "100g",
                "Cals_per100grams": "48 cal",
                "KJ_per100grams": "202 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Kale",
                "per100grams": "100g",
                "Cals_per100grams": "49 cal",
                "KJ_per100grams": "206 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Kohlrabi",
                "per100grams": "100g",
                "Cals_per100grams": "27 cal",
                "KJ_per100grams": "113 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Kumara",
                "per100grams": "100g",
                "Cals_per100grams": "86 cal",
                "KJ_per100grams": "361 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Leek",
                "per100grams": "100g",
                "Cals_per100grams": "61 cal",
                "KJ_per100grams": "256 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Lettuce",
                "per100grams": "100g",
                "Cals_per100grams": "15 cal",
                "KJ_per100grams": "63 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Mushrooms",
                "per100grams": "100g",
                "Cals_per100grams": "22 cal",
                "KJ_per100grams": "92 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Mustard Greens",
                "per100grams": "100g",
                "Cals_per100grams": "27 cal",
                "KJ_per100grams": "113 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Nori",
                "per100grams": "100g",
                "Cals_per100grams": "35 cal",
                "KJ_per100grams": "147 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Okra",
                "per100grams": "100g",
                "Cals_per100grams": "33 cal",
                "KJ_per100grams": "139 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Olives",
                "per100grams": "100g",
                "Cals_per100grams": "115 cal",
                "KJ_per100grams": "483 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Onion",
                "per100grams": "100g",
                "Cals_per100grams": "40 cal",
                "KJ_per100grams": "168 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Parsnips",
                "per100grams": "100g",
                "Cals_per100grams": "75 cal",
                "KJ_per100grams": "315 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Peas",
                "per100grams": "100g",
                "Cals_per100grams": "81 cal",
                "KJ_per100grams": "340 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Pepper",
                "per100grams": "100g",
                "Cals_per100grams": "27 cal",
                "KJ_per100grams": "113 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Potato",
                "per100grams": "100g",
                "Cals_per100grams": "77 cal",
                "KJ_per100grams": "323 kJ"
            },
            {
                "Category": "Vegetables",
                "FoodItem": "Pumpkin",
                "per100grams": "100g",
                "Cals_per100grams": "26 cal",
                "KJ_per100grams": "109 kJ"
            }
        ]
    }

    mychat = Chat(food_data)
    page.add(mychat)

ft.app(target=main, view=ft.WEB_BROWSER)
