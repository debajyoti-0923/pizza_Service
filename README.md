To run on local machine :
1. Download the Repo.
2. start the virtual environment : `./env/Scripts/activate`
3. Start the app : `uvicorn main:app`

OR

Use the already hosted API at : `https://pizza-service-gdi8.onrender.com`

ENDPOINTS:
1. `/menu` : GET -> Get all the pizza details.
2. `/ingredients/get` : GET -> Get all the ingredients from the database.
3. `/ingredients/add` : POST -> Add ingredient to the database.
    ```
    REQUEST BODY:
    {
    "name": "name of ingredient"
    }
    ```
4. `/pizza/get` : GET -> Get all the pizza details.
5. `/pizza/add` : POST -> Add pizza to db.
    ```
    REQUEST BODY:
    {
    "name": "name of pizza",
    "unitPrice": 0,
    "priorityPrice": 0,
    "imageUrl": "image link",
    "soldOut": true,
    "preparingTime": 0,
    "ingredients": [
        ""
    ]
    }
    ```
6. `/order` : POST -> Add order to db.
    ```
    REQUEST BODY:
    {
    "customer": "name of customer",
    "priority": true,
    "cart": [
        {
        "pizzaId": 0,
        "name": "string",
        "quantity": 0,
        "unitPrice": 0,
        "totalPrice": 0,
        "addIngredients": [
            ""
        ],
        "removeIngredients": [
            ""
        ],
        "additionalNote": ""
        }
    ],
    "phone": 0,
    "address": "",
    "position": ""
    }
    ```
7. `/order/{id}` : GET -> Get details of Order.
8. `/order/{id}` : PATCH -> Make the order priority.
    ```
    REQUEST BODY
    {
    "priority": true
    }
    ```
