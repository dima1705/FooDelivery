import requests
from bs4 import BeautifulSoup
import psycopg2


def get_food():

    conn = psycopg2.connect(
        host='localhost',
        database='burgers',
        user='postgres',
        password='postgres'
    )

    urls = 'https://burger-king.by/#burgery-iz-govyadiny'

    r = requests.get(urls)
    food = BeautifulSoup(r.content, "html.parser")

    data = food.find_all("div", {'id': 'burgery-iz-govyadiny'})

    for el in data:
        elem = el.find_all("div", class_="sc-1hg54s1-0 LGqMD")
        for dat in elem:
            name = dat.find('p', class_="sc-1hg54s1-4 qJHVg").text
            description = dat.find('p', class_="sc-1hg54s1-5 llWhSp").text
            # wt = dat.find('p', class_="sc-m9jcdl-6 ryxmH").text
            price = dat.find('p', class_="sc-1hg54s1-7 dNhVcj").text.split('руб.')
            image = dat.find('img', class_="sc-1hg54s1-3 hoMPrH")['src']
            price = float(price[0])

            # return image, name, description, price)
            #
            # cursor_object = conn.cursor()
            # cursor_object.execute(
            #     """
            #         CREATE TABLE IF NOT EXISTS burgers_burger
            #         (
            #             id serial PRIMARY KEY,
            #             photo text,
            #             name text,
            #             description text,
            #             price integer
            #         )
            #     """
            # )
            # conn.commit()

            cursor = conn.cursor()
            insert_query = f"INSERT INTO burgers_burger (image, name, description, price) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (image, name, description, price))
            conn.commit()

    # conn.close()


get_food()




