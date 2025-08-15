from os import getenv, path, getcwd  
import sqlite3  
from pathlib import Path  

def main():  
   pass  

def get_db_connection():  

   # Establishes and returns a connection to the SQLite database.  
   DATABASE_NAME = "generator.db"  

   app_data_path = getenv("FLET_APP_STORAGE_DATA")  
   if not app_data_path:  
       app_data_path = getcwd()  
   db_path = Path(path.join(app_data_path, DATABASE_NAME))   

   connection = sqlite3.connect(db_path)  
   connection.row_factory = sqlite3.Row  

   return connection  

def create_table():  

   # Creates table(s) in the database if they don't exist.  
   connection = get_db_connection()  
   cursor = connection.cursor()  
   sql_script = '''  
        CREATE TABLE IF NOT EXISTS contact_info (  
            contact_id INTEGER PRIMARY KEY AUTOINCREMENT,  
            name TEXT NOT NULL, 
            phone TEXT,  
            email TEXT,  
            url TEXT  
        );  

        CREATE TABLE IF NOT EXISTS education (  
            education_id INTEGER PRIMARY KEY AUTOINCREMENT,  
            school_name TEXT NOT NULL,  
            start_date DATE NOT NULL,  
            graduation_date DATE,  
            degree TEXT NOT NULL  
        );  

        CREATE TABLE IF NOT EXISTS summary (  
            summary_id INTEGER PRIMARY KEY AUTOINCREMENT,  
            summary_text TEXT NOT NULL  
        );  

        CREATE TABLE IF NOT EXISTS skill (  
            skill_id INTEGER PRIMARY KEY AUTOINCREMENT,  
            skill_name TEXT NOT NULL  
        );  

        CREATE TABLE IF NOT EXISTS job_history (  
            job_id INTEGER PRIMARY KEY AUTOINCREMENT,  
            company_name TEXT NOT NULL,  
            start_date DATE NOT NULL,  
            finish_date DATE  
        );  

        CREATE TABLE IF NOT EXISTS job_description (  
            description_id INTEGER PRIMARY KEY AUTOINCREMENT,  
            job_id INTEGER NOT NULL,  
            description TEXT NOT NULL,  
            FOREIGN KEY (job_id) REFERENCES job_history(job_id)  
        );  

        CREATE TABLE IF NOT EXISTS tagging (  
            tagging_id INTEGER PRIMARY KEY AUTOINCREMENT,  
            tag_id INTEGER NOT NULL,  
            foreign_id INTEGER NOT NULL,  
            table_ref TEXT NOT NULL,  
            FOREIGN KEY (tag_id) REFERENCES tags(tag_id)  
        );  

        CREATE TABLE IF NOT EXISTS tags (  
            tag_id INTEGER PRIMARY KEY AUTOINCREMENT,  
            tag_name TEXT NOT NULL  
        );  
    '''  
   cursor.executescript(sql_script)  
   connection.commit()  
   connection.close()  

def get_all_rows(table):  

   # Retrieves all rwos from table.  
   connection = get_db_connection()  
   cursor = connection.cursor()  
   cursor.execute("SELECT * FROM ?", (table))  
   rows = cursor.fetchall()  
   connection.close()  
   return rows  

def insert_item(name, quantity):  

   # Inserts a new item into the 'items' table  
   connection = get_db_connection()  
   cursor = connection.cursor()  
   cursor.execute("INSERT INTO items (name, quantity) VALUES (?, ?)", (name, quantity))  
   connection.commit()  
   connection.close()  

def update_item_quantity(item_id, new_quantity):  

   # Updates the quantity of a specific item.  
   connection = get_db_connection()  
   cursor = connection.cursor()  
   cursor.execute("UPDATE items SET quantity = ? WHERE id = ?", (new_quantity, item_id))  
   connection.commit()  
   connection.close()  

def delete_row(id, table):  

   # Deletes row from a table.  
   connection = get_db_connection()  
   cursor = connection.cursor()  
   cursor.execute("DELETE FROM ? WHERE id = ?", (table, id,))  
   connection.commit()  
   connection.close()  

if __name__ == "__main__":  

   main()  