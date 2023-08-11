Based on the assumptions, we will be using Python with Flask for the backend and SQLite for the database. The core classes and functions will be:

1. `Customer`: A class to represent a customer. It will have attributes such as `id`, `name`, `email`, `phone`, and `address`.
2. `Interaction`: A class to represent an interaction with a customer. It will have attributes such as `id`, `customer_id`, `date`, `notes`.
3. `app.py`: The entry point of the application. It will contain the routes for the web application.
4. `database.py`: This file will contain the functions to interact with the database, such as `get_customer`, `add_customer`, `update_customer`, `delete_customer`, `get_interaction`, `add_interaction`, `update_interaction`, `delete_interaction`.

Now, let's start with the `app.py` file:

app.py
