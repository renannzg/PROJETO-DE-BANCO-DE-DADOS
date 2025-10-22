import oracledb

class OracleConnection:
    def __init__(self):
        self.user = "labdatabase"
        self.password = "lab@Database2025"
        self.dsn = "localhost/XEPDB1"
        self.conn = None

    def connect(self):
        try:
            self.conn = oracledb.connect(
                user=self.user,
                password=self.password,
                dsn=self.dsn
            )
            print("✅ Conectado ao Oracle com sucesso!")
        except Exception as e:
            print("❌ Erro na conexão com o Oracle:", e)
            self.conn = None

    def disconnect(self):
        if self.conn:
            self.conn.close()
            print("🔌 Conexão encerrada.")

    def execute(self, query, data=None):
        try:
            with self.conn.cursor() as cursor:
                if data:
                    cursor.execute(query, data)
                else:
                    cursor.execute(query)
                self.conn.commit()
        except Exception as e:
            print("❌ Erro ao executar comando:", e)

    def query(self, query, data=None):
        try:
            with self.conn.cursor() as cursor:
                if data:
                    cursor.execute(query, data)
                else:
                    cursor.execute(query)
                results = cursor.fetchall()
                return results  # Agora retorna a lista de tuplas
        except Exception as e:
            print("❌ Erro ao consultar:", e)
            return []  # Retorna lista vazia em erro

    def query_and_print(self, query, data=None):
        results = self.query(query, data)
        for row in results:
            print(row)
        return results
