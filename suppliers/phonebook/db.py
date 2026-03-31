import psycopg2
import csv
import os
from config import load_config


def get_connection():
    config = load_config()
    return psycopg2.connect(**config)


def create_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL UNIQUE
                );
            """)


def insert_contact(name, phone):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (name, phone)
            )


def insert_from_csv(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)

    with get_connection() as conn:
        with conn.cursor() as cur:
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)

                for row in reader:
                    cur.execute(
                        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                        (row[0], row[1])
                    )


def show_all():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook;")
            return cur.fetchall()


def search(name):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM phonebook WHERE name ILIKE %s",
                (f"%{name}%",)
            )
            return cur.fetchall()


def update_contact(old_name, new_name, new_phone):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE phonebook
                SET name = %s, phone = %s
                WHERE name = %s
                """,
                (new_name, new_phone, old_name)
            )


def delete_contact(name):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM phonebook WHERE name = %s",
                (name,)
            )