import mysql.connector

def db_connection():
    try:
        conn = mysql.connector.connect(
        host="127.0.0.1", # Change to match your MySQL server
        user="zotstream", # I made a separate user, but you guys can use root #zotstream
        password="password123", # password for my user #password123
        database="ZotStreaming" # Schema name #ZotStreaming
    )
        return conn
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None

# # Maybe split this up to update and select?
# def execute_query(query, params=None, fetch=None):
#     conn = db_connection()
    
#     if conn is None:
#         print("Database connection has failed. :( )")
#         return False if not fetch else []
    
#     cursor = conn.cursor()

#     try:
#         cursor.execute(query, params)
#         if fetch:
#             return cursor.fetchall()
#         conn.commit()
#         return True
    
#     except mysql.connector.Error as e:
#         print(f"Error: {e}")
#         return False
    
#     finally:
#         cursor.close()
#         conn.close()
