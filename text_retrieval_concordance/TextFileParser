import os
import sqlite3
from text_processing import TextData


#def initialize_database(db_path='concordance.db'):
#    if not os.path.exists(db_path):
#        conn = sqlite3.connect(db_path)
#        cursor = conn.cursor()
#        cursor.execute('''CREATE TABLE text_data
#                          (word TEXT, idx INTEGER, metadata TEXT)''')
#        conn.commit()
#        conn.close()
#    return db_path

def initialize_database(db_path='concordance.db'):
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE text_data
                          (word TEXT, idx INTEGER, metadata TEXT)''')
        cursor.execute('''CREATE INDEX word_index ON text_data (word)''')
        cursor.execute('''CREATE INDEX idx_index ON text_data (idx)''')
        conn.commit()
        conn.close()
    return db_path

class TextFileParser:
    def __init__(self, db_path='concordance.db'):
        self.db_path = db_path

    def load_text_file(self, file_path):
        with open(file_path, 'r') as file:
            input_text = file.read()

        tokens = TextData.tokenize_text(input_text)
        metadata_list = []  # You can generate metadata as needed
        text_data = TextData(tokens, metadata_list)

        self._store_text_data(text_data)

    def _store_text_data(self, text_data):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        for wd in text_data.data:
            word_data = (wd.word, wd.index, str(wd.metadata))
            cursor.execute('''INSERT INTO text_data (word, idx, metadata) VALUES (?, ?, ?)''', word_data)

        conn.commit()
        conn.close()



#initialize the database first and then create a TextFileParser object with the database path:
#   db_path = initialize_database()
#   file_parser = TextFileParser(db_path)
#   file_parser.load_text_file('example.txt')