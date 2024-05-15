class Estudante:
    escola = "Digital innovation One"
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
primeiro_aluno = Estudante("Luis Sousa", 2203)
segundo_aluno = Estudante("Isa de Brito", 2204)

mostrar_valores(primeiro_aluno, segundo_aluno)

segundo_aluno.matricula = 2205

mostrar_valores(primeiro_aluno, segundo_aluno)

primeiro_aluno.escola = "Impacta"

mostrar_valores(primeiro_aluno, segundo_aluno)