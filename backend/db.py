import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="pet_adoption_tujr",
        user="ravin",
        password="smKJJp03QRMoJhVanbTZUOtUoQAiCnIM",
        host="dpg-cvs9k2mr433s73c1kcb0-a.oregon-postgres.render.com",
        port="5432"
    )
