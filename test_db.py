import psycopg2

config = {
    'dbname': 'myprojectdb',
    'user': 'myuser',
    'password': 'mypassword',
    'host': 'localhost',
    'port': '5432'
}

try:
    conn = psycopg2.connect(**config)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", ('admin', 'admin123'))
    result = cur.fetchone()
    print("Result:", result)
    conn.close()
except Exception as e:
    print("Database error:", e)

