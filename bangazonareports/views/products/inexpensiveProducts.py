"""Module for generating report of products $999 or less"""


from django.shortcuts import render
import sqlite3

from bangazonapi.models import Product
from bangazonareports.views import Connection


def inexpensive_products_list(request):
    """Function builds an HTML report of products $999 or less"""
    if request.method == 'GET':
        with sqlite3.connect(Connection.absolute_path_to_db) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT
                    p.id,
                    p.name,
                    p.price,
                    p.description,
                    p.quantity
                FROM bangazonapi_product p
                WHERE price <= 999
                ORDER BY price DESC;
            """)

            dataset = db_cursor.fetchall()

            products = []

            for row in dataset:
                products.append({
                    "id": row["id"],
                    "name": row["name"],
                    "price": row["price"],
                    "quantity": row["quantity"],
                    "description": row["description"],
                })
        template = 'products/list_inexepensive_products.html'
        context = {
            'products': products,
            'count': len(products)
        }

        return render(request, template, context)
