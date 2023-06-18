import sqlite3

with sqlite3.connect('sqlite.db') as connection:
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS product(
    #         id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #         name TEXT NOT NULL,
    #         price INTEGER
    #     );
    # """)
    #
    # cursor.execute("""
    #     INSERT INTO product (name, price)
    #     VALUES
    #           ('cheese', 7),
    #           ('tomato', 8),
    #           ('coke', 120),
    #           ('no sugar coke', 130),
    #           ('sprite', 110),
    #           ('no sugar sprite', 120),
    #           ('pizza', 120),
    #           ('sandwich', 70),
    #           ('sugar', 100000),
    #           ('apple', 6)
    # """)

    # data = cursor.execute("""
    #     SELECT *
    #     FROM product
    #     WHERE
    #         price > 100 AND
    #         name LIKE '%sugar%'
    #     ;
    # """)
    #
    # print(data.fetchall())

    # data = cursor.execute("""
    #     SELECT *
    #     FROM product
    # """)
    #
    # print(data.fetchmany(5))

    # cursor.execute("""
    #     Update product
    #     SET
    #         price = price + 12
    #     WHERE
    #         price < 10
    # """)

    # cursor.execute("""
    #     DELETE FROM product
    #     WHERE name LIKE '%coke';
    # """)
