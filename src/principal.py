import oracledb
from utils import config
from utils.splash_screen import splash
from controllers.controller_usuario import ControllerUsuario
from controllers.controller_tarefa import ControllerTarefa

GROUP_MEMBERS = ["Renan Miguel", "Membro 2", "Membro 3", "Membro 4", "Membro 5"]

def conectar():
    try:
        conn = oracledb.connect(user=config.DB_USER, password=config.DB_PASSWORD, dsn=config.DB_DSN)
        return conn
    except Exception as e:
        print("Erro ao conectar:", e)
        return None

def main():
    splash(GROUP_MEMBERS)
    conn = conectar()
    if conn is None:
        return

    cu = ControllerUsuario(conn)
    ct = ControllerTarefa(conn)

    # show counts
    with conn.cursor() as cur:
        cur.execute("SELECT COUNT(1) FROM USUARIOS")
        total_usuarios = cur.fetchone()[0]
        cur.execute("SELECT COUNT(1) FROM TAREFAS")
        total_tarefas = cur.fetchone()[0]
    print(f"Tabelas: USUARIOS={total_usuarios}, TAREFAS={total_tarefas}\n")

    while True:
        print("""
1 - Relatórios
2 - Inserir registros
3 - Remover registros
4 - Atualizar registros
5 - Listar tarefas (com usuário)
0 - Sair
""")
        opc = input("Escolha: ")
        if opc == "1":
            print("\nRelatórios disponíveis:")
            print("1 - Total de tarefas por usuário (GROUP BY)")
            print("2 - Lista de tarefas com nome do usuário (JOIN)")
            r = input("Escolha relatório: ")
            if r == "1":
                rows = ct.contar_por_usuario()
                print("\nNome | Total Tarefas")
                for row in rows:
                    print(f"{row[0]} | {row[1]}")
            elif r == "2":
                rows = ct.listar_com_usuario()
                for row in rows:
                    print(f"ID:{row[0]} | {row[1]} | {row[2]} | {row[3]}")
        elif opc == "2":
            print("\n1 - Inserir Usuário")
            print("2 - Inserir Tarefa")
            sub = input("Escolha: ")
            if sub == "1":
                nome = input("Nome: ")
                email = input("Email: ")
                cu.inserir(nome, email)
                print("Usuário inserido.")
            elif sub == "2":
                titulo = input("Título: ")
                descricao = input("Descrição: ")
                data_limite = input("Data limite (YYYY-MM-DD): ")
                status = input("Status: ")
                id_usuario = input("ID do usuário: ")
                ct.inserir(titulo, descricao, data_limite, status, id_usuario)
                print("Tarefa inserida.")
        elif opc == "3":
            id_t = input("ID da tarefa para remover: ")
            ct.excluir(id_t)
            print("Removido.")
        elif opc == "4":
            id_t = input("ID da tarefa para atualizar: ")
            novo = input("Novo status: ")
            ct.atualizar_status(id_t, novo)
            print("Atualizado.")
        elif opc == "5":
            rows = ct.listar_com_usuario()
            for row in rows:
                print(f"ID:{row[0]} | {row[1]} | {row[2]} | {row[3]}")
        elif opc == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
    conn.close()

if __name__ == "__main__":
    main()

