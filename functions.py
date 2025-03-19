import os
import csv
from db import db_connection

def import_data(folder_name):
    try:
        conn = db_connection()
        if conn is None:
            print("Database connection failed! Womp womp")
            return
        
        cursor = conn.cursor()

        with open('ddl.sql', 'r') as f:
            queries = f.read().split(";")
            for query in queries:
                if query.strip():
                    cursor.execute(query.strip())

        if not os.path.isdir(folder_name):
            print(f"Error: {folder_name} is not a valid directory.")
            return

        for file in sorted(os.listdir(folder_name)): 
            file_path = os.path.join(folder_name, file)

            if not file.endswith(".csv"):
                continue  
            table_name = os.path.splitext(file)[0] 
            with open(file_path, "r") as file:
                reader = csv.reader(file)
                columns = next(reader) 
                columns = [col.strip() for col in columns]  

                placeholders = ",".join(["%s"] * len(columns)) 
                insert_query = f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({placeholders})"

                for row in reader:
                    cursor.execute(insert_query, tuple(row)) 

        conn.commit() 
        cursor.close()
        conn.close()
        print("Success")
        
    except Exception as e:
        print(f"Error: {e}")


def insert_viewer():
    pass

def add_genre():
    pass

def delete_viewer():
    pass

def insert_movie():
    pass

def insert_session():
    pass

def update_release():
    pass

def list_releases():
    pass

def popular_release():
    pass

def release_title():
    pass

def active_viewer():
    pass

def videos_viewed():
    pass

