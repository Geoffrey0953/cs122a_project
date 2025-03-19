import mysql.connector

def db_connection():
    try:
        conn = mysql.connector.connect(
        host="127.0.0.1", # Change to match your MySQL server
        user="zotstream", # I made a separate user, but you guys can use root
        password="password123", # password for my user
        database="ZotStreaming" # Schema name
    )
        if conn.is_connected():
            print("Connected to ZotStreaming Database! // Remove later probs")
    except mysql.connection.Error as e:
        print(f"Error: {e}")

# Maybe split this up to update and select?
def execute_query(query, params=None, fetch=None):
    conn = db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(query, params)
        if fetch:
            return cursor.fetchall()
        conn.commit()
        return True
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

# db_connection()