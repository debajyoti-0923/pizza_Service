#run to populate the database

import requests
from time import sleep
# Define the URL to which you want to send the POST request
url = 'http://127.0.0.1:8000/ingredients/add'

# Define the data you want to send in the POST request
data = [
  "tomato",
    "mozzarella",
"basil",
"ham",
"mushrooms",
"artichoke",
"prosciutto",
"arugula",
"spicy salami",
"chili flakes",
"bell peppers",
"onions",
"fresh tomato",
"anchovies",
"olives",
"capers",
"pepperoni",
"pineapple",
"spinach",
"sun-dried tomatoes",
"feta",
"pepperoncini",
"pesto",
"chicken",
"marinara",
"eggplant",
"parmesan",
"zucchini",
"peppers",
"tofu",
]



# Send the POST request
for i in data:
    k={"name":i}
    response = requests.post(url, json=k)
    sleep(0.5)

print("done")

data=[
    {
      "name": "Margheritaaa",
      "unitPrice": 12,
      "priorityPrice": 3,
      "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-1.jpg",
      "soldOut": False,
      "preparingTime": 25,
      "ingredients": [
        "tomato",
        "mozzarella",
        "basil"
      ]
    },
    {
      "name": "Capricciosa",
      "unitPrice": 14,
      "priorityPrice": 3,
      "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-2.jpg",
      "soldOut": True,
      "preparingTime": 25,
      "ingredients": [
        "tomato",
        "mozzarella",
        "ham",
        "mushrooms",
        "artichoke"
      ]
    },
    {
      "name": "Romana",
      "unitPrice": 15,
      "priorityPrice": 3,
      "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-3.jpg",
      "soldOut": False,
      "preparingTime": 25,
      "ingredients": [
        "tomato",
        "mozzarella",
        "prosciutto"
      ]
    },
    {
      "name": "Prosciutto e Rucola",
      "unitPrice": 16,
      "priorityPrice": 3,
      "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-4.jpg",
      "soldOut": False,
      "preparingTime": 25,
      "ingredients": [
        "tomato",
        "mozzarella",
        "prosciutto",
        "arugula"
      ]
    },
    {
      "name": "Diavola",
      "unitPrice": 16,
      "priorityPrice": 3,
      "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-5.jpg",
      "soldOut": False,
      "preparingTime": 25,
      "ingredients": [
        "tomato",
        "mozzarella",
        "spicy salami",
        "chili flakes"
      ]
    },
    {
      "name": "Vegetale",
      "unitPrice": 13,
      "priorityPrice": 3,
      "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-6.jpg",
      "soldOut": False,
      "preparingTime": 25,
      "ingredients": [
        "tomato",
        "mozzarella",
        "bell peppers",
        "onions",
        "mushrooms"
      ]
    },
    {
      "name": "Napoli",
      "unitPrice": 16,
      "priorityPrice": 3,
      "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-7.jpg",
      "soldOut": False,
      "preparingTime": 25,
      "ingredients": [
        "tomato",
        "mozzarella",
        "fresh tomato",
        "basil"
      ]
    },
    {
      "name": "Siciliana",
      "unitPrice": 16,
      "priorityPrice": 3,
      "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-8.jpg",
      "soldOut": True,
      "preparingTime": 25,
      "ingredients": [
        "tomato",
        "mozzarella",
        "anchovies",
        "olives",
        "capers"
      ]
    },
    {
      "name": "Pepperoni",
      "unitPrice": 14,
      "priorityPrice": 3,
      "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-9.jpg",
      "soldOut": False,
      "preparingTime": 25,
      "ingredients": [
        "tomato",
        "mozzarella",
        "pepperoni"
      ]
    },
    {
      "name": "Hawaiian",
      "unitPrice": 15,
      "priorityPrice": 3,
      "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-10.jpg",
      "soldOut": False,
      "preparingTime": 25,
      "ingredients": [
        "tomato",
        "mozzarella",
        "pineapple",
        "ham"
      ]
    },
    {
      "name": "Spinach and Mushroom",
      "unitPrice": 15,
      "priorityPrice": 3,
      "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-11.jpg",
      "soldOut": False,
      "preparingTime": 25,
      "ingredients": [
        "tomato",
        "mozzarella",
        "spinach",
        "mushrooms"
      ]
    },
    {
      "name": "Mediterranean",
      "unitPrice": 16,
      "priorityPrice": 3,
      "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-12.jpg",
      "soldOut": False,
      "preparingTime": 25,
      "ingredients": [
        "tomato",
        "mozzarella",
        "sun-dried tomatoes",
        "olives",
        "artichoke"
      ]
    },
    {
      "name": "Greek",
      "unitPrice": 16,
      "priorityPrice": 3,
      "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-13.jpg",
      "soldOut": True,
      "preparingTime": 25,
      "ingredients": [
        "tomato",
        "mozzarella",
        "spinach",
        "feta",
        "olives",
        "pepperoncini"
      ]
    },
    {
      "name": "Abruzzese",
      "unitPrice": 16,
      "priorityPrice": 3,
      "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-14.jpg",
      "soldOut": False,
      "preparingTime": 25,
      "ingredients": [
        "tomato",
        "mozzarella",
        "prosciutto",
        "arugula"
      ]
    },
    {
      "name": "Pesto Chicken",
      "unitPrice": 16,
      "priorityPrice": 3,
      "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-15.jpg",
      "soldOut": False,
      "preparingTime": 25,
      "ingredients": [
        "pesto",
        "mozzarella",
        "chicken",
        "sun-dried tomatoes",
        "spinach"
      ]
    },
    {
      "name": "Eggplant Parmesan",
      "unitPrice": 15,
      "priorityPrice": 3,
      "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-16.jpg",
      "soldOut": False,
      "preparingTime": 25,
      "ingredients": [
        "marinara",
        "mozzarella",
        "eggplant",
        "parmesan"
      ]
    },
    {
      "name": "Roasted Veggie",
      "unitPrice": 15,
      "priorityPrice": 3,
      "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-17.jpg",
      "soldOut": False,
      "preparingTime": 25,
      "ingredients": [
        "marinara",
        "mozzarella",
        "zucchini",
        "eggplant",
        "peppers",
        "onions"
      ]
    },
    {
      "name": "Tofu and Mushroom",
      "unitPrice": 15,
      "priorityPrice": 3,
      "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-18.jpg",
      "soldOut": False,
      "preparingTime": 25,
      "ingredients": [
        "marinara",
        "mozzarella",
        "tofu",
        "mushrooms",
        "bell peppers"
      ]
    }
  ]
url = 'http://127.0.0.1:8000/pizza/add'
for i in data:
    response = requests.post(url, json=i)
    sleep(0.5)

print("done")