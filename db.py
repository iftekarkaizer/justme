import psycopg2

db_config = {
    'dbname': 'myprojectdb',
    'user': 'myuser',
    'password': 'mypassword',
    'host': 'postgresqlme',
    'port': '5432'
}

def get_connection():
    return psycopg2.connect(**db_config)

def check_user(username, password):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()
        cur.close()
        conn.close()
        return user is not None
    except Exception as e:
        print(f"Database error: {e}")
        return False
