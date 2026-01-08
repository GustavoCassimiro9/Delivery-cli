import psycopg2

def get_connection():
    return psycopg2.connect(
        host="127.0.0.1",          # ← ou "localhost" também costuma funcionar
        database="delivery_app",
        user="delivery_user",
        password="delivery123",
        port=5433
    )

def existe_id(tabela: str, id_: int) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT 1 FROM {tabela} WHERE id = %s", (id_,))
    ok = cur.fetchone() is not None
    cur.close()
    conn.close()
    return ok
