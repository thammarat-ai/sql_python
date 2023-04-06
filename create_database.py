import sqlite3
import random
import datetime

# Define SQL commands for creating the tables
create_sales_table = '''CREATE TABLE sales (
                        sale_id INTEGER PRIMARY KEY,
                        sale_date DATE,
                        customer_id INTEGER,
                        product_id INTEGER,
                        quantity INTEGER,
                        unit_price DECIMAL(10, 2),
                        total_price DECIMAL(10, 2),
                        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                        FOREIGN KEY (product_id) REFERENCES products(product_id)
                     )'''

create_products_table = '''CREATE TABLE products (
                            product_id INTEGER PRIMARY KEY,
                            product_name TEXT,
                            unit_cost DECIMAL(10, 2)
                         )'''

create_customers_table = '''CREATE TABLE customers (
                            customer_id INTEGER PRIMARY KEY,
                            first_name TEXT,
                            last_name TEXT,
                            email TEXT,
                            phone TEXT
                         )'''


# Define SQL commands for inserting sample data into the tables
insert_products_data = '''INSERT INTO products(product_name, unit_cost) VALUES(?, ?)'''

insert_customers_data = '''INSERT INTO customers(first_name, last_name, email, phone) VALUES(?, ?, ?, ?)'''

insert_sales_data = '''INSERT INTO sales(sale_date, customer_id, product_id, quantity, unit_price, total_price) VALUES(?, ?, ?, ?, ?, ?)'''

# Define sample data for the products and customers tables

products = [('Apple', 0.99), ('Orange', 0.99), ('Banana', 0.99), ('Pineapple', 0.99), ('Strawberry', 0.99), ('Blueberry', 0.99), ('Raspberry', 0.99), ('Blackberry', 0.99), ('Watermelon', 0.99), ('Cantaloupe', 0.99), ('Honeydew', 0.99), ('Grapes', 0.99), ('Mango', 0.99), ('Peach', 0.99), ('Pear', 0.99), ('Cherry', 0.99), ('Pomegranate', 0.99), ('Kiwi', 0.99), ('Lemon', 0.99), ('Lime', 0.99), ('Coconut', 0.99), ('Avocado', 0.99), ('Tomato', 0.99), ('Potato', 0.99), ('Onion', 0.99), ('Garlic', 0.99), ('Carrot', 0.99), ('Celery', 0.99), ('Lettuce', 0.99), ('Spinach', 0.99), ('Cucumber', 0.99), ('Broccoli', 0.99), ('Cauliflower', 0.99), ('Asparagus', 0.99), ('Mushroom', 0.99), ('Peas', 0.99), ('Zucchini', 0.99), ('Squash', 0.99), ('Eggplant', 0.99), ('Cabbage', 0.99), ('Corn', 0.99), ('Beans', 0.99), ('Sweet Potato', 0.99), ('Pumpkin', 0.99), ('Radish', 0.99), ('Turnip', 0.99), ('Beet', 0.99), ('Brussel Sprout', 0.99), ('Cranberry', 0.99), ('Raisin', 0.99), ('Candy', 0.99), ('Chocolate', 0.99), ('Ice Cream', 0.99), ('Cake', 0.99)]

customers = [
    ('John', 'Doe', 'johndoe@example.com', '555-1234'),
    ('Jane', 'Doe', 'janedoe@example.com', '555-5678'),
    ('Bob', 'Smith', 'bobsmith@example.com', '555-9012'),
    ('Alice', 'Jones', 'alicejones@example.com', '555-3456'),
    ('David', 'Brown', 'davidbrown@example.com', '555-7890'),
    ('Emily', 'Davis', 'emilydavis@example.com', '555-2345'),
    ('Frank', 'Wilson', 'frankwilson@example.com', '555-6789'),
    ('Grace', 'Lee', 'gracelee@example.com', '555-1234'),
    ('Henry', 'Chen', 'henrychen@example.com', '555-5678'),
    ('Isabel', 'Garcia', 'isabelgarcia@example.com', '555-9012')
]

# Define the start and end dates for generating sales data
start_date = datetime.date(2022, 1, 1)
end_date = datetime.date(2022, 12, 31)

# Connect to the database and create the tables
with sqlite3.connect('sales.db') as conn:
    # Create the sales table
    conn.execute(create_sales_table)

    # Create the products table
    conn.execute(create_products_table)

    # Create the customers table
    conn.execute(create_customers_table)

    # Insert sample data into the products table
    for product in products:
        conn.execute(insert_products_data, product)

    # Insert sample data into the customers table
    for customer in customers:
        conn.execute(insert_customers_data, customer)

    # Insert sample data into the sales table
    for i in range(1000):
        sale_date = start_date + datetime.timedelta(days=random.randint(0, 364))
        customer_id = random.randint(1, len(customers))
        product_id = random.randint(1, len(products))
        quantity = random.randint(1, 10)
        unit_price = products[product_id - 1][1]
        total_price = quantity * unit_price
        conn.execute(insert_sales_data, (sale_date, customer_id, product_id, quantity, unit_price, total_price))

    # commit the changes
    conn.commit()

    print('Database created successfully.')


    
