from flask import Flask, render_template, request
from TextFileParser import TextFileParser, initialize_database
import text_processing

app = Flask(__name__, template_folder='.')
db_path = initialize_database()
file_parser = TextFileParser(db_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        search_string = request.form['search']
        results = text_processing.search_words_in_db(search_string, db_path)
    template_list = ["templates/index.html"]
    return render_template(template_list, results=results)

if __name__ == "__main__":
    app.run(debug=True)