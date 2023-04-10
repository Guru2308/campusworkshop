"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgprceou9tun42u66sr0-a.oregon-postgres.render.com",
        database="todo_qqzb",
        user="root",
        password="zVDiUmW5nPoT8Q3PEYGmmrWVdJepe5fa")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
