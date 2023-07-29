import os
import sqlite3
from TextFileParser import TextFileParser  # replace with your text file parser class if different

def parse_txt_file(file_path):
    # Implement your text file parsing logic here
    # E.g., using TextFileParser
    parser = TextFileParser(file_path)
    parsed_data = parser.parse()

    return parsed_data

def load_data_into_database(parsed_data, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Implement your database insertion logic here
    # E.g., for each data item in parsed_data:
    for data_item in parsed_data:
        # Your table and column names may vary
        cursor.execute("""
            INSERT INTO your_table_name (column1, column2) VALUES (?, ?)
        """, (data_item["column1"], data_item["column2"]))
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    txt_files_directory = "path/to/your/txt_files_folder"
    db_file = "path/to/your/database.file"

    for file_name in os.listdir(txt_files_directory):
        if file_name.endswith(".txt"):
            file_path = os.path.join(txt_files_directory, file_name)
            parsed_data = parse_txt_file(file_path)
            load_data_into_database(parsed_data, db_file)