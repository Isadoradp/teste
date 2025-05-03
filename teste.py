import mysql.connector

# Estabelecendo a conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',  # servidor
    user='root',  # usuário
    password='',  # senha
    database='clinica'  # banco de dados
)

cursor = conexao.cursor()


# Função para inserir novo paciente
def inserir():
    # C - INSERT
    novo_usuario = input("Digite o nome do novo paciente: ")
    cpf_usuario = input(f"Digite o CPF do paciente {novo_usuario}: ")

    # Criando o comando SQL para inserção
    comandoSQL = f'INSERT INTO paciente (nome_paciente, cpf) VALUES ("{novo_usuario}", {cpf_usuario})'

    # Executando o comando no banco de dados
    cursor.execute(comandoSQL)
    conexao.commit()


# Função para consultar todos os pacientes
def consultarTodosPacientes():
    comandoSQL = 'SELECT * FROM paciente'
    cursor.execute(comandoSQL)
    resultadoConsulta = cursor.fetchall()  # Exibir dados
    print(resultadoConsulta)


# Função para atualizar o nome de um paciente
def atualizarNomePaciente():
    # U - UPDATE
    id_paciente = int(input("Digite o id do paciente: "))
    atualizar_nome = input("Digite o novo nome do paciente: ")
    comandoSQL = f'UPDATE paciente SET nome_paciente = "{atualizar_nome}" WHERE id_paciente = {id_paciente}'

    # Executando o comando no banco de dados
    cursor.execute(comandoSQL)
    conexao.commit()


# Função para deletar um paciente pelo ID
def deletarPacientepeloId():
    # D - DELETE
    id_paciente = int(input("Digite o id do paciente: "))
    comandoSQL = f'DELETE FROM paciente WHERE id_paciente = {id_paciente}'

    # Executando o comando no banco de dados
    cursor.execute(comandoSQL)
    conexao.commit()


# Menu para o usuário escolher a ação
menu = int(input('Digite o que você irá fazer pelos números:\n'
                 '1 - C - Cadastrar paciente\n'
                 '2 - R - Consultar todos os pacientes\n'
                 '3 - U - Atualizar paciente\n'
                 '4 - D - Deletar paciente\n'))

# Execução da ação escolhida
if menu == 1:
    print("\n")
    inserir()
elif menu == 2:
    print("\n")
    consultarTodosPacientes()
elif menu == 3:
    print("\n")
    atualizarNomePaciente()
elif menu == 4:
    print("\n")
    deletarPacientepeloId()
