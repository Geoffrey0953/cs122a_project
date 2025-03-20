import os
import csv
from db import db_connection
import mysql.connector

TABLE_ORDER = [
    "Users",
    "Producers",
    "Viewers",
    "Releases",
    "Movies",
    "Series",
    "Videos",
    "Sessions",
    "Reviews"
]

def import_data(folder_name):
    try:
        conn = db_connection()
        if conn is None:
            print("Fail")
            return "Fail"

        cursor = conn.cursor()

        execute_ddl(cursor)

        for table_name in TABLE_ORDER:
            file_path = os.path.join(folder_name, f"{table_name}.csv")
            if os.path.exists(file_path):
                import_csv(cursor, file_path, table_name)

        conn.commit()
        cursor.close()
        conn.close()

        print("Success")
        return "Success"
    except Exception as e:
        print(f"Error: {e}")
        return "Fail"

def execute_ddl(cursor):
    try:
        with open("ddl.sql", "r") as ddl_file:
            ddl_statements = ddl_file.read()
            for statement in ddl_statements.split(";"):
                statement = statement.strip()
                if statement:
                    cursor.execute(statement)
    except Exception as e:
        print(f"Error executing DDL: {e}")
        raise

def import_csv(cursor, file_path, table_name):
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        columns = next(reader)  
        placeholders = ", ".join(["%s"] * len(columns))
        sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
        for row in reader:
            try:
                cursor.execute(sql, row)
            except mysql.connector.Error as e:
                print(f"Skipping row {row} in {table_name}: {e}")

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
            print("Database connection failed")
            return "Fail"

        cursor = conn.cursor()

        # Check if user exists
        cursor.execute("SELECT genres FROM Users WHERE uid = %s;", (uid,))
        result = cursor.fetchone()
        if not result:
            print(f"Error: User {uid} does not exist.")
            return "Fail"

        # Convert existing genres to lowercase
        current_genres = result[0].lower() if result[0] else ""  
        genre = genre.lower().strip()

        genres_list = set(filter(None, current_genres.split(";")))

        # If the genre already exists, return success
        if genre in genres_list:
            print(f"Debug: Genre '{genre}' already exists for user {uid}.")
            return "Success"

        # Add the new genre
        genres_list.add(genre)
        new_genres = ";".join(sorted(genres_list))

        cursor.execute("UPDATE Users SET genres = LOWER(%s) WHERE uid = %s;", (new_genres, uid))
        conn.commit()

        print(f"Debug: Updated genres for user {uid} to {new_genres}.")
        return "Success"

    except mysql.connector.Error as e:
        print(f"MySQL Error in add_genre: {e}")
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
            print("Database connection failed")
            return "Fail"

        cursor = conn.cursor()

        # Check if user exists in Viewers or Users before deletion
        cursor.execute("SELECT uid FROM Viewers WHERE uid = %s;", (uid,))
        viewer_check = cursor.fetchone()

        cursor.execute("SELECT uid FROM Users WHERE uid = %s;", (uid,))
        user_check = cursor.fetchone()

        if not viewer_check and not user_check:
            print(f"Debug: User {uid} does not exist in Viewers or Users.")
            return "Success"

        # First delete from Viewers to prevent foreign key conflicts
        cursor.execute("DELETE FROM Viewers WHERE uid = %s;", (uid,))

        # Then delete from Users
        cursor.execute("DELETE FROM Users WHERE uid = %s;", (uid,))
        conn.commit()

        print(f"Debug: Successfully deleted user {uid} from Viewers and Users.")
        return "Success"

    except mysql.connector.Error as e:
        print(f"MySQL Error in delete_viewer: {e}")
        return "Fail"

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def insert_movie(rid, website_url):
    try:
        conn = db_connection()
        if conn is None:
            print("Database connection failed")
            return "Fail"

        cursor = conn.cursor()

        # Check if the Release ID exists in Releases table
        cursor.execute("SELECT rid FROM Releases WHERE rid = %s;", (rid,))
        release_exists = cursor.fetchone()

        if not release_exists:
            print(f"Error: Release {rid} does not exist in Releases table.")
            return "Fail"

        # Insert into Movies Table
        query_movie = """
        INSERT INTO Movies (rid, website_url)
        VALUES (%s, %s)
        """
        params_movie = (rid, website_url)

        cursor.execute(query_movie, params_movie)
        conn.commit()

        print(f"Successfully inserted movie with rid {rid} and website {website_url}")
        return "Success"

    except mysql.connector.Error as e:
        print(f"MySQL Error in insert_movie: {e}")
        return "Fail"

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

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

