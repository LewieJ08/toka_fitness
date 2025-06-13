from dotenv import load_dotenv
from os import getenv
import psycopg2 as pg

load_dotenv()

HOST = getenv("HOST")
DBNAME = getenv("DBNAME")
USER = getenv("USER")
PORT = getenv("PORT")
PASSWORD = getenv("PASSWORD")

# DB Setup Functions

def get_connection():
    return pg.connect(host=HOST, dbname=DBNAME, user=USER, port=PORT, password=PASSWORD)

def init_database():
    with open("schema.sql", "r") as file:
        schema = file.read()

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(schema)
            conn.commit()

# User DB Functions

def add_user(username, password, email, membership_type):
    with open("queries/add_user.sql") as file:
        query = file.read()
    
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query,(username, password, email, membership_type))
            conn.commit()