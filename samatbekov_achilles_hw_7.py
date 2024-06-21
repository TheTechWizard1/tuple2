import sqlite3

def create_database():
    conn = sqlite3.connect('hw.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS products
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 product_title TEXT NOT NULL CHECK(length(product_title) <= 200),
                 price REAL NOT NULL DEFAULT 0.0 CHECK(length(price) <= 10),
                 quantity INTEGER NOT NULL DEFAULT 0)''')

    conn.commit()
    conn.close()
    print('Database and table created successfully')

def add_products():
    products = [
        ('Product 1', 10.99, 50),
        ('Product 2', 5.99, 100),
        ('Product 3', 20.49, 30),
        ('Product 4', 15.75, 75),
        ('Product 5', 8.25, 90),
        ('Product 6', 12.99, 60),
        ('Product 7', 6.49, 120),
        ('Product 8', 18.75, 45),
        ('Product 9', 22.99, 25),
        ('Product 10', 9.99, 80),
        ('Product 11', 14.49, 65),
        ('Product 12', 19.99, 40),
        ('Product 13', 7.25, 110),
        ('Product 14', 11.49, 70),
        ('Product 15', 17.99, 35)
    ]

    conn = sqlite3.connect('hw.db')
    c = conn.cursor()

    c.executemany('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', products)

    conn.commit()
    conn.close()
    print('Products added successfully')

def update_quantity_by_id(product_id, new_quantity):
    conn = sqlite3.connect('hw.db')
    c = conn.cursor()

    c.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))

    conn.commit()
    conn.close()
    print(f'Quantity updated for product with ID {product_id}')

def update_price_by_id(product_id, new_price):
    conn = sqlite3.connect('hw.db')
    c = conn.cursor()

    c.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))

    conn.commit()
    conn.close()
    print(f'Price updated for product with ID {product_id}')

def delete_product_by_id(product_id):
    conn = sqlite3.connect('hw.db')
    c = conn.cursor()

    c.execute('DELETE FROM products WHERE id = ?', (product_id,))

    conn.commit()
    conn.close()
    print(f'Product with ID {product_id} deleted successfully')

create_database()

add_products()

update_quantity_by_id(3, 40)
update_price_by_id(5, 7.99)
delete_product_by_id(10)

