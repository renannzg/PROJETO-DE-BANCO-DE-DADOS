class Usuario:
    def __init__(self, id_usuario=None, nome=None, email=None):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"{self.id_usuario} - {self.nome} ({self.email})"

