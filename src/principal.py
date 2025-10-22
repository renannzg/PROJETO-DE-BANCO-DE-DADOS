from connection import OracleConnection

def splash_screen():
    print("=" * 50)
    print("SISTEMA DE GERENCIAMENTO DE TAREFAS")
    print("Grupo: Renan Miguel e Matheus Rhamet")  # Substitua pelos nomes reais do grupo
    print("=" * 50)

def verificar_registros():
    db = OracleConnection()
    db.connect()
    print("\n🔍 Verificando registros nas tabelas:\n")
    
    # Debug: Verifique se a conexão foi bem-sucedida
    if db.conn is None:
        print("❌ Conexão falhou, abortando verificação.")
        return
    
    # Verificar USUARIOS
    result_usuarios = db.query("SELECT COUNT(1) FROM USUARIOS")
    print(f"Debug: result_usuarios = {result_usuarios}")  # Debug: Veja o que query retorna
    if result_usuarios and len(result_usuarios) > 0:
        count_usuarios = result_usuarios[0][0]
        if count_usuarios > 0:
            print(f"✅ Tabela USUARIOS possui {count_usuarios} registros.")
        else:
            print("❌ Tabela USUARIOS não possui registros.")
    else:
        print("❌ Erro ou tabela USUARIOS não encontrada.")
    
    # Verificar TAREFAS
    result_tarefas = db.query("SELECT COUNT(1) FROM TAREFAS")
    print(f"Debug: result_tarefas = {result_tarefas}")  # Debug: Veja o que query retorna
    if result_tarefas and len(result_tarefas) > 0:
        count_tarefas = result_tarefas[0][0]
        if count_tarefas > 0:
            print(f"✅ Tabela TAREFAS possui {count_tarefas} registros.")
        else:
            print("❌ Tabela TAREFAS não possui registros.")
    else:
        print("❌ Erro ou tabela TAREFAS não encontrada.")
    
    db.disconnect()

def menu_relatorios():
    while True:
        print("\n📊 MENU DE RELATÓRIOS")
        print("1 - Total de tarefas por usuário (sumarização)")
        print("2 - Lista de tarefas com nome do usuário (junção)")
        print("0 - Voltar ao menu principal")
        opcao = input("Escolha: ")
        
        db = OracleConnection()
        db.connect()
        
        if opcao == "1":
            print("\n📈 Total de tarefas por usuário:")
            db.query_and_print("""
                SELECT U.NOME, COUNT(T.ID_TAREFA) AS TOTAL_TAREFAS
                FROM USUARIOS U
                LEFT JOIN TAREFAS T ON U.ID_USUARIO = T.ID_USUARIO
                GROUP BY U.ID_USUARIO, U.NOME
                ORDER BY U.NOME
            """)
        elif opcao == "2":
            print("\n📋 Lista de tarefas com nome do usuário:")
            db.query_and_print("""
                SELECT T.ID_TAREFA, T.TITULO, T.STATUS, U.NOME
                FROM TAREFAS T
                JOIN USUARIOS U ON T.ID_USUARIO = U.ID_USUARIO
                ORDER BY T.ID_TAREFA
            """)
        elif opcao == "0":
            db.disconnect()
            break
        else:
            print("Opção inválida.")
        
        db.disconnect()

def menu_inserir():
    while True:
        print("\n➕ MENU DE INSERÇÃO")
        print("1 - Inserir Usuário")
        print("2 - Inserir Tarefa")
        print("0 - Voltar ao menu principal")
        opcao = input("Escolha: ")
        
        if opcao == "0":
            break
        
        db = OracleConnection()
        db.connect()
        
        if opcao == "1":
            while True:
                nome = input("Nome: ")
                email = input("Email: ")
                db.execute("INSERT INTO USUARIOS (NOME, EMAIL) VALUES (:1, :2)", (nome, email))
                print("✅ Usuário inserido!")
                mais = input("Deseja inserir outro usuário? (S/N): ").strip().upper()
                if mais != "S":
                    break
        elif opcao == "2":
            while True:
                titulo = input("Título: ")
                descricao = input("Descrição: ")
                data_limite = input("Data limite (YYYY-MM-DD) ou vazio: ")
                status = input("Status (Pendente, Em andamento, Concluída): ")
                id_usuario = input("ID do Usuário: ")
                data = (titulo, descricao, data_limite if data_limite else None, status, id_usuario)
                db.execute("""
                    INSERT INTO TAREFAS (TITULO, DESCRICAO, DATA_LIMITE, STATUS, ID_USUARIO)
                    VALUES (:1, :2, TO_DATE(:3,'YYYY-MM-DD'), :4, :5)
                """, data)
                print("✅ Tarefa inserida!")
                mais = input("Deseja inserir outra tarefa? (S/N): ").strip().upper()
                if mais != "S":
                    break
        else:
            print("Opção inválida.")
        
        db.disconnect()

