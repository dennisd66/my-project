import os
import sqlite3
from TextFileParser import TextFileParser

def parse_txt_file(file_path):
    print(file_path)
    parser = TextFileParser(file_path)
    parsed_data = parser.load_text_file(file_path)
    return parsed_data

def load_data_into_database(parsed_data, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    for data_item in parsed_data:
        # Your table and column names may vary
        cursor.execute("""
            INSERT INTO your_table_name (column1, column2) VALUES (?, ?)
        """, (data_item["column1"], data_item["column2"]))
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    txt_files_directory = "text_retrieval_concordance/songs"
    db_file = "concordance.db"

    for file_name in os.listdir(txt_files_directory):
        if file_name.endswith(".txt"):
            file_path = os.path.join(txt_files_directory, file_name)
            parsed_data = parse_txt_file(file_path)
            load_data_into_database(parsed_data, db_file)
