from db import get_connection

def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    endereco = input("Endereço: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO clientes (nome, endereco) VALUES (%s, %s)",
        (nome, endereco)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("✅ Cliente cadastrado com sucesso!")
