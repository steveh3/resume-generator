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

# --- Helper / safe utilities ---
_VALID_TABLES = {
    "contact_info",
    "education",
    "summary",
    "skill",
    "job_history",
    "job_description",
    "tagging",
    "tags",
}

def _validate_table_name(table: str):
    if table not in _VALID_TABLES:
        raise ValueError(f"Invalid table name: {table}")

def _row_to_dict(row):
    if row is None:
        return None
    return dict(row)

# --- CRUD functions for specific tables ---

# contact_info
def add_contact(name: str, phone: str = None, email: str = None, url: str = None) -> int:
    """Insert a contact_info row. Returns the inserted contact_id."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO contact_info (name, phone, email, url) VALUES (?, ?, ?, ?)",
        (name, phone, email, url),
    )
    conn.commit()
    contact_id = cur.lastrowid
    conn.close()
    return contact_id

def get_contacts() -> list:
    """Return all contacts as list of dicts."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contact_info ORDER BY contact_id")
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_contact(contact_id: int) -> dict | None:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contact_info WHERE contact_id = ?", (contact_id,))
    row = cur.fetchone()
    conn.close()
    return _row_to_dict(row)

# education
def add_education(school_name: str, start_date: str, degree: str, graduation_date: str = None) -> int:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO education (school_name, start_date, graduation_date, degree) VALUES (?, ?, ?, ?)",
        (school_name, start_date, graduation_date, degree),
    )
    conn.commit()
    education_id = cur.lastrowid
    conn.close()
    return education_id

def get_education() -> list:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM education ORDER BY education_id")
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_education_by_id(education_id: int) -> dict | None:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM education WHERE education_id = ?", (education_id,))
    row = cur.fetchone()
    conn.close()
    return _row_to_dict(row)

# summary
def add_summary(summary_text: str) -> int:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO summary (summary_text) VALUES (?)",
        (summary_text,),
    )
    conn.commit()
    summary_id = cur.lastrowid
    conn.close()
    return summary_id

def get_summaries() -> list:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM summary ORDER BY summary_id")
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_summary(summary_id: int) -> dict | None:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM summary WHERE summary_id = ?", (summary_id,))
    row = cur.fetchone()
    conn.close()
    return _row_to_dict(row)

# skill
def add_skill(skill_name: str) -> int:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO skill (skill_name) VALUES (?)",
        (skill_name,),
    )
    conn.commit()
    skill_id = cur.lastrowid
    conn.close()
    return skill_id

def get_skills() -> list:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM skill ORDER BY skill_id")
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_skill(skill_id: int) -> dict | None:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM skill WHERE skill_id = ?", (skill_id,))
    row = cur.fetchone()
    conn.close()
    return _row_to_dict(row)

# job_history and job_description
def add_job_history(company_name: str, start_date: str, finish_date: str = None) -> int:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO job_history (company_name, start_date, finish_date) VALUES (?, ?, ?)",
        (company_name, start_date, finish_date),
    )
    conn.commit()
    job_id = cur.lastrowid
    conn.close()
    return job_id

def add_job_description(job_id: int, description: str) -> int:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO job_description (job_id, description) VALUES (?, ?)",
        (job_id, description),
    )
    conn.commit()
    description_id = cur.lastrowid
    conn.close()
    return description_id

def get_job_history() -> list:
    """Return all jobs (without descriptions)."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM job_history ORDER BY job_id")
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_job_with_descriptions(job_id: int) -> dict | None:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM job_history WHERE job_id = ?", (job_id,))
    job_row = cur.fetchone()
    if job_row is None:
        conn.close()
        return None
    cur.execute("SELECT * FROM job_description WHERE job_id = ? ORDER BY description_id", (job_id,))
    desc_rows = cur.fetchall()
    conn.close()
    job = dict(job_row)
    job["descriptions"] = [dict(d) for d in desc_rows]
    return job

def get_job_descriptions(job_id: int) -> list:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM job_description WHERE job_id = ? ORDER BY description_id", (job_id,))
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]

# --- Updated generic helpers (safe table usage) ---
def get_all_rows(table: str) -> list:
   """Return all rows from a validated table name as list of dicts."""
   _validate_table_name(table)
   conn = get_db_connection()
   cur = conn.cursor()
   query = f"SELECT * FROM {table} ORDER BY 1"
   cur.execute(query)
   rows = cur.fetchall()
   conn.close()
   return [dict(r) for r in rows]


def delete_row(id, table: str, id_column: str = None):
   """Delete a row by id from a validated table.
      id_column can be supplied when the primary key column is not 'id' (use full column name)."""
   _validate_table_name(table)
   conn = get_db_connection()
   cur = conn.cursor()
   # Determine column name
   if id_column:
       col = id_column
   else:
       # default heuristics based on table name
       col_map = {
           "contact_info": "contact_id",
           "education": "education_id",
           "summary": "summary_id",
           "skill": "skill_id",
           "job_history": "job_id",
           "job_description": "description_id",
           "tagging": "tagging_id",
           "tags": "tag_id",
       }
       col = col_map.get(table, "id")
   query = f"DELETE FROM {table} WHERE {col} = ?"
   cur.execute(query, (id,))
   conn.commit()
   conn.close()  

if __name__ == "__main__":  
   main()