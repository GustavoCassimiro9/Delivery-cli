from db import get_connection

def cadastrar_restaurante():
    nome = input("Nome do restaurante: ")
    endereco = input("Endereço: ")
    categoria = input("Categoria: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO restaurantes (nome, endereco, categoria) VALUES (%s, %s, %s)",
        (nome, endereco, categoria)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("✅ Restaurante cadastrado com sucesso!")


def listar_restaurantes():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, nome, categoria FROM restaurantes ORDER BY id")
    restaurantes = cur.fetchall()

    print("\n=== RESTAURANTES ===")
    if not restaurantes:
        print("Nenhum restaurante cadastrado.")
    else:
        for r in restaurantes:
            print(f"{r[0]} - {r[1]} ({r[2]})")

    cur.close()
    conn.close()


def atualizar_restaurante():
    listar_restaurantes()
    restaurante_id = input("\nID do restaurante para atualizar: ")

    nome = input("Novo nome: ")
    endereco = input("Novo endereço: ")
    categoria = input("Nova categoria: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE restaurantes
        SET nome = %s,
            endereco = %s,
            categoria = %s
        WHERE id = %s
    """, (nome, endereco, categoria, restaurante_id))

    if cur.rowcount == 0:
        print("❌ Restaurante não encontrado.")
    else:
        print("✏️ Restaurante atualizado com sucesso!")

    conn.commit()
    cur.close()
    conn.close()


def excluir_restaurante():
    listar_restaurantes()
    restaurante_id = input("\nID do restaurante para excluir: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM restaurantes WHERE id = %s",
        (restaurante_id,)
    )

    if cur.rowcount == 0:
        print("❌ Restaurante não encontrado.")
    else:
        print("🗑️ Restaurante excluído com sucesso!")

    conn.commit()
    cur.close()
    conn.close()
