from app import db

class Tarefa(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(255), nullable = False)
    descricao =db.Column(db.Text)
    data = db.Column(db.Date)
    hour = db.Column(db.Time)
    finalizada = db.Column(db.Boolean, default=False)
    def __init__(self, titulo, descricao, data, hora, finalizada = False):
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.finalizada = finalizada