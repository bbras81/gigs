import sqlite3


def db_execute(query, params=(), fetch_one=False, fetch_all=False):
    """Executa uma consulta SQL e gerencia a conexão com o banco de dados.

    Args:
        query (str): A consulta SQL a ser executada.
        params (tuple): Parâmetros a serem passados na consulta.
        fetch_one (bool): Se for True, retorna apenas um resultado.
        fetch_all (bool): Se for True, retorna todos os resultados.

    Returns:
        O(s) resultado(s) da consulta ou None se não houver retorno.
    """
    conn = None
    result = None
    try:
        # Conectar ao banco de dados
        conn = sqlite3.connect("gigs_app.db")
        conn.row_factory = sqlite3.Row  # Para acessar os resultados por nome de coluna
        cursor = conn.cursor()

        # Executar a consulta
        cursor.execute(query, params)

        # Verificar se deve buscar um ou mais resultados
        if fetch_one:
            result = cursor.fetchone()  # Retorna apenas um registo
        elif fetch_all:
            result = cursor.fetchall()  # Retorna todos os registos

        # Commit se for uma operação de escrita (INSERT, UPDATE, DELETE)
        if not fetch_one and not fetch_all:
            conn.commit()

    except sqlite3.Error as e:
        print(f"Erro ao executar a consulta: {e}")
    finally:
        if conn:
            conn.close()  # Fechar a conexão

    return result
