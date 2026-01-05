import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="delivery_app",
        user="delivery_user",
        password="delivery123",
        port=5432
    )
