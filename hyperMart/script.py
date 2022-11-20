# from hyperMart.dashboard.models import Product
import csv
import datetime
import random


def make_database(Product):
    with open("../data2.csv", encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        products = []
        for row in csvreader:
            product_name = row['itemDescription']
            if product_name not in products:
                products.append(product_name)
                expiry_date = datetime.date.today() + datetime.timedelta(days=random.randint(7, 60))
                d = Product(product_name=product_name, expiry_date=expiry_date)
                d.save()
