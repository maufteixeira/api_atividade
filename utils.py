from models import Pessoas, Usuarios


# Insere novo registro na tabela Pessoas.db
def insere_pessoas(nome, idade):
    pessoa = Pessoas(nome=nome, idade=idade)
    print(pessoa)
    pessoa.save()


# Consulta pessoas noa tabela Pessoas.db
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    # pessoa = Pessoas.query.filter_by(nome='Mauricio').first()
    print(pessoa.nome, pessoa.idade)


# Altera registro na tabela Pessoas.db
def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='rafael').first()
    pessoa.nome = 'Pedro'
    pessoa.save()


# Exclui registro na tabela Pessoas.db
def exclui_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Pedro').first()
    pessoa.delete()


# Insere novo registro na tabela usuarios.db
def insere_usuarios(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    print(usuario)
    usuario.save()


# Consulta os usuarios cadastrados na tabela usuarios.db
def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    # insere_usuarios('mauricio', '4321')
    # insere_usuarios('icaro', '4567')
    consulta_todos_usuarios()
    # insere_pessoas('Mauricio', 44)
    # insere_pessoas('rafael', 29)
    # insere_pessoas('Icaro', 18)
    # insere_pessoas('Gabriel', 29)
    # altera_pessoas()
    # exclui_pessoas()
    # consulta_pessoas()