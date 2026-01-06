import psycopg2

def get_connection():
    return psycopg2.connect(
        host="127.0.0.1",          # ← ou "localhost" também costuma funcionar
        database="delivery_app",
        user="delivery_user",
        password="delivery123",
        port=5433
    )
