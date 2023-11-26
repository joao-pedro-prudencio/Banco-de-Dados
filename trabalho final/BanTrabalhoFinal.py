import psycopg2
from prettytable import PrettyTable

# Parâmetros de conexão
host = "localhost"
database = "TrabalhoFinalBan"
user = "postgres"
password = "postgres"

try:
    # Obter entrada do usuário para escolher a operação desejada
    escolha_usuario = int(input("""Digite: \n1 para inserir uma nova tupla\n2 para mostrar todas as tuplas de todas as tabelas
3 para mostrar Nome e CPF dos clientes que já compraram presencialmente e o título do livro
4 para mostrar o cliente que mais comprou livros online e a quantidade comprada\n"""))

    # Conectar ao banco de dados
    connection = psycopg2.connect(host=host, database=database, user=user, password=password)

    # Criar um cursor
    cursor = connection.cursor()

    if escolha_usuario == 1:
        # Obter escolha do usuário para o tipo de inserção
        tipo_insercao = int(input("""Digite: \n1 para inserir novo autor \n2 para inserir novo cliente \n3 para para inserir nova compra 
4 para inserir nova distribuidora \n5 para inserir novo fornecedor \n6 para inserir novo funcionario
7 para inserir novo livro \n8 para inserir nova preparação \n9 para inserir nova transportadora 
10 para inserir nova venda online \n11 para inserir nova venda presencial"""))
        
        if tipo_insercao == 1:
            # Inserir um novo autor
            novo_autor = input("Digite o nome do novo autor: ")
            cursor.execute("INSERT INTO autor (autor) VALUES (%s) RETURNING codigo;", (novo_autor,))
            novo_codigo_autor = cursor.fetchone()[0]
            print(f"Autor inserido com sucesso! Código do autor: {novo_codigo_autor}")

        elif tipo_insercao == 2:
            # Inserir um novo cliente
            novo_cliente_nome = input("Digite o nome do novo cliente: ")
            novo_cliente_endereco = input("Digite o endereço do novo cliente: ")
            novo_cliente_datanasc = input("Digite a data de nascimento do novo cliente (no formato YYYY-MM-DD): ")
            novo_cliente_tipo = input("Digite o tipo do novo cliente (1- Presencial ou 2- Online): ")
            novo_cliente_cpf = input("Digite o CPF do novo cliente: ")

            cursor.execute("INSERT INTO cliente (cpf, nome, endereco, datanasc, tipo) VALUES (%s, %s, %s, %s, %s) RETURNING cpf;",
                            (novo_cliente_cpf, novo_cliente_nome, novo_cliente_endereco, novo_cliente_datanasc, novo_cliente_tipo))
            novo_cpf_cliente = cursor.fetchone()[0]
            print(f"Cliente inserido com sucesso! CPF do cliente: {novo_cpf_cliente}")

        elif tipo_insercao == 3:
            # Inserir uma nova compra
            novo_cnpj_fornecedor = input("Digite o CNPJ do fornecedor: ")
            novo_codigo_livro = input("Digite o código do livro: ")
            nova_quantidade = input("Digite a quantidade: ")
            nova_data_hora = input("Digite a data e hora (no formato YYYY-MM-DD HH:MI:SS): ")
            nova_data_entrega_distribuicao = input("Digite a data de entrega para distribuição (no formato YYYY-MM-DD): ")
            novo_cnpj_distribuidora = input("Digite o CNPJ da distribuidora: ")

            cursor.execute("""
                INSERT INTO compra (cnpj_fornecedor, codigo_livro, quantidade, data_hora, data_entrega_distribuicao, cnpj_distribuidora)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING cnpj_fornecedor, codigo_livro;
            """, (novo_cnpj_fornecedor, novo_codigo_livro, nova_quantidade, nova_data_hora, nova_data_entrega_distribuicao, novo_cnpj_distribuidora))

            resultado_compra = cursor.fetchone()
            print(f"Compra inserida com sucesso! Detalhes da compra: {resultado_compra}")

        elif tipo_insercao == 4:
            # Inserir uma nova distribuidora
            novo_cnpj_distribuidora = input("Digite o CNPJ da distribuidora: ")
            nova_razao_social = input("Digite a razão social da distribuidora: ")
            novo_endereco_distribuidora = input("Digite o endereço da distribuidora: ")

            cursor.execute("""
                INSERT INTO distribuidora (cnpj, razao_social, endereco)
                VALUES (%s, %s, %s)
                RETURNING cnpj, razao_social;
            """, (novo_cnpj_distribuidora, nova_razao_social, novo_endereco_distribuidora))

            resultado_distribuidora = cursor.fetchone()
            print(f"Distribuidora inserida com sucesso! Detalhes da distribuidora: {resultado_distribuidora}")

        elif tipo_insercao == 5:
            # Inserir uma nova fornecedor
            novo_cnpj_fornecedor = input("Digite o CNPJ do fornecedor: ")
            nova_razao_social = input("Digite a razão social do fornecedor: ")
            novo_endereco_fornecedor = input("Digite o endereço do fornecedor: ")

            cursor.execute("""
                INSERT INTO fornecedor (cnpj, razao_social, endereco)
                VALUES (%s, %s, %s)
                RETURNING cnpj, razao_social;
            """, (novo_cnpj_fornecedor, nova_razao_social, novo_endereco_fornecedor))

            resultado_fornecedor = cursor.fetchone()
            print(f"Fornecedor inserido com sucesso! Detalhes da fornecedor: {resultado_fornecedor}")    

        elif tipo_insercao == 6:
            # Inserir um novo funcionario
            novo_funcionario_nome = input("Digite o nome do novo funcionario: ")
            novo_funcionario_datanasc = input("Digite a data de nascimento do novo funcionario (no formato YYYY-MM-DD): ")
            novo_funcionario_tipo = input("Digite o tipo do novo funcionario (1- Presencial ou 2- Online): ")
            novo_funcionario_cpf = input("Digite o CPF do novo funcionario: ")

            cursor.execute("INSERT INTO funcionario (cpf, nome, datanasc, tipo) VALUES (%s, %s, %s, %s) RETURNING cpf;",
                            (novo_funcionario_cpf, novo_funcionario_nome, novo_funcionario_datanasc, novo_funcionario_tipo))
            novo_cpf_funcionario = cursor.fetchone()[0]
            print(f"Funcionario inserido com sucesso! CPF do funcionario: {novo_cpf_funcionario}")

        elif tipo_insercao == 7:
            # Inserir um novo livro
            novo_codigo_livro = int(input("Digite o código do livro: "))
            novo_titulo_livro = input("Digite o título do livro: ")
            novo_autor_livro = input("Digite o autor do livro: ")
            nova_editora_livro = input("Digite a editora do livro: ")
            novo_genero_livro = input("Digite o gênero do livro: ")
            nova_altura_livro = float(input("Digite a altura do livro: "))
            nova_largura_livro = float(input("Digite a largura do livro: "))
            nova_profundidade_livro = float(input("Digite a profundidade do livro: "))
            novo_preco_compra_livro = float(input("Digite o preço de compra do livro: "))
            novo_preco_venda_livro = float(input("Digite o preço de venda do livro: "))
            novo_num_prateleira_livro = int(input("Digite o número da prateleira do livro: "))
            novo_num_andar_livro = int(input("Digite o número do andar do livro: "))
            nova_quantidade_disponivel_livro = int(input("Digite a quantidade disponível do livro: "))

            cursor.execute("""
                INSERT INTO livro (
                    codigo, titulo, autor, editora, genero, altura, largura, profundidade,
                    preco_compra, preco_venda, num_prateleira, num_andar, quantidade_disponivel
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING codigo, titulo;
            """, (
                novo_codigo_livro, novo_titulo_livro, novo_autor_livro, nova_editora_livro,
                novo_genero_livro, nova_altura_livro, nova_largura_livro, nova_profundidade_livro,
                novo_preco_compra_livro, novo_preco_venda_livro, novo_num_prateleira_livro,
                novo_num_andar_livro, nova_quantidade_disponivel_livro
            ))

            resultado_livro = cursor.fetchone()
            print(f"Livro inserido com sucesso! Detalhes do livro: {resultado_livro}")

        elif tipo_insercao == 8:
            # Inserir uma nova preparação
            novo_cpf_cliente_prepara = input("Digite o CPF do cliente: ")
            novo_codigo_livro_prepara = input("Digite o código do livro: ")
            novo_cpf_funcionario_prepara = input("Digite o CPF do funcionário: ")

            cursor.execute("""
                INSERT INTO prepara (cpf_cliente, codigo_livro, cpf_funcionario)
                VALUES (%s, %s, %s)
                RETURNING cpf_cliente, codigo_livro, cpf_funcionario;
            """, (novo_cpf_cliente_prepara, novo_codigo_livro_prepara, novo_cpf_funcionario_prepara))

            resultado_preparacao = cursor.fetchone()
            print(f"Preparação inserida com sucesso! Detalhes da preparação: {resultado_preparacao}")

        elif tipo_insercao == 9:
                    # Inserir uma nova transportadora
                    novo_cnpj_transportadora = input("Digite o CNPJ da transportadora: ")
                    nova_razao_social = input("Digite a razão social da transportadora: ")
                    novo_endereco_transportadora = input("Digite o endereço da transportadora: ")

                    cursor.execute("""
                        INSERT INTO transportadora (cnpj, razao_social, endereco)
                        VALUES (%s, %s, %s)
                        RETURNING cnpj, razao_social;
                    """, (novo_cnpj_transportadora, nova_razao_social, novo_endereco_transportadora))

                    resultado_transportadora = cursor.fetchone()
                    print(f"Transportadora inserida com sucesso! Detalhes da transportadora: {resultado_transportadora}")

        elif tipo_insercao == 10:
            # Inserir uma nova venda online
            novo_cpf_cliente_venda_online = input("Digite o CPF do cliente: ")
            novo_codigo_livro_venda_online = input("Digite o código do livro: ")
            nova_data_entrega_transporte = input("Digite a data de entrega do transporte (no formato YYYY-MM-DD): ")
            novo_met_pag_online = input("Digite o método de pagamento online: ")
            nova_data_hora_venda_online = input("Digite a data e hora da venda (no formato YYYY-MM-DD HH:MI:SS): ")
            nova_quantidade_venda_online = input("Digite a quantidade: ")
            novo_cnpj_transportadora_venda_online = input("Digite o CNPJ da transportadora: ")

            cursor.execute("""
                INSERT INTO venda_online (
                    cpf_cliente, codigo_livro, data_entrega_transporte, met_pag_online,
                    data_hora, quantidade, cnpj_transportadora
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING cpf_cliente, codigo_livro;
            """, (
                novo_cpf_cliente_venda_online, novo_codigo_livro_venda_online,
                nova_data_entrega_transporte, novo_met_pag_online, nova_data_hora_venda_online,
                nova_quantidade_venda_online, novo_cnpj_transportadora_venda_online
            ))

            resultado_venda_online = cursor.fetchone()
            print(f"Venda online inserida com sucesso! Detalhes da venda online: {resultado_venda_online}")

        elif tipo_insercao == 11:
            # Inserir uma nova venda presencial
            novo_cpf_cliente_venda_presencial = input("Digite o CPF do cliente: ")
            novo_codigo_livro_venda_presencial = input("Digite o código do livro: ")
            novo_cpf_funcionario_venda_presencial = input("Digite o CPF do funcionário: ")
            nova_quantidade_venda_presencial = input("Digite a quantidade: ")
            novo_met_pag_presencial = input("Digite o método de pagamento: ")
            nova_data_hora_venda_presencial = input("Digite a data e hora da venda (no formato YYYY-MM-DD HH:MI:SS): ")

            cursor.execute("""
                INSERT INTO venda_presencial (
                    cpf_cliente, codigo_livro, cpf_funcionario, quantidade,
                    met_pag_presencial, data_hora
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING cpf_cliente, codigo_livro, cpf_funcionario;
            """, (
                novo_cpf_cliente_venda_presencial, novo_codigo_livro_venda_presencial,
                novo_cpf_funcionario_venda_presencial, nova_quantidade_venda_presencial,
                novo_met_pag_presencial, nova_data_hora_venda_presencial
            ))

            resultado_venda_presencial = cursor.fetchone()
            print(f"Venda presencial inserida com sucesso! Detalhes da venda presencial: {resultado_venda_presencial}")

        else:
            print("Escolha inválida. Digite 1 ou 2.")

    elif escolha_usuario == 2:
        # Lista de tabelas
        tabelas = ["autor", "cliente", "compra", "distribuidora", "fornecedor", 
                "funcionario", "livro", "prepara", "transportadora", 
                "venda_online", "venda_presencial"]

        for tabela in tabelas:
            # Executar a consulta SQL para mostrar todas as tuplas de cada tabela
            consulta = f"SELECT * FROM {tabela};"
            cursor.execute(consulta)
            
            # Imprimir cabeçalho da tabela
            print(f"\nTabela {tabela.capitalize()}:")
            colunas = [desc[0] for desc in cursor.description]

            # Configurar a tabela PrettyTable
            pt = PrettyTable(colunas)
            pt.align = 'l'  # Alinhar à esquerda

            # Adicionar as tuplas à tabela PrettyTable
            results = cursor.fetchall()
            for row in results:
                pt.add_row(row)

            # Imprimir a tabela formatada
            print(pt)
    elif escolha_usuario == 3:
        # Consultar clientes que compraram livros presencialmente
        consulta_clientes_compras_presenciais = """
            SELECT distinct nome, cpf, titulo
            FROM cliente c
            JOIN venda_presencial vp ON c.cpf = vp.cpf_cliente
            JOIN livro l ON l.codigo = vp.codigo_livro
        """

        cursor.execute(consulta_clientes_compras_presenciais)
        resultados = cursor.fetchall()

        if resultados:
            print("\nClientes que compraram livros presencialmente:")
            for row in resultados:
                print(f"Nome: {row[0]}, CPF: {row[1]}, Título do Livro: {row[2]}")
        else:
            print("Nenhum cliente encontrato que comprou livros presencialmente.")

    elif escolha_usuario == 4:
            consulta_clientes_mais_compras = """
                SELECT
                    c.nome AS cliente,
                    total_vendas.total_quantidade
                FROM
                    cliente c
                JOIN (
                    SELECT
                        vp.cpf_cliente,
                        SUM(vp.quantidade) AS total_quantidade
                    FROM
                        venda_online vp
                    GROUP BY
                        vp.cpf_cliente
                    ORDER BY
                        total_quantidade DESC
                    LIMIT 1
                ) AS total_vendas ON c.cpf = total_vendas.cpf_cliente;
            """

            cursor.execute(consulta_clientes_mais_compras)
            resultados = cursor.fetchall()

            if resultados:
                print("\nCliente que mais comprou online:")
                for row in resultados:
                    print(f"Nome: {row[0]}, Total de Livros comprados Online: {row[1]}")
            else:
                print("Nenhum cliente encontrado que comprou online.")



    else:
        print("Escolha inválida. Digite 1 ou 2.")

except (Exception, psycopg2.Error) as error:
    print("Erro ao conectar ou executar consulta:", error)

finally:
    # Confirmar a transação e fechar o cursor e a conexão
    if connection:
        connection.commit()
        connection.close()