def menu_remover():
    while True:
        print("\n🗑️ MENU DE REMOÇÃO")
        print("1 - Remover Usuário")
        print("2 - Remover Tarefa")
        print("0 - Voltar ao menu principal")
        opcao = input("Escolha: ")
        
        if opcao == "0":
            break
        
        db = OracleConnection()
        db.connect()
        
        if opcao == "1":
            while True:
                # Listar usuários
                print("\nUsuários disponíveis:")
                usuarios = db.query("SELECT ID_USUARIO, NOME FROM USUARIOS ORDER BY ID_USUARIO")
                for i, (id_u, nome) in enumerate(usuarios, 1):
                    print(f"{i} - ID: {id_u}, Nome: {nome}")
                
                if not usuarios:
                    print("Nenhum usuário encontrado.")
                    break
                
                escolha = input("Escolha o número do usuário a remover (ou 0 para cancelar): ")
                if escolha == "0":
                    break
                try:
                    idx = int(escolha) - 1
                    id_usuario = usuarios[idx][0]
                except:
                    print("Escolha inválida.")
                    continue
                
                # Verificar FK
                count_tarefas = db.query("SELECT COUNT(1) FROM TAREFAS WHERE ID_USUARIO = :1", (id_usuario,))[0][0]
                if count_tarefas > 0:
                    print(f"Este usuário tem {count_tarefas} tarefa(s) associada(s).")
                    remover_tarefas = input("Deseja remover as tarefas associadas? (S/N): ").strip().upper()
                    if remover_tarefas == "S":
                        db.execute("DELETE FROM TAREFAS WHERE ID_USUARIO = :1", (id_usuario,))
                        print("Tarefas removidas.")
                    else:
                        print("Operação cancelada.")
                        continue
                
                confirmar = input("Confirma remoção do usuário? (S/N): ").strip().upper()
                if confirmar == "S":
                    db.execute("DELETE FROM USUARIOS WHERE ID_USUARIO = :1", (id_usuario,))
                    print("✅ Usuário removido!")
                else:
                    print("Operação cancelada.")
                
                mais = input("Deseja remover outro usuário? (S/N): ").strip().upper()
                if mais != "S":
                    break
        elif opcao == "2":
            while True:
                # Listar tarefas
                print("\nTarefas disponíveis:")
                tarefas = db.query("SELECT ID_TAREFA, TITULO FROM TAREFAS ORDER BY ID_TAREFA")
                for i, (id_t, titulo) in enumerate(tarefas, 1):
                    print(f"{i} - ID: {id_t}, Título: {titulo}")
                
                if not tarefas:
                    print("Nenhuma tarefa encontrada.")
                    break
                
                escolha = input("Escolha o número da tarefa a remover (ou 0 para cancelar): ")
                if escolha == "0":
                    break
                try:
                    idx = int(escolha) - 1
                    id_tarefa = tarefas[idx][0]
                except:
                    print("Escolha inválida.")
                    continue
                
                confirmar = input("Confirma remoção da tarefa? (S/N): ").strip().upper()
                if confirmar == "S":
                    db.execute("DELETE FROM TAREFAS WHERE ID_TAREFA = :1", (id_tarefa,))
                    print("✅ Tarefa removida!")
                else:
                    print("Operação cancelada.")
                
                mais = input("Deseja remover outra tarefa? (S/N): ").strip().upper()
                if mais != "S":
                    break
        else:
            print("Opção inválida.")
        
        db.disconnect()

