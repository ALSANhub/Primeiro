print("bom dia", end="")
print("Boa noite")


x = 2.3456

print("{:.2f}".format(x))


idade: int
salario: float
nome: str
sexo: str

idade = 32
salario = 4560.9
nome = "Maria Silva"
sexo = "F"

print(f"A Funcionaria {nome}, sexo {sexo}, ganha {salario} e tem {idade} anos ")
print("A Funcionaria {:s}, sexo {:s}, ganha {:.2f} e tem {:d} anos" .format(nome, sexo, salario, idade))