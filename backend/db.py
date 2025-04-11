import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="pet_adoption",
        user="danish",
        password="2709",
        host="localhost",
        port="5432"
    )
