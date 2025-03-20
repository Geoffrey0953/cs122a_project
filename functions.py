import os
import csv
from db import db_connection
import mysql.connector

def import_data(folder_name):
    try:
        conn = db_connection()
        if conn is None:
            return "Fail"
        
        cursor = conn.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS cs122a;")
        cursor.execute("USE cs122a;")

        with open('ddl.sql', 'r') as f:
            queries = f.read().split(";")
            for query in queries:
                if query.strip():
                    try:
                        cursor.execute(query.strip())
                    except mysql.connector.Error as e:
                        print(f"DDL Execution Error: {e}")
                        return "Fail"

        if not os.path.isdir(folder_name):
            return "Fail"

        for file in sorted(os.listdir(folder_name)): 
            if not file.endswith(".csv"):
                continue 

            file_path = os.path.join(folder_name, file)
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
        return "Success"
        
    except mysql.connection.Error:
        return "Fail"


def insert_viewer(uid, email, nickname, street, city, state, zip_code, genres, joined_date, first, last, subscription):
    try:
        conn = db_connection()
        if conn is None:
            print("Database connection ")
            return "Fail"

        cursor = conn.cursor()

        cursor.execute("SELECT uid FROM Users WHERE uid = %s;", (uid,))
        if cursor.fetchone():
            return "Fail"

        query_users = """
        INSERT INTO Users (uid, email, nickname, street, city, state, zip, genres, joined_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params_users = (uid, email, nickname, street, city, state, zip_code, genres, joined_date)
        cursor.execute(query_users, params_users)
        query_viewers = """
        INSERT INTO Viewers (uid, first_name, last_name, subscription)
        VALUES (%s, %s, %s, %s)
        """
        params_viewers = (uid, first, last, subscription)
        cursor.execute(query_viewers, params_viewers)

        conn.commit()
        return "Success"

    except mysql.connector.Error:
        return "Fail"

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def add_genre(uid, genre):
    try:
        conn = db_connection()
        if conn is None:
            return "Fail"

        cursor = conn.cursor()

        cursor.execute("SELECT uid FROM Users WHERE uid = %s;", (uid,))
        user_check = cursor.fetchone()  
        if not user_check:
            return "Fail"

        query = "SELECT genres FROM Users WHERE uid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()

        current_genres = result[0] if result[0] else ""

        genres_list = set(filter(None, current_genres.split(";")))

        if genre in genres_list:
            return "Success"

        genres_list.add(genre)
        new_genres = ";".join(sorted(genres_list))

        update_query = "UPDATE Users SET genres = %s WHERE uid = %s;"
        cursor.execute(update_query, (new_genres, uid))
        conn.commit()

        return "Success"

    except mysql.connector.Error:
        return "Fail"

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def delete_viewer(uid):
    try:
        conn = db_connection()
        if conn is None:
            return "Fail"

        cursor = conn.cursor()

        cursor.execute("SELECT uid FROM Viewers WHERE uid = %s;", (uid,))
        viewer_check = cursor.fetchone()

        if not viewer_check:
            return "Fail" 

        delete_query = "DELETE FROM Users WHERE uid = %s;"
        cursor.execute(delete_query, (uid,))
        conn.commit()

        return "Success"  

    except mysql.connector.Error:
        return "Fail"  

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

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

