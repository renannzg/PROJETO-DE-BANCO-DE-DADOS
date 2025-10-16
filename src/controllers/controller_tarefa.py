import oracledb

class ControllerTarefa:
    def __init__(self, conn):
        self.conn = conn

    def inserir(self, titulo, descricao, data_limite, status, id_usuario):
        sql = """
          INSERT INTO TAREFAS (TITULO, DESCRICAO, DATA_LIMITE, STATUS, ID_USUARIO)
          VALUES (:1, :2, TO_DATE(:3,'YYYY-MM-DD'), :4, :5)
        """
        with self.conn.cursor() as cur:
            cur.execute(sql, (titulo, descricao, data_limite, status, id_usuario))
            self.conn.commit()

    def listar_com_usuario(self):
        sql = """
           SELECT T.ID_TAREFA, T.TITULO, T.STATUS, U.NOME
           FROM TAREFAS T
           JOIN USUARIOS U ON T.ID_USUARIO = U.ID_USUARIO
           ORDER BY T.ID_TAREFA
        """
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()

    def atualizar_status(self, id_tarefa, novo_status):
        sql = "UPDATE TAREFAS SET STATUS = :1 WHERE ID_TAREFA = :2"
        with self.conn.cursor() as cur:
            cur.execute(sql, (novo_status, id_tarefa))
            self.conn.commit()

    def excluir(self, id_tarefa):
        sql = "DELETE FROM TAREFAS WHERE ID_TAREFA = :1"
        with self.conn.cursor() as cur:
            cur.execute(sql, (id_tarefa,))
            self.conn.commit()

    def contar_por_usuario(self):
        sql = """
          SELECT U.NOME, COUNT(T.ID_TAREFA) AS TOTAL_TAREFAS
          FROM USUARIOS U
          LEFT JOIN TAREFAS T ON U.ID_USUARIO = T.ID_USUARIO
          GROUP BY U.NOME
        """
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()

