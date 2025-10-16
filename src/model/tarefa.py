class Tarefa:
    def __init__(self, id_tarefa=None, titulo=None, descricao=None, data_criacao=None, data_limite=None, status=None, id_usuario=None):
        self.id_tarefa = id_tarefa
        self.titulo = titulo
        self.descricao = descricao
        self.data_criacao = data_criacao
        self.data_limite = data_limite
        self.status = status
        self.id_usuario = id_usuario

    def __str__(self):
        return f"{self.id_tarefa} - {self.titulo} [{self.status}] - Usuário: {self.id_usuario}"

