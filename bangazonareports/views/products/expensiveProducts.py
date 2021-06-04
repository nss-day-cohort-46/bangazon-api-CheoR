"""Module for generating report of products $1000 or more"""

from django.shortcuts import render
import sqlite3

from bangazonapi.models import Product
from bangazonareports.views import Connection


def expensive_products_list(request):
    """Function build an HTML report of products $1000 or more"""

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
                    p.quanity
                FROM bangazonapi_product p
                WHERE price >= 1000
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

        template = 'products/list_exepensive_products.html'
        context = {
            'products': products,
            'count': len(products)
        }

        return render(request, template, context)
