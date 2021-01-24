from psycopg2 import connect

CONN_PARAMS = {
    "user": "artemsenin",
    "password": "P1pvc1vd1",
    "host": "127.0.0.1",
    "port": "5432",
    "database": "econ_articles"
}

def execute_query(query, output=False):
    with connect(**CONN_PARAMS) as conn:
        with conn.cursor() as curs:
            curs.execute(query)
            if output:
                return curs.fetchall()
        conn.commit()