def menu_atualizar():
    while True:
        print("\n✏️ MENU DE ATUALIZAÇÃO")
        print("1 - Atualizar Usuário")
        print("2 - Atualizar Tarefa")
        print("0 - Voltar ao menu principal")
        opcao = input("Escolha: ")
        
        if opcao == "0":
            break
        
        db = OracleConnection()
        db.connect()
        
        if opcao == "1":
            while True:
                # Listar usuários
                print("\nUsuários disponíveis:")
                usuarios = db.query("SELECT ID_USUARIO, NOME, EMAIL FROM USUARIOS ORDER BY ID_USUARIO")
                for i, (id_u, nome, email) in enumerate(usuarios, 1):
                    print(f"{i} - ID: {id_u}, Nome: {nome}, Email: {email}")
                
                if not usuarios:
                    print("Nenhum usuário encontrado.")
                    break
                
                escolha = input("Escolha o número do usuário a atualizar (ou 0 para cancelar): ")
                if escolha == "0":
                    break
                try:
                    idx = int(escolha) - 1
                    id_usuario, nome_atual, email_atual = usuarios[idx]
                except:
                    print("Escolha inválida.")
                    continue
                
                nome = input(f"Nome atual ({nome_atual}): ") or nome_atual
                email = input(f"Email atual ({email_atual}): ") or email_atual
                
                db.execute("UPDATE USUARIOS SET NOME = :1, EMAIL = :2 WHERE ID_USUARIO = :3", (nome, email, id_usuario))
                print("✅ Usuário atualizado!")
                
                # Exibir atualizado
                db.query_and_print("SELECT * FROM USUARIOS WHERE ID_USUARIO = :1", (id_usuario,))
                
                mais = input("Deseja atualizar outro usuário? (S/N): ").strip().upper()
                if mais != "S":
                    break
        elif opcao == "2":
            while True:
                # Listar tarefas
                print("\nTarefas disponíveis:")
                tarefas = db.query("SELECT ID_TAREFA, TITULO, DESCRICAO, DATA_LIMITE, STATUS, ID_USUARIO FROM TAREFAS ORDER BY ID_TAREFA")
                for i, (id_t, titulo, desc, data_l, status, id_u) in enumerate(tarefas, 1):
                    print(f"{i} - ID: {id_t}, Título: {titulo}, Status: {status}")
                
                if not tarefas:
                    print("Nenhuma tarefa encontrada.")
                    break
                
                escolha = input("Escolha o número da tarefa a atualizar (ou 0 para cancelar): ")
                if escolha == "0":
                    break
                try:
                    idx = int(escolha) - 1
                    id_tarefa, titulo_atual, desc_atual, data_l_atual, status_atual, id_u_atual = tarefas[idx]
                except:
                    print("Escolha inválida.")
                    continue
                
                titulo = input(f"Título atual ({titulo_atual}): ") or titulo_atual
                descricao = input(f"Descrição atual ({desc_atual}): ") or desc_atual
                data_limite = input(f"Data limite atual ({data_l_atual}): ") or data_l_atual
                status = input(f"Status atual ({status_atual}): ") or status_atual
                id_usuario = input(f"ID Usuário atual ({id_u_atual}): ") or id_u_atual
                
                db.execute("""
                    UPDATE TAREFAS SET TITULO = :1, DESCRICAO = :2, DATA_LIMITE = TO_DATE(:3,'YYYY-MM-DD'), STATUS = :4, ID_USUARIO = :5
                    WHERE ID_TAREFA = :6
                """, (titulo, descricao, data_limite, status, id_usuario, id_tarefa))
                print("✅ Tarefa atualizada!")
                
                # Exibir atualizado
                db.query_and_print("SELECT * FROM TAREFAS WHERE ID_TAREFA = :1", (id_tarefa,))
                
                mais = input("Deseja atualizar outra tarefa? (S/N): ").strip().upper()
                if mais != "S":
                    break
        else:
            print("Opção inválida.")
        
        db.disconnect()

def main():
    splash_screen()
    verificar_registros()
    
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Relatórios")
        print("2 - Inserir registros")
        print("3 - Remover registros")
        print("4 - Atualizar registros")
        print("5 - Sair")
        opcao = input("Escolha: ")
        
        if opcao == "1":
            menu_relatorios()
        elif opcao == "2":
            menu_inserir()
        elif opcao == "3":
            menu_remover()
        elif opcao == "4":
            menu_atualizar()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
