import os
import re
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

    def tokenize_text(input_text):
        tokens = input_text.split()
        print("TOKER")
        print(tokens)
        return tokens
        
    def load_text_file(self, file_path):
        #with open(file_path, 'r') as file:
        #    input_text = file.read()

        with open('text_retrieval_concordance/songs/white_christmas.txt', 'r') as f:
            data_into_list = re.split(' |\n',f.read())

        print("HI")
        tokens = data_into_list

        with open('text_retrieval_concordance/songs/white_christmas.txt', 'r') as f:
            line_list = re.split('\n',f.read())
        
        i = 1
        metadata_list = []
        for line in line_list:
            words_in_line = re.split(' ',line)
            for word in words_in_line:
                metadata_list.append({"sentence_number": i})
            i+=1
        
        text_data = TextData(tokens, metadata_list)

        self._store_text_data(text_data)

    def _store_text_data(self, text_data):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        print("text_data.data")
        print(text_data.data)
        for wd in text_data.data:
            word_data = (wd.word, wd.index, str(wd.metadata))
            cursor.execute('''INSERT INTO text_data (word, idx, metadata) VALUES (?, ?, ?)''', word_data)

        conn.commit()
        conn.close()



#initialize the database first and then create a TextFileParser object with the database path:
#   db_path = initialize_database()
#   file_parser = TextFileParser(db_path)
#   file_parser.load_text_file('example.txt')