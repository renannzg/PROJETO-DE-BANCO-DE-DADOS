import oracledb

class ControllerUsuario:
    def __init__(self, conn):
        self.conn = conn

    def inserir(self, nome, email):
        sql = "INSERT INTO USUARIOS (NOME, EMAIL) VALUES (:1, :2)"
        with self.conn.cursor() as cur:
            cur.execute(sql, (nome, email))
            self.conn.commit()

    def listar(self):
        sql = "SELECT ID_USUARIO, NOME, EMAIL FROM USUARIOS ORDER BY ID_USUARIO"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()

