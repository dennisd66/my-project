import re
import sqlite3
from collections import defaultdict
from TextData import TextData


# A function to tokenize the text into words and phrases.
# Usage example:
#   sample_text = "This is an example text for tokenization. Let's see how it works!"
#   tokens = tokenize_text(sample_text)
#   print(tokens)
def tokenize_text(text):
    words = re.findall(r'\w+', text.lower())
    return words


# A function to index words and their occurrences in the text.
# Usage example:
#   sample_tokens = ['this', 'is', 'an', 'example', 'text', 'for', 'tokenization', 'let', 's', 'see', 'how', 'it', 'works']
#   word_index = index_words(sample_tokens)
#   print(word_index)
def index_words(tokens):
    word_index = defaultdict(list)
    
    for i, token in enumerate(tokens):
        word_index[token].append(i)
        
    return word_index

# A search function that allows users to query for specific words or phrases.
# Usage example:
#   query = "example"
#   occurrences = search(query, word_index)
#   print(f"The word '{query}' occurs at the following indices: {occurrences}")
def search(query, word_index):
    if query in word_index:
        occurrences = word_index[query]
        return occurrences
    else:
        return []


# A filtering functionality to search results by metadata and other criteria.
# Usage example
#   search_results = [
#       ('example', 3, {'sentence_number': 1, 'is_capitalized': False}),
#       ('example', 12, {'sentence_number': 2, 'is_capitalized': True})
#   ]
#   criteria = {'is_capitalized': True}
#   filtered_results = filter_search_results(search_results, criteria)
#   print(filtered_results)
def filter_search_results(results, criteria):
    filtered_results = []

    for word, index, metadata in results:
        match = True

        for key, value in criteria.items():
            if key not in metadata or metadata[key] != value:
                match = False
                break

        if match:
            filtered_results.append((word, index, metadata))

    return filtered_results


# This function takes a search_string and the db_path as input parameters, 
# retrieves all records from the text_data table where the word contains the search string, 
# and returns a list of TextData objects containing the results.
def search_words_in_db(search_string, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = '''SELECT word, idx, metadata FROM text_data WHERE word LIKE ?'''
    cursor.execute(query, ('%' + search_string + '%',))

    results = cursor.fetchall()
    conn.close()

    return [TextData(word=row[0], index=row[1], metadata=row[2]) for row in results]